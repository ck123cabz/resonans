"""Round 12: the idea inside the letters. Nothing is added to the name; the name itself builds.

"resonans" has no tall letters and no tails: all eight sit between the same two lines.
So each letter can be a little larger than the one before it, and the word becomes its
own crescendo: the swing that goes higher with every push. Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/voice_grow.py
"""
from build_concepts import stroke
from letters import FIT, GLYPHS, R, SIDES

WEIGHT, GAP = 16, 34


def growing(small=0.62, large=1.38, text="resonans", centred=True, even_stroke=False):
    """The name with letter i scaled from `small` to `large` in equal steps. Returns (svg, box)."""
    sizes = [small + (large - small) * i / (len(text) - 1) for i in range(len(text))]
    x, out = 0.0, ""
    for i, (ch, s) in enumerate(zip(text, sizes)):
        stems, curves, advance = GLYPHS[ch](0, 0, 0) if ch == "n" else GLYPHS[ch](0, 0)
        w = WEIGHT / s if even_stroke else WEIGHT
        lift = f"translate({x:.1f},{-R}) scale({s:.3f}) translate(0,{R})" if centred \
            else f"translate({x:.1f},0) scale({s:.3f})"
        out += f'<g transform="{lift}">{(stroke(stems, w) if stems else "") + stroke(curves, w)}</g>'
        if i + 1 < len(text):
            fit = FIT[SIDES[ch][1] + SIDES[text[i + 1]][0]]
            x += advance * s + (WEIGHT + GAP * fit) * (s + sizes[i + 1]) / 2
    width, top = x + advance * sizes[-1], R + R * large + WEIGHT
    height = 2 * top if centred else 2 * R * large + 2 * WEIGHT
    return out, (-14, (-R - top) if centred else (-2 * R * large - WEIGHT), width + 28, height)


def crescendo():
    """1. Crescendo: each letter a step larger and heavier, all centred on one line."""
    return growing()


def gentle():
    """2. Gentle: the same idea with half the growth."""
    return growing(0.8, 1.22)


def standing():
    """3. Standing: the letters grow upward from a flat baseline."""
    return growing(centred=False)


def one_weight():
    """4. One weight: the letters grow and the stroke stays the same."""
    return growing(even_stroke=True)


IDEAS = [("a", crescendo), ("b", gentle), ("c", standing), ("d", one_weight)]

if __name__ == "__main__":
    from story_sheet import build
    build(IDEAS, name="grow", cols=2, rows=2)
