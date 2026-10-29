"""Round 5: the four directions from explore.py worth keeping, each with the wordmark.

Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools \
      python brand/logo/explore_refine.py
Writes concepts/sheet-refine.svg.
"""
from pathlib import Path

import numpy as np

from build_concepts import draw, placed, stroke
from explore import BOX, INK, PAPER, band, dots, echoes, settle, still
from letters import R, _n, word

ROOT = "#F14441"


def loose(count, seed):
    """Stray grains that have not reached a still line yet, thinning toward the edge."""
    rng = np.random.default_rng(seed)
    p = rng.uniform(-0.86, 0.86, (count * 6, 2))
    keep = rng.random(len(p)) < np.exp(-still(p[:, 0], p[:, 1]) / 0.3)
    return p[keep][:count] * 100 / 0.86


def piled():
    """A. Piled sand: the solid figure, with 420 grains still settling around it."""
    return band() + dots(settle(260, 0.09, seed=5), 1.5) + dots(loose(160, 9), 1.1)


def grains():
    """B. All grain: 2,400 grains and nothing solid, thick enough to hold at 32 px."""
    return dots(settle(2100, 0.06, seed=2), 1.7) + dots(loose(300, 4), 1.2)


def arriving():
    """C. Arriving: loose on the left, settled on the right. Noise turning into a figure."""
    rng = np.random.default_rng(11)
    home = np.vstack([settle(2300, 0.05, seed=3), loose(200, 8)])
    away = rng.uniform(-100, 100, home.shape)
    drift = np.clip((10 - home[:, 0]) / 105, 0, 1)[:, None] ** 1.5
    return dots(home + (away - home) * drift, 1.7)


def ringing():
    """D. Ringing: the solid figure with one fine line each side, caught mid-swing."""
    return echoes()


def answering(mark, weight=16):
    """The mark beside a wordmark whose second n answers the first with three echoes."""
    items, width = word(weights=[weight] * 8)
    second = [i for i, ch in enumerate("resonans") if ch == "n"][1]
    x = float(items[second][0].split(",")[0][1:])
    extra = "".join(stroke(_n(x, 0, rise)[1], w) for rise, w in ((26, 8), (46, 5), (62, 3)))
    body = (f'<g transform="translate(104,{-R}) scale(1.05)">{mark}</g>'
            f'<g transform="translate(262,0)">{draw(items)}{extra}</g>')
    return body, (-8, -172, 262 + width + 20, 250)


IDEAS = [piled, grains, arriving, ringing]


def sheet():
    pw, ph, out = 940, 470, ""
    for i, fn in enumerate(IDEAS):
        ox, oy, mark = (i % 2) * pw, (i // 2) * ph, fn()
        body, box = answering(mark)
        out += f'<rect x="{ox}" y="{oy}" width="{pw}" height="{ph}" fill="{PAPER}" stroke="#E0D7D6"/>'
        out += (f'<text x="{ox + 24}" y="{oy + 38}" font-family="Helvetica Neue" font-size="18" '
                f'fill="#5D4F4D">{fn.__doc__.split(":")[0].strip()}</text>')
        out += placed(mark, BOX, ox + 40, oy + 70, 300, 300, INK)
        out += placed(body, box, ox + 390, oy + 80, 500, 130, INK)
        out += f'<rect x="{ox + 390}" y="{oy + 250}" width="300" height="120" rx="8" fill="{INK}"/>'
        out += placed(body, box, ox + 410, oy + 270, 260, 80, PAPER)
        out += f'<rect x="{ox + 710}" y="{oy + 250}" width="120" height="120" rx="8" fill="{ROOT}"/>'
        out += placed(mark, BOX, ox + 725, oy + 265, 90, 90, INK)
        for j, px in enumerate((64, 32, 16)):
            out += placed(mark, BOX, ox + 60 + j * 90, oy + 425 - px / 2, px, px, INK)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {2 * pw} {2 * ph}" '
            f'width="{2 * pw}" height="{2 * ph}">{out}</svg>')


if __name__ == "__main__":
    (Path(__file__).parent / "concepts" / "sheet-refine.svg").write_text(sheet())
