"""Round 4: eight ways to make the mark feel like resonance again. One sheet, ink on paper.

Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools \
      python brand/logo/explore.py
Writes concepts/sheet-explore.svg. Every direction returns SVG for a +-100 box.
Grain positions come from a seeded generator, so each run draws the same sand.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from build_concepts import draw, placed, stroke
from letters import R, _n, word
from plate import _move, sand

INK, PAPER = "#211513", "#FBF5F5"
REACH = 0.86
BOX = (-104, -104, 208, 208)


def still(x, y, n=1, m=5):
    """How little the plate moves at (x, y), with the outer frame pushed away."""
    return np.abs(_move(n, m, x, y)) + np.maximum(0, np.maximum(np.abs(x), np.abs(y)) - 0.78) * 3


def settle(count, heat, seed=7):
    """Drop `count` grains where the plate is still: denser the stiller it is."""
    rng, pts = np.random.default_rng(seed), []
    while len(pts) < count:
        p = rng.uniform(-REACH, REACH, (count * 4, 2))
        keep = rng.random(len(p)) < np.exp(-still(p[:, 0], p[:, 1]) / heat)
        pts.extend(p[keep])
    return np.array(pts[:count]) * 100 / REACH


def dots(pts, radius):
    return "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="currentColor"/>'
                   for (x, y), r in zip(pts, np.broadcast_to(radius, len(pts))))


def grain():
    """1. Sand: 1,500 grains, as on the live plate."""
    return dots(settle(1500, 0.045), 1.25)


def band():
    """2. Packed sand: the same figure as one solid shape, thick where sand piles up."""
    return f'<path d="{sand(band=0.3)}" fill="currentColor" fill-rule="evenodd"/>'


def halftone(size=15):
    """3. A grid of 225 dots. A dot is large where the plate is still."""
    g = np.linspace(-REACH, REACH, size)
    x, y = np.meshgrid(g, g)
    r = 5.6 * np.clip(1 - np.abs(_move(1, 5, x, y)) / 0.55, 0, 1) ** 1.4
    pts = np.column_stack([x.ravel(), y.ravel()]) * 100 / REACH
    return dots(pts[r.ravel() > 0.5], r.ravel()[r.ravel() > 0.5])


def tuning():
    """4. Scatter on the left, figure on the right: a message before and after it is tuned."""
    rng = np.random.default_rng(11)
    home = settle(1500, 0.04, seed=3)
    loose = rng.uniform(-100, 100, home.shape)
    drift = np.clip((20 - home[:, 0]) / 110, 0, 1)[:, None] ** 1.6
    return dots(home + (loose - home) * drift, 1.25)


def echoes():
    """5. The still line and two fainter lines either side of it, like a string caught mid-swing."""
    from cuts import RINGING, lines     # imported here because cuts is newer than this sheet
    return lines(RINGING)


def answer():
    """6. The word itself: the first n sounds and the second n answers with three echoes."""
    items, width = word(weights=[16] * 8)
    second = [i for i, ch in enumerate("resonans") if ch == "n"][1]
    x = float(items[second][0].split(",")[0][1:])
    extra = "".join(stroke(_n(x, 0, rise)[1], w) for rise, w in ((26, 8), (46, 5), (62, 3)))
    k = 200 / (width + 16)
    return f'<g transform="translate(-100,{R * k}) scale({k}) translate(8,0)">{draw(items)}{extra}</g>'


def chord():
    """7. One pen driven at 3 : 2, a fifth, and left to die away. No plate, only the ratio."""
    t = np.linspace(0, 30 * np.pi, 6000)
    fade = np.exp(-0.022 * t)
    x, y = 92 * fade * np.sin(3 * t + np.pi / 2), 92 * fade * np.sin(2 * t)
    return stroke("M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in zip(x, y)), 1.5)


def meeting(size=15):
    """8. Two voices: a dot grid where the waves from two points add up or cancel."""
    g = np.linspace(-1, 1, size)
    x, y = np.meshgrid(g, g)
    wave = np.cos(9 * np.hypot(x + 0.45, y)) + np.cos(9 * np.hypot(x - 0.45, y))
    r = 5.6 * np.clip(np.abs(wave) / 2, 0, 1) ** 1.3
    r[np.hypot(x, y) > 1.02] = 0
    pts = np.column_stack([x.ravel(), y.ravel()]) * 96
    return dots(pts[r.ravel() > 0.6], r.ravel()[r.ravel() > 0.6])


IDEAS = [grain, band, halftone, tuning, echoes, answer, chord, meeting]


def sheet():
    pw, ph, out = 470, 430, ""
    for i, fn in enumerate(IDEAS):
        ox, oy, mark = (i % 4) * pw, (i // 4) * ph, fn()
        out += f'<rect x="{ox}" y="{oy}" width="{pw}" height="{ph}" fill="{PAPER}" stroke="#E0D7D6"/>'
        out += (f'<text x="{ox + 20}" y="{oy + 34}" font-family="Helvetica Neue" font-size="17" '
                f'fill="#5D4F4D">{fn.__doc__.split(":")[0].strip()}</text>')
        out += placed(mark, BOX, ox + 95, oy + 60, 280, 280, INK)
        for j, px in enumerate((64, 32, 16)):
            out += placed(mark, BOX, ox + 150 + j * 80, oy + 388 - px / 2, px, px, INK)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {4 * pw} {2 * ph}" '
            f'width="{4 * pw}" height="{2 * ph}">{out}</svg>')


if __name__ == "__main__":
    (Path(__file__).parent / "concepts" / "sheet-explore.svg").write_text(sheet())
