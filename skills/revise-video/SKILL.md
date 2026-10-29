---
name: revise-video
description: A revision round on a video that already has a render. Use when Christian sends notes on a version ("notes on v6", "here are my notes", "apply my notes", timestamped notes after a render), asks for the next version ("make v7"), or wants the narration re-voiced or the voice changed. Not for a first build; that is make-a-video.
---

# Revise a video

A **round** takes one render plus Christian's notes on it and ends with the next stamped render and its VERIFY.md
section. Sound and script go first. Picture changes ride the next round, so he judges the new voice inside a
video before anything else moves.

Run every command from the project folder unless a step says `content-studio/`. The project's own `tools/`
(narrate, asr, retake, sfx, mix) and its VERIFY.md "Rebuild" block are the commands; read them there.

## His calls

Christian decides these, every round. Prepare each one as something he can hear or read, then wait:

- which script lines change (the grilling round in step 3)
- anything judged by ear: voice, speed, stress words, where delivery cues go
- any download, and any paid call beyond re-voicing the lines he approved
- every message to another person (Sai, a client) and every post
- whether a draft is good

A blanket go-ahead ("proceed with recommendations") approves the open items as you recommended them, those
and nothing new. Name each one you applied in the reply.

## Steps

1. **Version.** Name the render the notes are about. If he did not say, ask: a relayed "too abrupt" note
   once came from v9 or earlier. Done when the notes have a version stamp.
2. **Items.** Split the notes into numbered items, one change each. Copy every lesson that reaches past this
   video into the `writing-video-scripts` blocks (script rules) or `content-studio/LEARNINGS.md` (build and
   voice gotchas). Done when every sentence of his notes maps to an item number.
3. **Lines.** Put each script change to him through the `grilling` skill: one question per line, with its id
   (`scene.line`) and current wording in the question and the proposed wording as the first option. Check any
   fact a new line adds against the sources first. Never a table of rows (his call, 23 Oct 2026). Done when he
   has answered every question.
4. **Ear check.** List the words in changed lines whose meaning turns on stress (lamang, kita, upa, ani,
   lupa) and voice them in their lines through the project's `voice()`, then send the clip with the intended
   stress written beside each word. A Tagalog ear catches these; Scribe passes them, since the spelling
   matches. A reword that drops the word beats a respelling. Done when he has heard the clip, or approved the
   recommendation.
5. **Apply.** Write the approved lines into SCRIPT.md, then into every mirror of it (a recording script for a
   person, a posting kit, a caption). Grep the old wording across the project and the fork folder to find them.
6. **Anchors.** From `content-studio/`: `node scripts/check-anchors.mjs video-projects/<slug>`. Move each
   miss to a word the new line holds, and change any on-screen text that quoted the old line. Done when it
   exits 0, before any voice call.
7. **Voice.** Run narrate (it re-voices only changed lines), then asr. Move the last round's `qa/asr.json`
   and `qa/asr-raw.json` aside first, or asr reads the stale transcript. For each flagged line, run retake:
   a word heard wrong at every seed is the voice; one heard right when voiced alone was the full-mix read.
   Also search the transcript for every delivery cue word, to prove none was spoken. Done when each flagged
   line is fixed by a seed or listed as open for his ear.
8. **Build.** sfx, mix, build, lint and layout from the Rebuild block, then render to
   `renders/<slug>-v<N><letter>-<what>.mp4`, and encode a 720p share copy next to it (`-share.mp4`, x264 CRF 26,
   the master's audio copied, faststart; about 17 MB for 6 minutes; a 96k audio re-encode clipped at +1.2 dBFS). Christian shares the copy; the full render is the checkpoint.
   Give him the live studio's URL while a render runs. Leave src/ and index.html alone while a render runs; it reads
   them live.
9. **Verify and send.** Run the `review-video` skill on the render first. Add a VERIFY.md section above the last round's: what changed, then a checks table of
   measured numbers (Scribe word error rate, lint, layout, runtime against the last version). Send the render.
   Done when the section exists, the render is sent, and every open item names who holds it.

## Picture changes

Notes about the picture (new scenes, scale, b-roll, motion) wait for the next round. Ask for or reuse an
approved list, then follow `make-a-video` and `hyperframes` for the build, with the live studio open first.
