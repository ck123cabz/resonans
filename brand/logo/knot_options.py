"""Round 25: the two ways to handle the r, side by side, each in four places.

Christian, 6 Oct 2026, 11:10 pm: "visualize both for me first". Option 1: the logo is the knot, and
"resonans" is spelled whole when the brand has to be named. Option 2: the knot stands in for the r
and "esonans" sits under the line. Both use the lower letter height he chose, 3 pens under the line.
Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy --with contourpy \
      python brand/logo/knot_options.py
Writes concepts/sheet-knot-options.svg and .png.
"""
import subprocess
from pathlib import Path

from build_concepts import draw, placed
from knot_chaos import alone, lockup
from knot_cuts import MARK, cut
from letters import word

OUT = Path(__file__).parent / "concepts"
PLATE, SAND, BRASS, STEEL, PAPER = "#0E1320", "#EFE9DB", "#C4963F", "#8A93A6", "#F7F4EC"
W, H, PAD, TOP, GAP = 440, 300, 40, 150, 14
COLS = ("Logo", "When the brand is named", "Site header", "Avatar and card")
FONT = 'font-family="Helvetica Neue, Arial, sans-serif"'


def text(x, y, words, size=15, fill=PLATE, weight=400, anchor="start"):
    return f'<text x="{x}" y="{y}" {FONT} font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{words}</text>'


def tile(x, y, fill=SAND):
    return f'<rect x="{x}" y="{y}" width="{W}" height="{H}" rx="6" fill="{fill}"/>'


def typed_name():
    """The name in the typeface, with nothing added."""
    items, width = word("resonans", weights=[16] * 8)
    return draw(items), (-12, -112, width + 24, 124)


def shown(art, x, y, inset=50):
    """One drawing centred in a sand tile."""
    return tile(x, y) + placed(*art, x + inset, y + inset, W - 2 * inset, H - 2 * inset, PLATE)


def header(art, x, y):
    """A site header: the logo at the left, two links and a button at the right, a headline under it."""
    out = tile(x, y) + f'<line x1="{x}" x2="{x + W}" y1="{y + 92}" y2="{y + 92}" stroke="{PLATE}" stroke-opacity="0.14"/>'
    out += placed(*art, x + 22, y + 16, 190, 62, PLATE)
    out += text(x + 266, y + 52, "Cases", 13, weight=500) + text(x + 318, y + 52, "Process", 13, weight=500)
    out += f'<rect x="{x + W - 62}" y="{y + 32}" width="44" height="30" rx="3" fill="{PLATE}"/>' + text(x + W - 40, y + 52, "Call", 12, SAND, 500, "middle")
    return out + text(x + 24, y + 170, "From chaos to clarity.", 30, weight=700) + text(x + 24, y + 204, "Example header, placeholder words.", 13, STEEL)


def avatar_and_card(card_art, named, x, y):
    """A round avatar and a business card. `named` adds the name in type under the person's name."""
    out = tile(x, y, PLATE) + f'<circle cx="{x + 86}" cy="{y + H / 2}" r="58" fill="{BRASS}"/>'
    out += placed(*cut("small"), x + 44, y + H / 2 - 40, 88, 80, PLATE)
    cx, cy, cw, ch = x + 172, y + 66, 244, 158
    out += f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="5" fill="{SAND}"/>' + placed(*card_art, cx + 18, cy + 16, 150, 62, PLATE)
    out += text(cx + 20, cy + ch - 34, "Christian Cabaluna", 13, weight=600)
    if named:
        return out + placed(*typed_name(), cx + 20, cy + ch - 26, 74, 14, PLATE)
    return out


def build():
    knot = alone(MARK)
    whole = lockup(MARK, "resonans", size=0.5, top=-90, start=150)
    as_r = lockup(MARK, size=0.5, top=-90, start=150)
    xs = [PAD + i * (W + GAP) for i in range(4)]
    y1, y2 = TOP, TOP + H + 110
    body = text(PAD, 56, "Resonans: two ways to handle the r", 30, weight=700)
    body += text(PAD, 86, f"Knot {MARK}, clean letters, the lower spacing. 6 Oct 2026.", 15, STEEL)
    body += "".join(text(x, TOP - 46, name.upper(), 12, STEEL, 600) for x, name in zip(xs, COLS))
    for y, title, note in ((y1, "1 · The logo is the knot", "The name is spelled whole, in type, only when the brand has to be named."),
                           (y2, "2 · The knot is the r", "One drawing everywhere. The letters under the line start at e.")):
        body += text(PAD, y - 16, title, 19, weight=700) + text(PAD + 250, y - 16, note, 14, STEEL)
    body += shown(knot, xs[0], y1, 70) + shown(whole, xs[1], y1) + header(whole, xs[2], y1) + avatar_and_card(knot, True, xs[3], y1)
    body += shown(as_r, xs[0], y2) + shown(as_r, xs[1], y2) + header(as_r, xs[2], y2) + avatar_and_card(as_r, False, xs[3], y2)
    body += text(xs[1] + W / 2, y2 + H + 24, "The same drawing: the name is already in the logo.", 13, STEEL, anchor="middle")
    wide, tall = 2 * PAD + 4 * W + 3 * GAP, y2 + H + 60
    sheet = OUT / "sheet-knot-options.svg"
    sheet.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {wide} {tall}" width="{wide}" height="{tall}">'
                     f'<rect width="{wide}" height="{tall}" fill="{PAPER}"/>{body}</svg>')
    subprocess.run(["rsvg-convert", str(sheet), "-o", str(sheet.with_suffix(".png"))], check=True, timeout=300)


if __name__ == "__main__":
    build()
