"""Check a technique map and print the `files` argument for its Artifact publish.

Usage: python3 skills/visual-techniques/scripts/check_map.py <slug>

Reads design-artifacts/technique-maps/<slug>/map.json against
skills/visual-techniques/references/techniques.json. Exit 1 with every problem
listed when the map is wrong, so a broken map never reaches the page.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills/visual-techniques"
MAPS = ROOT / "design-artifacts/technique-maps"
IMAGE_TYPES = {".jpg", ".jpeg", ".png", ".webp"}
MAX_BYTES = 2 * 1024 * 1024


def problems(m, ids, jobs, folder):
    out = []
    if m.get("job") and m["job"] not in jobs:
        out.append(f"job {m['job']!r} is not one of {sorted(jobs)}")
    seen = set()
    for ref in m.get("refs", []):
        rid = ref.get("id", "?")
        if rid in seen:
            out.append(f"ref id {rid!r} is used twice")
        seen.add(rid)
        f = folder / ref.get("file", "")
        if f.suffix.lower() not in IMAGE_TYPES or not f.is_file():
            out.append(f"{rid}: image {ref.get('file')!r} missing or not jpg/png/webp")
        elif f.stat().st_size > MAX_BYTES:
            out.append(f"{rid}: {f.name} is over 2 MB; resize with sips -Z 800")
        reads = ref.get("reads", [])
        if not 1 <= len(reads) <= 3:
            out.append(f"{rid}: {len(reads)} reads; name one to three")
        out += [f"{rid}: unknown technique {r.get('t')!r}" for r in reads if r.get("t") not in ids]
    short = m.get("shortlist", [])
    if len(short) > 4:
        out.append(f"shortlist has {len(short)} entries; four at most")
    out += [f"shortlist: unknown technique {s.get('t')!r}" for s in short if s.get("t") not in ids]
    return out


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    folder = MAPS / sys.argv[1]
    vocab = json.loads((SKILL / "references/techniques.json").read_text())
    ids = {t["id"] for t in vocab["techniques"]}
    m = json.loads((folder / "map.json").read_text())
    found = problems(m, ids, set(vocab["jobs"]), folder)
    if found:
        print("\n".join(found), file=sys.stderr)
        sys.exit(1)
    rel = lambda p: str(p.relative_to(ROOT))
    files = {
        "app.js": rel(SKILL / "map/app.js"),
        "techniques.json": rel(SKILL / "references/techniques.json"),
        "map.json": rel(folder / "map.json"),
    }
    for ref in m.get("refs", []):
        files[ref["file"]] = rel(folder / ref["file"])
    print(json.dumps(files, indent=2))


if __name__ == "__main__":
    main()
