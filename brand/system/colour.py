"""Colour maths for the Resonans palette: a pitch becomes a wavelength becomes a hue.

A sound doubled in frequency 40 times lands in visible light. A = 440 Hz becomes
484 THz, which is light of 620 nm. The palette takes its hues from the A major
triad transposed that way. Lightness and chroma are then set for legibility.
"""
from math import atan2, cos, degrees, exp, radians, sin

LIGHT_SPEED = 299_792_458  # metres per second
OCTAVES = 40


def wavelength(pitch_hz):
    """Wavelength in nanometres of the pitch raised 40 octaves."""
    return LIGHT_SPEED / (pitch_hz * 2 ** OCTAVES) * 1e9


def _lobe(x, mu, s1, s2):
    return exp(-0.5 * ((x - mu) / (s1 if x < mu else s2)) ** 2)


def _xyz(nm):
    """CIE 1931 colour matching functions, Wyman, Sloan and Shirley's 2013 fit."""
    x = 1.056 * _lobe(nm, 599.8, 37.9, 31.0) + 0.362 * _lobe(nm, 442.0, 16.0, 26.7) \
        - 0.065 * _lobe(nm, 501.1, 20.4, 26.2)
    y = 0.821 * _lobe(nm, 568.8, 46.9, 40.5) + 0.286 * _lobe(nm, 530.9, 16.3, 31.1)
    z = 1.217 * _lobe(nm, 437.0, 11.8, 36.0) + 0.681 * _lobe(nm, 459.0, 26.0, 13.8)
    return x, y, z


def _cbrt(v):
    return abs(v) ** (1 / 3) * (1 if v >= 0 else -1)


def _oklab(r, g, b):
    l = _cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b)
    m = _cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b)
    s = _cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b)
    return (0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
            1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
            0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s)


def hue_of(nm):
    """OKLCH hue angle, in degrees, of single-wavelength light."""
    x, y, z = _xyz(nm)
    r = 3.2404542 * x - 1.5371385 * y - 0.4985314 * z
    g = -0.9692660 * x + 1.8760108 * y + 0.0415560 * z
    b = 0.0556434 * x - 0.2040259 * y + 1.0572252 * z
    _, a, bb = _oklab(r, g, b)
    return degrees(atan2(bb, a)) % 360


def _linear(light, chroma, hue):
    a, b = chroma * cos(radians(hue)), chroma * sin(radians(hue))
    l = (light + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (light - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (light - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
            -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
            -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)


def to_hex(light, chroma, hue):
    """OKLCH to sRGB hex. Chroma drops in small steps until the colour fits sRGB."""
    while True:
        rgb = _linear(light, chroma, hue)
        if all(-0.0005 <= v <= 1.0005 for v in rgb) or chroma <= 0:
            break
        chroma -= 0.002
    out = []
    for v in rgb:
        v = min(1, max(0, v))
        out.append(round(255 * (12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055)))
    return "#{:02X}{:02X}{:02X}".format(*out)


def luminance(hex_colour):
    vals = [int(hex_colour[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    lin = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in vals]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def contrast(one, two):
    hi, lo = sorted((luminance(one), luminance(two)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)
