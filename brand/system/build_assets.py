"""Write the logo and pattern files the design system serves, in fixed colours.

Run from the repo root, after logo/build_final.py:
  uv run --with numpy --with matplotlib python brand/system/build_assets.py
A picture shown through <img> cannot inherit a colour, so every file names its ink.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "logo"))
from plate import rings, sand  # noqa: E402

FINAL = HERE.parent / "logo" / "final"
ASSETS = HERE / "project" / "assets"
AIR = {t["name"]: t["value"]["air"] for t in
       json.loads((HERE / "project" / "tokens.json").read_text())["color"]["tokens"]
       if isinstance(t["value"], dict)}
INKS = {"ink": AIR["ink"], "air": AIR["ground"], "root": AIR["root"]}
LOGOS = {"mark": ("ink", "air", "root"), "mark-small": ("ink", "air"), "wordmark": ("ink", "air"),
         "lockup-horizontal": ("ink", "air"), "lockup-stacked": ("ink", "air")}
MODES = ((1, 3), (1, 5), (3, 5), (1, 7), (3, 7), (5, 7))


def logos():
    out = ASSETS / "Logos"
    out.mkdir(parents=True, exist_ok=True)
    for name, inks in LOGOS.items():
        text = (FINAL / f"{name}.svg").read_text()
        for ink in inks:
            fixed = re.sub(r' color="[^"]+"', "", text).replace("currentColor", INKS[ink])
            (out / f"{name}-{ink}.svg").write_text(fixed)
    for name in ("icon-app", "favicon"):
        text = (FINAL / f"{name}.svg").read_text()
        colour = re.search(r' color="([^"]+)"', text).group(1)
        (out / f"{name}.svg").write_text(
            re.sub(r' color="[^"]+"', "", text).replace("currentColor", colour))


def patterns():
    out = ASSETS / "Patterns"
    out.mkdir(parents=True, exist_ok=True)
    for n, m in MODES:
        d = sand(n, m, band=0.2, reach=0.999)
        (out / f"mode-{n}-{m}.svg").write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-100 -100 200 200" width="400" '
            f'height="400" role="img" aria-label="Plate mode {n}, {m}">'
            f'<path d="{d}" fill="{INKS["ink"]}" fill-rule="evenodd"/></svg>\n')


def cover():
    """The system's cover: colour blocks cut from the space scale, crossed by the mark's rings."""
    html = f'''<!-- @dsCard height=288 -->
<style>
  html, body {{ margin: 0; background: var(--ground); }}
  .cover {{ position: relative; width: 960px; height: 288px; overflow: hidden; background: var(--ground); }}
  .cover svg {{ position: absolute; inset: 0; }}
  .root {{ fill: var(--root); }} .ink {{ fill: var(--ink); }} .third {{ fill: var(--third); }}
  .fifth {{ fill: var(--fifth); }} .wash {{ fill: var(--root-wash); }}
  .ring {{ fill: none; stroke: var(--ground); stroke-width: var(--space-3); }}
  .name {{ position: absolute; left: var(--space-8); bottom: var(--space-8); width: 440px; }}
  .name b {{ display: block; font: 500 88px/0.95 var(--font-display); letter-spacing: -0.02em; color: var(--ink); }}
  .name span {{ display: block; margin-top: var(--space-3); font: 400 14px/1.5 var(--font-body); color: var(--ink-soft); }}
</style>
<div class="cover">
  <svg viewBox="0 0 960 288" width="960" height="288" aria-hidden="true">
    <!-- blocks: root 192 x 288, ink 96 x 192, third 96 x 96, fifth 96 x 96, root-wash 96 x 192; sides are space-24 and its multiples
         arrangement: one tall root slab bleeding off the top and bottom, with four satellites flush to it
         pattern: the literal motif. The mark is two rings of a ringing plate, so the same two rings cross the blocks, cut out in ground
         steps and radii: space-24 block module, space-3 ring stroke, square corners because blocks are fields, not controls -->
    <rect class="wash" x="576" y="0" width="96" height="192"/>
    <rect class="fifth" x="576" y="192" width="96" height="96"/>
    <rect class="root" x="672" y="0" width="192" height="288"/>
    <rect class="ink" x="864" y="0" width="96" height="192"/>
    <rect class="third" x="864" y="192" width="96" height="96"/>
    <path class="ring" transform="translate(768 144) scale(1.62)" d="{rings()}"/>
  </svg>
  <div class="name"><b>Resonans</b><span>Communication, taken apart and rebuilt.</span></div>
</div>
'''
    out = HERE / "project" / "components" / "Cover"
    out.mkdir(parents=True, exist_ok=True)
    (out / "preview.html").write_text(html)


if __name__ == "__main__":
    logos()
    patterns()
    cover()
