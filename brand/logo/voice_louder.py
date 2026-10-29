"""Round 11: the answer has to look louder than the call, and less like a wifi sign.

A reader who was told the story said the second n's fine arcs made it "look quieter, not
louder", and that arcs pointing straight up did not look like one letter answering another.
Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/voice_louder.py
"""
from answer import WEIGHT, rings
from build_concepts import draw, stroke
from letters import R, word
from voice_variants import tops

def lettered(extra_for):
    items, width = word(weights=[WEIGHT] * 8)
    one, two = tops(items)
    return draw(items) + extra_for(one, two), (-12, -2 * R - 78, width + 24, 2 * R + 92)


def even():
    """1. Even: one arc for the call, three for the answer, all at one weight so three reads as more."""
    return lettered(lambda a, b: rings(a, (7,), 9, 30, 150) + rings(b, (7, 7, 7), 9, 30, 150))


def swelling():
    """2. Swelling: the answer's arcs get heavier as they go out, so the reply grows."""
    return lettered(lambda a, b: rings(a, (5,), 9, 30, 150) + rings(b, (5, 7.5, 10), 9, 30, 150))


def facing():
    """3. Facing: the call leans toward the second n and the answer leans back, three times as much."""
    return lettered(lambda a, b: rings(a, (7,), 9, 28, 78) + rings(b, (7, 7, 7), 9, 97, 137))


def bigger():
    """4. Bigger: no arcs at all. The second n is the first n, a third larger."""
    items, width = word(weights=[WEIGHT] * 8)
    second = [i for i, ch in enumerate("resonans") if ch == "n"][1]
    x, k = float(items[second][0].split(",")[0][1:]), 1.34
    grow = 2 * R * (k - 1)
    big = stroke(f"M{x},0 V{-R * k} a{R * k},{R * k} 0 0 1 {2 * R * k},0 V0", WEIGHT)
    last = draw(items[second + 1:])
    return (draw(items[:second]) + big + f'<g transform="translate({grow},0)">{last}</g>',
            (-12, -2 * R - 78, width + grow + 24, 2 * R + 92))


def gain():
    """5. Gain: no arcs. Every letter is a little heavier than the one before it."""
    items, width = word(weights=[7 + i * 15 / 7 for i in range(8)])
    return draw(items), (-12, -2 * R - 78, width + 30, 2 * R + 92)


IDEAS = [("a", even), ("b", swelling), ("c", facing), ("d", bigger), ("e", gain)]

if __name__ == "__main__":
    from story_sheet import build
    build(IDEAS, name="louder", cols=3, rows=2)
