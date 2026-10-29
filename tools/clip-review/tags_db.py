"""Tag store: an append-only SQLite log of every save and every delete.

No event is ever updated or removed, so no mistake can lose a tag: the current tags
are the newest event per point, read at query time, and any earlier moment can be
rebuilt by reading the log up to it. tags.csv is a copy written from here after
every change, for people and scripts that read files.

Usage:
  python3 tags_db.py import <project> <rows.json> [who]   # merge rows back in
  python3 tags_db.py asof <project> <unix time>           # tags as they stood then
"""
import csv
import json
import os
import sqlite3
import sys
import threading
import time
from pathlib import Path

FIELDS = ["key", "file", "in_s", "out_s", "match", "score", "shots", "turn", "outcome",
          "placement", "won_by", "build", "difficulty", "camera", "crowd", "roles", "note"]
SCHEMA = """
CREATE TABLE IF NOT EXISTS events (
  id  INTEGER PRIMARY KEY,
  at  REAL NOT NULL,
  who TEXT NOT NULL DEFAULT '',
  key TEXT NOT NULL,
  op  TEXT NOT NULL CHECK (op IN ('save', 'delete')),
  row TEXT
);
CREATE INDEX IF NOT EXISTS events_by_key ON events (key, id);
"""
_lock = threading.RLock()  # one shared connection: reads and writes take turns


def connect(project):
    con = sqlite3.connect(project / "tags.db", timeout=10, isolation_level=None,
                          check_same_thread=False)
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA busy_timeout=10000")
    con.executescript(SCHEMA)
    seed_from_csv(con, project)
    return con


def seed_from_csv(con, project):
    """A project tagged before tags.db existed brings its tags.csv rows in, once."""
    path = project / "tags.csv"
    if last_id(con) or not path.exists():
        return
    with path.open(newline="") as f:
        rows = [clean(r) for r in csv.DictReader(f)]
    if rows:
        apply(con, project, saves=rows, who="seed:tags.csv")


def key_of(row):
    return f'{row["file"]}#{float(row["in_s"]):.2f}'


def clean(row):
    """The one check at the door: a row needs a file and a numeric in-time."""
    if not isinstance(row, dict) or not str(row.get("file", "")).strip():
        raise ValueError("a point needs a file")
    try:
        float(row.get("in_s"))
    except (TypeError, ValueError):
        raise ValueError(f'a point needs a numeric in_s, got {row.get("in_s")!r}') from None
    out = {k: str(row.get(k, "")) for k in FIELDS}
    out["key"] = key_of(out)
    return out


def current(con, until=None):
    with _lock:
        rows = _current(con, until)
    return sorted((json.loads(r[0]) for r in rows), key=lambda r: (r["file"], float(r["in_s"])))


def _current(con, until):
    return con.execute(
        """SELECT e.row FROM events e
           JOIN (SELECT key, MAX(id) AS id FROM events WHERE at <= ? GROUP BY key) last
             ON e.id = last.id
           WHERE e.op = 'save'""", (until or time.time() + 1,)).fetchall()


def last_id(con):
    with _lock:
        return con.execute("SELECT COALESCE(MAX(id), 0) FROM events").fetchone()[0]


def apply(con, project, saves=(), deletes=(), who=""):
    """Record deletes then saves in one transaction, then rewrite the tags.csv copy."""
    now = time.time()
    with _lock:
        con.execute("BEGIN IMMEDIATE")
        con.executemany("INSERT INTO events (at, who, key, op, row) VALUES (?, ?, ?, 'delete', NULL)",
                        [(now, who, k) for k in deletes if k])
        con.executemany("INSERT INTO events (at, who, key, op, row) VALUES (?, ?, ?, 'save', ?)",
                        [(now, who, r["key"], json.dumps(r, ensure_ascii=False)) for r in saves])
        con.execute("COMMIT")
        export(con, project)


def export(con, project):
    tmp = project / "tags.csv.tmp"
    with tmp.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(current(con))
    os.replace(tmp, project / "tags.csv")


if __name__ == "__main__":
    cmd, project = sys.argv[1], Path(sys.argv[2]).resolve()
    con = connect(project)
    if cmd == "import":
        rows = [clean(r) for r in json.loads(Path(sys.argv[3]).read_text())]
        apply(con, project, saves=rows, who=sys.argv[4] if len(sys.argv) > 4 else "import")
        print(f"imported {len(rows)} rows, {len(current(con))} points now")
    elif cmd == "asof":
        print(json.dumps(current(con, float(sys.argv[3])), indent=1, ensure_ascii=False))
