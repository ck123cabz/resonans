"""Monoline lowercase letters for the Resonans wordmark.

Every letter is built from two parts only: a straight stem and a circle arc of
radius R. Each function takes the left edge x and the baseline y and returns
(stems, curves, advance), where stems and curves are SVG path strings.
"""
from math import cos, radians, sin

R = 50  # centreline radius; the x-height is 2R


def _o(x, b):
    c = f"M{x},{b - R} a{R},{R} 0 1 0 {2 * R},0 a{R},{R} 0 1 0 {-2 * R},0"
    return "", c, 2 * R


def _n(x, b, rise=0):
    """rise lifts the arch and lengthens both stems by that many units."""
    top = b - R - rise
    stems = f"M{x},{b} V{top} M{x + 2 * R},{b} V{top}"
    return stems, f"M{x},{top} a{R},{R} 0 0 1 {2 * R},0", 2 * R


def _a(x, b):
    _, c, w = _o(x, b)
    return f"M{x + 2 * R},{b} V{b - 2 * R}", c, w


def _r(x, b):
    t = radians(42)
    ex, ey = x + R + R * sin(t), b - R - R * cos(t)
    stems = f"M{x},{b} V{b - 2 * R}"
    return stems, f"M{x},{b - R} A{R},{R} 0 0 1 {ex:.1f},{ey:.1f}", R + R * sin(t)


def _e(x, b):
    t = radians(38)
    ex, ey = x + R + R * cos(t), b - R + R * sin(t)
    c = f"M{x},{b - R} H{x + 2 * R} A{R},{R} 0 1 0 {ex:.1f},{ey:.1f}"
    return "", c, 2 * R


def _s(x, b):
    """Two half-height bowls, a little wider than they are tall so the s holds its place."""
    rx, ry, t = 0.58 * R, R / 2, radians(35)
    cx = x + rx
    sx, sy = cx + rx * cos(t), b - 1.5 * R - ry * sin(t)
    ex, ey = cx - rx * cos(t), b - 0.5 * R + ry * sin(t)
    c = (f"M{sx:.1f},{sy:.1f} A{rx},{ry} 0 1 0 {cx},{b - R} "
         f"A{rx},{ry} 0 1 1 {ex:.1f},{ey:.1f}")
    return "", c, 2 * rx


GLYPHS = {"r": _r, "e": _e, "s": _s, "o": _o, "n": _n, "a": _a}
# What each letter shows its neighbour: a straight stem, a round bowl, or r's open arm.
SIDES = {"r": "so", "e": "rr", "s": "rr", "o": "rr", "n": "ss", "a": "rs"}
FIT = {"ss": 1.0, "sr": 0.8, "rs": 0.8, "rr": 0.62, "os": 0.5, "or": 0.34}


def word(text="resonans", gap=34, weights=None, rises=None, b=0):
    """Lay the word out. Returns a list of (stems, curves, weight) and the width.

    `gap` is the space between two stems. Round sides sit closer, by FIT, so the
    white between letters looks even.
    """
    weights = weights or [14] * len(text)
    rises = rises or [0] * len(text)
    x, out = 0, []
    for i, (ch, w, rise) in enumerate(zip(text, weights, rises)):
        args = (x, b, rise) if ch == "n" else (x, b)
        stems, curves, adv = GLYPHS[ch](*args)
        out.append((stems, curves, w))
        if i + 1 < len(text):
            x += adv + w + gap * FIT[SIDES[ch][1] + SIDES[text[i + 1]][0]]
    return out, x + adv


def layout(text="resonans", sizes=None, gap=34, weight=16):
    """Where each letter starts when letter i is drawn at sizes[i] times full size.

    Returns a list of (left edge, advance at full size) and the total width. Use it when
    letters are moved, turned or scaled one by one; `word` covers the plain case.
    """
    sizes = sizes or [1] * len(text)
    x, out = 0.0, []
    for i, ch in enumerate(text):
        advance = GLYPHS[ch](0, 0)[2]
        out.append((x, advance))
        if i + 1 < len(text):
            fit = FIT[SIDES[ch][1] + SIDES[text[i + 1]][0]]
            x += advance * sizes[i] + (weight + gap * fit) * (sizes[i] + sizes[i + 1]) / 2
    return out, x + advance * sizes[-1]
