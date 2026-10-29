"""Round 6: drawings of "scattered, then resonating" that have to explain themselves.

Each function returns (svg, box). The grains are the same grains on both sides of a
picture: every grain has a home on the figure, and is pushed off it by a random step
that grows toward the scattered side. Seeds are fixed, so each run draws the same sand.
"""
import numpy as np

from build_concepts import stroke
from explore import dots, settle

BESSEL = (2.405, 5.520, 8.654)                    # first three zeros of J0
RINGS = np.array(BESSEL) / BESSEL[-1]             # still circles of a round plate: 0.278, 0.638, 1
SQUARE = (-104, -104, 208, 208)


def toward_left(x, start, span, power=1.3):
    """Looseness of a grain whose home is at x: 0 right of `start`, 1 a full `span` left of it."""
    return np.clip((start - x) / span, 0, 1) ** power


def in_disc(p, radius=1.0):
    r = np.hypot(p[:, 0], p[:, 1])
    out = r > radius
    p[out] *= (np.clip(2 * radius - r[out], 0.05, None) / r[out])[:, None]
    return p


def in_box(p, half_w, half_h):
    for axis, half in ((0, half_w), (1, half_h)):
        v = p[:, axis]
        v = np.where(v > half, 2 * half - v, v)
        p[:, axis] = np.clip(np.where(v < -half, -2 * half - v, v), -half, half)
    return p


def loosen(home, k, spread, rng):
    return home + rng.normal(0, 1, home.shape) * (spread * k)[:, None]


def ring_homes(count, rng, jitter=0.016):
    ring = rng.choice(3, count, p=RINGS / RINGS.sum())
    t = rng.uniform(0, 2 * np.pi, count)
    r = RINGS[ring] + rng.normal(0, jitter, count)
    return np.column_stack([r * np.cos(t), r * np.sin(t)])


def plate_rings(count=2600, grain=1.3, seed=21):
    """Static to ripple: a round plate, loose sand on the left, three still rings on the right."""
    rng = np.random.default_rng(seed)
    home = ring_homes(count, rng)
    p = in_disc(loosen(home, toward_left(home[:, 0], 0.1, 1.0), 0.38, rng))
    return dots(p * 100, grain), SQUARE


def bold_rings(seed=5):
    """42 dots: the same plate with few, large grains that grow as they settle."""
    rng = np.random.default_rng(seed)
    home = np.vstack([np.column_stack([r * np.cos(t), r * np.sin(t)])
                      for r, n in zip(RINGS, (6, 14, 22))
                      for t in [np.linspace(0, 2 * np.pi, n, endpoint=False) + 0.2 * n]])
    k = toward_left(home[:, 0], 0.3, 1.1, 1.1)
    p, size = in_disc(loosen(home, k, 0.42, rng), 0.97), 0.078 - 0.05 * k
    for _ in range(80):                           # nudge loose dots apart so none overlap
        gap = p[:, None] - p[None]
        dist = np.hypot(gap[..., 0], gap[..., 1]) + np.eye(len(p))
        push = np.clip(size[:, None] + size[None] + 0.02 - dist, 0, None) / dist
        p = in_disc(p + (gap * push[..., None]).sum(1) * 0.5 * (k > 0.02)[:, None], 0.97)
    return dots(p * 100, size * 100), SQUARE


def plate_clover(count=2400, seed=3):
    """Control with an edge: the mode 1, 5 figure on a square plate, loose on the left."""
    rng = np.random.default_rng(seed + 1)
    home = settle(count, 0.05, seed=seed)
    p = in_box(loosen(home, toward_left(home[:, 0], 0, 95), 42, rng), 100, 100)
    return dots(p, 1.4), SQUARE


def gathering(count=2600, seed=8):
    """Signal in noise: loose at the rim, still at the heart."""
    rng = np.random.default_rng(seed)
    home = ring_homes(count, rng)
    k = np.clip((np.hypot(home[:, 0], home[:, 1]) - 0.4) / 0.6, 0, 1) ** 1.4
    return dots(in_disc(loosen(home, k, 0.3, rng)) * 100, 1.3), SQUARE


def wave(count=2000, seed=13):
    """Noise to tone: loose sand on the left becomes one wave that grows to the right."""
    rng = np.random.default_rng(seed)
    x = rng.uniform(-150, 150, count)
    swing = 16 + 26 * np.clip((x + 30) / 180, 0, 1)
    home = np.column_stack([x, swing * np.sin(2 * np.pi * x / 75) + rng.normal(0, 2.6, count)])
    k = toward_left(x, -20, 125)
    p = home + rng.normal(0, 1, home.shape) * np.column_stack([10 * k, 46 * k])
    return dots(in_box(p, 150, 50), 1.6), (-156, -56, 312, 112)


def solid_rings(seed=21, weight=11, cut=0.1, scale=94):
    """Static to signal: the same plate, with the settled half drawn solid at a letter's weight."""
    rng = np.random.default_rng(seed)
    home = ring_homes(3400, rng, jitter=0.03)
    home = home[home[:, 0] < cut + 0.04]
    p = in_disc(loosen(home, toward_left(home[:, 0], cut, 1.0), 0.38, rng))
    arcs = ""
    for r in RINGS * scale:
        a = np.arccos(min(1, cut * scale / r))
        x, y = r * np.cos(a), r * np.sin(a)
        arcs += stroke(f"M{x:.1f},{-y:.1f} A{r:.1f},{r:.1f} 0 0 1 {x:.1f},{y:.1f}", weight)
    return dots(p * scale, 1.5) + arcs, SQUARE
