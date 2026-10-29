"""Derive the Resonans tokens and write project/tokens.json.

Run: python3 brand/system/build_tokens.py
Every hue comes from a pitch (colour.py). Lightness is then nudged until each text
colour reaches 4.5 to 1 on the grounds its note names, and each fill 3 to 1.
The script prints the contrast table and stops if a pair cannot be met.
"""
import json
from pathlib import Path

from colour import contrast, hue_of, to_hex, wavelength
from scales import other_families, type_tokens

OUT = Path(__file__).parent / "project" / "tokens.json"
A = 440
PITCH = {"root": A, "third": A * 5 / 4, "fifth": A * 3 / 2, "offkey": A * 16 / 15}
HUE = {k: hue_of(wavelength(hz)) for k, hz in PITCH.items()}
HUE["clip"] = HUE["root"]          # an error is the root note driven too hard
NM = {k: round(wavelength(hz)) for k, hz in PITCH.items()}

# name: (lightness, chroma) in the Air theme, then in the Still theme
NEUTRAL = {
    "ground":        ((0.975, 0.006), (0.170, 0.012)),
    "ground-raised": ((0.995, 0.003), (0.215, 0.014)),
    "ground-sunken": ((0.945, 0.008), (0.130, 0.010)),
    "line":          ((0.885, 0.010), (0.290, 0.014)),
    "line-strong":   ((0.600, 0.015), (0.560, 0.015)),
    "ink":           ((0.210, 0.020), (0.950, 0.008)),
    "ink-soft":      ((0.440, 0.020), (0.760, 0.012)),
    "ink-faint":     ((0.600, 0.015), (0.580, 0.012)),
}
VOICE = {   # fill, text colour, wash
    "root":   (((0.640, 0.21), (0.530, 0.19), (0.950, 0.030)), ((0.700, 0.19), (0.770, 0.15), (0.270, 0.05))),
    "third":  (((0.700, 0.13), (0.450, 0.09), (0.950, 0.030)), ((0.760, 0.13), (0.800, 0.11), (0.250, 0.04))),
    "fifth":  (((0.560, 0.22), (0.470, 0.20), (0.950, 0.030)), ((0.660, 0.19), (0.770, 0.14), (0.270, 0.06))),
    "offkey": (((0.780, 0.15), (0.470, 0.10), (0.950, 0.045)), ((0.800, 0.15), (0.830, 0.13), (0.260, 0.04))),
    "clip":   (((0.470, 0.19), (0.420, 0.17), (0.940, 0.030)), ((0.520, 0.20), (0.740, 0.16), (0.240, 0.06))),
}
MEANING = {
    "root": "the brand's own voice: the mark, one emphasis per layout, the key number",
    "third": "in tune: success, a result that arrived, a metric going the right way",
    "fifth": "the overtone: links, focus, information",
    "offkey": "off key: a warning, something drifting",
    "clip": "clipping: an error, something that failed",
}
THEMES = ("air", "still")


def reach(light, chroma, hue, grounds, target, darker):
    """Move lightness in 0.005 steps until the colour clears `target` on every ground."""
    for _ in range(120):
        colour = to_hex(light, chroma, hue)
        if all(contrast(colour, g) >= target for g in grounds):
            return colour
        light += -0.005 if darker else 0.005
    raise SystemExit(f"cannot reach {target}:1 at hue {hue:.0f}")


