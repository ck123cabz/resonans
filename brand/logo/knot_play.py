"""Round 21: play around the lockup Christian likes.

6 Oct 2026, 10:35 pm: "I like B for now, but can you try to play around with different ideas?
Maybe above the line, whatever." B is knot 20 as sketched, standing in for the r, with "esonans"
at half size under the long line. Each drawing here moves one thing: where the letters sit,
whether the name is whole, or how the r stands. Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/knot_play.py
Writes concepts/sheet-knot-play.png and concepts/sheet-knot-swap.png (the lockup he picked with knots
16, 18, 20 and 22), plus one bare PNG per drawing in concepts/blind-knot-play/ and blind-knot-swap/.
"""
from knot_chaos import lockup
from knot_line import arch

HALF = 0.5


def liked():
    """The one he likes: esonans at half size, under the line."""
    return lockup(20, size=HALF, top=-98, start=150)


def on_the_line():
    """On the line: the letters stand on the long line, as if it were ruled for them."""
    return lockup(20, size=HALF, top=-122 - 14 - 100 * HALF, start=160)


def whole_name_on():
    """Whole name on the line: resonans stands on the line, and the mark is its lead-in."""
    return lockup(20, "resonans", size=HALF, top=-122 - 14 - 100 * HALF, start=160)


def whole_name_under():
    """Whole name under the line: the same as the one he likes, with the r spelled out."""
    return lockup(20, "resonans", size=HALF, top=-98, start=150)


def standing():
    """Standing r: the stem shows above the knot and the arm stops short, so the r reads sooner."""
    return lockup(20, size=HALF, top=-128, start=150, line=-152, over=arch(-90, 40, arm=140, back=32))


def into_the_name():
    """Into the name: the line runs straight into the whole name and stops there."""
    return lockup(20, "resonans", size=HALF, top=-122 - 50 * HALF, start=356, reach=330)


def stacked():
    """Stacked: the mark above, the whole name under all of it, for a square space."""
    return lockup(20, "resonans", size=0.36, top=58, start=-10, reach=350)


def at_the_end():
    """At the end: small letters under the far end of the line, like a name under a signature."""
    return lockup(20, "resonans", size=0.24, top=-102, start=300 - 990 * 0.24 + 60, reach=360)


IDEAS = [("a", liked), ("b", on_the_line), ("c", whole_name_on), ("d", whole_name_under),
         ("e", standing), ("f", into_the_name), ("g", stacked), ("h", at_the_end)]



def _swap(seed):
    def draw():
        return lockup(seed, size=HALF, top=-98, start=150)
    draw.__doc__ = f"Knot {seed}{', the one he picked' if seed == 20 else ''}: the same lockup, only the knot changes"
    return draw


SWAPS = [(chr(97 + i), _swap(seed)) for i, seed in enumerate((16, 18, 20, 22))]

if __name__ == "__main__":
    from story_sheet import build
    build(IDEAS, name="knot-play", cols=4, rows=2)
    build(SWAPS, name="knot-swap", cols=2, rows=2)
