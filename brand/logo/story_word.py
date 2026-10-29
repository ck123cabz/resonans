"""Round 6, the drawings that use the name or any other finished artwork as the figure.

mask_points turns any SVG into sand: it renders the file and picks points from the
inked pixels. That is what lets the same scatter-then-settle picture take any subject.
"""
import re
import subprocess
import tempfile
from pathlib import Path

import matplotlib.image as mpimg
import numpy as np

from build_concepts import draw
from explore import dots
from letters import R, word
from story import loosen, plate_rings, toward_left

FINAL = Path(__file__).parent / "final"


def mask_points(svg, count, rng, width=1600):
    """Random points inside any drawing: render it, then pick from the inked pixels."""
    x0, y0, w, _ = map(float, re.search(r'viewBox="([^"]+)"', Path(svg).read_text()).group(1).split())
    with tempfile.TemporaryDirectory() as tmp:
        png = Path(tmp) / "mask.png"
        subprocess.run(["rsvg-convert", "-w", str(width), str(svg), "-o", str(png)], check=True, timeout=60)
        ys, xs = np.nonzero(mpimg.imread(png)[:, :, 3] > 0.5)
    pick = rng.choice(len(xs), count)
    return np.column_stack([x0 + (xs[pick] + rng.random(count)) * w / width,
                            y0 + (ys[pick] + rng.random(count)) * w / width])


def settling(svg, count, start, span, spread, grain, seed=4):
    """The device on any subject: its shape in sand, loose on the left, settled on the right."""
    rng = np.random.default_rng(seed)
    home = mask_points(svg, count, rng)
    return dots(loosen(home, toward_left(home[:, 0], start, span, 2), spread, rng), grain)


def sand_word(seed=17):
    """Scatter to name: sand streams in from the left and packs into the word itself."""
    rng = np.random.default_rng(seed)
    x = -rng.exponential(90, 420)
    tail = np.column_stack([x, -50 + rng.normal(0, 1, 420) * (22 + 0.4 * np.abs(x))])
    body = settling(FINAL / "wordmark.svg", 5200, 170, 300, 13, 2.0)
    return body + dots(tail, 2.0), (-330, -190, 1340, 290)


def plate_o():
    """One gesture inside the name: the o is the plate, static on its left, rings on its right."""
    items, width = word(weights=[16] * 8)
    x = float(items[3][1].split(",")[0][1:])
    rest = draw(items[:3] + items[4:])
    disc, _ = plate_rings(count=1500, grain=2.1, seed=30)
    return (f'{rest}<g transform="translate({x + R},{-R}) scale(0.58)">{disc}</g>',
            (-12, -114, width + 24, 128))
