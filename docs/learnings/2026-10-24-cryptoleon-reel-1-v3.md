---
job: tell
---
# Cryptoleon "Survived Rugs" reel 1, all-vector v3 and v4, 24 October 2026

Christian asked at about 10:00 am on 24 Oct for reel 1 rebuilt in HyperFrames as studio-grade 2D vector, with no paid
AI generation, Haiku agents allowed for assets. The night before had tried four methods (vector v1, vector v2, Grok
stills with Kling, rig v2); v2 vector read as a flat icon with a star crown and no rooms.

## What worked

- One cut-out puppet in SVG, instanced three times (2023 top, today bottom, end tag). Head on a neck pivot, flippers
  on shoulder pivots, eye sets swapped whole, shades that sit up or down. Matched poses are one table of angles both
  halves read at the same second, so "same pose, different life" holds by construction.
- Pushing the 2023 shades up onto the crown gave his eyes a job: tired, gritted, asleep, and the first smile.
- Four Haiku agents drew the room plate, the deck plate and eight props in about 4 minutes each, against a written
  spec (`art/STYLE.md`) with fixed canvas, calm zone, palette, id prefixes and a render-and-look loop. They needed one
  follow-up each at most (laptop keys). Their one weak piece, the clink backdrop, was replaced by the two real plates
  pushed in 2.2x and blurred.
- Night grade on the character through an `feColorMatrix` filter. The first matrix turned him lavender; a near-neutral
  one (0.80, 0.83, 0.86 diagonal) kept his green and white.
- Effects synthesized in ffmpeg (`mix.sh`): pink-noise whoosh, a decaying-sine click, a gated square buzz, a
  four-partial glass clink. Click sat 17 dB and clink 7.5 dB over the bed in their band.

## What the blind reader caught (v3), all fixed in v4

A chin-on-flipper beat that read as nothing (replaced by noodles against a sip), props floating at flipper tips (a
flipper tip now wraps each held prop), a phone that landed far from where he set it down, a locked camera for 12
seconds (each panel now moves per beat), crown sparkles on the sad 2023 Leon, a floor shadow under the counter, eyes
peeking over the shades when he looked up, and a translucent clink burst.

## Gotchas

- `npm run sheet` takes the OUTPUT path first. Passing frames only overwrote the first frame with the sheet.
- The HyperFrames studio stamps `data-hf-id` into every .html file in the project, a source template included, so an
  exact-string edit of the template fails afterwards. Match with a pattern.
- `gsap.from(el, { y })` on an SVG element that carries a `transform` attribute animates from the absolute value, so
  the element flies in from the top. Wrap it in a bare `<g>` and tween the wrapper.
- A `back.out` slide of a half-height panel overshoots past its slot; make the panel taller than its slot.
