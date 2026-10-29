"""Assemble the second-cut identity page: the knot-and-line logo Christian picked on 6 Oct 2026.

It reuses the first cut's fonts and styles from page/template.html, so both pages stay one family.
Run from the repo root:
  uv run --with numpy --with matplotlib --with fonttools --with scipy \
      python brand/logo/build_cut2.py
Writes page/resonans-second-cut.html, the file that gets published.
"""
import base64
import re
from pathlib import Path

import numpy as np
from scipy import ndimage

from build_concepts import draw, stroke
from build_page import placed_use
from knot_chaos import alone, lockup, rough, scribble
from knot_cuts import MARK, cut
from knot_line import arch, path
from letters import word
from stress import raster
from voice import wave_path

PAGE = Path(__file__).parent / "page"
SEED, PEN, BRASS = MARK, 8, "#C4963F"
FAMILY = (16, 18, 22, 26, 25, 27)                   # six knots that pass the print check; MARK is the mark
PLATE_BOX = (-60, -180, 705, 260)                   # the sand plate in the hero: the lockup with air round it


def construction():
    """The mark with its knot in brass, so the two halves of the story show apart."""
    knot = scribble(SEED)
    x, y = rough(*path(knot, arch()), 3.5, SEED)
    run = np.r_[0, np.cumsum(np.hypot(np.diff(x), np.diff(y)))]
    cut = np.searchsorted(run, np.hypot(np.diff(knot[0]), np.diff(knot[1])).sum())
    return (f'<svg viewBox="-40 -150 390 220" role="img" aria-label="The mark with its knot in brass">'
            f'{stroke(wave_path(x[:cut + 1], y[:cut + 1]), PEN, BRASS)}{stroke(wave_path(x[cut:], y[cut:]), PEN)}</svg>')


def letters():
    items, width = word("esonans", weights=[16] * 7)
    return (f'<svg viewBox="-12 -112 {width + 24:.0f} 124" role="img" aria-label="The letters with their stems in brass">'
            f'{draw(items, BRASS)}</svg>')


def field(body, wide=282):
    """How far each spot of the plate is from the logo's ink, as bytes the page's sand can read."""
    ink = raster(body, PLATE_BOX, 2 * wide)
    rows = ink.shape[0] // 2 * 2
    far = ndimage.distance_transform_edt(~ink[:rows]).reshape(rows // 2, 2, wide, 2).mean((1, 3))
    return base64.b64encode(np.clip(far * 2, 0, 255).astype(np.uint8).tobytes()).decode(), far.shape


def build():
    first = (PAGE / "template.html").read_text()
    head = re.search(r"<link[^>]+>", first).group(0) + re.search(r"<style>.*?</style>", first, re.S).group(0)
    html = ('<title>Resonans second cut</title>\n<meta name="job" content="show">\n' + head
            + f"<style>{(PAGE / 'cut2.css').read_text()}</style>\n" + (PAGE / "cut2.html").read_text()
            + f"<script>{(PAGE / 'cut2.js').read_text()}</script>\n")
    art = {"lockup": lockup(SEED, size=0.5, top=-98, start=150), "mark": alone(SEED), "mark-short": cut("full")}
    art.update({f"knot-{s}": alone(s) for s in FAMILY})
    boxes = {name: " ".join(f"{v:.0f}" for v in box) for name, (_, box) in art.items()}
    boxes["plate"] = " ".join(str(v) for v in PLATE_BOX)
    defs = "".join(f'<symbol id="{name}" viewBox="{boxes[name]}">{body}</symbol>' for name, (body, _) in art.items())
    data, (rows, cols) = field(art["lockup"][0])
    family = "".join(
        f'<figure class="tile{" is-mark" if s == SEED else ""}"><div class="pad on-plate"><svg viewBox="{boxes[f"knot-{s}"]}">'
        f'<use href="#knot-{s}"/></svg></div><div class="foot"><span>Knot {s}</span><span>{"the mark" if s == SEED else "pattern"}</span></div></figure>'
        for s in FAMILY)
    for slot, value in (("<!--SYMBOLS-->", defs), ("<!--FIG:construction-->", construction()), ("<!--FIG:letters-->", letters()),
                        ("<!--FAMILY-->", family), ("/*FIELD*/", data), ("/*ROWS*/", str(rows)), ("/*COLS*/", str(cols))):
        html = html.replace(slot, value)
    html = re.sub(r"/\*VB:([\w-]+)\*/", lambda m: boxes[m.group(1)], html)
    html = re.sub(r'<use href="#([\w-]+)"/>', lambda m: placed_use(m.group(1), boxes), html)
    left = re.findall(r"<!--[A-Z:]+[\w-]*-->|/\*[A-Z]+[:\w-]*\*/", html)
    if left:
        raise RuntimeError(f"unfilled slots: {left}")
    (PAGE / "resonans-second-cut.html").write_text(html)


if __name__ == "__main__":
    build()
