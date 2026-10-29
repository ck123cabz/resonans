"""Two ways to line the six plate modes up as steps that end on the mark.

Christian said on 6 Oct that the modes are a progression toward resonance, usable for
anything that has a status or a sequence. Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/ladder.py
Writes concepts/sheet-ladder.svg and .png.
"""
import subprocess
from pathlib import Path

from build_concepts import placed
from cuts import SQUARE, lines

INK, PAPER, SOFT, FAINT = "#211513", "#FBF5F5", "#5D4F4D", "#CFC4C2"
LADDERS = [
    ("A. Thinning out: the pitch falls until one figure is left", [(5, 7), (3, 7), (1, 7), (3, 5), (1, 5)]),
    ("B. Take apart, find the core, ring: four busy figures, the single ring, then the mark",
     [(5, 7), (3, 7), (1, 7), (3, 5), (1, 3), (1, 5)]),
]


def figure(n, m, weight=5):
    """One mode as an even line, cropped where the mark is cropped."""
    return lines(((0, weight),), n, m)


def label(x, y, text, size=16, colour=SOFT):
    return (f'<text x="{x}" y="{y}" font-family="Helvetica Neue" font-size="{size}" '
            f'fill="{colour}">{text}</text>')


def sheet():
    out, y = f'<rect width="1500" height="1010" fill="{PAPER}"/>', 40
    for title, steps in LADDERS:
        out += label(40, y, title)
        for i, (n, m) in enumerate(steps):
            x = 40 + i * 236
            out += placed(figure(n, m), SQUARE, x, y + 20, 200, 200, INK)
            out += label(x + 4, y + 244, f"step {i + 1}  ·  mode {n}·{m}  ·  pitch {n * n + m * m}", 13)
            out += placed(figure(n, m, 9), SQUARE, 40 + i * 60, y + 270, 40, 40, INK)
        y += 350
    out += label(40, y, "In use: ladder B as a status row. Step 4 of 6 is current; done steps are ink, later steps are faint.")
    for i, (n, m) in enumerate(LADDERS[1][1]):
        colour = INK if i <= 3 else FAINT
        out += placed(figure(n, m, 7 if i != 3 else 10), SQUARE, 40 + i * 110, y + 24, 88, 88, colour)
        out += label(44 + i * 110, y + 134, ["Found", "Sorted", "Named", "Drafted", "Core", "Resonating"][i], 13,
                     INK if i == 3 else SOFT)
    out += label(40, y + 176, "The six words under the status row are placeholders of mine.", 13)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1500 1010" width="1500" height="1010">{out}</svg>'


if __name__ == "__main__":
    target = Path(__file__).parent / "concepts" / "sheet-ladder.svg"
    target.write_text(sheet())
    subprocess.run(["rsvg-convert", str(target), "-o", str(target.with_suffix(".png"))], check=True, timeout=300)
