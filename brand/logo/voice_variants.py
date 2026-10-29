"""Round 10: ways to keep the two-n story while losing the accent reading, plus avatar options.

Two blind readers of round 9 told the call-and-answer story unprompted, and all three who
saw arcs above an n also said it could pass for an accented letter such as n with a tilde.
Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/voice_variants.py
"""
import numpy as np

from build_concepts import draw, stroke
from letters import R, word
from voice import ECHO, WEIGHT, arcs

WIDE = ((14, 6), (8, 4.5), (8, 3))                # a clear gap first, so the arcs leave the letter


def tops(items):
    return [float(items[i][0].split(",")[0][1:]) + R for i, ch in enumerate("resonans") if ch == "n"]


def named(first, second, spread=58):
    items, width = word(weights=[WEIGHT] * 8)
    one, two = tops(items)
    rings = arcs(one, -R, R + WEIGHT / 2, first, spread) + arcs(two, -R, R + WEIGHT / 2, second, spread)
    return draw(items) + rings, (-12, -2 * R - 70, width + 24, 2 * R + 84)


def as_tested():
    """1. As the readers saw it: one arc on the first n, three on the second, 6 units off the letter."""
    return named(ECHO[:1], ECHO)


def lifted():
    """2. Lifted: the same arcs with a 14-unit gap first, wider than the letter under them."""
    return named(WIDE[:1], WIDE, spread=64)


def inside():
    """3. Inside: the arcs sit under each n's arch, so nothing rides above the word."""
    items, width = word(weights=[WEIGHT] * 8)
    out = ""
    for cx, spec in zip(tops(items), (((7, 6),), ((7, 6), (6, 4.5), (6, 3)))):
        r = R - WEIGHT / 2
        for gap, w in spec:
            r -= gap + w / 2
            x, y = r * np.sin(np.radians(74)), r * np.cos(np.radians(74))
            out += stroke(f"M{cx + x:.1f},{-R - y:.1f} A{r:.1f},{r:.1f} 0 0 0 {cx - x:.1f},{-R - y:.1f}", w)
            r -= w / 2
    return draw(items) + out, (-12, -2 * R - 24, width + 24, 2 * R + 40)


def striped():
    """4. Ringing letter: the first n is solid, the second is the same n drawn as three fine lines."""
    items, width = word(weights=[WEIGHT] * 8)
    second = [i for i, ch in enumerate("resonans") if ch == "n"][1]
    stems, curve, _ = items[second]
    x = float(stems.split(",")[0][1:])
    lines = ""
    for shift in (-5.5, 0, 5.5):                  # three 3.6-unit lines inside the 16-unit stroke
        r = R + shift
        lines += stroke(f"M{x - shift},0 V{-R} a{r},{r} 0 0 1 {2 * r},0 V0", 3.6)
    return draw(items[:second] + items[second + 1:]) + lines, (-12, -2 * R - 24, width + 24, 2 * R + 40)


def ringing(letter, spec=ECHO, box=(-52, -2 * R - 56, 208, 208)):
    items, _ = word(letter, weights=[WEIGHT])
    return draw(items) + arcs(R, -R, R + WEIGHT / 2, spec), box


def avatar_r():
    """5. Avatar: the brand's first letter, ringing."""
    return ringing("r", box=(-70, -2 * R - 56, 208, 208))


def avatar_n():
    """6. Avatar: the answering n by itself."""
    return ringing("n")


IDEAS = [("a", as_tested), ("b", lifted), ("c", inside), ("d", striped), ("e", avatar_r), ("f", avatar_n)]

if __name__ == "__main__":
    from story_sheet import build
    build(IDEAS, name="variants", cols=3, rows=2)
