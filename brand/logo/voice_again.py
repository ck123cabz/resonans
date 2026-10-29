"""Round 13: the answer is the letter itself, said again and larger.

"Re" means again. So the second n is drawn again around itself, each time bigger: whole
n's with legs, where earlier rounds put arcs on top that readers took for a wifi sign.
Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/voice_again.py
"""
from build_concepts import stroke
from letters import FIT, GLYPHS, R, SIDES

WEIGHT, GAP = 16, 34


def again(x, steps):
    """Larger copies of an n around the n whose left stem is at x. steps = (gap, weight) outward."""
    out, d = "", WEIGHT / 2
    for gap, w in steps:
        d += gap + w / 2
        out += stroke(f"M{x - d:.1f},0 V{-R} a{R + d:.1f},{R + d:.1f} 0 0 1 {2 * (R + d):.1f},0 V0", w)
        d += w / 2
    return out, d - WEIGHT / 2


def name(first=(), second=((8, 8), (8, 8)), text="resonans"):
    """The name, with room made either side of each n for the copies it carries."""
    plan = dict(zip([i for i, ch in enumerate(text) if ch == "n"], (first, second)))
    x, out, top = 0.0, "", 0.0
    for i, ch in enumerate(text):
        steps = plan.get(i, ())
        room = sum(g + w for g, w in steps)
        x += room
        stems, curves, advance = GLYPHS[ch](x, 0, 0) if ch == "n" else GLYPHS[ch](x, 0)
        out += (stroke(stems, WEIGHT) if stems else "") + stroke(curves, WEIGHT)
        if steps:
            copies, reach = again(x, steps)
            out, top = out + copies, max(top, reach)
        if i + 1 < len(text):
            x += advance + room + WEIGHT + GAP * FIT[SIDES[ch][1] + SIDES[text[i + 1]][0]]
    return out, (-14, -2 * R - top - 16, x + advance + 28, 2 * R + top + 32)


def said_again():
    """1. Said again: the second n is drawn twice more around itself, bigger each time."""
    return name()


def one_then_three():
    """2. One, then three: the first n is said once more, the second three times more."""
    return name(((8, 7),), ((8, 7), (8, 7), (8, 7)))


def swelling():
    """3. Swelling: the copies of the second n get heavier as they get bigger."""
    return name((), ((8, 6), (8, 9), (9, 12)))


def mark():
    """4. Avatar: the n and its two larger selves, alone."""
    return name(((8, 8), (8, 8)), (), text="n")


IDEAS = [("a", said_again), ("b", one_then_three), ("c", swelling), ("d", mark)]

if __name__ == "__main__":
    from story_sheet import build
    build(IDEAS, name="again", cols=2, rows=2)
