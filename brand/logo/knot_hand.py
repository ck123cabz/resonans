"""Round 22: should the letters be handwritten too?

Christian, 6 Oct 2026, about 10:55 pm: "Do you think it's a good idea to change the typeface for
the logo to handwritten as well, or original? If we need to mention our brand, we can just have
full typeface resonans spelling, and then our logo is just the knot." He asked for a version with
the letters below the line handwritten. This sheet puts the clean letters, two hand-drawn
strengths, the knot alone, and the knot with the whole name side by side.
Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy --with svgpathtools \
      python brand/logo/knot_hand.py
Writes concepts/sheet-knot-hand.png and one bare PNG per drawing in concepts/blind-knot-hand/.
"""
import numpy as np
from svgpathtools import parse_path

from build_concepts import stroke
from knot_chaos import alone, lockup, rough
from letters import GLYPHS, R
from voice import wave_path

SEED, HALF = 20, 0.5


def scribe(seed, shake=6.0, tilt=3.0, hop=3.0):
    """A stand-in for the clean letter: the same skeleton traced by hand.

    Every stroke gets the pen's shake to its very end, and every letter sits a little off: up to
    `hop` units high or low and `tilt` degrees over.
    """
    rng = np.random.default_rng(seed)

    def draw(ch, x, size=1.0, lift=0.0, weight=16):
        stems, curves, advance = GLYPHS[ch](0, 0)
        art = ""
        for piece in parse_path(f"{stems} {curves}").continuous_subpaths():
            pts = np.array([piece.point(v) for v in np.linspace(0, 1, 60)])
            art += stroke(wave_path(*rough(pts.real, pts.imag, shake, int(rng.integers(1_000_000)), still=-120)), weight)
        return (f'<g transform="translate({x:.1f},{-R - lift + rng.uniform(-hop, hop):.1f}) '
                f'rotate({rng.uniform(-tilt, tilt):.1f} {advance * size / 2:.1f} 0) scale({size:.3f}) translate(0,{R})">{art}</g>')
    return draw


def clean():
    """Clean letters: the one he picked, for comparison."""
    return lockup(SEED, size=HALF, top=-98, start=150)


def traced():
    """Traced by hand: the same letters with a light shake, so they still line up."""
    return lockup(SEED, size=HALF, top=-98, start=150, scribe=scribe(3, shake=6, tilt=2, hop=2))


def written():
    """Handwritten: a heavier shake, and each letter sits a little high, low or tilted."""
    return lockup(SEED, size=HALF, top=-98, start=150, scribe=scribe(5, shake=11, tilt=6, hop=5))


def knot_only():
    """Just the knot: the logo with no letters at all."""
    return alone(SEED)


def knot_and_type():
    """Knot and typeface: the whole name in clean type under the line, for when the brand must be named."""
    return lockup(SEED, "resonans", size=HALF, top=-98, start=150)


def knot_and_hand():
    """Knot and handwriting: the whole name under the line, handwritten."""
    return lockup(SEED, "resonans", size=HALF, top=-98, start=150, scribe=scribe(8, shake=11, tilt=6, hop=5))


IDEAS = [("a", clean), ("b", traced), ("c", written), ("d", knot_only), ("e", knot_and_type), ("f", knot_and_hand)]

if __name__ == "__main__":
    from story_sheet import build
    build(IDEAS, name="knot-hand", cols=3, rows=2)
