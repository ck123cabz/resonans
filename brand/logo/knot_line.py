"""Round 17: Christian's sketch of 6 Oct 2026, 10:01 pm, in eight variations.

His drawing is one line: it starts as a knot at the foot, climbs a stem, arches over like an r,
comes down to a point, then kicks up and runs out straight to the right. Each variation keeps
that order and changes one thing: the knot, the weight, the arch, or where the straight line goes.
Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/knot_line.py
Writes concepts/sheet-knot-line.png and one bare PNG per drawing in concepts/blind-knot-line/.
"""
import numpy as np

from build_concepts import stroke
from letters import R, layout
from voice import wave_path
from voice_more import letter



def spiral(turns=2.4, wide=40, nested=0.85, foot=-18, tight=0.25, drift=0.0):
    """A knot that winds outward and ends on the stem at height `foot`, heading up.

    nested 1 hangs every loop off the stem side, as in the sketch; 0 is an even spiral.
    drift pushes the loops off centre so they cross like a scribble.
    """
    a = np.linspace(np.pi - 2 * np.pi * turns, np.pi, int(60 * turns))
    done = (a - a[0]) / (a[-1] - a[0])
    r = wide * (tight + (1 - tight) * done)
    loose = drift * np.sqrt(1 - done)
    return wide + nested * (r - wide) + r * np.cos(a) + loose * np.sin(0.9 * a), foot + r * np.sin(a) + loose * np.cos(1.4 * a)


def arch(shoulder=-66, rise=36, arm=180, point=-58, back=0, span=2 * R, square=2):
    """The arch, from the stem over to the right: it leaves the stem at `shoulder`, is `rise` tall and `span` wide.

    `arm` is how far round it goes, in degrees. A full arch drops to `point` and comes back up a little.
    A shorter one can retrace `back` degrees, which leaves the end of the r's arm standing as a stub.
    `square` above 2 flattens the top and tightens the corners.
    """
    t = np.radians(np.r_[np.linspace(0, arm, 40), np.linspace(arm, arm - back, 8)[1:] if back else []])
    x = span / 2 * (1 - np.sign(np.cos(t)) * np.abs(np.cos(t)) ** (2 / square))
    y = shoulder - rise * np.abs(np.sin(t)) ** (2 / square)
    if arm == 180:
        x, y = np.r_[x, span, span], np.r_[y, point, point - 16]
    return x, y


def path(knot, over, line=-122, kick=44, reach=320):
    """Knot, stem, arch, kick, straight line, as one run of points."""
    q = np.radians(np.linspace(0, 90, 20))
    fx, fy = over[0][-1] + kick * (1 - np.cos(q)), over[1][-1] + (line - over[1][-1]) * np.sin(q)
    return np.r_[knot[0], over[0], fx, reach], np.r_[knot[1], over[1], fy, line]


def mark(knot, over=None, weight=16, **how):
    """The whole drawing as one stroke. `how` goes to path: line, kick, reach."""
    return stroke(wave_path(*path(knot, over or arch(), **how)), weight)


def sketch():
    """As sketched: nested loops off the stem, a thin pen, a flat arch down to a point."""
    return mark(spiral(drift=5), weight=6), (-40, -150, 390, 200)


def heavier():
    """Heavier pen: the same drawing with one loop fewer, so the knot stays open."""
    return mark(spiral(1.9, 44, drift=4), weight=10), (-40, -150, 390, 200)


def logo_weight():
    """Logo weight: the letters' own weight, with a bigger knot that hangs lower."""
    return mark(spiral(1.7, 60, nested=0.5, foot=4), weight=16), (-40, -150, 390, 240)


def tangled():
    """Tangled: the loops are pushed off centre so they cross, like a real knot."""
    return mark(spiral(2.6, 44, nested=0.4, drift=16), weight=8), (-40, -150, 390, 200)


def round_arch():
    """Round arch: the arch is the same half circle as the n in the name."""
    return mark(spiral(1.7, 60, nested=0.5, foot=14), arch(-50, 50, point=-40), line=-140), (-40, -165, 390, 260)


def no_point():
    """No point: the arch never comes down. Its top runs straight out as the line."""
    return mark(spiral(1.7, 60, nested=0.5, foot=4), arch(arm=90), line=-102, kick=10), (-40, -140, 390, 230)


def with_name(gap=30, hang=64):
    """With the name: the mark is the r, the knot hangs below, and the straight line runs over the name."""
    spots, width = layout("esonans")
    start = R + R * np.sin(np.radians(42)) + 16 + gap
    art = mark(spiral(1.7, 54, nested=0.5, foot=hang), arch(-50, 50, arm=132), line=-142, kick=40, reach=start + width)
    return art + "".join(letter(ch, start + x) for ch, (x, _) in zip("esonans", spots)), (-20, -165, start + width + 40, 300)


def with_name_under(gap=30, hang=92, under=40):
    """With the name, line under: after the point the line drops and runs under the name."""
    spots, width = layout("esonans")
    start = 2 * R + 16 + gap
    kx, ky = spiral(1.6, 50, nested=0.5, foot=hang)
    t = np.radians(np.linspace(0, 180, 40))
    x = np.r_[kx, R - R * np.cos(t), 2 * R, 2 * R + 34, start + width]
    y = np.r_[ky, -R - R * np.sin(t), under - 34, under, under]
    art = stroke(wave_path(x, y), 16)
    return art + "".join(letter(ch, start + x0) for ch, (x0, _) in zip("esonans", spots)), (-20, -125, start + width + 40, 300)


IDEAS = [("a", sketch), ("b", heavier), ("c", logo_weight), ("d", tangled),
         ("e", round_arch), ("f", no_point), ("g", with_name), ("h", with_name_under)]

if __name__ == "__main__":
    from story_sheet import build
    build(IDEAS, name="knot-line", cols=4, rows=2)
