"""Round 20: Christian's pick to try, 6 Oct 2026, 10:30 pm: "b. as sketched knot 20. with the letters below".

The mark is knot 20 from round 18, drawn as sketched, and it stands in for the r. The letters
"esonans" sit below the long line. Three placements, since "below" could mean any of them.
Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/knot_under.py
Writes concepts/sheet-knot-under.png and one bare PNG per drawing in concepts/blind-knot-under/.
"""
from knot_chaos import lockup


def full():
    """Letters at the r's height: the arch is as tall as the letters and the line runs over the whole name."""
    return lockup(20, line=-130)


def half():
    """Letters at half size: hung just under the line, so the mark stays the bigger thing."""
    return lockup(20, size=0.5, top=-98, start=150)


def tucked():
    """Letters tucked in: small, under the line as you drew it, with the line a little longer."""
    return lockup(20, size=0.3, top=-100, start=152)


IDEAS = [("a", full), ("b", half), ("c", tucked)]

if __name__ == "__main__":
    from story_sheet import build
    build(IDEAS, name="knot-under", cols=3, rows=1)
