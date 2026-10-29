"""Round 18: the knot-and-line mark with a hint of chaos.

Christian, 6 Oct 2026, after round 17: he likes D (the tangled mark) and G (the mark as the r,
line over the name), "but we definitely have to make it more random, like the design squiggly
version", and "the R should still be recognizable, but it doesn't have to be too refined".
So the knot here is scribbled from random loops and the pen shakes a little, while the stem,
the arch and the long line stay in their places. Each drawing is one seed; change the seed and
the knot changes. Seeds 16, 18, 20 and 22 were picked by eye from 1 to 24 for open loops that cross. Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/knot_chaos.py
Writes concepts/sheet-knot-chaos.png and one bare PNG per drawing in concepts/blind-knot-chaos/.
"""
import numpy as np
from scipy.interpolate import splev, splprep

from build_concepts import stroke
from knot_line import arch, path
from letters import R, layout
from voice import wave_path
from voice_more import letter

def scribble(seed, size=46, foot=-18, loops=3, wander=0.55):
    """A knot the way a hand scribbles: loops of different sizes whose centres wander, ending on the stem heading up."""
    rng = np.random.default_rng(seed)
    pts, a = [], rng.uniform(0, 2 * np.pi)
    for _ in range(loops):
        cx, cy = np.array((size + 4, foot + 6)) + rng.uniform(-wander, wander, 2) * size
        r, squash, sweep = size * rng.uniform(0.5, 0.85), rng.uniform(0.7, 1.0), rng.uniform(1.6, 2.2) * np.pi
        t = a + np.linspace(0, sweep, 7)[:-1]
        pts += zip(cx + r * np.cos(t), cy + squash * r * np.sin(t))
        a += sweep
    xs, ys = zip(*pts, (10, foot + 26), (0, foot + 6), (0, foot - 14))
    return splev(np.linspace(0, 1, 500), splprep([xs, ys], s=0, k=3)[0])


def rough(x, y, amount, seed, still=130, fall=0.0):
    """Shake the line a little, the way a pen does. The last `still` units stay dead straight; -120 shakes to the end.

    With `fall` above 0 the shake is strongest at the start and weakens all the way along.
    """
    rng = np.random.default_rng(seed)
    d = np.r_[0, np.cumsum(np.hypot(np.diff(x), np.diff(y)))]
    s = np.linspace(0, d[-1], 900)
    x, y = np.interp(s, d, x), np.interp(s, d, y)
    fade = np.clip((s[-1] - still - s) / 120, 0, 1) * (1 - s / s[-1]) ** fall
    for wave in (130, 71):
        x = x + amount * fade * 0.5 * np.sin(2 * np.pi * s / wave + rng.uniform(0, 6.3))
        y = y + amount * fade * 0.5 * np.sin(2 * np.pi * s / (wave * 1.3) + rng.uniform(0, 6.3))
    return x, y


def alone(seed, weight=8):
    """As sketched: a scribbled knot under a flat arch, then the long line."""
    x, y = rough(*path(scribble(seed), arch()), 3.5, seed)
    return stroke(wave_path(x, y), weight), (-40, -150, 390, 220)


def standing(seed, weight=8):
    """Standing r: the stem shows above the knot and the arch stops short like an r's arm, so the letter reads first."""
    x, y = rough(*path(scribble(seed), arch(-90, 40, arm=140, back=32), line=-152, kick=46), 3.5, seed)
    return stroke(wave_path(x, y), weight), (-40, -180, 390, 250)


def named(seed, text="esonans", pen=10, gap=30):
    """With the name, in one light pen: the r is as tall as the letters, the knot sits at its foot, the line runs over.

    With "esonans" the mark stands in for the r; with the whole name it stands in front of it.
    """
    spots, width = layout(text, weight=pen)
    start = R + R * np.sin(np.radians(50)) + pen + gap
    over = arch(-70, 34, arm=140, back=32)
    x, y = rough(*path(scribble(seed, size=40), over, line=-130, kick=40, reach=start + width), 3, seed, still=width - 40)
    art = stroke(wave_path(x, y), pen) + "".join(letter(ch, start + at, weight=pen) for ch, (at, _) in zip(text, spots))
    return art, (-50, -160, start + width + 70, 220)


def lockup(seed, text="esonans", size=1.0, top=-100, start=138, line=-122, reach=None, over=None, pen=8, scribe=letter, gap=34):
    """The mark as sketched, with letters set beside it in the same pen.

    `size` scales the letters, `top` is their top edge and `start` their left edge. `reach` is where the long
    line ends; left out, it ends with the letters. `over` swaps the arch. `scribe` draws one letter; the default
    is the clean typeface. `gap` is the space between two stems at full size.
    """
    spots, width = layout(text, [size] * len(text), gap=gap, weight=pen / size)
    lift = R * (size - 1) - (top + 2 * R * size)
    reach = reach or start + width
    x, y = rough(*path(scribble(seed), over or arch(), line=line, reach=reach), 3.5, seed, still=max(130, reach - 190))
    art = stroke(wave_path(x, y), pen)
    art += "".join(scribe(ch, start + at, size=size, lift=lift, weight=pen / size) for ch, (at, _) in zip(text, spots))
    low = max(50, top + 2 * R * size + 24)
    return art, (min(-40, start - 30), line - 28, max(reach, start + width) + 40 - min(-40, start - 30), low - line + 28)


def _idea(fn, title, *how):
    def draw():
        return fn(*how)
    draw.__doc__ = f"{title}, knot {how[0]}: one of the random knots"
    return draw


IDEAS = [("a", _idea(alone, "As sketched", 16)), ("b", _idea(alone, "As sketched", 20)),
         ("c", _idea(standing, "Standing r", 18)), ("d", _idea(standing, "Standing r", 22)),
         ("e", _idea(named, "As the r", 16)), ("f", _idea(named, "As the r", 20)), ("g", _idea(named, "As the r", 22)),
         ("h", _idea(named, "Before the whole name", 20, "resonans"))]

if __name__ == "__main__":
    from story_sheet import build
    build(IDEAS, name="knot-chaos", cols=4, rows=2)
