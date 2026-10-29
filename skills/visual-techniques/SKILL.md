---
name: visual-techniques
description: >
  Art-direct an image with a named vocabulary of 30 visual techniques, grouped by
  the job each does for the eye (differentiate, group, sequence, predict). Four
  verbs: read (name the techniques in references), brief (grill the job, then
  shortlist techniques), map (publish a matrix artifact of references against
  techniques), check (test a draft against its brief). Mixes the jason-murray and
  kole-jain lenses, thinking-tools select, and the grilling skill. Triggers:
  "/visual-techniques", "what techniques are in this", "read these references",
  "art direct this", "which technique fits", "technique map".
---

# visual-techniques

A working vocabulary for making and judging images: posters, covers, ads, key visuals,
photography. The vocabulary is `references/techniques.json`, 30 techniques built on 20 Oct
2026 from Jason Murray's public Shorts and newsletter. Murray's names and quotes are
credited per entry; every definition marked `ours` was written here. Nothing comes from his
Iris app, which is behind a sign-in. Never call this tool Iris or present it as his.

Paths are from the repo root. A project's map lives in
`design-artifacts/technique-maps/<slug>/`: `map.json` and a `refs/` folder of images.

## Domain check, before any verb

Strongest on still images with an idea behind them. Say so in the first line, then route:

- **UI and product screens**: run `/lens kole-jain classify` in its place; these techniques
  read pictures, not interfaces.
- **Logos and marks**: the `logo-design` skill owns construction and small-size tests. This
  skill can still say which technique a mark uses.
- **Motion**: one frame at a time only. Say what a single frame cannot show.

## read: name the techniques in references

Input: image files, a folder, a URL, or an Eden board (`eden_read_board`).

1. Copy each image into `refs/`, longest side 800 px (`sips -Z 800`). These copies are the
   map's record of what was read.
2. Look at each image and name its **two or three standout techniques**, never ten. Murray's
   chef rule: many ingredients, two or three stand out. Each read carries the evidence, what in
   this image shows it, in one line.
3. When the image has an idea, name it with `/lens jason-murray classify`: insight, idea (the
   verb), then the techniques as execution. No idea readable: say so.
4. When nothing in the 30 fits, write the move in plain words under `gaps` in `map.json`.
   Never stretch a technique to cover it.

## brief: grill the job, then shortlist

Follow the `grilling` skill: rounds through AskUserQuestion, recommendation first. The
design tree, in order:

1. **References first.** Ask for his moodboard or earlier drafts and run `read` on them
   before any shortlist. On 6 Oct four wordmarks were drawn before his Eden board was seen,
   and he went back to his own drawing.
2. **The idea.** What the image does with its truth, as a verb (Murray's pyramid).
3. **The eye's job.** One of the four jobs in `techniques.json`, with the reason.
4. **Medium and limits**: size, format, one colour, print, platform.

Then shortlist: **two techniques by default, four at most**, each with what it would have
him do here and a reference from `refs/` that shows it. Add one dissent from
`/lens thinking-tools select "<the brief in one sentence>"`: the entry that argues against
the shortlist, or "none fits" when none does. Show the shortlist and stop. Nothing is drawn
or generated until he picks.

## map: publish the matrix

1. Write `map.json` to the format in `references/map-format.md`.
2. Run `python3 skills/visual-techniques/scripts/check_map.py <slug>`. It rejects unknown
   technique ids, missing images and more than three reads per image, and prints the `files`
   argument for the publish.
3. Copy `skills/visual-techniques/map/index.html` to the session scratchpad as
   `<slug>.html` and publish that copy with the Artifact tool and that `files` map. One page
   path per project: publishing the shared file itself would overwrite whichever map that
   session published first. First publish: `icon: "grid"`, then record the URL in
   `map.json` as `artifact`. Every later publish passes it as `url` so the link stays.

## check: test a draft against its brief

Input: a draft image and the project's `map.json`. Run `read` on the draft, then
`/lens jason-murray challenge`: does the idea survive, and are the shortlisted techniques
present and serving it or decorating it. Add the draft to the map with `"draft": true`.

## Rules

- **Provenance.** A definition from Murray is quoted and carries his source; one marked
  `ours` is ours. A job placement marked `ours` was never shown on his map.
- **Low-confidence names.** Six names were read from 4-pixel letters (`conf: low`). Use them,
  and say so when one decides a read.
- **Restraint.** Two or three techniques per image, two per shortlist. A long list means the
  read failed.
- **Show before acting.** Every verb ends by showing its output. Files outside the map
  folder change only after he answers.
- **Adding a technique.** A new name goes into `techniques.json` only with a public source
  or marked `ours`, never from the Iris app.