def build_colour():
    values, report = {}, []
    for t, theme in enumerate(THEMES):
        air = theme == "air"
        v = {name: to_hex(*spec[t], HUE["root"]) for name, spec in NEUTRAL.items()}
        grounds = [v["ground"], v["ground-raised"], v["ground-sunken"]]
        v["ink"] = reach(*NEUTRAL["ink"][t], HUE["root"], grounds, 7, air)
        v["ink-soft"] = reach(*NEUTRAL["ink-soft"][t], HUE["root"], grounds, 4.5, air)
        v["ink-faint"] = reach(*NEUTRAL["ink-faint"][t], HUE["root"], grounds[:2], 3, air)
        v["line-strong"] = reach(*NEUTRAL["line-strong"][t], HUE["root"], grounds, 3, air)
        for name, spec in VOICE.items():
            fill, text, wash = spec[t]
            v[f"{name}-wash"] = to_hex(*wash, HUE[name])
            v[name] = reach(*fill, HUE[name], grounds[:2], 3, air)
            v[f"{name}-ink"] = reach(*text, HUE[name], grounds + [v[f"{name}-wash"]], 4.5, air)
            dark, pale = to_hex(0.21, 0.02, HUE["root"]), to_hex(0.985, 0.004, HUE["root"])
            v[f"on-{name}"] = max((dark, pale), key=lambda c: contrast(c, v[name]))
            report.append((theme, name, v[name], contrast(v[name], v["ground"]),
                           contrast(v[f"{name}-ink"], v["ground-sunken"]),
                           contrast(v[f"on-{name}"], v[name])))
            if contrast(v[f"on-{name}"], v[name]) < 4.5:
                raise SystemExit(f"{theme} on-{name} below 4.5:1")
        values[theme] = v
    return values, report


def colour_tokens(values):
    note = {
        "ground": "Page background.",
        "ground-raised": "Cards, fields and menus that sit on `ground`.",
        "ground-sunken": "Wells, table headers and code on `ground`.",
        "line": "Hairline dividers and card edges. Decoration only, below 3 to 1.",
        "line-strong": "Borders of fields and other controls. 3 to 1 on every ground.",
        "ink": "Body copy and headings on `ground`, `ground-raised` and `ground-sunken`. 7 to 1.",
        "ink-soft": "Captions and secondary copy on the three grounds. 4.5 to 1.",
        "ink-faint": "Placeholder text and disabled labels on `ground` and `ground-raised`. 3 to 1, never for copy that must be read.",
    }
    order = list(NEUTRAL)
    for name in VOICE:
        order += [name, f"{name}-ink", f"on-{name}", f"{name}-wash"]
        where = f"{NM.get(name, NM['root'])} nm" + (", the root hue at lower lightness" if name == "clip" else "")
        note[name] = f"Fill, {where}. Use for {MEANING[name]}. 3 to 1 on `ground` and `ground-raised`."
        note[f"{name}-ink"] = f"Text and icons in the {name} hue on the three grounds and on `{name}-wash`. 4.5 to 1."
        note[f"on-{name}"] = f"Text and icons on a `{name}` fill. 4.5 to 1."
        note[f"{name}-wash"] = f"Tinted background for a {name} notice or tag. Pair with `{name}-ink`."
    tokens = [{"name": n, "value": {t: values[t][n] for t in THEMES}, "usage": note[n]} for n in order]
    tokens.append({"name": "focus", "value": "{fifth}",
                   "usage": "Focus ring: 2px solid, 2px offset, on every interactive element. 3 to 1 on every ground."})
    return {"themes": [{"id": "air", "name": "Air"}, {"id": "still", "name": "Still"}], "tokens": tokens}


if __name__ == "__main__":
    values, report = build_colour()
    doc = {"name": "Resonans", "version": 1,
           "meta": {"note": "Generated by brand/system/build_tokens.py."},
           "color": colour_tokens(values), "type": type_tokens()}
    doc.update(other_families(values))
    OUT.write_text(json.dumps(doc, indent=2) + "\n")
    print("hues", {k: round(h, 1) for k, h in HUE.items()}, "nm", NM)
    for row in report:
        print("{:5s} {:7s} {}  fill/ground {:4.1f}  ink/sunken {:4.1f}  on-fill {:4.1f}".format(*row))
    for t in THEMES:
        print(t, {k: values[t][k] for k in NEUTRAL})
