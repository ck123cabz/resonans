"""The Resonans mark and wordmark at several levels of detail, for different sizes and print methods.

Every mark cut is the same figure: where a square plate stays still in mode 1, 5.
A cut only changes how many lines are drawn around it and how heavy they are.
Each entry returns (svg, box); everything draws in currentColor.
"""
import numpy as np
from contourpy import contour_generator
from scipy import ndimage

from build_concepts import draw, stroke
from letters import R, word
from plate import _move, sand

REACH = 0.86
SQUARE = (-104, -104, 208, 208)
# (level of plate motion, stroke weight): level 0 is the still line, the others ride either side of it
RINGING = ((0, 5), (0.22, 2.2), (-0.22, 2.2), (0.42, 1), (-0.42, 1))


def lines(spec, n=1, m=5, limit=0.8, reach=REACH):
    """Contour lines of the plate's motion in mode (n, m), one stroke per (level, weight)."""
    g = np.linspace(-reach, reach, 500)
    x, y = np.meshgrid(g, g)
    f = _move(n, m, x, y)
    f[np.maximum(np.abs(x), np.abs(y)) > limit] = np.nan
    field, out = contour_generator(x=x, y=y, z=np.ma.masked_invalid(f)), ""
    for level, weight in spec:
        for line in field.lines(level):
            pts = line * 100 / reach
            out += stroke("M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts), weight)
    return out


def band(width):
    """The figure as one solid piece: every point that moves less than `width`."""
    return f'<path d="{sand(band=width)}" fill="currentColor" fill-rule="evenodd"/>'


def echoes(width, spec, size=720):
    """Lines that run beside a band at a fixed distance, so every gap is the same all the way round.

    spec is (distance from the band's edge to the middle of the line, stroke weight), in mark units.
    The lines appear outside the figure and inside its five openings.
    """
    g = np.linspace(-104, 104, size)
    x, y = np.meshgrid(g, g)
    px, py = x * REACH / 100, y * REACH / 100
    ink = (np.abs(_move(1, 5, px, py)) < width) & (np.maximum(np.abs(px), np.abs(py)) < REACH)
    away = ndimage.distance_transform_edt(~ink) * 208 / (size - 1)
    field, out = contour_generator(x=x, y=y, z=away), ""
    for distance, weight in spec:
        for line in field.lines(distance):
            out += stroke("M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in line), weight)
    return out


def wordmark(echo=(), weight=16):
    """The name. Each echo is (gap below it, its stroke weight): arcs above the second n, evenly spaced."""
    items, width = word(weights=[weight] * 8)
    second = [i for i, ch in enumerate("resonans") if ch == "n"][1]
    cx, r, extra = float(items[second][0].split(",")[0][1:]) + R, R + weight / 2, ""
    for gap, w in echo:
        r += gap + w / 2
        x, y = r * np.cos(np.radians(32)), r * np.sin(np.radians(32))
        extra += stroke(f"M{cx + x:.1f},{-R - y:.1f} A{r:.1f},{r:.1f} 0 0 0 {cx - x:.1f},{-R - y:.1f}", w)
        r += w / 2
    return draw(items) + extra, (-12, -2 * R - 76, width + 24, 2 * R + 90)


def marks():
    """Most detail first. `ringing` is the drawing Christian chose on 6 Oct; the rest are print cuts."""
    return {
        "ringing": (lines(RINGING), SQUARE),
        "fine": (band(0.16) + echoes(0.16, ((4.5, 3), (10.5, 2))), SQUARE),
        "medium": (band(0.22) + echoes(0.22, ((7, 4),)), SQUARE),
        "solid": (band(0.32), SQUARE),
    }


def words():
    return {"three echoes": wordmark(((6, 6), (6, 4.5), (6, 3))), "one echo": wordmark(((9, 8),)),
            "plain": wordmark()}
