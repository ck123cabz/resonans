"""Chladni figures: where sand settles on a square plate ringing in mode (n, m).

The plate moves by cos(n pi x / 2) cos(m pi y / 2) + cos(m pi x / 2) cos(n pi y / 2).
Sand is thrown off the moving parts and gathers where that sum is zero. The Resonans
mark is mode (1, 5). Every function returns SVG path data in a box of +-scale units.
"""
import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


def field(n, m, size=900):
    x = np.linspace(-1, 1, size)
    gx, gy = np.meshgrid(x, x)
    f = (np.cos(n * np.pi * gx / 2) * np.cos(m * np.pi * gy / 2)
         + np.cos(m * np.pi * gx / 2) * np.cos(n * np.pi * gy / 2))
    return gx, gy, f


def _inside(gx, gy, reach):
    return np.maximum(np.abs(gx), np.abs(gy)) < reach


def _polygons(path, scale, reach):
    d = ""
    for poly in path.to_polygons():
        pts = poly * scale / reach
        d += "M" + " L".join(f"{px:.2f},{py:.2f}" for px, py in pts) + "Z "
    return d


def sand(n=1, m=5, band=0.3, reach=0.86, scale=100):
    """The filled figure: every point that moves less than `band`, inside `reach`."""
    gx, gy, f = field(n, m)
    still = np.where(_inside(gx, gy, reach), band - np.abs(f), -1.0)
    fig = plt.figure()                     # a figure of its own, so a caller's drawing is left alone
    path = fig.gca().contourf(gx, gy, still, levels=[0, 10]).get_paths()[0]
    plt.close(fig)
    return _polygons(path, scale, reach)


def _move(n, m, x, y):
    return (np.cos(n * np.pi * x / 2) * np.cos(m * np.pi * y / 2)
            + np.cos(m * np.pi * x / 2) * np.cos(n * np.pi * y / 2))


def crossings(n=1, m=5, counts=(48, 96), reach=0.86, scale=100):
    """Where rays from the centre meet the first nodal rings: one point array per ring.

    Along each ray the plate's motion changes sign where a ring crosses it. Taking
    the crossings at evenly spaced angles gives every ring exact four-fold symmetry.
    """
    radii = np.linspace(0.02, reach, 4000)
    out = []
    for ring, count in enumerate(counts):
        pts = []
        for k in range(count):
            t = 2 * np.pi * k / count
            v = _move(n, m, radii * np.cos(t), radii * np.sin(t))
            i = np.nonzero(np.sign(v[:-1]) != np.sign(v[1:]))[0][ring]
            r = radii[i] + (radii[i + 1] - radii[i]) * v[i] / (v[i] - v[i + 1])
            pts.append((r * np.cos(t) * scale / reach, r * np.sin(t) * scale / reach))
        out.append(np.array(pts))
    return out


def rings(**how):
    """The mark's two rings as smooth closed curves you can edit by hand."""
    return " ".join(_closed_curve(p) for p in crossings(**how))


def _closed_curve(p):
    """Catmull-Rom through the points, written as cubic Beziers."""
    d = f"M{p[0][0]:.2f},{p[0][1]:.2f}"
    for i in range(len(p)):
        a, b, c, e = p[i - 1], p[i], p[(i + 1) % len(p)], p[(i + 2) % len(p)]
        c1, c2 = b + (c - a) / 6, c - (e - b) / 6
        d += f" C{c1[0]:.2f},{c1[1]:.2f} {c2[0]:.2f},{c2[1]:.2f} {c[0]:.2f},{c[1]:.2f}"
    return d + "Z"
