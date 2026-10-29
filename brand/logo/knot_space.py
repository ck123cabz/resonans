"""Round 23: spacing in the lockup Christian picked.

6 Oct 2026, about 11:00 pm: "Let's keep clean letters, but I think there's still a spacing issue.
I'm going to focus on that." He has not said which gap, so each drawing here moves one gap and
leaves the rest alone. Measures are in pens: the line is 8 units wide, so 1 pen is 8 units.
Today's lockup has 2 pens of air between the line and the letters, 5 pens between the arch and
the e, about 2 pens between two stems, and a line that stops level with the s.
Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/knot_space.py
Writes concepts/sheet-knot-space.png, then concepts/sheet-knot-space-lower.png: more variations at the
lower letter height he chose from the first sheet. Bare PNGs go to concepts/blind-knot-space*/.
"""
from knot_chaos import lockup
from knot_line import arch
from letters import layout

HALF, PEN = 0.5, 8


def spaced(top=-98, start=150, gap=34, past=0, size=HALF):
    """The picked lockup with one or more gaps changed. `past` is how far the line runs beyond the s, in units."""
    width = layout("esonans", [size] * 7, gap=gap, weight=PEN / size)[1]
    return lockup(20, size=size, top=top, start=start, gap=gap, reach=start + width + past)


def now():
    """Now: the lockup as picked."""
    return spaced()


def lower():
    """Letters lower: 3 pens of air under the line, where now there are 2."""
    return spaced(top=-90)


def higher():
    """Letters higher: 1 pen of air under the line."""
    return spaced(top=-106)


def later():
    """Letters start later: the e moves 2 pens right, clear of the corner where the line turns."""
    return spaced(start=166)


def tighter():
    """Letters tighter: stems 1.3 pens apart, where now they are 2."""
    return spaced(gap=22)


def looser():
    """Letters looser: stems 3 pens apart."""
    return spaced(gap=48)


def past_the_s():
    """Line runs on: it goes 3 pens past the s, so the word does not stop the line."""
    return spaced(past=24)


def tuned():
    """My pick of the gaps: letters 2.5 pens under the line, starting 1 pen later, a little tighter, line 2 pens past the s."""
    return spaced(top=-94, start=158, gap=28, past=16)


IDEAS = [("a", now), ("b", lower), ("c", higher), ("d", later), ("e", tighter), ("f", looser), ("g", past_the_s), ("h", tuned)]

LOW = -90                                           # the height he chose from the first sheet: 3 pens of air under the line


def _low(title, **how):
    def draw():
        return spaced(top=LOW, **how)
    draw.__doc__ = title
    return draw


LOWER = [
    ("a", _low("Lower, as on the first sheet: nothing else moved")),
    ("b", _low("e 1 pen later: a little clear of the corner", start=158)),
    ("c", _low("e 2 pens later: well clear of the corner", start=166)),
    ("d", _low("Tighter: stems 1.6 pens apart", gap=28)),
    ("e", _low("Tighter still: stems 1.3 pens apart", gap=22)),
    ("f", _low("Line runs on: 3 pens past the s", past=24)),
    ("g", _low("Bigger letters: a sixth larger, same air above", size=0.58)),
    ("h", _low("My pick at this height: e 1 pen later, stems 1.6 pens apart, line 2 pens past the s", start=158, gap=28, past=16)),
]



def near():
    """e close: the e sits 2 pens from the arch, the same gap the letters keep between themselves."""
    return spaced(top=LOW, start=124)


def near_and_big():
    """e close, letters bigger: the letters grow toward the arch's size, so the mark looks like one of them."""
    return spaced(top=LOW, start=128, size=0.72)


def near_and_standing():
    """e close, r standing: the stem shows above the knot, the arm stops short, and the knot hangs below the letters."""
    return lockup(20, size=HALF, top=-128, start=112, line=-152, over=arch(-90, 40, arm=140, back=32))


# Three tries at one question: what makes the eye take the mark as the r of the name?
AS_R = [("a", near), ("b", near_and_big), ("c", near_and_standing)]

if __name__ == "__main__":
    from story_sheet import build
    build(IDEAS, name="knot-space", cols=4, rows=2)
    build(LOWER, name="knot-space-lower", cols=4, rows=2)
    build(AS_R, name="knot-as-r", cols=3, rows=1)
