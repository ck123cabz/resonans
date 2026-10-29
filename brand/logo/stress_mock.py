"""Mock the logo on nine printed things, each through its own print method at its real size.

For every item the rule in lockup.choose picks the most detailed cut that holds, the
simulation in stress.printed says what the method leaves, and the result is drawn on the
item and enlarged beside it. Run from the repo root, after stress_sheets.py:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/stress_mock.py
Writes concepts/sheet-stress-mock.png.
"""
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from cuts import marks, words
from lockup import choose, lockup, shares
from scenes import SCENES
from stress import METHODS, printed, raster

OUT = Path(__file__).parent / "concepts"
INK, PAPER, SOFT = "#211513", "#FBF5F5", "#5D4F4D"
MARK_ORDER, WORD_ORDER = ["ringing", "fine", "medium", "solid"], ["three echoes", "one echo", "plain"]
plt.rcParams["font.family"] = ["Helvetica Neue", "Arial", "DejaVu Sans"]

# title, print method, what goes on it, its width in mm
ITEMS = [
    ("Business card", "Offset or digital print", "lockup", 50),
    ("Receipt", "Thermal receipt, 203 dpi", "lockup", 40),
    ("Stamp on kraft paper", "Rubber stamp", "lockup", 45),
    ("Shirt, left chest", "Screen print on a shirt", "lockup", 90),
    ("Shirt, back", "Screen print on a shirt", "mark", 250),
    ("Cap", "Embroidery", "mark", 50),
    ("Foil on a dark card", "Hot foil", "mark", 14),
    ("Shop window", "Cut vinyl", "lockup", 600),
    ("Tarpaulin, 2 m wide", "Offset or digital print", "lockup", 1500),
]


def cropped(body, box, px):
    ink = raster(body, box, px)
    rows, cols = np.nonzero(ink.any(1))[0], np.nonzero(ink.any(0))[0]
    return ink[rows[0]:rows[-1] + 1, cols[0]:cols[-1] + 1]


def tinted(mask, colour):
    rgb = [int(colour[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    out = np.zeros(mask.shape + (4,))
    out[..., :3], out[..., 3] = rgb, mask
    return out


def halves(result):
    """A lockup is wide, so show its left half over its right half at twice the size."""
    cut, gap = int(result.shape[1] * 0.452), result.shape[0] // 3      # between the s and the o
    spacer = np.zeros((gap, result.shape[1] - cut), bool)
    rest = result.shape[1] - cut
    return np.vstack([np.pad(result[:, :cut], ((0, 0), (0, rest - cut))), spacer, result[:, cut:]])


def pick(table, method, kind, width):
    """Which cuts go on this item, and a line saying so."""
    if kind == "mark":
        cut = choose(MARK_ORDER, table, method, width)
        return (cut or "solid", None), f"mark {width} mm: {cut or 'too small, even solid'}"
    mark_share, word_share = shares(words()["plain"][1][2] - 24)
    m = choose(MARK_ORDER, table, method, width * mark_share)
    w = choose(WORD_ORDER, table, method, width * word_share)
    note = (f"mark {width * mark_share:.0f} mm: {m or 'too small, even solid'}\n"
            f"name {width * word_share:.0f} mm: {w or 'too small, even plain'}")
    return (m or "solid", w or "plain"), note


def build():
    table = json.loads((OUT / "stress.json").read_text())
    by_name = {m[0]: m for m in METHODS}
    fig = plt.figure(figsize=(18, 15.5), facecolor=PAPER)
    grid = fig.add_gridspec(3, 6, width_ratios=[3, 2] * 3, wspace=0.08, hspace=0.3,
                            left=0.02, right=0.99, top=0.93, bottom=0.03)
    for i, (title, method, kind, width) in enumerate(ITEMS):
        (mark_cut, word_cut), note = pick(table, method, kind, width)
        body, box = marks()[mark_cut] if kind == "mark" else lockup(mark_cut, word_cut)
        ink = cropped(body, box, 1000 if kind == "mark" else 2600)
        _, line, gap, _ = by_name[method]
        result = printed(ink, width, line, gap)
        scene, zoom = fig.add_subplot(grid[i // 3, (i % 3) * 2]), fig.add_subplot(grid[i // 3, (i % 3) * 2 + 1])
        ground, colour, (cx, cy) = SCENES[title](scene)
        h = width * result.shape[0] / result.shape[1]
        scene.imshow(tinted(result, colour), extent=[cx - width / 2, cx + width / 2, cy - h / 2, cy + h / 2],
                     zorder=5, interpolation="lanczos")
        scene.set_aspect("equal")
        scene.axis("off")
        scene.set_title(f"{title}  ·  {method.lower()}", fontsize=12, color=INK, loc="left")
        zoom.set_facecolor(ground)
        zoom.imshow(tinted(halves(result) if kind == "lockup" else result, colour), interpolation="lanczos")
        zoom.set_xticks([])
        zoom.set_yticks([])
        zoom.margins(0.12)
        for side in zoom.spines.values():
            side.set_color("#E0D7D6")
        ok = "too small" not in note
        zoom.set_title("as printed, enlarged", fontsize=9.5, color=SOFT, loc="left")
        zoom.set_xlabel(note, fontsize=10.5, color=INK if ok else "#AC0315", loc="left")
    fig.suptitle("Nine printed things. Each shows the most detailed cut that survives its method at that size.",
                 fontsize=16, color=INK, x=0.02, ha="left")
    fig.savefig(OUT / "sheet-stress-mock.png", dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    build()
