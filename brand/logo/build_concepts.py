"""Build the Resonans logo concepts and one contact sheet.

Run: .venv/bin/python brand/logo/build_concepts.py
Writes concepts/<n>-<name>.svg and concepts/sheet.svg next to this file.
Every concept draws in currentColor, so one file serves light and dark.
"""
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTCollection

from letters import R, word

OUT = Path(__file__).parent / "concepts"
INK, PAPER, SIGNAL = "#141414", "#F3F0E8", "#FF4A1C"


def stroke(d, w, color="currentColor"):
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def draw(items, stem_color="currentColor"):
    return "".join(stroke(s, w, stem_color) * bool(s) + stroke(c, w)
                   for s, c, w in items)


def gain():
    """The stroke gains weight letter by letter, 4 units to 21."""
    weights = [4 + i * 17 / 7 for i in range(8)]
    items, width = word(weights=weights)
    return draw(items), (-6, -2 * R - 16, width + 22, 2 * R + 32)


def driven():
    """Three arches, each taller than the last, beside an even wordmark."""
    x, d = 0, ""
    for r, stem in ((14, 26), (22, 48), (34, 76)):
        d += f"M{x},0 V{-stem} a{r},{r} 0 0 1 {2 * r},0 V0 "
        x += 2 * r
    items, width = word()
    body = stroke(d, 14) + f'<g transform="translate({x + 80},0)">{draw(items)}</g>'
    return body, (-10, -120, x + 80 + width + 20, 130)


def parts():
    """Stems in the signal colour, curves in ink: the word shown as its two parts."""
    items, width = word()
    return draw(items, SIGNAL), (-10, -2 * R - 10, width + 20, 2 * R + 20)


def root():
    """Optima capitals for the Latin word; the O is a ring with one echo inside."""
    font = TTCollection("/System/Library/Fonts/Optima.ttc").fonts[0]
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    bounds = BoundsPen(glyphs)
    glyphs[cmap[ord("E")]].draw(bounds)
    cap, track = bounds.bounds[3], 0.16 * font["head"].unitsPerEm
    x, body = 0, ""
    for ch in "RESONANS":
        name = cmap[ord(ch)]
        if ch == "O":
            cx, cy = x + cap / 2, -cap / 2
            for rad, w in ((cap / 2 - 30, 60), (cap / 4, 34)):
                body += (f'<circle cx="{cx}" cy="{cy}" r="{rad}" fill="none" '
                         f'stroke="currentColor" stroke-width="{w}"/>')
            x += cap + track
            continue
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        body += (f'<path transform="translate({x},0) scale(1,-1)" '
                 f'd="{pen.getCommands()}" fill="currentColor"/>')
        x += glyphs[name].width + track
    return body, (0, -cap - 20, x - track, cap + 40)


CONCEPTS = [("1-gain", gain), ("2-driven", driven), ("3-parts", parts), ("4-root", root)]


def svg(body, box, color=INK):
    x, y, w, h = box
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:.0f} {y:.0f} '
            f'{w:.0f} {h:.0f}" color="{color}" role="img" aria-label="Resonans">'
            f"{body}</svg>")


def placed(body, box, px, py, pw, ph, color):
    """Fit a concept inside a pw x ph slot whose top-left is (px, py)."""
    x, y, w, h = box
    k = min(pw / w, ph / h)
    tx, ty = px + (pw - w * k) / 2 - x * k, py + (ph - h * k) / 2 - y * k
    return f'<g color="{color}" transform="translate({tx:.1f},{ty:.1f}) scale({k:.4f})">{body}</g>'


def sheet(built):
    pw, ph, out = 900, 520, ""
    for i, (name, body, box) in enumerate(built):
        ox, oy = (i % 2) * pw, (i // 2) * ph
        out += f'<rect x="{ox}" y="{oy}" width="{pw}" height="{ph}" fill="{PAPER}" stroke="#D8D3C6"/>'
        out += (f'<text x="{ox + 28}" y="{oy + 44}" font-family="Helvetica Neue" '
                f'font-size="20" fill="#7A766C">{name}</text>')
        out += placed(body, box, ox + 110, oy + 110, 680, 190, INK)
        out += f'<rect x="{ox + 560}" y="{oy + 380}" width="300" height="100" rx="8" fill="{INK}"/>'
        out += placed(body, box, ox + 590, oy + 400, 240, 60, PAPER)
        out += placed(body, box, ox + 40, oy + 440, 140, 22, INK)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {2 * pw} {2 * ph}" '
            f'width="{2 * pw}" height="{2 * ph}">{out}</svg>')


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    built = [(name, *fn()) for name, fn in CONCEPTS]
    for name, body, box in built:
        (OUT / f"{name}.svg").write_text(svg(body, box))
    (OUT / "sheet.svg").write_text(sheet(built))
