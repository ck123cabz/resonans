"""Round 7: the same story drawn on forms that already run left to right in time.

Round 6's blind reading found that a half-scattered round figure reads as falling
apart. A waveform, a line of text and a row of frames are read from left to right,
so the scatter comes first. Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools \
      python brand/logo/story_time.py
"""
import numpy as np

from build_concepts import draw, stroke
from explore import dots
from letters import R, word
from story import in_box, in_disc, loosen, ring_homes, toward_left, wave
from story_sheet import FINAL_WORD, build
from story_word import settling

NECK, PERIOD, GROWTH = -40, 70, 48 / 210      # where the wave starts, its length, its rise per unit


def swing(x):
    """x = t sin(wt): the motion of anything driven at its own pitch. Its size grows in a straight line."""
    t = np.clip(x - NECK, 0, None)
    return -GROWTH * t * np.sin(2 * np.pi * t / PERIOD)


def resonance(grains=520, weight=13, seed=2):
    """Noise, a neck, a growing wave: loose sand narrows to one line, then swings wider each time."""
    rng = np.random.default_rng(seed)
    x = rng.uniform(-170, NECK + 12, grains)
    k = toward_left(x, NECK, 130, 1.2)
    p = np.column_stack([x, np.zeros(grains)]) + rng.normal(0, 1, (grains, 2)) * np.column_stack([6 * k, 2 + 40 * k])
    xs = np.linspace(NECK, 170, 420)
    line = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in zip(xs, swing(xs)))
    return dots(in_box(p, 170, 52), 2.6) + stroke(line, weight), (-178, -62, 356, 124)


def first_wave():
    """Round 6's G again: a block of loose sand becomes one wave made of sand."""
    return wave()


def tuned_word():
    """The name tunes itself: the r is loose sand and each letter after it sits tighter."""
    return settling(FINAL_WORD, 6500, 800, 800, 13, 2.0, seed=12), (-40, -150, 1060, 200)


def three_plates(seed=9):
    """Three frames of one plate: loose sand, sand finding its rings, three still rings."""
    rng, out = np.random.default_rng(seed), ""
    for i, k in enumerate((1.0, 0.2, 0.0)):
        home = ring_homes(950, rng)
        p = in_disc(loosen(home, np.full(len(home), k), 0.38, rng)) * 45
        out += dots(p + [(i - 1) * 110, 0], 1.5)
    return out, (-162, -52, 324, 104)


def with_name():
    """The growing wave above the name, sharing its stroke weight."""
    mark, _ = resonance(weight=16)
    items, width = word(weights=[16] * 8)
    k = width / 340
    return (f'<g transform="translate({width / 2},{-2 * R - 60 - 62 * k}) scale({k})">{mark}</g>'
            f'{draw(items)}'), (-20, -2 * R - 80 - 124 * k, width + 40, 2 * R + 100 + 124 * k)


IDEAS = [("a", first_wave), ("b", resonance), ("c", tuned_word), ("d", three_plates), ("e", with_name)]

if __name__ == "__main__":
    build(IDEAS, name="time", cols=3, rows=2)
