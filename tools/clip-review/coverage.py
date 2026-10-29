"""Coverage report from tags.csv: is there enough to cut the story yet?

Usage: python3 coverage.py <project folder>

Prints markdown and writes it to <project>/qa/coverage.md. For each match it
lists the tagged points best first (difficulty, then shot count), so picking
featured points is reading down a list. Everything here is counted from
tags.csv on each run.
"""
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

import prefill

# "<t>:<name>" pairs; a name can hold spaces, so a pair runs to the next "<number>:".
SHOT = re.compile(r"(\d+(?:\.\d+)?):(.+?)(?=\s+\d+(?:\.\d+)?:|$)")


def shots(r):
    return [(t, name.strip()) for t, name in SHOT.findall(r["shots"])]


def split(v):
    return [x for x in v.split("|") if x]


def report(project):
    vocab = json.loads((project / "tags.vocab.json").read_text())
    matches = {str(m["id"]): m for m in json.loads((project / "matches.json").read_text())}
    clips = prefill.clips(project)
    tags_path = project / "tags.csv"
    tags = list(csv.DictReader(tags_path.open())) if tags_path.exists() else []
    tier_of = {c["file"]: c["tier"] for c in clips}
    lines = [f"# Coverage, {len(tags)} points tagged", ""]

    lines += ["| Tier | Clips | Clips tagged | Points |", "|---|---|---|---|"]
    for t in vocab["tiers"]:
        files = {c["file"] for c in clips if c["tier"] == t["name"]}
        rows = [r for r in tags if r["file"] in files]
        lines.append(f'| {t["name"]} | {len(files)} | {len({r["file"] for r in rows})} | {len(rows)} |')

    for label, field in (("Build patterns", "build"), ("Roles", "roles")):
        n = Counter(x for r in tags for x in split(r[field]))
        lines += ["", f"## {label}", ""] + [f"- {k}: {v}" for k, v in n.most_common()]
    won = Counter(r["won_by"] for r in tags if r["won_by"])
    lines += ["", "## Points won", ""] + [f"- {k}: {v}" for k, v in won.most_common()]

    knockout = [m for m in matches.values() if m["stage"] != "groups"]
    for m in sorted(knockout, key=lambda m: m["id"]):
        rows = [r for r in tags if r["match"] == str(m["id"])]
        rows.sort(key=lambda r: (-int(r["difficulty"] or 0), -len(shots(r))))
        lines += ["", f'## #{m["id"]} {m["stage"]}: {m["a"]} vs {m["b"]}, {m["score"]}',
                  "", f"{len(rows)} points tagged.", ""]
        if rows:
            lines += ["| Diff | Shots | Turn | Outcome | Build | Score | Clip at |", "|---|---|---|---|---|---|---|"]
        for r in rows[:12]:
            names = [name for _, name in shots(r)]
            turn = next((name for t, name in shots(r) if t == r["turn"]), "")
            lines.append(f'| {r["difficulty"]} | {" › ".join(names)} | {turn} | {r["outcome"]} | '
                         f'{", ".join(split(r["build"]))} | {r["score"]} | {r["file"]} {float(r["in_s"]):.1f} s |')

    montage = [r for r in tags if "montage" in split(r["roles"]) and tier_of.get(r["file"]) == "groups"]
    lines += ["", f"## Group montage: {len(montage)} clips", ""]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    project = Path(sys.argv[1]).resolve()
    text = report(project)
    (project / "qa").mkdir(exist_ok=True)
    (project / "qa" / "coverage.md").write_text(text)
    print(text)
