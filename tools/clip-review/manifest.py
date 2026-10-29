"""Build <project>/manifest.csv from Christian's filenames plus ffprobe.

The filename is the record: players, stage, rally length and shot are parsed
from it, never typed twice. Re-run after any rename in Finder; same input,
same output.

Usage: python3 manifest.py <source folder> <project folder>
"""
import csv
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

VIDEO = {".mov", ".mp4"}
PHOTO = {".heic", ".jpg"}
STAGES = ("groups", "quarters", "semis", "semi finals", "bronze", "gold", "finals")


def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-print_format", "json",
         "-show_format", "-show_streams", str(path)],
        capture_output=True, text=True, timeout=60, check=True,
    ).stdout
    data = json.loads(out)
    video = next(s for s in data["streams"] if s["codec_type"] == "video")
    rotation = next((int(d.get("rotation", 0)) for d in video.get("side_data_list", [])
                     if "rotation" in d), 0)
    w, h = video["width"], video["height"]
    if abs(rotation) == 90:
        w, h = h, w
    return {
        "duration": round(float(data["format"]["duration"]), 2),
        "orientation": "portrait" if h > w else "landscape",
        "shot_at": data["format"].get("tags", {}).get("creation_time", ""),
    }


def parse(stem):
    parts = [p.strip() for p in stem.split(" - ")]
    row = {"players": "", "stage": "", "rally_shots": "", "label": ""}
    if " vs " in parts[0].lower():
        row["players"] = parts.pop(0)
    for i, p in enumerate(parts):
        m = re.fullmatch(r"([a-z ]+?)\s*(\d*)", p.lower())
        if m and m.group(1) in STAGES:
            row["stage"] = m.group(1)
            if m.group(2) and m.group(1) == "groups":
                row["rally_shots"] = m.group(2)
            parts.pop(i)
            break
    if not row["stage"]:
        m = re.search(r"\b(quarters|semis|semi finals|bronze|gold|finals?)\b", stem.lower())
        row["stage"] = m.group(1) if m else ""
    if parts and re.fullmatch(r"\d+( shots)?", parts[0]):
        row["rally_shots"] = parts.pop(0).split()[0]
    row["label"] = " - ".join(parts) if parts else stem
    return row


def kind(stem, row, suffix):
    s = stem.lower()
    if suffix in PHOTO:
        return "photo"
    if "pov" in s:
        return "pov"
    if "blooper" in s or "miscommunication" in s:
        return "blooper"
    if "fault" in s or "failed" in s:
        return "fault"
    if row["stage"] not in ("", "groups") and not row["rally_shots"]:
        return "match"
    return "winner"


def build(path):
    row = {"file": path.name, **parse(path.stem)}
    row["kind"] = kind(path.stem, row, path.suffix.lower())
    if row["kind"] == "photo":
        row.update(duration="", orientation="", shot_at="")
    else:
        row.update(probe(path))
    return row


def main(src, project):
    out = project / "manifest.csv"
    files = sorted(p for p in src.iterdir() if p.suffix.lower() in VIDEO | PHOTO)
    with ThreadPoolExecutor(8) as pool:
        rows = list(pool.map(build, files))
    rows.sort(key=lambda r: (r["shot_at"] or "~", r["file"]))
    fields = ["file", "kind", "players", "stage", "rally_shots", "label",
              "duration", "orientation", "shot_at"]
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    counts = {}
    for r in rows:
        counts[r["kind"]] = counts.get(r["kind"], 0) + 1
    print(f"{len(rows)} rows -> {out}", counts, file=sys.stderr)


if __name__ == "__main__":
    main(Path(sys.argv[1]).expanduser(), Path(sys.argv[2]))
