"""Round 15: six more drawings with no sound sign in them, by the logo-design skill's method.

Christian liked the story of one end sounding and the other answering, and liked the
crescendo, and agreed that arcs read as a wifi sign. So each concept here carries its idea
with the letters alone: no arcs, no dots, nothing added. Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/voice_more.py
"""
from build_concepts import stroke
from letters import GLYPHS, R, layout

WEIGHT = 16
NAME = "resonans"


def letter(ch, x, size=1.0, lift=0.0, turn=0.0, weight=WEIGHT):
    """One letter with its left edge at x: scaled about its middle line, lifted, then turned."""
    stems, curves, advance = GLYPHS[ch](0, 0)
    art = (stroke(stems, weight) if stems else "") + stroke(curves, weight)
    mid = advance * size / 2
    return (f'<g transform="translate({x:.1f},{-R - lift:.1f}) rotate({turn:.1f} {mid:.1f} 0) '
            f'scale({size:.3f}) translate(0,{R})">{art}</g>')


def jump(lift=38, first=0):
    """Jump: the first n stays on the line and its twin leaps off it."""
    spots, width = layout(NAME)
    lifts = dict(zip((i for i, ch in enumerate(NAME) if ch == "n"), (first, lift)))
    art = "".join(letter(ch, x, lift=lifts.get(i, 0)) for i, (ch, (x, _)) in enumerate(zip(NAME, spots)))
    return art, (-14, -2 * R - lift - 20, width + 28, 2 * R + lift + 40)


def stir():
    """Stir and leap: the first n lifts a little and its twin leaps three times as high."""
    return jump(lift=45, first=15)


def twins(lift=30):
    """Twins: the two n's are the same note, so they rise off the line together."""
    return jump(lift=lift, first=lift)


def re_colon(dot=11, space=26):
    """The letters re with a colon after them. Returns the drawing and where the colon ends."""
    spots, width = layout("re")
    x = width + WEIGHT / 2 + space + dot
    dots = "".join(f'<circle cx="{x:.1f}" cy="{y}" r="{dot}" fill="currentColor"/>' for y in (3 - 2 * R, -3))
    return "".join(letter(ch, at) for ch, (at, _) in zip("re", spots)) + dots, x + dot


def reply(space=26):
    """Reply: a colon after re, the two letters that start every reply."""
    head, end = re_colon(space=space)
    spots, width = layout("sonans")
    start = end + space + WEIGHT / 2
    art = head + "".join(letter(ch, start + x) for ch, (x, _) in zip("sonans", spots))
    return art, (-14, -2 * R - 20, start + width + 28, 2 * R + 40)


def in_step():
    """In step: the first letters tumble, each one less, and by the first n the word walks in line."""
    lifts, turns = (-20, 16, -9, 4, 0, 0, 0, 0), (-17, 12, -8, 0, 0, 0, 0, 0)
    spots, width = layout(NAME, gap=38)
    art = "".join(letter(ch, x, lift=lifts[i], turn=turns[i]) for i, (ch, (x, _)) in enumerate(zip(NAME, spots)))
    return art, (-22, -2 * R - 44, width + 40, 2 * R + 84)


def crescendo(small=0.56, large=1.3, bend=0.72, ink=0.55):
    """Crescendo: every letter is a step larger than the last, with the steps evened out by eye."""
    sizes = [small + (large - small) * (i / 7) ** bend for i in range(8)]
    spots, width = layout(NAME, sizes)
    art = "".join(letter(ch, x, size=s, weight=WEIGHT * s ** (ink - 1)) for ch, (x, _), s in zip(NAME, spots, sizes))
    top = R * large + WEIGHT
    return art, (-14, -R - top, width + 28, 2 * top)


def pair(first, second, gap=30):
    """Two letters side by side, for a square avatar. Each is (letter, size, lift, turn)."""
    (a, sa, la, ta), (b, sb, lb, tb) = first, second
    wa = GLYPHS[a](0, 0)[2] * sa
    wb = GLYPHS[b](0, 0)[2] * sb
    art = letter(a, 0, sa, la, ta, WEIGHT * sa ** -0.45) + letter(b, wa + gap, sb, lb, tb, WEIGHT * sb ** -0.45)
    width = wa + gap + wb
    side = max(width, 2 * R * max(sa, sb) + max(la, lb)) + 60
    return art, ((width - side) / 2, -R - max(la, lb) / 2 - side / 2, side, side)


def jump_avatar():
    """Jump, small: one n on the ground, one in the air."""
    return pair(("n", 1, 0, 0), ("n", 1, 38, 0))


def in_step_avatar():
    """In step, small: a tumbling r beside an upright s."""
    return pair(("r", 1, -6, -17), ("s", 1, 0, 0))


def crescendo_avatar():
    """Crescendo, small: the first letter small, the last one large."""
    return pair(("r", 0.6, 0, 0), ("s", 1.3, 0, 0))


def reply_avatar():
    """Reply, small: re and its colon, alone."""
    art, end = re_colon()
    side = end + 60
    return art, (-34, -R - side / 2, side, side)


def stir_avatar():
    """Stir and leap, small: one n a little off the ground, one well clear of it."""
    return pair(("n", 1, 15, 0), ("n", 1, 45, 0))


IDEAS = [("a", jump), ("b", in_step), ("c", crescendo), ("g", reply), ("h", stir), ("k", twins),
         ("d", jump_avatar), ("e", in_step_avatar), ("f", crescendo_avatar), ("i", reply_avatar), ("j", stir_avatar)]

if __name__ == "__main__":
    from story_sheet import build
    build(IDEAS, name="more", cols=6, rows=2)
