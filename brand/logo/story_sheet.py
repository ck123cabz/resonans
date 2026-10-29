"""Lay the round 6 drawings on one sheet and export each alone for a blind reading.

Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools \
      python brand/logo/story_sheet.py
Writes concepts/sheet-story.svg and concepts/blind-story/<letter>.png. A blind file shows
one drawing with no name and no caption, so a fresh reader can say what it tells.
"""
import subprocess
from pathlib import Path

from build_concepts import placed
from explore import BOX, INK, PAPER
from explore_refine import arriving
from story import bold_rings, gathering, plate_clover, plate_rings, solid_rings, wave
from story_word import plate_o, sand_word, settling

HERE = Path(__file__).parent
FINAL_WORD = HERE / "final" / "wordmark.svg"
CLIENT = HERE.parent.parent / "pickleblinders" / "brand" / "marks" / "icon-soot.svg"


def control():
    """Round 5's C, unchanged: loose on the left, the four-lobe figure on the right, no edge."""
    return arriving(), BOX


def client():
    """The same device on another subject: the Pickle Blinders icon settling out of sand."""
    import re
    x0, y0, w, h = map(float, re.search(r'viewBox="([^"]+)"', CLIENT.read_text()).group(1).split())
    grains = settling(CLIENT, 14000, x0 + 0.36 * w, 0.4 * w, 0.1 * w, w / 420, seed=6)
    return grains, (x0 - 0.12 * w, y0 - 0.06 * h, 1.2 * w, 1.12 * h)


IDEAS = [("a", control), ("b", plate_clover), ("c", plate_rings), ("d", solid_rings),
         ("e", bold_rings), ("f", gathering), ("g", wave), ("h", sand_word), ("i", plate_o),
         ("j", client)]


def tile(letter, fn, ox, oy, pw, ph):
    body, box = fn()
    wide = box[2] > 1.4 * box[3]
    out = f'<rect x="{ox}" y="{oy}" width="{pw}" height="{ph}" fill="{PAPER}" stroke="#E0D7D6"/>'
    out += (f'<text x="{ox + 20}" y="{oy + 34}" font-family="Helvetica Neue" font-size="16" '
            f'fill="#5D4F4D">{letter.upper()}. {fn.__doc__.split(":")[0].strip()}</text>')
    if wide:
        out += placed(body, box, ox + 30, oy + 80, pw - 60, 210, INK)
        for j, width in enumerate((250, 130)):
            out += placed(body, box, ox + 40 + j * 290, oy + 330, width, 70, INK)
    else:
        out += placed(body, box, ox + (pw - 290) / 2, oy + 52, 290, 290, INK)
        for j, px in enumerate((64, 32, 16)):
            out += placed(body, box, ox + pw / 2 - 110 + j * 90, oy + 392 - px / 2, px, px, INK)
    return out, body, box


def build(ideas=None, name="story", cols=4, rows=3):
    """Write concepts/sheet-<name>.svg and .png, and one bare PNG per idea in concepts/blind-<name>/."""
    pw, ph, out = 480, 440, ""
    blind = HERE / "concepts" / f"blind-{name}"
    blind.mkdir(parents=True, exist_ok=True)
    for i, (letter, fn) in enumerate(ideas or IDEAS):
        svg, body, box = tile(letter, fn, (i % cols) * pw, (i // cols) * ph, pw, ph)
        out += svg
        x, y, w, h = box
        pad = 0.12 * max(w, h)
        alone = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x - pad} {y - pad} '
                 f'{w + 2 * pad} {h + 2 * pad}" color="{INK}"><rect x="{x - pad}" y="{y - pad}" '
                 f'width="{w + 2 * pad}" height="{h + 2 * pad}" fill="{PAPER}"/>{body}</svg>')
        (blind / f"{letter}.svg").write_text(alone)
        subprocess.run(["rsvg-convert", "-w", "1000", str(blind / f"{letter}.svg"),
                        "-o", str(blind / f"{letter}.png")], check=True, timeout=120)
        (blind / f"{letter}.svg").unlink()
    sheet = HERE / "concepts" / f"sheet-{name}.svg"
    sheet.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cols * pw} {rows * ph}" '
                     f'width="{cols * pw}" height="{rows * ph}"><rect width="{cols * pw}" '
                     f'height="{rows * ph}" fill="{PAPER}"/>{out}</svg>')
    subprocess.run(["rsvg-convert", str(sheet), "-o", str(sheet.with_suffix(".png"))],
                   check=True, timeout=300)


if __name__ == "__main__":
    build()
