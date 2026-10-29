"""Find paddle hits in each clip from its audio; write hits.csv.

A paddle pop is a sharp broadband click, so the audio is high-passed at
2 kHz, reduced to a 10 ms peak envelope, and a hit is any envelope peak
that is the loudest within 0.2 s and stands 12 dB over the clip's median.
The last hit before the rally goes quiet is normally the point-ending shot.

Usage: python3 hits.py <project folder> [kind ...]
Long clips (whole matches) are included, so the review page can split them
into rallies from the gaps between hits.
"""
import csv
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np

RATE, WIN = 16000, 160  # 10 ms envelope bins
GAP_BINS, OVER_DB = 20, 12.0


def envelope(proxy):
    raw = subprocess.run(
        ["ffmpeg", "-nostdin", "-v", "error", "-i", str(proxy), "-vn",
         "-af", "highpass=f=2000,highpass=f=2000", "-ac", "1", "-ar", str(RATE),
         "-f", "s16le", "-"],
        capture_output=True, check=True, timeout=300).stdout
    x = np.abs(np.frombuffer(raw, np.int16).astype(np.float32))
    n = len(x) // WIN
    return x[: n * WIN].reshape(n, WIN).max(axis=1) + 1.0


def hits(env):
    db = 20 * np.log10(env)
    floor = np.median(db) + OVER_DB
    out = []
    for i in np.flatnonzero(db > floor):
        lo, hi = max(0, i - GAP_BINS), i + GAP_BINS + 1
        if db[i] == db[lo:hi].max() and (not out or i - out[-1][0] > GAP_BINS):
            out.append((i, db[i] - np.median(db)))
    return [(round(i * WIN / RATE, 2), round(float(h), 1)) for i, h in out]


def row(r, project):
    proxy = project / "proxies" / (Path(r["file"]).stem + ".mp4")
    found = hits(envelope(proxy))
    return {
        "file": r["file"],
        "kind": r["kind"],
        "n_hits": len(found),
        "last_hit": found[-1][0] if found else "",
        "hits": " ".join(f"{t}@{h}" for t, h in found),
    }


def main(project, kinds):
    rows = [r for r in csv.DictReader((project / "manifest.csv").open())
            if r["kind"] in kinds]
    with ThreadPoolExecutor(8) as pool:
        out = list(pool.map(lambda r: row(r, project), rows))
    with (project / "hits.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    print(f"{len(out)} clips -> hits.csv", file=sys.stderr)


if __name__ == "__main__":
    main(Path(sys.argv[1]), sys.argv[2:] or ["winner", "fault", "blooper", "match"])
