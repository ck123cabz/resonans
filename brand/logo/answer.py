"""The Resonans logo, round 14: the second n answers the first.

The name has two n's. The first carries one arc: it sounds once. Its twin carries three:
it sounds back, three times over. "Re-sonans" is Latin for sounding back. Three fresh
readers shown this with no explanation each said one n hums and the other rings louder.
Every function returns (svg, box) and draws in currentColor.
"""
import numpy as np

from build_concepts import draw, stroke
from letters import R, word

WEIGHT = 16
EDGE = R + WEIGHT / 2                              # the outside of an n's arch
ARC, GAP, FROM, TO = 6.5, 8.5, 40, 140             # arc weight, gap between arcs, and their sweep in degrees
SMALL = (9, 9)                                     # the one arc of the small cut: weight, gap


def arc(cx, r, start, end, w):
    """One arc centred on an n, from `start` to `end` degrees measured up from the right."""
    a, b = np.radians(start), np.radians(end)
    return stroke(f"M{cx + r * np.cos(a):.1f},{-R - r * np.sin(a):.1f} A{r:.1f},{r:.1f} 0 0 0 "
                  f"{cx + r * np.cos(b):.1f},{-R - r * np.sin(b):.1f}", w)


def rings(cx, weights, gap, start=FROM, end=TO):
    out, r = "", EDGE
    for w in weights:
        r += gap + w / 2
        out += arc(cx, r, start, end, w)
        r += w / 2
    return out


def wordmark(cut="full"):
    """The name. full: one arc, then three. small: one heavier arc on the second n. plain: none."""
    items, width = word(weights=[WEIGHT] * 8)
    one, two = [float(items[i][0].split(",")[0][1:]) + R for i, ch in enumerate("resonans") if ch == "n"]
    extra = {"full": rings(one, (ARC,), GAP) + rings(two, (ARC,) * 3, GAP),
             "small": rings(two, SMALL[:1], SMALL[1]), "plain": ""}[cut]
    return draw(items) + extra, (-12, -2 * R - 66, width + 24, 2 * R + 80)


def avatar(cut="full"):
    """The answering n by itself, for a profile picture. small: one heavier arc, for 32 px and under."""
    items, _ = word("n", weights=[WEIGHT])
    extra = rings(R, (ARC,) * 3, GAP) if cut == "full" else rings(R, (12,), 11)
    return draw(items) + extra, (-54, -176 if cut == "full" else -166, 208, 208)   # centred on its ink
