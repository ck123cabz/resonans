"""Work out the review page's guesses for every clip, on each load.

Reads manifest.csv, hits.csv, matches.json and tags.vocab.json from the project.
Nothing here is stored: a guess shows on the page as unconfirmed until
Christian saves the point. The guesses:

- match: the match whose pairs share the most names with the filename and whose
  score was entered soonest after the clip was shot, else the only match of the
  filename's stage
- tier: final, semis, bronze or groups, from that match or the filename stage
- outcome and placement: from words in the filename
- rallies: for whole-match clips, runs of paddle hits split by gaps over 3 s
"""
import csv
import json
import re
from datetime import datetime

GAP_S, MIN_HITS, PAD_S = 3.0, 3, 1.5
WORD = re.compile(r"[a-z]+")


def when(iso):
    return datetime.fromisoformat(iso.replace("Z", "+00:00")) if iso else None


def names(text):
    return {w for w in WORD.findall(text.lower()) if len(w) > 1 and w not in ("and", "partner", "vs")}


def guess_match(stem, shot_at, matches, aliases):
    s = stem.lower()
    for a in sorted(aliases, key=len, reverse=True):
        s = s.replace(a, aliases[a])
    tokens, t = names(s.split(" - ")[0]), when(shot_at)
    best = None
    for m in matches:
        overlap = len(tokens & names(m["a"] + " " + m["b"]))
        entered = when(m["entered_at"])
        if not overlap or not t or not entered or entered < t:
            continue
        rank = (-overlap, (entered - t).total_seconds())
        if best is None or rank < best[0]:
            best = (rank, m["id"])
    return best[1] if best else None


def tier_of(stage, vocab):
    return next((t["name"] for t in vocab["tiers"] if stage in t["stages"]), "groups")


def outcome(stem):
    s = stem.lower()
    if "fault" not in s and "failed" not in s:
        return "winner"
    if "net" in s:
        return "fault net"
    return "fault out" if "away" in s or "out" in s else "fault other"


def rallies(hits):
    runs = []
    for t in hits:
        if runs and t - runs[-1][-1] <= GAP_S:
            runs[-1].append(t)
        else:
            runs.append([t])
    return [{"in": round(max(0, r[0] - PAD_S), 2), "out": round(r[-1] + PAD_S, 2), "n": len(r)}
            for r in runs if len(r) >= MIN_HITS]


def clips(project):
    vocab = json.loads((project / "tags.vocab.json").read_text())
    matches = json.loads((project / "matches.json").read_text())
    by_id = {m["id"]: m for m in matches}
    hits = {r["file"]: [float(x.split("@")[0]) for x in r["hits"].split()]
            for r in csv.DictReader((project / "hits.csv").open())}
    out = []
    for r in csv.DictReader((project / "manifest.csv").open()):
        if r["kind"] == "photo":
            continue
        stem = r["file"].rsplit(".", 1)[0]
        mid = guess_match(stem, r["shot_at"], matches, vocab["aliases"])
        only = [m["id"] for m in matches if m["stage"] == r["stage"]]
        if mid is None and len(only) == 1:  # "Finals Match" names no one, but there was one final
            mid = only[0]
        stage = by_id[mid]["stage"] if mid else r["stage"]
        h = hits.get(r["file"], [])
        whole = float(r["duration"] or 0) >= 120
        out.append({
            "file": r["file"], "proxy": stem + ".mp4", "label": stem, "kind": r["kind"],
            "duration": float(r["duration"] or 0), "shot_at": r["shot_at"],
            "rally_shots": r["rally_shots"], "match": mid, "tier": tier_of(stage, vocab),
            "outcome": outcome(stem),
            "placement": next((p for p in vocab["placement"] if p in stem.lower()), ""),
            "hits": h, "rallies": rallies(h) if whole else [],
        })
    order = {t["name"]: i for i, t in enumerate(vocab["tiers"])}
    out.sort(key=lambda c: (order[c["tier"]], c["shot_at"] or "~", c["file"]))
    return out
