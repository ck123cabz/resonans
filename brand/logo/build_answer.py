"""Export the answering-n logo as outlined SVGs and PNGs, into final/.

Run from the repo root (needs Inkscape on PATH):
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/build_answer.py
The stroked originals stay in final/src/ for hand editing. Colours are the ones
build_final.py uses and are still unsettled.
"""
import subprocess

from answer import avatar, wordmark
from build_final import AIR, INK, OUT, filled, outline, page


def build():
    files = {}
    for cut in ("full", "small", "plain"):
        body, box = wordmark(cut)
        files[f"answer-wordmark-{cut}.svg"] = page(filled(outline(f"answer-wordmark-{cut}", body, box)), box)
    for cut in ("full", "small"):
        body, box = avatar(cut)
        art = filled(outline(f"answer-avatar-{cut}", body, box))
        files[f"answer-avatar-{cut}.svg"] = page(art, box)
        x, y, w, h = box
        tile = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w * 0.22:.0f}" fill="{INK}"/>'
        files[f"answer-avatar-{cut}-tile.svg"] = page(
            f'<g transform="translate({x + w / 2},{y + h / 2}) scale(0.74) translate({-x - w / 2},{-y - h / 2})">'
            f'{art}</g>', box, AIR, tile)
    for name, text in files.items():
        (OUT / name).write_text(text)
    png = OUT / "png"
    png.mkdir(exist_ok=True)
    for name, width in (("answer-wordmark-full", 2000), ("answer-wordmark-small", 1200),
                        ("answer-avatar-full-tile", 1024), ("answer-avatar-small-tile", 64),
                        ("answer-avatar-small-tile", 32), ("answer-avatar-small-tile", 16)):
        subprocess.run(["rsvg-convert", "-w", str(width), str(OUT / f"{name}.svg"),
                        "-o", str(png / f"{name}-{width}.png")], check=True, timeout=60)


if __name__ == "__main__":
    build()
