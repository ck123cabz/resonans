---
name: writing-video-scripts
description: Use when writing or revising a script for a sales video, VSL, explainer, process video, YouTube brand video or the video slot in a cold email, for any product, including faceless AI-voiced videos and any voiceover with screen directions.
---

# Writing video scripts

A script is built in a fixed order. Words come last. Each step below has its own block file; read the block before doing the step.

## The order

| Step | Do | Block |
|---|---|---|
| 1 | Name the viewer, the surface, and the one feeling at the end | `blocks/universal/01-insight.md` |
| 2 | Find the insight about that viewer, then the one idea | `blocks/universal/01-insight.md` |
| 3 | Lay out the segments with a time budget each | `blocks/universal/02-structure.md` |
| 4 | Plan the visuals per segment and list the assets | `blocks/universal/03-visuals.md` |
| 5 | Write the voice lines | `blocks/universal/04-copy.md` |
| 6 | Check every claim against a public source | `blocks/universal/05-claims.md` |
| 7 | Stress-test with lenses and a cold read | `blocks/universal/06-stress-test.md` |


## Output

One markdown file per script, in the project's video folder, with:

1. Frontmatter: `job: persuade`, title, surface, viewer, voice, length, date.
2. The first voice line, alone, as the first line after the frontmatter. The linter reads it as the opener.
3. The block 01 table: viewer, surface, feeling, insight, idea.
4. The segment table from step 3.
5. The visual plan and asset list from step 4.
6. The script: one `## m:ss · beat` section per beat, each with **Voice.** and **Screen.**
7. Claims: the block 05 record and the "left out on purpose" list.
8. Still open: every fact only a named person can give. When no person is named, ask who owns it. Leave out the person's own decisions, because the grilling round in the gates below asks them.

Then run `python3 scripts/ai_slop_lint.py <file>`. The file is finished at CLEAN: 0 tier1, 0 tier2 over cap, 0 structural. A structural hit in a script is a failure to fix, never a hint to judge.

## Gates

- Show the person the segment table and the first line before writing the rest.
- Before step 5, the product's owner, not only the person directing the video, reads the step 2 idea and the step 3 table. Ask them what the product does before the viewer's own work starts that the draft leaves out; that is the story by default (block 02, first rule). A client scrapped a script after the build began, though it had passed 2 stress tests.
- When asked to flesh out a section, add the events, people and dates behind it, not more screen time for what is already there. On 13 Oct 2026 the first draft of a longer Philippine section for Why Nations Fail Ep 1 only stretched it; Christian meant more of what happened and more context.
- When the owner redirects, archive the old script and rebuild from a new step 3 table; a patch keeps the old story.
- Put changes to the person through the `grilling` skill, stress-test findings included: one question per line, its id and current wording in the question, the recommended wording as the first option, and the competing proposals as the others. Apply only what they pick. Never hand them a review file or a table to approve; Christian set this on 23 Oct 2026 because a grilling round gets his feedback faster. Their earlier calls stay locked unless they reopen them.
- Never lift a writing ban because the copy is marketing. See `blocks/universal/04-copy.md`.

## Common mistakes

| Mistake | Seen as | Fix |
|---|---|---|
| Writing words first | a feature tour: sellers, buyers, file, proof | Steps 1 to 3 before any line |
| Plain report voice | lines a person would not say aloud to a buyer | The insight scene in step 2 sets the voice |
| Lifting the bans for "marketing" | tricolons, "Picture...", a closing beat | The bans hold; see block 04 |
| Naming the product first | the viewer leaves before the problem lands | Product named at about 45% of the run time |
| An unsourced claim | "every firm", "weeks of work" | Block 05: cut it or source it |
| Owner never saw the spine | the script is scrapped after the build begins | The owner gate above, before step 5 |
