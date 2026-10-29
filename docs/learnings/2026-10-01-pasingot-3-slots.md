---
job: tell
---
# Pasingot "3 slots left" reel, 1–4 October 2026

Project: `video-projects/pasingot-3-slots/`. A 20.4s 9:16 motion reel for the Pickle
Blinders × Marey Courts money game on Sunday 4 October, built from a designer's asset kit
(README, layered HTML, logo parts, storyboard frames).

## How Christian works on a reel

- He gives direction in short turns while watching renders: "pickle blinders intro and
  outro", "collab with marey", "In collaboration with" on the hand-off. All 3 came after he
  watched a render, so render early.
- He catches what the checks miss. On 10/1 he saw a 12px layout jump at 7.73s that every
  frame sheet had passed. Watch the actual mp4 in motion before calling a pass done.
- He picks from options he can see. The footer was chosen from five full-size
  mockups (A–E in `qa/mock/`); he took C, the collab lockup, at the designer's spacing,
  over D's bigger hierarchy rework.
- On 10/1 he kept the designer's layout and added brand moments on top: the intro, the
  outro, the collab lockup. Treat the designer's README as the plan and confirm before
  changing its spacing.
- He says "7–8 mins" for 7–8 seconds. Read timestamps in context.

## Process that worked

- A designer's README is the plan. The motion-showreel skill's grammar (HUD, chapters,
  flurry) fought the poster brief, so only its beat grid, cue sheet, mixer and checks were used.
- Show the beat plan before building. The intro, outro and 20.4s length were decided at
  that gate, before any code.
- Prove every claim with a measurement: hit onsets with `analyze-reference.mjs`, loudness
  and peak after AAC with ebur128, layout jumps with a frame-to-frame row-profile scan,
  font changes with a PSNR diff.
- Keep audio rebuildable from tracked files: `mix.sh` in the project rebuilds both mixes.

## HyperFrames and layout gotchas

- Text that types on by growing `textContent` reflows a flex layout: an empty line has no
  height, so the first letter pushes everything up. Keep the full string in the line and
  hide the untyped part (`visibility:hidden` span).
- `url()` inside a CSS file resolves from the CSS file's folder. `fonts.css` pointed at
  `assets/fonts/...` and loaded nothing; HyperFrames hid the bug by fetching the same
  Google families at compile time. Check fonts in a plain browser too.
- A full-frame clip's `data-duration` can cover the next scene: the hand-off square ran to
  14.6s and hid the first 0.2s of the court. End a cover clip when it stops changing.
- Lint rules met here: no `letterSpacing` tweens (split into glyph spans and tween `x`),
  a `tl.set` hard kill at a clip's end, and one root composition per project folder
  (name templates `.tmpl`).
- Logo parts with cut-outs move only while the part covering the cut is in place, and
  every part transforms from its `parts.json` origin.
- Logo parts are full-canvas PNGs; to size a mark, crop the layered parts to their union bbox
  (`crop()` in `build.py`).
- zsh: `$L:a` is a path modifier and unquoted variables do not word-split. Use `${L}`,
  `${=pair}`, or `bash -c`.

- Keep composition scripts out of the global scope. External `<script src>` files that
  declare top-level `const $`, `E` or `T` loaded fine in plain Chrome but ran nothing
  under HyperFrames (Pasingot recap, 5 Oct): every frame came out static with no error in
  the render log. Inlining them inside one `(() => { ... })()` after the composition div
  fixed it; `build.py` there does the inlining. A timeline created in an inline script
  was also not visible to an external file, and `tl is not defined` was the only clue.
- `hyperframes snapshot --at t1,t2,...` gives frames in about a minute; a full render
  took 4 to 8 minutes. Debug layout with snapshots.

## Sound

- ElevenLabs free plan: sound effects work (about 338 credits for ten effects, two of them
  14s and 9s beds); the music API is paid-only; four requests at a time, so `sfx.mjs`
  needs a rerun (it skips files it has); one generation came back silent at -66 LUFS.
  Measure every file before using it.
- Epidemic Sound on this account: search and the edit tool work; every download returns
  FORBIDDEN, so previews are draft-only. Its `forceDuration` edit stretched or rearranged
  the song, so cut from the full track yourself.
- Use the search's BPM filter to match the reel's grid (100 bpm here), then check where in
  the song the cut starts. The first cut used the 45s breakdown and Christian said it did
  not sound like the track he picked; the opening riff from 0.45s did.
- Dense rock clipped at +1.1 dBFS after AAC; `alimiter=limit=0.7` before encoding fixed it.
- When effects are picked by measurement, say so and give him an A/B file
  (`renders/sfx-AB.wav`).

## Still open from this project

- Epidemic needs a paid plan before the Midnight Mode version can be posted; recipe in
  the project's `SOUND.md`.
- The four close effect calls in `sfx-AB.wav` and a phone-speaker listen are his.
