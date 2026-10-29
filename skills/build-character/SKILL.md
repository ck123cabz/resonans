---
name: build-character
description: Build a client's recurring drawn character (mascot, NFT avatar, illustrated person) into a character standard that every shot draws from, matched to a style target and checked step by step with the user. Use when a character must appear in more than one shot or video, when a character looks off-model or drifts between shots, or when the user says "build the character", "rig this mascot" or "make a character standard".
---

# Build a character

A **character standard** is the one signed-off set of numbers, shapes, arm rig, paint, poses and expressions a
character is drawn from in every shot (terms in `content-studio/GLOSSARY.md`, section "Character standard"). This
skill ends at signed-off sheets. Putting the character into a reel belongs to `make-a-video` and `revise-video`.

Leon (Cryptoleon, Survived Rugs, 24 Oct 2026) is the worked run behind every step: his rig is
`video-projects/cryptoleon/survived-rugs/rig/`, and the decision log is `../LEON-RIG-BRIEF.md` beside it.
`references/rig-layout.md` says what each rig file does.

## Two sources, two jobs

Name both before anything else. The skill does not start without them.

- **Style target**: the existing show or art the character must look like it belongs in. Every size, the line weight
  and the paint style come from it. For Leon: Lil Pudgys, the pink penguin in overalls at 30 s of YouTube VE2ouVTiitU.
- **Identity source**: the client's own art. It gives traits and colours only, never a size.

Leon drifted for eight art passes while his avatar was both. The drift stopped the moment the show became the
target and the avatar went traits-only.

## The loop: grill, build, sheet, sign-off

Every step runs the same four beats, and the next step starts only after the last one.

1. **Grill.** Load the `grilling` skill and put that step's open calls to the user (each step file lists them). Facts
   are found, never asked: frames, pixel readings and file contents are the agent's job. Record each answer in the
   character's brief as it lands.
2. **Build.** Do the step's work from its step file.
3. **Sheet.** Render the step's check sheet, beside the style target at the target's scale. Run the step's checks.
   For proportions, arm, paint, poses and expressions, send the sheet to one fresh reader (`references/reader.md`),
   then measure every claim it makes before applying it.
4. **Sign-off.** Send the sheet to the user with what changed, what was measured and what is still an estimate.
   The step is done when the user passes it. A correction from the user re-enters the same step at Build.

## Steps

Read each step's file when you reach that step, not before.

| # | Step | File | Done when |
|---|---|---|---|
| 1 | Sources | `references/1-sources.md` | both sources named, frames saved beside the rig |
| 2 | Measure | `references/2-measure.md` | every number in `spec.js` cites a pixel reading |
| 3 | Proportions | `references/3-proportions.md` | the grey outline sits on the target's edge in the onion skin |
| 4 | Arm | `references/4-arm.md` | one arm, one length in every view, joins invisible |
| 5 | Paint | `references/5-paint.md` | front and side painted, the reader's measured faults fixed |
| 6 | Poses | `references/6-poses.md` | each pose reads as its action, front and side |
| 7 | Expressions | `references/7-expressions.md` | each expression reads at phone size, no two alike |
| 8 | Idle cycles | `references/8-idle.md` | not yet run |
| 9 | Framing presets | `references/9-framing.md` | not yet run |
| 10 | Props to scale | `references/10-props.md` | not yet run |

Steps 8 to 10 have never been run, not even on Leon. Say so to the user when you reach one, follow its file as a
first draft, and rewrite that file's checks from what the run teaches.

## When a view is missing

If the style target never shows a view (Lil Pudgys never turned a penguin to profile in VE2ouVTiitU), search more
episodes or official art for it first. If none turns up, estimate the view from the front numbers, write "estimate"
on every sheet that shows it, and put it to the user at that step's grill.

## Finish

When the last run step is signed off, post the outcome as a comment on the character's issue: the sheets, the files,
what is still an estimate. Then add this run's new lessons to the step files they belong to.

Renders use `rig/sheets/render.sh`: headless Chrome often exits non-zero after writing the PNG, so the script
checks for a fresh file instead of the exit code.
