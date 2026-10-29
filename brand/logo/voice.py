"""Round 9: back to first principles. Resonance, said plainly, is a call that gets an answer.

No dots anywhere: every drawing is a few strokes at the letters' own weight. The three
concepts follow the logo-design skill's rule of one idea you can say in one sentence.
Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/voice.py
Writes concepts/sheet-voice.png and one bare PNG per drawing in concepts/blind-voice/.
"""
import numpy as np

from build_concepts import draw, stroke
from letters import R, word

WEIGHT = 16
ECHO = ((6, 6), (6, 4.5), (6, 3))            # (gap below the arc, its weight), nearest first


def arcs(cx, cy, start, spec, spread=58):
    """Arcs above a point, evenly spaced: each one is the arc before it, a little further out."""
    out, r = "", start
    for gap, w in spec:
        r += gap + w / 2
        x, y = r * np.sin(np.radians(spread)), r * np.cos(np.radians(spread))
        out += stroke(f"M{cx + x:.1f},{cy - y:.1f} A{r:.1f},{r:.1f} 0 0 0 {cx - x:.1f},{cy - y:.1f}", w)
        r += w / 2
    return out


def answer(first=1, second=3):
    """A. Call and answer: the first n speaks once, and its twin answers three times over."""
    items, width = word(weights=[WEIGHT] * 8)
    tops = [float(items[i][0].split(",")[0][1:]) + R for i, ch in enumerate("resonans") if ch == "n"]
    rings = arcs(tops[0], -R, R + WEIGHT / 2, ECHO[:first]) + arcs(tops[1], -R, R + WEIGHT / 2, ECHO[:second])
    return draw(items) + rings, (-12, -2 * R - 52, width + 24, 2 * R + 66)


def answer_alone():
    """A2. Only the second n rings: the same name with no sign of who spoke first."""
    return answer(first=0)


def ringing_n():
    """A, small: the answering n by itself, for a round avatar."""
    items, _ = word("n", weights=[WEIGHT])
    return draw(items) + arcs(R, -R, R + WEIGHT / 2, ECHO), (-48, -2 * R - 50, 196, 196)


def wave_path(xs, ys):
    return "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in zip(xs, ys))


def in_step(weight=9):
    """B. Same wavelength: two lines start out of step, fall into step, and go on as one."""
    x = np.linspace(-150, 30, 400)
    s = np.clip((x + 110) / 130, 0, 1) ** 2 * (3 - 2 * np.clip((x + 110) / 130, 0, 1))
    together = 26 * np.sin(2 * np.pi * (x - 30) / 64)
    one = (1 - s) * 30 * np.sin(2 * np.pi * x / 118 + 0.6) + s * together
    two = (1 - s) * 22 * np.sin(2 * np.pi * x / 47 + 2.4) + s * together
    xr = np.linspace(30, 150, 260)
    grown = (26 + 14 * (xr - 30) / 120) * np.sin(2 * np.pi * (xr - 30) / 64)
    return (stroke(wave_path(x, -one), weight) + stroke(wave_path(x, -two), weight)
            + stroke(wave_path(xr, -grown), WEIGHT)), (-162, -58, 324, 116)


def finds_its_note(weight=12):
    """C. One line: it starts as a scribble, finds its note, and swings wider each time."""
    u = np.linspace(0, 1, 500)
    sx = -150 + 105 * u + 30 * (1 - u) ** 1.2 * np.sin(2 * np.pi * 4.6 * u + 0.5)
    sy = 34 * (1 - u) ** 0.9 * np.sin(2 * np.pi * 6.3 * u + 1.3)
    t = np.linspace(0, 195, 420)
    wx, wy = -45 + t, -46 * t / 195 * np.sin(2 * np.pi * t / 60)
    return stroke(wave_path(np.r_[sx, wx], np.r_[sy, wy]), weight), (-178, -62, 356, 124)


IDEAS = [("a", answer), ("b", answer_alone), ("c", in_step), ("d", finds_its_note), ("e", ringing_n)]

if __name__ == "__main__":
    from story_sheet import build
    build(IDEAS, name="voice", cols=3, rows=2)
