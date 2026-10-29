"""Round 16: the logo's idea moves from reply to understanding.

Christian, 6 Oct 2026: resonance is rooted in understanding, the layer between a message and
the response to it. He and Sai take complicated things apart, test them, and turn them into
something everyone can use. A louder response can be a false alarm, so the drawings here show
the making clear, with no reply in them. Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy --with svgpathtools \
      --with contourpy python brand/logo/understand.py
Writes concepts/sheet-understand.png and one bare PNG per drawing in concepts/blind-understand/.
"""
import re

import numpy as np
from scipy.interpolate import splev, splprep
from svgpathtools import Path as Curve
from svgpathtools import parse_path

from build_concepts import stroke
from cuts import lines
from letters import GLYPHS, R, layout
from voice import wave_path
from voice_more import letter

WEIGHT = 16
NAME = "resonans"
# The R's knot, placed by hand: one loop per row as (centre x, centre y, radius x, radius y, start angle, sweep, points).
LOOPS = [(68, -162, 30, 30, 262, 350, 6), (102, -156, 24, 26, 240, 350, 6), (132, -144, 30, 32, 240, 250, 5)]


def segments(ch, x):
    """A letter as its straight and curved pieces, cut where one piece meets the middle of another."""
    stems, curves, _ = GLYPHS[ch](x, 0)
    segs = list(parse_path(f"{stems} {curves}"))
    if ch == "r":                                  # the arm hugs the stem for its first 60 of 132 degrees
        return [segs[0], segs[1].cropped(60 / 132, 1)]
    if ch == "e":                                  # the bar's left end lands half way round the bowl
        return [segs[0], segs[1].cropped(0, 180 / 322), segs[1].cropped(180 / 322, 1)]
    return segs


def broken(path, piece, space=27, weight=WEIGHT):
    """A line drawn as evenly spaced dashes with a dash at each end. A piece of 0 gives dots."""
    length = path.length()
    n = max(2, round((length + space) / (piece + space)))
    if piece:
        piece = (length - (n - 1) * space) / n
    else:
        space = length / (n - 1)
    return stroke(path.d(), weight).replace("/>", f' stroke-dasharray="{max(piece, 0.01):.2f} {space:.2f}"/>')


def dots(pieces=(0, 0, 12, 40)):
    """Connect the dots: the name starts as separate grains, the grains join, and it ends as one line."""
    spots, width = layout(NAME)
    art = "".join(broken(Curve(seg), piece) for ch, (x, _), piece in zip(NAME, spots, pieces)
                  for seg in segments(ch, x))
    art += "".join(letter(ch, x) for ch, (x, _) in list(zip(NAME, spots))[len(pieces):])
    return art, (-14, -2 * R - 20, width + 28, 2 * R + 40)


def knot_r(leg=((138, 0),), weight=16):
    """A capital R in one line: up the stem, a knot of loops where the bowl goes, back to the stem, a straight leg out.

    `leg` is the points the line runs through after the knot; the default stops at the baseline.
    """
    pts = [(20, -156), (22, -178), (34, -194)]
    for cx, cy, rx, ry, start, sweep, n in LOOPS:
        turn = np.radians(start + np.linspace(0, sweep, n))
        pts += zip(cx + rx * np.cos(turn), cy + ry * np.sin(turn))
    xs, ys = zip(*pts, (50, -101), (24, -98))
    x, y = splev(np.linspace(0, 1, 1200), splprep([xs, ys], s=0, k=3)[0])
    lx, ly = zip(*leg)
    return stroke(wave_path(np.r_[20, 20, x, lx], np.r_[0, -156, y, ly]), weight)


def untangle(gap=30, under=38):
    """Untangle: the first letter is an R whose bowl is a knot; its leg comes out straight and runs under the name."""
    spots, width = layout(NAME[1:])
    start = 146 + gap
    art = knot_r(leg=((24 + 136 * (98 + under) / 98, under), (start + width, under)))
    art += "".join(letter(ch, start + x) for ch, (x, _) in zip(NAME[1:], spots))
    return art, (-4, -222, start + width + 28, 222 + under + 22)


def r_avatar():
    """Untangle, small: the R alone."""
    return knot_r(), (-34, -225, 250, 250)


def figure(weight=12, edges=(-38, 12)):
    """The plate's still line, as grains on the left that join into a solid line on the right."""
    still = parse_path(" ".join(re.findall(r'd="([^"]+)"', lines(((0, weight),)))))
    runs = []                                      # [zone, pieces]: 0 grains, 1 dashes, 2 solid, by x
    for curve in still.continuous_subpaths():
        for seg in curve:
            zone = int(np.searchsorted(edges, seg.point(0.5).real))
            if runs and runs[-1][0] == zone and runs[-1][1][-1].end == seg.start:
                runs[-1][1].append(seg)
            else:
                runs.append([zone, [seg]])
    return "".join(stroke(Curve(*segs).d(), weight) if zone == 2 else broken(Curve(*segs), 30 * zone, 23, weight)
                   for zone, segs in runs)


def pattern(size=1.0, gap=64):
    """The pattern in the sand: loose grains join into the figure a plate draws when it rings."""
    spots, width = layout(NAME)
    start = 208 * size + gap
    art = f'<g transform="translate({104 * size:.1f},{-R}) scale({size})">{figure()}</g>'
    art += "".join(letter(ch, start + x) for ch, (x, _) in zip(NAME, spots))
    return art, (-20, -R - 104 * size - 14, start + width + 40, 208 * size + 28)


def pattern_avatar():
    """The pattern in the sand, small: the figure alone."""
    return figure(), (-118, -118, 236, 236)


IDEAS = [("a", dots), ("b", untangle), ("c", pattern), ("d", r_avatar), ("e", pattern_avatar)]

if __name__ == "__main__":
    from story_sheet import build
    build(IDEAS, name="understand", cols=3, rows=2)
