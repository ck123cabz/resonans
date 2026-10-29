#!/usr/bin/env python3
"""Check that an SOP is machine-ready, and read whether it has been tested.

Machine-ready: a script can find the trigger, one primed callout per pause point, a
value-seen check on every step, and a gate on every never-rule. The rules cite the
calls in knowledge/learning/sop-craft/judgment.md (20 Oct 2026).

Tested is read from the Runs callout, never stored. A run line is
`- YYYY-MM-DD · who · cold|warm · questions: none|<asked> · changed: <what>`.
untested: no cold run. revising: the latest cold run asked something. tested: it asked none.
Notes without `kind: field` are method notes; only their state is read.

Usage: sop_check.py [PATH ...] [--json]   (default 04-resources/sops; exit 1 on a problem)
"""

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

from frontmatter import split_frontmatter

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ["pack", "follower", "mode", "trigger", "runs", "miss-costs", "owner"]
MODES = {"read-do", "do-confirm"}
VAGUE_TRIGGER = re.compile(r"before (you )?finish|when ready|as needed|when appropriate", re.I)
GOAL_VERBS = re.compile(r"\b(make sure|ensure|clean up|handle|the usual|as needed)\b", re.I)
EMPTY_CHECK = re.compile(r"^(checked|done|sent|ok|okay|complete|completed|verified|yes)\.?$", re.I)
STEP = re.compile(r"^\s*(\d+)\.\s+\*\*")
PRIMING = {"time · setting": r"^\*\*[^*]+ · [^*]+\*\*$", "Do": r"^\*\*Do:\*\*", "Why": r"^\*\*Why:\*\*",
           "Stuck": r"^\*\*Stuck:\*\*"}
RUN = re.compile(r"^-\s*(\d{4}-\d{2}-\d{2})\s*·\s*([^·]+)·\s*(cold|warm)\s*·\s*questions:\s*([^·]+)", re.I)


def callouts(body: str, prefix: str) -> list[tuple[str, list[str]]]:
    """Each `> [!type]+ <title>` callout whose title starts with prefix: (title, lines without `> `)."""
    found, current = [], None
    for raw in body.splitlines():
        head = re.match(r"^>\s*\[!\w+\][+-]?\s*(.+)$", raw)
        if head:
            current = (head[1].strip(), []) if head[1].strip().startswith(prefix) else None
            if current:
                found.append(current)
        elif current and raw.startswith(">"):
            current[1].append(raw[1:].strip())
        else:
            current = None
    return found


def callout(body: str, title: str) -> list[str]:
    return next((lines for t, lines in callouts(body, title)), [])


def state(body: str) -> str:
    cold = [m for m in map(RUN.match, callout(body, "Runs")) if m and m[3].lower() == "cold"]
    if not cold:
        return "untested"
    latest = max(cold, key=lambda m: m[1])
    return "tested" if latest[4].strip().lower() == "none" else "revising"


def pause_problems(title: str, lines: list[str]) -> list[str]:
    problems = [f"'{title}' has no {name} line (priming, decision 5)"
                for name, rx in PRIMING.items() if not any(re.match(rx, ln) for ln in lines)]
    steps = []
    for line in lines:
        if STEP.match(line):
            steps.append([line])
        elif steps and line and not line.lower().startswith("reason:"):
            steps[-1].append(line)
    if not steps:
        return problems + [f"'{title}' has no numbered steps"]
    if len(steps) > 9 and not any(ln.lower().startswith("reason:") for ln in lines):
        problems.append(f"{len(steps)} steps at '{title}' with no 'Reason:' line (judgment 5)")
    for step in steps:
        text, head = " ".join(step), STEP.match(step[0])[1]
        check = re.search(r"Check:\s*(.+)$", text)
        if not check:
            problems.append(f"'{title}' step {head} has no 'Check:' (judgment 9)")
        elif EMPTY_CHECK.match(check[1].strip().strip('"')):
            problems.append(f"'{title}' step {head} checks '{check[1].strip()}', not the value seen (judgment 9)")
        if GOAL_VERBS.search(text.split("Check:")[0]):
            problems.append(f"'{title}' step {head} uses a goal verb (judgment 7)")
    return problems


def field_problems(meta: dict, body: str) -> list[str]:
    problems = [f"frontmatter '{k}' is empty" for k in REQUIRED if not str(meta.get(k) or "").strip()]
    if meta.get("mode") and meta["mode"] not in MODES:
        problems.append(f"mode '{meta['mode']}' is not read-do or do-confirm (judgment 3)")
    if VAGUE_TRIGGER.search(str(meta.get("trigger") or "")):
        problems.append("trigger is not an observable event (judgment 6)")
    pack = str(meta.get("pack") or "").strip("[]")
    if pack and not (ROOT / pack).exists():
        problems.append(f"pack '{pack}' does not exist")
    pauses = callouts(body, "When ")
    problems += [p for t, lines in pauses for p in pause_problems(t, lines)]
    if not pauses:
        problems.append("no 'When <event>' pause-point callout (judgment 6)")
    for line in callout(body, "Never"):
        if line.startswith("- **Never") and not re.search(r"(No gate|Gate):", line):
            problems.append(f"never-rule names no gate: {line[:60]} (judgment 12)")
    for line in callout(body, "Exits"):
        if re.search(r"\bescalate\b", line, re.I) and not re.search(r"\bescalate to \S+", line, re.I):
            problems.append(f"escalation names no one: {line[:60]} (judgment 11)")
    return problems


def load(path: Path) -> tuple[dict, str]:
    """Frontmatter and body. Bad YAML reads as {"type": "sop", "yaml-error": ...} only for SOPs."""
    lines, body = split_frontmatter(path.read_text())
    try:
        return (yaml.safe_load("\n".join(lines or [])) or {}), body
    except yaml.YAMLError as err:
        is_sop = any(line.strip() == "type: sop" for line in lines or [])
        return ({"type": "sop", "yaml-error": str(err).splitlines()[0]} if is_sop else {}), body


def check(path: Path, meta: dict, body: str) -> dict:
    kind = meta.get("kind") or "method"
    problems = field_problems(meta, body) if kind == "field" else []
    if meta.get("yaml-error"):
        problems.append(f"frontmatter is not valid YAML: {meta['yaml-error']}")
    return {"file": str(path), "kind": kind, "state": state(body), "problems": problems}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="*", default=[str(ROOT / "04-resources/sops")])
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    files = [f for p in map(Path, args.paths) for f in (sorted(p.glob("*.md")) if p.is_dir() else [p])]
    notes = [(f, *load(f)) for f in files]
    results = [check(f, meta, body) for f, meta, body in notes if meta.get("type") == "sop"]
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            print(f"{r['state']:9} {r['kind']:6} {Path(r['file']).name}")
            for p in r["problems"]:
                print(f"          - {p}")
    return 1 if any(r["problems"] for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
