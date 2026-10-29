"""Round 19: chaos to clarity, drawn with a pen.

Christian's three sketches of 6 Oct 2026, 10:20 pm, share one order: a tight scribble in the
middle, a clean loop that unwinds round it, up the side into a flat arch that ends in a small
teardrop, then a kick up and a long straight line. "We must emphasize the chaos to clarity,
pen drawn like the design squiggle." So the line here is thin, the scribble is small and dense,
and the pen's shake is strongest at the start and gone by the long line. Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/knot_pen.py
Writes concepts/sheet-knot-pen.png and one bare PNG per drawing in concepts/blind-knot-pen/.
"""
import numpy as np
from scipy.interpolate import splev, splprep

from build_concepts import stroke
from knot_chaos import rough
from knot_line import arch, path, spiral
from letters import layout
from voice import wave_path
from voice_more import letter


def smooth(pts, n=400):
    xs, ys = zip(*pts)
    return splev(np.linspace(0, 1, n), splprep([xs, ys], s=0, k=3)[0])


def knot(seed, turns=1.3, wide=50, nested=0.3, tight=0.36, mess=6, grain=23):
    """The chaos and the way out of it: `mess` small loops piled on one spot, then a spiral that opens to the stem.

    `grain` is how big the small loops are; `turns` is how many times the line goes round before it reaches the stem.
    """
    rng = np.random.default_rng(seed)
    sx, sy = spiral(turns, wide, nested, foot=0, tight=tight)
    pts, a = [], rng.uniform(0, 2 * np.pi)
    for _ in range(mess):
        cx, cy = np.array((sx[0], sy[0])) + rng.uniform(-0.6, 0.6, 2) * grain
        r, squash, sweep = grain * rng.uniform(0.35, 0.9), rng.uniform(0.6, 1.0), rng.uniform(1.2, 2.0) * np.pi
        t = a + np.linspace(0, sweep, 6)[:-1]
        pts += zip(cx + r * np.cos(t), cy + squash * r * np.sin(t))
        a += sweep + rng.uniform(-0.7, 0.7)                 # the hand changes its mind
    return smooth(pts + list(zip(sx[::6], sy[::6])) + [(0, 0), (0, -16)], 700)


def over(shoulder=-44, rise=54, span=122, square=3.2, point=-74, tear=5):
    """The flat arch and the teardrop at its end: down the right side, round a small loop, and back up."""
    ax, ay = arch(shoulder, rise, span=span, square=square, point=point)
    loop = [(span, point - tear), (span + 0.4 * tear, point + 0.8 * tear), (span + 1.6 * tear, point + 0.6 * tear),
            (span + 1.7 * tear, point - 0.7 * tear), (span + 0.5 * tear, point - 2.4 * tear), (span - 0.4 * tear, point - 5 * tear)]
    lx, ly = smooth(list(zip(ax[-6:-2], ay[-6:-2])) + loop, 60)
    return np.r_[ax[:-6], lx], np.r_[ay[:-6], ly]


def drawn(seed, weight=5, line=-152, reach=330, kick=30, shake=9, still=110, **how):
    """One drawing. `how` goes to knot and over: turns, mess, grain, span, rise and so on."""
    shape = {k: how.pop(k) for k in ("shoulder", "rise", "span", "square", "point", "tear") if k in how}
    x, y = rough(*path(knot(seed, **how), over(**shape), line=line, kick=kick, reach=reach), shake, seed, still=still, fall=0.5)
    return stroke(wave_path(x, y), weight), (-50, line - 30, reach + 90, 110 - line)


def with_name(seed, pen=8, gap=44, size=0.92):
    """Before the whole name, in one pen: the long line runs over the letters."""
    spots, width = layout("resonans", weight=pen)
    start = 122 * size + gap
    art, _ = drawn(seed, weight=pen / size, line=-128 / size, reach=(start + width) / size, shake=7, still=width / size)
    art = f'<g transform="scale({size})">{art}</g>' + "".join(letter(ch, start + at, weight=pen) for ch, (at, _) in zip("resonans", spots))
    return art, (-50, -165, start + width + 90, 240)


def _idea(title, fn, *args, **how):
    def draw():
        return fn(*args, **how)
    draw.__doc__ = title
    return draw


IDEAS = [
    ("a", _idea("Third sketch: scribble against the stem, one clean loop, flat arch, teardrop", drawn, 3, nested=0.75)),
    ("b", _idea("First sketch: scribble in the middle of the loop, shorter arch", drawn, 7, span=104, rise=48)),
    ("c", _idea("Second sketch: rounder arch and a long sweeping kick", drawn, 11, square=2.3, kick=120, reach=350)),
    ("d", _idea("More chaos: a bigger, denser scribble", drawn, 5, mess=10, grain=30)),
    ("e", _idea("Slow way out: the line goes round twice before it clears", drawn, 9, turns=2.3, tight=0.3)),
    ("f", _idea("More clarity: the straight line is half as long again", drawn, 3, nested=0.75, reach=430)),
    ("g", _idea("Heavier pen: the same line at a weight that survives small sizes", drawn, 11, weight=9, mess=3, grain=30)),
    ("h", _idea("With the whole name: the line runs over the letters", with_name, 3)),
]

if __name__ == "__main__":
    from story_sheet import build
    build(IDEAS, name="knot-pen", cols=4, rows=2)
