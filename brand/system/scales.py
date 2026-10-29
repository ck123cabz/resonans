"""The Resonans scales that are not colour: type, space, radius, stroke, time.

Each one is built from the interval ratios of the A major triad, 4 : 5 : 6.
  5 : 4  major third      type sizes step by it
  3 : 2  perfect fifth    body line height, and each duration to the next
  2 : 1, 3 : 2, 4 : 3     the only ratios between neighbouring space steps
"""
THIRD, FIFTH = 5 / 4, 3 / 2
BASE = 16                      # px; the body size every type step is counted from
UNIT = 4                       # px; the space fundamental
PARTIALS = (1, 2, 3, 4, 6, 8, 12, 16, 24)   # products of 2 and 3 only


def size(step):
    return f"{BASE * THIRD ** step:.2f}px".replace(".00px", "px")


def type_tokens():
    def style(name, step, line, weight, usage, sample, **more):
        return {"name": name, "fontSize": size(step), "lineHeight": line, "fontWeight": weight,
                "usage": usage, "sample": sample, **more}

    return {
        "fonts": [
            {"family": "Jost", "file": "fonts/Jost-Variable.woff2", "weight": "100 900"},
            {"family": "Atkinson Hyperlegible Next",
             "file": "fonts/AtkinsonHyperlegibleNext-Variable.woff2", "weight": "200 800"},
            {"family": "Atkinson Hyperlegible Mono",
             "file": "fonts/AtkinsonHyperlegibleMono-Variable.woff2", "weight": "200 800"},
        ],
        "families": {
            "display": '"Jost", "Futura", "Century Gothic", sans-serif',
            "body": '"Atkinson Hyperlegible Next", "Verdana", "Segoe UI", sans-serif',
            "data": '"Atkinson Hyperlegible Mono", ui-monospace, "Menlo", monospace',
        },
        "groups": [
            {"name": "Display", "family": "display", "styles": [
                style("display", 7, 1, 500, "One per page: a cover or a hero line.", "In tune", letterSpacing="-0.02em"),
                style("headline", 5, 1.125, 500, "Page titles.", "What the audience hears", letterSpacing="-0.015em"),
                style("title", 3, 1.25, 500, "Section headings.", "Brand kit, then calendar, then posts", letterSpacing="-0.01em"),
                style("subtitle", 2, 1.25, 500, "Card titles and sub-headings.", "First customer"),
            ]},
            {"name": "Text", "family": "body", "styles": [
                style("lead", 1, 1.5, 400, "The opening paragraph under a headline.", "We take what a business means and work out how its buyers say it."),
                style("body", 0, 1.5, 400, "Running copy. Keep lines near 65 characters.", "Free until the first customer arrives."),
                style("body-strong", 0, 1.5, 700, "Emphasis inside running copy, and button labels.", "3 posts a day, 2 videos a week"),
                style("small", -1, 1.5, 400, "Captions, helper text and footnotes.", "Counted from the first post on 2 October"),
            ]},
            {"name": "Data", "family": "data", "styles": [
                style("readout", 3, 1, 600, "The number in a Readout.", "1,284"),
                style("data", 0, 1.5, 400, "Tables, codes and figures inside copy.", "620 nm  496 nm  413 nm"),
                style("label", -1, 1.25, 500, "Uppercase labels over a value or a section.", "REACH THIS WEEK", letterSpacing="0.08em"),
            ]},
        ],
    }


def other_families(values):
    ratio = {2: "an octave", 1.5: "a fifth", 4 / 3: "a fourth"}
    space = []
    for i, p in enumerate(PARTIALS):
        up = f" Up {ratio[round(p / PARTIALS[i - 1], 4)] if round(p / PARTIALS[i - 1], 4) in ratio else ratio[4 / 3]} from the step below." if i else " The fundamental."
        use = {1: "Icon to label, tag padding.", 2: "Between a label and its field.", 3: "Button and field padding.",
               4: "Card padding on phones, gaps in a form.", 6: "Card padding, gaps between cards.",
               8: "Between groups inside a section.", 12: "Between sections on phones.",
               16: "Between sections.", 24: "Page top and bottom, around a hero."}[p]
        space.append({"name": f"space-{p}", "value": f"{UNIT * p}px", "usage": use + up})
    focus = {t: f"0 0 0 2px {values[t]['ground']}, 0 0 0 4px {values[t]['fifth']}" for t in values}
    return {
        "spacing": {"note": "A 4px fundamental times partials 1, 2, 3, 4, 6, 8, 12, 16, 24.", "tokens": space},
        "radius": {"note": "The wordmark's stroke ends in a half circle, so controls do too.", "tokens": [
            {"name": "radius-1", "value": "4px", "usage": "Tags, checkboxes, small marks."},
            {"name": "radius-2", "value": "8px", "usage": "Fields, notices, menus."},
            {"name": "radius-3", "value": "12px", "usage": "Cards and panels."},
            {"name": "radius-round", "value": "9999px", "usage": "Buttons and pills: a half circle at each end, like the letters' stroke."},
        ]},
        "shadow": {"note": "No drop shadows. Height is shown by a lighter ground and a hairline.", "tokens": [
            {"name": "ring-focus", "value": focus, "usage": "Focus ring where an outline cannot be used: a 2px gap in `ground`, then 2px of `fifth`."},
        ]},
        "stroke": {"note": "The mark and the letters share one stroke: 16 units on an x-height of 100.", "tokens": [
            {"name": "stroke-hair", "value": "1px", "usage": "Dividers and card edges."},
            {"name": "stroke-firm", "value": "2px", "usage": "Field borders on focus, the focus ring, chart lines. An octave above the hairline."},
        ]},
        "time": {"note": "Each duration is a fifth longer than the one before: 120 ms times 3/2.", "tokens": [
            {"name": "time-1", "value": "120ms", "usage": "Hover and press on small controls."},
            {"name": "time-2", "value": "180ms", "usage": "Fields, tags, toggles."},
            {"name": "time-3", "value": "270ms", "usage": "Cards, menus, notices arriving."},
            {"name": "time-4", "value": "405ms", "usage": "Page-level moves and the mark settling."},
        ]},
        "ease": {"note": "One curve. It passes the target by 4% and comes back, like a struck plate settling.", "tokens": [
            {"name": "ease-settle", "value": "cubic-bezier(0.2, 0.9, 0.3, 1.04)", "usage": "Every transition. Under reduced motion, cut the move and keep the end state."},
        ]},
    }
