"""Round 2: three symbols for Resonans, each locked up with the even wordmark.

Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools \
      python brand/logo/build_marks.py
Writes concepts/mark-<name>.svg, concepts/lockup-<name>.svg and concepts/sheet-marks.svg.
Every mark sits in a 200 x 200 box centred on the origin and draws in currentColor.
"""
from pathlib import Path

from build_concepts import INK, PAPER, draw, placed, stroke, svg  # noqa: E402
from letters import R, word  # noqa: E402
from plate import sand  # noqa: E402

OUT = Path(__file__).parent / "concepts"
BOX = (-100, -100, 200, 200)


def plate(n=1, m=5, band=0.36, reach=0.9):
    """A Chladni figure, cropped by a circle as it was in round 2. Maths in plate.py."""
    d = sand(n, m, band, reach=reach * 0.955)
    return f'<path d="{d}" fill="currentColor" fill-rule="evenodd"/>'


def meeting(gap=26, rings=(30, 58, 86), edge=92, weight=8):
    """Two sources side by side; their rings cross inside one circle."""
    body = f'<clipPath id="edge"><circle r="{edge}"/></clipPath><g clip-path="url(#edge)">'
    for cx in (-gap, gap):
        body += f'<circle cx="{cx}" r="{weight * 0.9}" fill="currentColor"/>'
        for r in rings:
            body += (f'<circle cx="{cx}" r="{r}" fill="none" stroke="currentColor" '
                     f'stroke-width="{weight}"/>')
    return body + "</g>"


def letter(weight=16):
    """A capital R whose leg leaves the bowl as a wave and rises once."""
    stem = "M-62,84 V-84"
    bowl = "M-62,-84 H-22 a42,42 0 0 1 0,84 H-62"
    leg = "M-22,0 C8,0 8,84 38,84 S62,34 84,34"
    return stroke(stem, weight) + stroke(bowl, weight) + stroke(leg, weight)


MARKS = [("plate", plate), ("meeting", meeting), ("letter", letter)]


def lockup(mark):
    """The mark at x-height-and-a-half, then the wordmark at an even weight of 14."""
    items, width = word()
    size = 3.2 * R
    body = (f'<g transform="translate({size / 2},{-R}) scale({size / 200})">{mark}</g>'
            f'<g transform="translate({size + 70},0)">{draw(items)}</g>')
    return body, (-6, -R - size / 2 - 6, size + 70 + width + 20, size + 12)


def sheet(built):
    pw, ph, out = 1000, 460, ""
    for i, (name, mark, (body, box)) in enumerate(built):
        oy = i * ph
        out += f'<rect y="{oy}" width="{pw}" height="{ph}" fill="{PAPER}" stroke="#D8D3C6"/>'
        out += (f'<text x="28" y="{oy + 44}" font-family="Helvetica Neue" '
                f'font-size="20" fill="#7A766C">{name}</text>')
        out += placed(mark, BOX, 60, oy + 110, 240, 240, INK)
        out += placed(body, box, 360, oy + 80, 580, 150, INK)
        out += f'<rect x="360" y="{oy + 280}" width="380" height="120" rx="8" fill="{INK}"/>'
        out += placed(body, box, 390, oy + 305, 320, 70, PAPER)
        for j, px in enumerate((64, 32, 16)):
            out += placed(mark, BOX, 790 + j * 70, oy + 340 - px / 2, px, px, INK)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {pw} {len(built) * ph}" '
            f'width="{pw}" height="{len(built) * ph}">{out}</svg>')


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    built = []
    for name, fn in MARKS:
        mark = fn()
        body, box = lockup(mark)
        (OUT / f"mark-{name}.svg").write_text(svg(mark, BOX))
        (OUT / f"lockup-{name}.svg").write_text(svg(body, box))
        built.append((name, mark, (body, box)))
    (OUT / "sheet-marks.svg").write_text(sheet(built))
