"""One A4 page to print for real: every cut at a ladder of true sizes, and a ladder of line weights.

The stress sheets are a simulation. This page is the proof. Print it at 100% on the
printer, press or shop you mean to use, then look for the smallest size that still reads.
Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/print_test.py
Writes final/resonans-print-test-A4.pdf and a PNG preview beside it.
"""
import subprocess
from pathlib import Path

from cuts import marks, words
from stress import raster

OUT = Path(__file__).parent / "final"
INK = "#000000"
MARK_SIZES, NAME_SIZES = (40, 25, 15, 10, 6), (70, 45, 28)
WEIGHTS = (0.10, 0.15, 0.20, 0.35, 0.50, 0.60, 0.70, 1.00, 1.27)


def text(x, y, words_, size=2.6, weight="normal"):
    return (f'<text x="{x}" y="{y}" font-family="Helvetica Neue, Arial" font-size="{size}" '
            f'font-weight="{weight}" fill="{INK}">{words_}</text>')


def placed(body, box, x, y, ink_width):
    """Put a drawing at (x, y) so that its ink, not its box, is `ink_width` mm wide."""
    ink = raster(body, box, 600)
    cols = ink.any(0).nonzero()[0]
    share = (cols[-1] - cols[0] + 1) / ink.shape[1]
    w = ink_width / share
    h = w * box[3] / box[2]
    return (f'<svg x="{x - (w - ink_width) / 2:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" '
            f'viewBox="{box[0]} {box[1]} {box[2]} {box[3]}" color="{INK}">{body}</svg>'), h


def page():
    out = text(12, 13, "Resonans print test", 5, "bold")
    out += text(12, 18.5, "Print at 100%. The first mark in each row should measure 40 mm across its ink.")
    y = 23
    for name, (body, box) in marks().items():
        out += text(12, y + 4, f"mark: {name}", 3, "bold")
        x = 52
        for size in MARK_SIZES:
            svg, _ = placed(body, box, x, y + (42 - size) / 2, size)
            out += svg + text(x, y + 46, f"{size} mm")
            x += size + 9
        y += 47.5
    for name, (body, box) in words().items():
        out += text(12, y + 3, f"name: {name}, at {', '.join(map(str, NAME_SIZES))} mm", 3, "bold")
        x = 12
        for size in NAME_SIZES:
            svg, _ = placed(body, box, x, y + 4.5, size)
            out += svg
            x += size + 9
        y += 19.5
    out += text(12, y + 5, "line weights, in mm", 3, "bold")
    for i, w in enumerate(WEIGHTS):
        x = 12 + i * 20.5
        out += (f'<line x1="{x}" y1="{y + 10}" x2="{x + 15}" y2="{y + 10}" stroke="{INK}" '
                f'stroke-width="{w}"/>') + text(x, y + 15, f"{w:.2f}")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" '
            f'viewBox="0 0 210 297"><rect width="210" height="297" fill="#FFFFFF"/>{out}</svg>')


if __name__ == "__main__":
    src = OUT / "resonans-print-test-A4.svg"
    src.write_text(page())
    subprocess.run(["rsvg-convert", "-f", "pdf", str(src), "-o", str(src.with_suffix(".pdf"))], check=True, timeout=120)
    subprocess.run(["rsvg-convert", "-w", "1240", str(src), "-o", str(src.with_suffix(".png"))], check=True, timeout=120)
    src.unlink()
