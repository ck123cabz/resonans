"""RES-48 logo concepts from the creative-grill idea "Taken apart, put back".

A  parts R: a capital R built from three separate pieces, gaps left showing.
B  seamed name: "resonans" cut once along the middle, halves set back in line.
C  split o: the o taken apart into two halves; the halves are the symbol.

Black only. Letters are Inter Display SemiBold outlines, a stand-in typeface for
exploration; the brand typeface is not picked yet.
Run: .venv/bin/python brand/logo/res48/concepts.py
"""
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

OUT = Path(__file__).parent / "svg"
FONT = TTFont(Path.home() / "Library/Fonts/InterDisplay-SemiBold.otf")
UPM, XH = 2048, 1056
GAP = 14  # every cut in every concept is this wide, in 256-unit space


def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}">{body}</svg>\n'


def word(text, size, x0, baseline, swap=None):
    """Outline `text` at `size` px; `swap` maps a char to a drawer(x, advance, scale)."""
    gs, cmap, hmtx = FONT.getGlyphSet(), FONT.getBestCmap(), FONT["hmtx"]
    s, x, parts = size / UPM, x0, []
    for ch in text:
        name = cmap[ord(ch)]
        adv = hmtx[name][0] * s
        if swap and ch in swap:
            parts.append(swap[ch](x, adv, s))
        else:
            pen = SVGPathPen(gs)
            gs[name].draw(TransformPen(pen, (s, 0, 0, -s, x, baseline)))
            parts.append(f'<path d="{pen.getCommands()}"/>')
        x += adv
    return "".join(parts), x


def parts_r():
    """Stem, open bowl and leg, each a separate piece, GAP apart."""
    stem_w, bowl_r, t, top, bot = 42, 54, 38, 32, 224
    sx, bx = 0, 42 + GAP
    cx, by2 = bx + 34, top + 2 * bowl_r
    ir = bowl_r - t
    stem = f"M{sx},{top}H{sx + stem_w}V{bot}H{sx}Z"
    bowl = (f"M{bx},{top}H{cx}A{bowl_r},{bowl_r} 0 0 1 {cx},{by2}H{bx}V{by2 - t}"
            f"H{cx}A{ir},{ir} 0 0 0 {cx},{top + t}H{bx}Z")
    ly, run = by2 + GAP, bot - (by2 + GAP)
    lw = 58
    leg = f"M{bx},{ly}H{bx + lw}L{bx + lw + run},{bot}H{bx + run}Z"
    right = max(cx + bowl_r, bx + lw + run)
    dx = (256 - right) / 2
    return f'<g transform="translate({dx:g},0)"><path d="{stem} {bowl} {leg}"/></g>', right


def split_ring(cx, cy, r, t):
    """A ring cut top to bottom, two halves GAP apart."""
    ir, h = r - t, GAP / 2
    left = (f"M{cx - h},{cy - r}A{r},{r} 0 0 0 {cx - h},{cy + r}V{cy + ir}"
            f"A{ir},{ir} 0 0 1 {cx - h},{cy - ir}Z")
    right = (f"M{cx + h},{cy - r}A{r},{r} 0 0 1 {cx + h},{cy + r}V{cy + ir}"
             f"A{ir},{ir} 0 0 0 {cx + h},{cy - ir}Z")
    return f'<path d="{left} {right}"/>'


def ring_o(baseline):
    def draw(x, adv, s):
        r = XH * s / 2 * 1.04  # round overshoot
        return split_ring(x + adv / 2, baseline - XH * s / 2, r, r * 0.36)
    return {"o": draw}


def seamed(body, w, seam_y):
    """Clip the drawing above and below a GAP-wide cut (exploration only)."""
    a, b = seam_y - GAP / 2, seam_y + GAP / 2
    return (f'<defs><clipPath id="t"><rect width="{w:g}" height="{a:g}"/></clipPath>'
            f'<clipPath id="b"><rect y="{b:g}" width="{w:g}" height="{256 - b:g}"/></clipPath></defs>'
            f'<g clip-path="url(#t)">{body}</g><g clip-path="url(#b)">{body}</g>')


def lockup(symbol, word_size=150, pad=40):
    base = 128 + XH * word_size / UPM / 2
    text, end = word("resonans", word_size, 256 + pad, base)
    return svg(end + 8, 256, symbol + text)


def main():
    OUT.mkdir(exist_ok=True)
    files = {}
    r_sym, _ = parts_r()
    files["a-symbol"] = svg(256, 256, r_sym)
    files["a-lockup"] = lockup(r_sym)

    size = 190
    base = 128 + XH * size / UPM / 2
    text, end = word("resonans", size, 8, base)
    w = end + 8
    files["b-lockup"] = svg(w, 256, seamed(text, w, base - XH * size / UPM / 2))
    rtext, rend = word("r", 420, 0, 0)
    rs = 420 / UPM
    r_base = 128 + XH * rs / 2
    rtext, rend = word("r", 420, (256 - rend) / 2, r_base)
    files["b-symbol"] = svg(256, 256, seamed(rtext, 256, r_base - XH * rs / 2))

    files["c-symbol"] = svg(256, 256, split_ring(128, 128, 96, 36))
    text, end = word("resonans", size, 8, base, swap=ring_o(base))
    files["c-lockup"] = svg(end + 8, 256, text)

    for name, body in files.items():
        (OUT / f"{name}.svg").write_text(body)
    print("wrote", ", ".join(sorted(files)))


if __name__ == "__main__":
    main()
