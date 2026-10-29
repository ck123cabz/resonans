"""Round 8: the growing wave drawn as a mark, with its lockup, avatar and small sizes.

Both blind readers of round 7's wave said loose specks come together into one line that
swings harder as it goes. This file shows that same drawing, unchanged, in use, with the
three-frame plate beside it as the second finalist. Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools \
      python brand/logo/story_final.py
Writes concepts/sheet-final.svg and .png.
"""
import subprocess
from pathlib import Path

from build_concepts import draw, placed
from explore import INK, PAPER
from letters import R, word
from story_time import resonance, three_plates, with_name

ROOT = "#F14441"


def frames_with_name(weight=16):
    """The second finalist: three frames of one plate over the name."""
    items, width = word(weights=[weight] * 8)
    plates, box = three_plates()
    k = 0.62 * width / box[2]
    top = -2 * R - 70 - 52 * k
    body = f'<g transform="translate({width / 2},{top}) scale({k})">{plates}</g>{draw(items)}'
    return body, (-20, top - 52 * k - 20, width + 40, -top + 52 * k + 50)


def label(x, y, text):
    return (f'<text x="{x}" y="{y}" font-family="Helvetica Neue" font-size="16" '
            f'fill="#5D4F4D">{text}</text>')


def sheet():
    mark, MARK_BOX = resonance()
    out = f'<rect width="1800" height="1000" fill="{PAPER}"/>'
    out += label(40, 46, "1. The growing wave") + placed(mark, MARK_BOX, 60, 110, 780, 280, INK)
    out += label(40, 520, "Sizes: 192, 96, 48 and 24 px wide")
    for px, x in ((192, 60), (96, 290), (48, 420), (24, 500)):
        out += placed(mark, MARK_BOX, x, 600 - px / 6, px, px / 3, INK)
    out += label(40, 720, "Avatar, on ink and on root")
    for i, (ground, ink) in enumerate(((INK, PAPER), (ROOT, INK))):
        out += f'<circle cx="{130 + i * 220}" cy="850" r="90" fill="{ground}"/>'
        out += placed(mark, MARK_BOX, 55 + i * 220, 824, 150, 52, ink)
    body, box = with_name()
    out += label(900, 46, "With the name") + placed(body, box, 900, 80, 420, 330, INK)
    out += f'<rect x="1360" y="80" width="400" height="330" rx="8" fill="{INK}"/>'
    out += placed(body, box, 1400, 110, 320, 270, PAPER)
    body, box = frames_with_name()
    out += label(900, 520, "2. Three frames of one plate, with the name")
    out += placed(body, box, 900, 560, 420, 330, INK)
    plates, pbox = three_plates()
    out += label(1360, 520, "Sizes: 192, 96 and 48 px wide")
    for px, y in ((192, 580), (96, 690), (48, 760)):
        out += placed(plates, pbox, 1380, y, px, px / 3, INK)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1800 1000" width="1800" '
            f'height="1000">{out}</svg>')


if __name__ == "__main__":
    target = Path(__file__).parent / "concepts" / "sheet-final.svg"
    target.write_text(sheet())
    subprocess.run(["rsvg-convert", str(target), "-o", str(target.with_suffix(".png"))],
                   check=True, timeout=300)
