"""Simulate print methods on a logo and say whether it survives at a given size.

The model is first-order and has two rules per method, taken from print shops' own
artwork guides: a line thinner than the method's minimum does not print, and a gap
narrower than its minimum fills in. A thermal printer is modelled by its dot grid.
It is a filter for obvious failures, not a substitute for a printed proof.
"""
import subprocess
import tempfile
from pathlib import Path

import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage

# name, thinnest line in mm, narrowest gap in mm, whose guide the numbers come from
METHODS = [
    ("Offset or digital print", 0.10, 0.20, "Print Peppermint"),
    ("Letterpress", 0.15, 0.30, "Print Peppermint"),
    ("Rubber stamp", 0.20, 0.20, "Rubber Stamps 4U"),
    ("Thermal receipt, 203 dpi", None, None, "Zebra: 8 dots per mm"),
    ("Screen print on a shirt", 0.35, 0.70, "Print Your Cause"),
    ("Emboss or deboss", 0.50, 1.00, "Print Peppermint"),
    ("Hot foil", 0.60, 0.60, "Print Peppermint"),
    ("Screen print on a cap", 0.70, 0.70, "Print Your Cause"),
    ("Embroidery", 1.27, 1.27, "Printify; gap assumed equal to line"),
    ("Cut vinyl", 3.20, 3.20, "Decals.com"),
]
HOLDS, SIMPLER, BREAKS = "holds", "simpler", "breaks"


def raster(body, box, px=900):
    """Render SVG to a boolean ink array the size of its box."""
    x, y, w, h = box
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" '
           f'color="#000">{body}</svg>')
    with tempfile.TemporaryDirectory() as tmp:
        src, png = Path(tmp) / "a.svg", Path(tmp) / "a.png"
        src.write_text(svg)
        subprocess.run(["rsvg-convert", "-w", str(px), str(src), "-o", str(png)], check=True, timeout=120)
        return mpimg.imread(png)[:, :, 3] > 0.5


def opened(a, r):
    """Remove everything narrower than a disc of radius r pixels."""
    if r < 0.5:
        return a
    core = ndimage.distance_transform_edt(a) > r
    return ndimage.distance_transform_edt(~core) <= r if core.any() else np.zeros_like(a)


def printed(ink, width_mm, line, gap, dpi=203):
    """What the method leaves of `ink` when its ink is `width_mm` wide."""
    mm_per_px = width_mm / ink.shape[1]
    if line is None:                               # a dot grid: average onto dots, then on or off
        k = width_mm / 25.4 * dpi / ink.shape[1]
        soft = ndimage.gaussian_filter(ink.astype(float), 0.4 / k) if k < 1 else ink.astype(float)
        dots = ndimage.zoom(soft, k, order=1) > 0.5
        back = ndimage.zoom(dots, (ink.shape[0] / dots.shape[0], ink.shape[1] / dots.shape[1]), order=0)
        out = np.zeros_like(ink)
        h, w = min(ink.shape[0], back.shape[0]), min(ink.shape[1], back.shape[1])
        out[:h, :w] = back[:h, :w]
        return out
    pad = int(gap / 2 / mm_per_px) + 3
    a = np.pad(ink, pad)
    a = opened(a, line / 2 / mm_per_px)
    a = ~opened(~a, gap / 2 / mm_per_px)
    return a[pad:-pad, pad:-pad]


def census(ink, floor):
    """Count the separate pieces of ink and the enclosed patches of paper bigger than `floor` pixels."""
    a = np.pad(ink, 2)
    pieces, n = ndimage.label(a)
    paper, m = ndimage.label(~a)
    sizes = ndimage.sum(~a, paper, range(1, m + 1))
    enclosed = [i + 1 for i in range(m) if i + 1 != paper[0, 0] and sizes[i] > floor]
    big = ndimage.sum(a, pieces, range(1, n + 1)) > floor
    return int(big.sum()), enclosed, paper


class Subject:
    """One cut of the mark or the name, with the simplest cut of its family as its core."""

    def __init__(self, body, core_body, box, px=900):
        full, core = raster(body, box, px), raster(core_body, box, px)
        rows, cols = np.nonzero(full.any(1))[0], np.nonzero(full.any(0))[0]
        crop = (slice(rows[0], rows[-1] + 1), slice(cols[0], cols[-1] + 1))
        self.ink, core = full[crop], core[crop]          # both cut to the subject's own ink
        self.floor = (self.ink.shape[1] / 180) ** 2
        self.pieces, enclosed, _ = census(self.ink, self.floor)
        self.holes = len(enclosed)
        self.core_pieces, core_holes, paper = census(core, self.floor)
        seeds = ndimage.center_of_mass(np.ones_like(paper), paper, core_holes)
        self.seeds = [(int(r) - 2, int(c) - 2) for r, c in seeds]

    def verdict(self, result):
        pieces, enclosed, paper = census(result, self.floor)
        open_seeds = all(not result[r, c] and paper[r + 2, c + 2] != paper[0, 0] for r, c in self.seeds)
        if not open_seeds or pieces < self.core_pieces:
            return BREAKS
        return HOLDS if (pieces, len(enclosed)) == (self.pieces, self.holes) else SIMPLER

    def at(self, width_mm, method):
        result = printed(self.ink, width_mm, method[1], method[2])
        return result, self.verdict(result)

    def smallest(self, method, low=1.0, high=800.0, steps=11):
        """The smallest width in mm at which every line and gap of this cut survives the method."""
        if self.at(high, method)[1] != HOLDS:
            return None
        for _ in range(steps):
            mid = (low * high) ** 0.5
            low, high = (low, mid) if self.at(mid, method)[1] == HOLDS else (mid, high)
        return high
