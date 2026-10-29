"""Local clip review server: plays the proxies and keeps the tags.

Usage: python3 server.py <project folder> [port] [--lan]

--lan listens on every network interface, so a phone or laptop on the same Wi-Fi can
open http://<this Mac's IP>:<port>. Anyone on that network can then read and write tags.

Tags live in <project>/tags.db, an append-only log (tags_db.py): a save, a delete and a
restore each add events and nothing is ever removed. A point is keyed "<file>#<in_s>",
so saving it twice leaves one current row. Moving a point's in-time sends the old key as
`replace`, recorded as a delete of the old key in the same transaction. Everything the
page pre-fills is worked out on each load by prefill.py and never stored.
"""
import json
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

import prefill
import presence
import tags_db

HERE = Path(__file__).parent
PROJECT = Path(sys.argv[1]).resolve()
CON = tags_db.connect(PROJECT)
CHUNK = 1 << 20


def upsert(body, who):
    row = tags_db.clean(body["row"])
    old = body.get("replace")
    tags_db.apply(CON, PROJECT, saves=[row], deletes=[old] if old and old != row["key"] else [], who=who)
    return row


def restore(rows, who):
    """Rows pulled out of a page's memory go back in as saves; history keeps both."""
    saves = [tags_db.clean(r) for r in rows]
    tags_db.apply(CON, PROJECT, saves=saves, who=f"restore:{who}")
    return {"restored": len(saves), "points": len(tags_db.current(CON))}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(HERE), **kw)

    def send_json(self, data, code=200):
        raw = json.dumps(data, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        path = unquote(urlparse(self.path).path)
        if path == "/api/clips":
            return self.send_json(prefill.clips(PROJECT))
        if path == "/api/vocab":
            return self.send_json(json.loads((PROJECT / "tags.vocab.json").read_text()))
        if path == "/api/matches":
            return self.send_json(json.loads((PROJECT / "matches.json").read_text()))
        if path == "/api/tags":
            return self.send_json(tags_db.current(CON))
        if path.startswith("/media/"):
            return self.send_media(PROJECT / "proxies" / Path(path[7:]).name)
        return super().do_GET()

    def do_POST(self):
        try:
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            return self.route_post(urlparse(self.path).path, body)
        except (ValueError, KeyError, TypeError) as err:  # bad request body, refused whole
            return self.send_json({"error": str(err)}, 400)

    def route_post(self, path, body):
        who = (body.get("who") if isinstance(body, dict) else "") or self.client_address[0]
        if path == "/api/tags":
            return self.send_json(upsert(body, who))
        if path == "/api/tags/delete":
            tags_db.apply(CON, PROJECT, deletes=[body["key"]], who=who)
            return self.send_json({"deleted": body["key"]})
        if path == "/api/restore":
            return self.send_json(restore(body, who))
        if path == "/api/presence":
            here = presence.check_in(str(body["name"])[:40], body.get("file", ""), body.get("in_s", 0))
            return self.send_json({"here": here, "tags_at": tags_db.last_id(CON)})
        self.send_error(404)

    def send_media(self, file):
        if not file.is_file():
            return self.send_error(404)
        size = file.stat().st_size
        start, end = 0, size - 1
        rng = self.headers.get("Range")
        if rng and rng.startswith("bytes="):
            lo, _, hi = rng[6:].partition("-")
            start = int(lo) if lo else size - int(hi)
            end = int(hi) if lo and hi else size - 1
        self.send_response(206 if rng else 200)
        self.send_header("Content-Type", "video/mp4")
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Length", str(end - start + 1))
        if rng:
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.end_headers()
        with file.open("rb") as f:
            f.seek(start)
            left = end - start + 1
            try:
                while left > 0 and (buf := f.read(min(CHUNK, left))):
                    self.wfile.write(buf)
                    left -= len(buf)
            except (BrokenPipeError, ConnectionResetError):
                pass  # the browser drops a range request whenever it seeks

    def log_message(self, fmt, *args):
        if not self.path.startswith("/media/"):
            super().log_message(fmt, *args)


if __name__ == "__main__":
    args = [a for a in sys.argv[2:] if a != "--lan"]
    port = int(args[0]) if args else 4580
    host = "0.0.0.0" if "--lan" in sys.argv else "127.0.0.1"
    print(f"clip review: http://localhost:{port}  project: {PROJECT}  listening on {host}")
    ThreadingHTTPServer.request_queue_size = 64  # default 5 resets the page's parallel module loads
    ThreadingHTTPServer((host, port), Handler).serve_forever()
