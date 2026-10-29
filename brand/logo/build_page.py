"""Assemble the identity page: template.html plus the final SVGs and three figures.

Run from the repo root, after build_final.py:
  uv run --with numpy --with matplotlib --with fonttools \
      python brand/logo/build_page.py
Writes page/resonans-identity.html, the file that gets published.
"""
import re
from pathlib import Path

import numpy as np

from build_concepts import draw
from build_final import BOX, ROOT, WEIGHT
from letters import word
from plate import crossings, rings

HERE = Path(__file__).parent
FINAL, PAGE = HERE / "final", HERE / "page"
SYMBOLS = ["mark", "mark-small", "wordmark", "lockup-horizontal", "lockup-stacked"]


def symbol(name):
    text = (FINAL / f"{name}.svg").read_text()
    box = re.search(r'viewBox="([^"]+)"', text).group(1)
    inner = re.search(r"<svg[^>]*>(.*)</svg>", text, re.S).group(1)
    return box, f'<symbol id="{name}" viewBox="{box}">{inner}</symbol>'


def construction():
    """The two curves, twelve of the rays that find them, and the crossings as dots."""
    half = BOX / 2
    rays = dots = ""
    for k in range(12):
        t = 2 * np.pi * k / 12
        rays += (f'<line x2="{half * np.cos(t):.1f}" y2="{half * np.sin(t):.1f}" '
                 f'stroke="currentColor" stroke-width="0.8" opacity="0.35"/>')
    for ring in crossings(counts=(12, 12)):
        for x, y in ring:
            dots += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{ROOT}"/>'
    return (f'<svg viewBox="{-half} {-half} {BOX} {BOX}" role="img" '
            f'aria-label="Rays from the centre crossing the two curves of the mark">{rays}'
            f'<path d="{rings()}" fill="none" stroke="currentColor" stroke-width="{WEIGHT}" opacity="0.22"/>'
            f'<path d="{rings()}" fill="none" stroke="currentColor" stroke-width="1.6"/>{dots}</svg>')


def parts():
    items, width = word(weights=[WEIGHT] * 8)
    return (f'<svg viewBox="-12 -112 {width + 24:.0f} 124" role="img" '
            f'aria-label="The wordmark with its stems in brass">{draw(items, ROOT)}</svg>')


def clearspace(box):
    x, y, w, h = map(float, box.split())
    m = BOX / 2
    return (f'<svg viewBox="{x - m} {y - m} {w + 2 * m} {h + 2 * m}" style="width:min(100%,440px)" '
            f'role="img" aria-label="The lockup inside its clear space">'
            f'<rect x="{x - m}" y="{y - m}" width="{w + 2 * m}" height="{h + 2 * m}" fill="none" '
            f'stroke="{ROOT}" stroke-width="3" stroke-dasharray="14 10"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#0E1320" '
            f'stroke-width="1.5" opacity="0.3"/><use href="#lockup-horizontal" x="{x}" y="{y}" '
            f'width="{w}" height="{h}" color="#0E1320"/></svg>')


def placed_use(name, boxes):
    """A symbol whose viewBox does not start at 0,0 needs its own x, y, width and height."""
    x, y, w, h = boxes[name].split()
    return f'<use href="#{name}" x="{x}" y="{y}" width="{w}" height="{h}"/>'


def build():
    html = (PAGE / "template.html").read_text()
    boxes, defs = {}, ""
    for name in SYMBOLS:
        boxes[name], sym = symbol(name)
        defs += sym
    html = html.replace("<!--SYMBOLS-->", defs)
    html = re.sub(r"/\*VB:([\w-]+)\*/", lambda m: boxes[m.group(1)], html)
    html = re.sub(r'<use href="#([\w-]+)"/>', lambda m: placed_use(m.group(1), boxes), html)
    html = html.replace("<!--FIG:construction-->", construction())
    html = html.replace("<!--FIG:parts-->", parts())
    html = html.replace("<!--FIG:clearspace-->", clearspace(boxes["lockup-horizontal"]))
    html = html.replace("/*RINGS*/", rings())
    left = re.findall(r"<!--[A-Z:]+[\w-]*-->|/\*[A-Z]+[:\w-]*\*/", html)
    if left:
        raise RuntimeError(f"unfilled slots: {left}")
    (PAGE / "resonans-identity.html").write_text(html)


if __name__ == "__main__":
    build()
