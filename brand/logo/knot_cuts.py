"""The knot mark in three cuts, for big, small and tiny places.

The logo-design skill's scale test says a detailed mark needs a simpler companion for small sizes:
fewer elements, thicker strokes, bigger gaps. Each cut here is the same seed, so the small knot is
the first two loops of the full one and the tiny knot is its first loop.
Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/knot_cuts.py
Writes concepts/sheet-knot-cuts.svg and .png: every cut at five sizes, on sand and on plate.
"""
import subprocess
from pathlib import Path

from build_concepts import placed, stroke
from knot_chaos import rough, scribble
from knot_line import arch, path
from voice import wave_path

OUT = Path(__file__).parent / "concepts"
PLATE, SAND, STEEL, PAPER = "#0E1320", "#EFE9DB", "#8A93A6", "#F7F4EC"
BOX = (-45, -160, 275, 230)
CUTS = {"full": (3, 8, 3.5), "small": (2, 12, 2.0), "tiny": (1, 17, 0.0)}      # loops, pen, shake
SIZES = (96, 48, 32, 24, 16)
# Knot 26 is the mark since 6 Oct 2026, 11:25 pm. The skill's junction check failed knot 20: its loops run
# alongside each other, so the print check failed it at every size, and 4 readers saw an ear in it.
# Knot 26 holds at 6 mm in offset print, 20 mm on a shirt and 37 mm embroidered, and no reader saw an ear.
MARK = 26


def cut(name="full", seed=MARK, reach=215):
    """One cut of the mark with a short line, drawn in currentColor. Returns the drawing and its box."""
    loops, pen, shake = CUTS[name]
    x, y = rough(*path(scribble(seed, loops=loops), arch(), reach=reach), shake, seed, still=50)
    return stroke(wave_path(x, y), pen), BOX


def build():
    body, y = "", 70
    for name in CUTS:
        loops, pen, _ = CUTS[name]
        body += (f'<text x="30" y="{y + 4}" font-family="Helvetica Neue, Arial" font-size="16" font-weight="700" fill="{PLATE}">'
                 f'{name.capitalize()} cut</text><text x="150" y="{y + 4}" font-family="Helvetica Neue, Arial" font-size="13" '
                 f'fill="{STEEL}">{loops} loop{"s" if loops > 1 else ""}, pen {pen}</text>')
        for row, (ground, ink) in enumerate(((SAND, PLATE), (PLATE, SAND))):
            top = y + 18 + row * 128
            body += f'<rect x="30" y="{top}" width="640" height="120" rx="5" fill="{ground}"/>'
            x = 60
            for px in SIZES:
                body += placed(*cut(name), x, top + 60 - px * 0.42, px, px * 0.84, ink)
                x += px + 60
        y += 300
    for i, px in enumerate(SIZES):
        body += (f'<text x="{60 + sum(s + 60 for s in SIZES[:i])}" y="40" font-family="Helvetica Neue, Arial" font-size="12" '
                 f'fill="{STEEL}">{px} px</text>')
    sheet = OUT / "sheet-knot-cuts.svg"
    sheet.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 {y - 10}" width="1400" height="{2 * (y - 10)}">'
                     f'<rect width="700" height="{y - 10}" fill="{PAPER}"/>{body}</svg>')
    subprocess.run(["rsvg-convert", str(sheet), "-o", str(sheet.with_suffix(".png"))], check=True, timeout=300)


if __name__ == "__main__":
    build()
