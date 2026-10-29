"""Flat drawings of printed things, in millimetres, for the logo mockups.

Each scene draws its object on a matplotlib axis and returns three things: the colour
the logo sits on, the colour the logo prints in, and the point its centre goes to.
"""
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon, Rectangle

INK, SAND, BRASS, FLOOR = "#211513", "#EFE9DB", "#C4963F", "#E6DEDB"
TEE = [(-260, 0), (-260, 470), (-345, 395), (-430, 470), (-300, 630), (-105, 690), (-55, 655), (55, 655),
       (105, 690), (300, 630), (430, 470), (345, 395), (260, 470), (260, 0)]


def _stage(ax, x0, x1, y0, y1, colour=FLOOR):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, color=colour, zorder=0))
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)


def card(ax):
    _stage(ax, -12, 97, -12, 67)
    ax.add_patch(FancyBboxPatch((0, 0), 85, 55, boxstyle="round,pad=0,rounding_size=2.5", color="#FFFFFF", zorder=1))
    return "#FFFFFF", INK, (42.5, 27.5)


def receipt(ax):
    _stage(ax, -30, 88, -8, 128)
    ax.add_patch(Rectangle((0, 0), 58, 120, color="#FFFFFF", zorder=1))
    for i, w in enumerate((40, 28, 44, 20, 36, 30, 46, 18)):
        ax.add_patch(Rectangle((6, 78 - i * 9), w, 2.4, color="#B9AEAD", zorder=2))
    return "#FFFFFF", "#000000", (29, 100)


def stamp(ax):
    _stage(ax, -10, 110, -8, 78)
    ax.add_patch(Rectangle((0, 0), 100, 70, color="#CDAE84", zorder=1))
    return "#CDAE84", "#2B1D1A", (50, 35)


def chest(ax):
    _stage(ax, -470, 470, -40, 730)
    ax.add_patch(Polygon(TEE, color=INK, zorder=1))
    return INK, SAND, (125, 505)


def back(ax):
    _stage(ax, -470, 470, -40, 730)
    ax.add_patch(Polygon(TEE[:5] + [(-105, 690), (105, 690)] + TEE[9:], color=INK, zorder=1))
    return INK, SAND, (0, 400)


def cap(ax):
    _stage(ax, -150, 150, -70, 150)
    ax.add_patch(Ellipse((0, -6), 250, 50, color="#18110F", zorder=1))
    ax.add_patch(Ellipse((0, 20), 200, 230, color=INK, zorder=2))
    ax.add_patch(Rectangle((-150, -70), 300, 64, color=FLOOR, zorder=3))
    ax.add_patch(Ellipse((0, -6), 250, 50, color="#18110F", zorder=4))
    return INK, SAND, (0, 62)


def foil(ax):
    _stage(ax, -12, 97, -12, 67)
    ax.add_patch(FancyBboxPatch((0, 0), 85, 55, boxstyle="round,pad=0,rounding_size=2.5", color=INK, zorder=1))
    return INK, BRASS, (42.5, 27.5)


def window(ax):
    _stage(ax, -80, 1080, -80, 780)
    ax.add_patch(Rectangle((0, 0), 1000, 700, color="#5D4F4D", zorder=1))
    ax.add_patch(Rectangle((18, 18), 964, 664, color="#9FB2B8", zorder=2))
    return "#9FB2B8", "#FFFFFF", (500, 350)


def tarp(ax):
    _stage(ax, -560, 2120, -360, 1500)
    ax.add_patch(Rectangle((0, 0), 2000, 1000, color="#FFFFFF", zorder=1))
    for x in (40, 1960):
        for y in (40, 960):
            ax.add_patch(Circle((x, y), 14, color="#B9AEAD", zorder=2))
    ax.add_patch(Circle((-290, 1240), 105, color="#B9AEAD", zorder=2))            # a 1.7 m person, for scale
    ax.add_patch(FancyBboxPatch((-400, -350), 220, 1470, boxstyle="round,pad=0,rounding_size=105",
                                color="#B9AEAD", zorder=2))
    return "#FFFFFF", INK, (1000, 500)


SCENES = {"Business card": card, "Receipt": receipt, "Stamp on kraft paper": stamp,
          "Shirt, left chest": chest, "Shirt, back": back, "Cap": cap,
          "Foil on a dark card": foil, "Shop window": window, "Tarpaulin, 2 m wide": tarp}
