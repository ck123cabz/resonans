"""Draw the stress test: the ringing mark across ten print methods, and the size each cut needs.

Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/stress_sheets.py
Writes concepts/sheet-stress-matrix.png, concepts/sheet-stress-sizes.png and concepts/stress.json.
"""
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from cuts import marks, words
from stress import BREAKS, HOLDS, METHODS, SIMPLER, Subject

OUT = Path(__file__).parent / "concepts"
INK, PAPER, SOFT = "#211513", "#FBF5F5", "#5D4F4D"
TONE = {HOLDS: "#016359", SIMPLER: "#765402", BREAKS: "#AC0315"}
SIZES = (80, 40, 25, 15, 10, 6)
plt.rcParams["font.family"] = ["Helvetica Neue", "Arial", "DejaVu Sans"]


def subjects():
    m, w = marks(), words()
    out = {name: Subject(body, m["solid"][0], box) for name, (body, box) in m.items()}
    out.update({name: Subject(body, w["plain"][0], box, px=1400) for name, (body, box) in w.items()})
    return out, list(m), list(w)


def show(ax, ink, tone=None):
    ax.imshow(np.where(ink, 0.13, 0.985), cmap="gray", vmin=0, vmax=1, interpolation="lanczos")
    ax.set_xticks([])
    ax.set_yticks([])
    for side in ax.spines.values():
        side.set_color(tone or "#E0D7D6")
        side.set_linewidth(2.2 if tone else 0.8)


def limits(method):
    name, line, gap, _ = method
    return name if line is None else f"{name}\nline {line:.2f} mm, gap {gap:.2f} mm"


def matrix(subject):
    """Every method at every size, for one cut. Each cell is what the method would leave."""
    fig, axes = plt.subplots(len(METHODS), len(SIZES), figsize=(13.5, 21.5), facecolor=PAPER)
    for r, method in enumerate(METHODS):
        for c, size in enumerate(SIZES):
            result, verdict = subject.at(size, method)
            show(axes[r, c], result, TONE[verdict])
            axes[r, c].set_title(f"{size} mm · {verdict}", fontsize=10, color=TONE[verdict], pad=4)
        axes[r, 0].set_ylabel(limits(method), fontsize=9.5, color=INK, rotation=0, ha="right",
                              va="center", labelpad=12)
    fig.suptitle("The ringing mark, as drawn on 6 Oct, through 10 print methods at 6 widths",
                 fontsize=15, color=INK, x=0.02, ha="left", y=0.995)
    fig.text(0.02, 0.978, "holds: every line and gap survives.   simpler: the figure and its 5 openings "
             "survive, some lines or gaps do not.   breaks: an opening fills or the figure is gone.",
             fontsize=10, color=SOFT)
    fig.subplots_adjust(left=0.17, right=0.99, top=0.955, bottom=0.01, wspace=0.08, hspace=0.22)
    fig.savefig(OUT / "sheet-stress-matrix.png", dpi=110)
    plt.close(fig)


def sizes(subs, mark_names, word_names):
    """The cuts, and the smallest width in mm at which each one holds in each method."""
    names = mark_names + word_names
    table = {n: {m[0]: subs[n].smallest(m) for m in METHODS} for n in names}
    (OUT / "stress.json").write_text(json.dumps(table, indent=1))
    fig = plt.figure(figsize=(15, 11.5), facecolor=PAPER)
    grid = fig.add_gridspec(3, 12, height_ratios=[2.6, 1.0, 4.6], hspace=0.28, wspace=0.3,
                            left=0.03, right=0.98, top=0.9, bottom=0.03)
    for i, n in enumerate(mark_names):
        ax = fig.add_subplot(grid[0, i * 3:i * 3 + 3])
        show(ax, subs[n].ink)
        ax.set_title(f"mark: {n}", fontsize=12, color=INK)
    for i, n in enumerate(word_names):
        ax = fig.add_subplot(grid[1, i * 4:i * 4 + 4])
        show(ax, subs[n].ink)
        ax.set_title(f"name: {n}", fontsize=12, color=INK)
    ax = fig.add_subplot(grid[2, :])
    ax.axis("off")
    cell = [[("none" if table[n][m[0]] is None else f"{np.ceil(table[n][m[0]]):.0f}") for n in names]
            for m in METHODS]
    t = ax.table(cellText=cell, rowLabels=[limits(m).replace("\n", "  ·  ") for m in METHODS],
                 colLabels=[f"{'mark' if n in mark_names else 'name'}\n{n}" for n in names],
                 bbox=[0.36, 0, 0.64, 1], cellLoc="center")
    t.auto_set_font_size(False)
    t.set_fontsize(11)
    for (r, c), box in t.get_celld().items():
        box.set_edgecolor("#E0D7D6")
        box.set_facecolor(PAPER)
        box.get_text().set_color(INK if r else SOFT)
    fig.suptitle("Smallest width, in mm, at which every line and gap of a cut survives",
                 fontsize=15, color=INK, x=0.03, ha="left")
    fig.savefig(OUT / "sheet-stress-sizes.png", dpi=110)
    plt.close(fig)


if __name__ == "__main__":
    subs, mark_names, word_names = subjects()
    matrix(subs["ringing"])
    sizes(subs, mark_names, word_names)
