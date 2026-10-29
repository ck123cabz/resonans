"""Build the Resonans logo set: mark, wordmark, lockups, app icon, PNG exports.

Run from the repo root (needs Inkscape on PATH):
  uv run --with numpy --with matplotlib --with fonttools \
      python brand/logo/build_final.py

The mark is the nodal line of plate mode (1, 5), drawn at the wordmark's stroke
weight. Python computes the line as smooth curves; Inkscape turns strokes into
outlines and merges them. final/src/ keeps the stroked versions for hand editing.
"""
import re
import subprocess
from pathlib import Path

from build_concepts import draw, stroke
from letters import R, word
from plate import rings

# Brand colours, from system/project/tokens.json (Air theme): ink, ground and root.
INK, AIR, ROOT = "#211513", "#FBF5F5", "#F14441"
OUT = Path(__file__).parent / "final"
SRC = OUT / "src"
WEIGHT = 16          # one stroke weight for the mark and the letters
SMALL = 24           # heavier cut of the mark for 32 px and under
BOX = 216            # the mark sits in a BOX x BOX square centred on the origin


def page(body, box, color=INK, extra=""):
    x, y, w, h = box
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:g} {y:g} {w:g} {h:g}" '
            f'width="{w:g}" height="{h:g}" color="{color}" role="img" '
            f'aria-label="Resonans">{extra}{body}</svg>\n')


def inkscape(src, dst, actions):
    run = subprocess.run(
        ["inkscape", str(src), f"--actions=select-all;{actions};export-plain-svg;"
         f"export-filename:{dst};export-do"], capture_output=True, text=True, timeout=180)
    if not Path(dst).exists() or "error" in run.stderr.lower():
        raise RuntimeError(f"Inkscape failed on {src}: {run.stderr.strip()}")


def outline(name, body, box):
    """Stroked drawing in, one filled outline out. Returns its path data."""
    line, flat = SRC / f"{name}-line.svg", SRC / f"{name}-flat.svg"
    line.write_text(page(body, box))
    inkscape(line, flat, "object-stroke-to-path;path-union")
    paths = re.findall(r'\sd="([^"]+)"', flat.read_text())
    flat.unlink()
    if len(paths) != 1:
        raise RuntimeError(f"{name}: expected 1 merged path, got {len(paths)}")
    return paths[0]


def filled(d):
    return f'<path d="{d}" fill="currentColor" fill-rule="evenodd"/>'


def build():
    SRC.mkdir(parents=True, exist_ok=True)
    half = BOX / 2
    square = (-half, -half, BOX, BOX)
    line = rings()
    mark = filled(outline("mark", stroke(line, WEIGHT), square))
    small = filled(outline("mark-small", stroke(line, SMALL), square))
    items, width = word(weights=[WEIGHT] * 8)
    pad = WEIGHT / 2 + 2
    letters = filled(outline("wordmark", draw(items), (-pad, -2 * R - pad, width + 2 * pad, 2 * R + 2 * pad)))

    mark_g, small_g, word_g = mark, small, letters   # Inkscape keeps our coordinates

    gap = 0.56 * R                   # white between mark and word: about half an x-height
    row = (f'<g transform="translate({half},{-R})">{mark_g}</g>'
           f'<g transform="translate({BOX + gap},0)">{word_g}</g>')
    row_box = (0, -R - half, BOX + gap + width + pad, BOX)
    k = 1.5
    stack = (f'<g transform="translate({width / 2},{-2 * R - 70 - half * k}) scale({k})">{mark_g}</g>'
             f'{word_g}')
    stack_box = (-pad - 20, -2 * R - 70 - BOX * k, width + 2 * pad + 40, BOX * k + 70 + 2 * R + pad + 20)

    files = {
        "mark.svg": page(mark_g, square),
        "mark-small.svg": page(small_g, square),
        "wordmark.svg": page(word_g, (-pad, -2 * R - pad, width + 2 * pad, 2 * R + 2 * pad)),
        "lockup-horizontal.svg": page(row, row_box),
        "lockup-stacked.svg": page(stack, stack_box),
        "lockup-horizontal-reversed.svg": page(row, row_box, AIR),
        "mark-root.svg": page(mark_g, square, ROOT),
        "icon-app.svg": page(
            f'<g transform="scale(3.3)">{mark_g}</g>', (-512, -512, 1024, 1024), AIR,
            f'<rect x="-512" y="-512" width="1024" height="1024" rx="230" fill="{INK}"/>'),
        "favicon.svg": page(
            f'<g transform="scale(0.82)">{small_g}</g>', square, AIR,
            f'<rect x="{-half}" y="{-half}" width="{BOX}" height="{BOX}" rx="48" fill="{INK}"/>'),
    }
    for name, text in files.items():
        (OUT / name).write_text(text)
    return files


def export():
    png = OUT / "png"
    png.mkdir(exist_ok=True)
    jobs = [("icon-app", 1024), ("icon-app", 512), ("icon-app", 180), ("favicon", 64),
            ("favicon", 32), ("favicon", 16), ("mark", 1024), ("lockup-horizontal", 2000),
            ("lockup-horizontal-reversed", 2000), ("lockup-stacked", 1400)]
    for name, width in jobs:
        subprocess.run(["rsvg-convert", "-w", str(width), str(OUT / f"{name}.svg"),
                        "-o", str(png / f"{name}-{width}.png")], check=True, timeout=60)


if __name__ == "__main__":
    build()
    export()
