---
name: review-video
description: The fresh-eye review loop on a rendered video. Fresh Opus readers with no context review the render, each finding is checked against frames, the ones that hold get fixed, and the loop re-renders until a review comes back clean. Use when Christian says "fresh review", "fresh eyes", "run a fresh Opus review", "blind-read this render", "review v13g" (any version with review, check or QA), "review until clean" or "keep fixing till the review passes", and as the last step of make-a-video and revise-video before a render goes to him.
---

# Review a video with fresh eyes

A **round** takes one stamped render and ends with either a clean review or the next stamped render and its
VERIFY.md section. The loop runs rounds until a review comes back clean. It ran this way in three sessions on
Cryptoleon reel 1 (v13 to v13g, 25 and 26 Oct 2026) before it became a skill.

## His calls

Christian decides these. Put them to him through the `grilling` skill, your pick first, never a table or a
review file (his call, 23 Oct 2026):

- any finding that changes a decision he already made: the holds ladder, runtime, how a character looks, the
  music, which take of a sound stays
- any paid call: ElevenLabs, image or video generation, each round, with the credit cost named
- whether the video is done. A clean review ends the loop; he watches the mp4 with sound before it ships

Fix without asking only what breaks a rule he already set (a hold under its floor, a hand clipping through a
prop, a sound off its frame). Name each such fix in the reply.

## Steps

1. **Render.** Name the render under review by its file. Read the project's VERIFY.md first: its open list
   and its rules (the holds ladder, his calls) are what readers get graded against. Done when the render path
   and the open list are in hand.
2. **Frames.** Extract every cut frame plus at least 1 frame per second, from the encoded mp4, into the
   session scratchpad. Also pull the voice or script text, and the mix's loudness (`volumedetect`).
3. **Readers.** Spawn fresh Opus readers with no context of the build, in parallel, one per pass: a viewer
   in the target role, and a motion reviewer. Never Fable. Each gets the frames, the script text, the rules
   from step 1 and these instructions:
   - return findings with a timestamp, a severity (blocking or not) and the frame file that shows it
   - report the count of frames actually loaded. One reader hit a rate limit and left 48 frames unchecked
     without saying so
   - what a transition looks like halfway: inside a growing wipe circle is the new scene. Two reviewers once
     called a flood edge a leak
   Every misreading by a reader is a defect in the video, not in the reader.
4. **Check each finding.** Open the frames around its timestamp at full resolution and read the source. A
   finding holds only when the frame shows it. Check a claimed proportion or duration against the data, not
   pixels: a pixel count put a map's violet share at 61 to 69%, the dot data held 76.3%. Compare the frames on
   both sides of every cut as contiguous strips. Done when each finding is marked holds, not real (with the
   frame that disproves it), or his call.
5. **Fix.** Fix each finding that holds at its cause, in the source, never with a patch over the frame. Put
   his calls to him (see above) and wait for those. Log a lesson that reaches past this video in
   `content-studio/LEARNINGS.md`.
6. **Re-render.** Run the project's Rebuild block (build, lint, mix, render, mux) to the next version letter.
   Leave `src/` and `index.html` alone while a render runs; it reads them live.
7. **Log.** Add a VERIFY.md section above the last one: what changed, each finding with its verdict, a checks
   table of measured numbers (lint, runtime against the last version, peak and mean loudness, holds against the
   ladder), and the open list with who holds each item.
8. **Loop.** Start the next round on the new render with new readers; never reuse a reader that saw an
   earlier version. Stop when a round finds nothing blocking that holds. Send him the render and ask for his
   watch.

## Notes

- Frame sheets, lint and contrast checks are a floor. Christian caught a 12 px layout jump, narration 2.6 s
  early and a logo off the music grid by watching, after every sheet passed. Watch the encoded mp4 with sound
  yourself before step 8.
- A reader sampling every 2 s never saw a wipe and called every one "arbitrary". Keep the 1 frame per second
  floor.
- When a fix moves time (a longer hold), every later cue moves with it: the timeline, the mix's effect
  times, the composition's `data-duration`, and a music bed that may now run short.
