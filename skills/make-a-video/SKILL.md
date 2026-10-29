---
name: make-a-video
description: Beginner-friendly end-to-end video creator for HyperFrames. Use when the user says "make a video", "create a video", "new video", "build a video", "video from scratch", "I want to make a video", "help me create a video", or when someone who's never used HyperFrames before arrives with a concept, script, or rough idea and wants a finished MP4. Interviews the user in one pass, then builds the full video with mandatory preview and visual-verification gates.
---

# Make a Video — The Beginner-to-Finished-MP4 Skill

Two phases, eight sequential gates. Every gate produces a concrete artifact the next gate consumes. Don't skip gates.

## When to use this skill — and when to hand off

**Use this skill when:**
- The user is new to HyperFrames and starting from a concept, script, or outline
- They want an end-to-end walkthrough, not framework reference material
- They haven't decided on format yet

**Hand off when:**
- The user pastes a URL and wants a video from that site → invoke `/website-to-hyperframes`
- The user explicitly wants a 9:16 vertical talking-head with face-cam + scene overlays → run Gates 1–4 here, then invoke `/short-form-edit` from Gate 5 onward
- The user asks for framework rules, not a video → invoke `/hyperframes`

## The two phases

- **Phase 1 — INTERVIEW (Gates 1–4):** one conversational pass to gather *everything* before touching code. Intent, format, script, voice, style, assets, pacing. Synthesize into a `BRIEF.md` and wait for explicit approval. Ask in short rounds with a recommended option first, and let the person talk a question through before forcing a pick. Settle open calls by showing (a beat plan, full-size mockups, A/B audio, several takes), not by describing them.
- **Phase 2 — BUILD (Gates 5–8):** scaffold → storyboard → compositions → lint → Studio preview → draft render → visual verification → MP4 preview → final render.
- **Between rounds:** put findings and proposed changes to the person through the `grilling` skill, one question per change with the recommended option first, and apply only what they pick. No review document or table of rows (Christian, 23 Oct 2026). Calls the person already made stay locked unless they reopen them.

---

## Gate 1 · Intent & format

Ask one question at a time via `AskUserQuestion`, multiple-choice where possible.

1. What's this video for? (promo · social ad · launch teaser · product demo · tutorial · explainer · intro/outro card · other)
2. Who's the audience? (open-ended)
3. Target duration? (10–20s short · 20–45s promo · 45–90s explainer · 1.5–3 min lesson · custom)
4. Aspect ratio? (16:9 1920×1080 · 9:16 1080×1920 · 1:1 1080×1080)
5. Frame rate? (30 default · 60 for crisp UI · 24 cinematic)
6. Platform / delivery constraints? (file size · deadline · where it'll play)

**Gate:** all six captured. If the answer is 9:16 + face-cam, plan to hand off to `/short-form-edit` at Gate 5.

Full question bank: `Read: references/interview-questions.md`

---

## Gate 2 · Script & voice

1. Script source? (paste · outline → I'll draft · I'll record · TTS from text · no narration)
2. If TTS: voice preference. Offer choices from `npx hyperframes tts --help`. Pace is the voice's measured words per minute, never a speed setting.
3. If face-cam: recording path · full-screen or corner placement · need transcription? (`npx hyperframes transcribe <file> --model small.en --json`)
4. Captions? (off · hype · corporate · karaoke-word-by-word · minimal)

Write or revise the script with `/writing-video-scripts`.

- **Never retime the voice.** No atempo, no speed change, not even at 1. Measure the chosen voice's words per minute, set a word budget per segment from it, and fit length with words and pauses. Christian: "i dont like it when we retime voice because it breaks quality."
- **Decide by ear on an audition page.** Voices, music, effects, and every acronym or term of art as 3 to 5 short clips; two guessed spellings of one acronym both read wrong. Write the picked spelling into the voice text with who picked it. Closing line: pinned seed, higher stability, a take whose pitch falls at the end (a rising one sounded unsure).

**Gate:** script captured (or drafted), audio plan captured, caption plan captured.

---

## Gate 3 · Style intake

**Before asking the user anything, inventory existing assets.** Check `<workspace-root>/assets/` and any project `assets/` folder. Don't ask for what's already there.

**The brand kit is the look.** If the client has a brand folder or live site, take colours and type from it as tokens in one core file and offer that as the default answer to every look question below. A deck, reference or past video is a source for copy only. The brand's rules beat any skill's motion grammar; take only the skill's mechanics. Flag any off-kit pick as a conflict before building. Christian picked a deck palette at intake and reversed it after the render: "we must still use the brand kit."

Then ask progressively — they don't need answers to all of these:

1. Style guide or brand doc? (paste/path · no)
2. Color palette? (brand kit tokens · hex codes · none — use MOTION_PHILOSOPHY defaults)
3. Fonts? (Google Fonts name(s) · file paths · none — use Inter + JetBrains Mono defaults)
4. Logo file? (path · none — use text wordmark instead)
5. Reference videos for vibe? (URLs/paths · none)
6. Other assets? (screenshots · product photos · b-roll · music — list paths)
7. MOTION_PHILOSOPHY aesthetic (black canvas · chrome type · perspective grid · whip transitions) or a different feel?
8. Pacing? (kinetic 1–2s · balanced 2–3s · relaxed 3–5s) Ask for a past approved video as the pacing reference now. Asked after a render, it came too late: "the pacing, everything is off."
9. Music? (none · ambient pad 0.15 · music bed 0.4 · full 0.8 — file path if they have one)
10. Outro / call-to-action text?

**Never impose a brand on the user.** Fall back to MOTION_PHILOSOPHY defaults *only* when they explicitly decline to supply a style.

Full style flow + MOTION_PHILOSOPHY defaults: `Read: references/style-intake.md`

---

## Gate 4 · Brief synthesis (HARD-GATE before building)

1. **Read `MOTION_PHILOSOPHY.md`** if it exists in the workspace root — mandatory if present. If missing, proceed with the defaults in `references/style-intake.md` and note the absence in the brief.
2. **Ask where projects live** if it's not obvious:
   - If `video-projects/` exists → use `video-projects/<slug>/`
   - Otherwise → ask the user
3. **Write `<project-folder>/BRIEF.md`**:
   - slug · intent · audience · dimensions · fps · duration
   - script (full or outline)
   - voice choice and its words per minute · caption plan · face-cam plan
   - style profile: palette (hex), fonts, logo path, reference videos
   - pacing, with the past approved video that sets it
   - asset inventory with paths
   - outro / CTA text
4. **Show the brief. WAIT for explicit approval.** Don't proceed to Gate 5 without a clear "yes, build it."

---

## Gate 5 · Scaffold & storyboard

### Handoff check first

If the brief describes a 9:16 vertical talking-head with face-cam + scene overlays, invoke `/short-form-edit` NOW and hand off the brief. Its transcript-driven workflow covers hooks, cuts, captions, footage, and sound.

Otherwise continue:

### Scaffold

1. `mkdir <project-folder>`
2. If a sibling project with similar format exists, offer to copy its `hyperframes.json` + `meta.json` as a template. Otherwise from inside the folder: `npx hyperframes init`
3. Edit `meta.json` with the user's slug, dimensions, fps.
4. Copy supplied assets into `<project-folder>/assets/`.
5. Create `<project-folder>/assets/style-profile.md` from Gate 3 — single source of truth for palette/fonts/logo.
6. **One command rebuilds everything.** Soundtrack and render come from tracked files with one command (mix scripts rebuilt a soundtrack in 2 to 3 s). When a finished build's scenes are worth reusing, copy it back into a starter; one VSL build seeded the next two cuts.
7. **Contact-sheet assets before use.** Every reusable asset and every large glyph at full size (an icon sheet caught floating heads; a display font at 380 px switched to a hairline optical size). Load fonts in a plain browser too: the renderer fetches fonts itself and hid a `fonts.css` whose `url()` resolved from the wrong folder.

### Storyboard

Generate `<project-folder>/STORYBOARD.md` using the template in `references/storyboard-template.md`. Every beat gets:

```
Beat N — TITLE (start–end, duration) — Concept in one sentence
Visual elements: [each element, size, animation, timing]
Motion language: [kind of motion]
Eases used: [3–4 distinct GSAP eases]
Exit: [transition into next beat]
Audio: [VO line / SFX / music layer]
```

Top of file: a timing table with scene · start · duration · composition file.

**Every `Exit:` names a visible reason for the cut.** A colour change rises as an arch or floods out of an object already on screen, in the next scene's colour. A same-colour cut carries one object across at the same position. Never paste in a clip or an empty colour frame; a wipe carries the next chapter's title. Christian: "it swaps into the next thing, and it doesn't flow." Readers called an empty wipe a dropped frame.

**Propose a rule-of-threes structure:**
- Act 1 (hook) ≈ 20% of duration
- Act 2 (body) ≈ 55%
- Act 3 (payoff + outro with 4–6 second hold) ≈ 25%. Hold the logo lockup long enough to read, then shrink it to a corner where it stays. Christian: "minimize it somewhere where it stays on the screen."

(MOTION_PHILOSOPHY §0 Law 9, §1.)

**Map user intents → catalog blocks:** `Read: references/catalog-intent-map.md`

**Gate:** show storyboard + timing table. Iterate until the user approves.

---

## Gate 6 · Build compositions

Invoke `/hyperframes` for framework rules. This skill owns the scaffold and discipline; `/hyperframes` enforces the rules.

### Scaffold every sub-composition

```html
<div data-composition-id="scene-name" data-start="..." data-duration="...">
  <style>[data-composition-id="scene-name"] { /* scoped */ }</style>
  <!-- DOM -->
  <script>
    (function(){
      const SLOT_DURATION = ...;
      const tl = gsap.timeline({ paused: true });
      // ... tweens ...
      tl.to({}, { duration: SLOT_DURATION }, 0);   // anchor — MOTION_PHILOSOPHY Law 11
      window.__timelines["scene-name"] = tl;
    })();
  </script>
</div>
```

Full boilerplate + captions pattern + ambient-bg pattern: `Read: references/composition-scaffold.md`

**Drive it as a pure function of time.** One paused timeline whose single driver calls `frame(t)`, each scene computing its state from `t` alone, exposed on `window` so tools can seek it (a 1:58 draft rendered in 1:41). Generate the composition with a build step that inlines CSS, fonts and scripts into one function body: top-level consts in external scripts rendered every frame static with no error. Use function replacements in `String.replace`, since a `$$` in a replacement string collapses to `$`. Variant cuts are a flag on the same build. Driver code: `/motion-showreel` §7.

### Build rules

- **Ambient background** on `data-track-index="0"` for the full composition duration.
- **Kinetic-type openers:** per-word stagger 0.06–0.10s.
- **Captions** as body-level siblings of the root composition in `index.html`, each with `data-track-index ≥ 20`. Never inside scene timelines (MOTION_PHILOSOPHY §3.13).
- **Catalog blocks** installed via `npx hyperframes add <name>`. Immediately **scope the block's CSS** to `[data-composition-id="..."]` — catalog blocks ship with `html, body { ... }` rules that bleed into the parent document when loaded as sub-compositions.
- **Vertical + face-cam:** wrap native 1920×1080 face in a transform (`translate` + `scale`) for bottom-half or full-screen mode. (If you end up here instead of `/short-form-edit`, strongly consider the handoff.)
- **Apply ONLY what the user supplied.** Their palette, their fonts, their logo. Don't inject anything else. If they chose MOTION_PHILOSOPHY defaults, pull the palette + font pair from `references/style-intake.md`.
- **Product UI is drawn, never captured.** No screenshots, lifted live pages, tilted planes or blur. Redraw each view as a flat card at video size from the app's real text, type at least 22 px at 1080p, one card per voice beat, push in on the element the voice names. Swap real names at the source. Christian on a lifted page: "it still looks like it's being screenshotted... low taste."
- **Scene boundaries hand off cleanly.** Keep the outgoing scene drawn and opaque under the incoming wipe until it ends, then clear it fully. Give each scene its own stacking context (`isolation: isolate`) so a child's z-index can't escape. Colour persistent overlays by what is actually behind each part of them mid-transition. Two black scenes crossfading flashed grey; a wipe with no overlap rose over an empty frame.
- **Voice and timing.** The voice is the clock. Voice each line as its own clip and write word times from the TTS alignment into one timing file; per-line clips placed words to about 0.1 s, Whisper on the joined file was off by over a second. Scenes, sound effects and mix all look times up by phrase through one shared function, never a hard-coded second or beat number, so a reworded line moves its pictures and sounds with it.
  - Anything the voice lists gets its own word cue. Key each step of a progress animation to the word that names it and move linearly between those knots; one playhead stretched over the whole line ran 3 s ahead of "Research" once the line was re-voiced.
  - A marker that announces a switch (a logo drop, a stamp) arrives on the word that names it. Dropped into the pause a second early, reviewers on both cuts read it as giving the switch away.
  - Narration variants share the timing file and the mix. Build and render one variant through the whole chain before starting the next.
  - Rebuild normalized narration, timing and mix in the same run as the voice, with no manual step between them. Key clip caches by a content hash of voice, model, settings, seed and text, never by position. A skipped loudness step once left the mix reading old narration, and the second half played 2.6 s early.
- **A state switch rewrites every label on the element.** When a card flips from problem to solved, its captions change in the same frame as its colours. A solved card still read "Sellers come from referrals" under the violet state.
- **Scripted edits put comments on their own line.** A find-and-replace that inserts code before a trailing `//` comment turns the rest of the line into comment, and the page still loads. It happened three times on one project.
- **Cut to the music grid.** Snap scene edges and hits to the bed's measured beat grid and loop it on bar lines. Reused beat-cut material (a logo open) keeps its native beat period; change length with whole beats or pauses, never by scaling time, which drifted off the grid and Christian heard it. No cue starts while the previous beat is still on screen. Start a licensed track at the section the person chose.

### Determinism

No `Math.random()`, no `Date.now()`, no render-time `fetch()`. Use seeded PRNGs or harmonic-sin hashes (MOTION_PHILOSOPHY §3.10).

Per-element variation (shimmer, tint, jitter) hashes that element's own index. A phase linear in x and y drew diagonal bands across a dot map, and a hash shared by a block of dots tinted each block as one patch.

---

## Gate 7 · Lint → Studio preview (PREVIEW GATE 1 — MANDATORY)

1. `npx hyperframes lint` — fix all errors, triage warnings.
2. `npx hyperframes preview` in the background.
3. Wait for "Studio running" on `http://localhost:3002`.
4. Hand the user the URL **plus** individual composition URLs (`http://localhost:3002/?comp=<id>`). If the project has WebGL shader blocks, lead with the individual URLs — software WebGL fallback can stall the master composition.
5. **WAIT for explicit "looks good, render a draft"** before proceeding. Silence is not approval.

Hot reload is on — edits show up live.

---

## Gate 8 · Draft render → visual verification → MP4 preview → final

### Draft render

**Measure the mix first.** The mix script ends by printing integrated LUFS and true peak after AAC encode. Measure every generated audio file before use. Bed about 14 dB under the voice with sidechain ducking, effects about 13 dB under, `alimiter` with `level=false` (its makeup gain read -12.6 LUFS against a -14 target). A bed at -21 dB "disappeared on a laptop speaker" (Christian).

Debug a scene with single-frame snapshots, but render the full cut as soon as one exists; watching it is what catches timing.

```bash
npx hyperframes render --quality draft --output renders/<slug>-draft.mp4
```

### Visual verification (MANDATORY before delivery)

Lint passing ≠ design working. Extract frames and **view them**.

1. `mkdir -p renders/frames`
2. For every beat hero moment AND every transition:
   ```bash
   ffmpeg -y -ss <t> -i renders/<slug>-draft.mp4 -frames:v 1 -q:v 2 renders/frames/t<t>.png
   ```
3. **Call the `Read` tool on every PNG.** The Read tool loads the image into context — don't just list filenames.
4. Confirm per frame: no cropped faces, correct face-mode per scene, text readable and on-palette, no overflow, transitions land on intended words, no blank frames. Every frame must be true if paused: counters count up from about 80% and land on the spoken number on the word that says it, related counters share one clock, scramble effects resolve before any hold, and labels match the voice in name, figure and order. Blind readers caught a card at 5 deals while the voice said 7, after frame checks passed it.
5. Check the frames on both sides of every scene boundary as contiguous strips, then watch the encoded mp4 with sound. Frame sheets, lint and contrast checks are a floor: Christian caught a 12 px layout jump, narration 2.6 s early and a logo off the music grid by watching, after every sheet passed.
6. **Blind-read every full render** before anyone else sees it: run the `review-video` skill, which loops fresh Opus readers until a review comes back clean.
7. If anything's wrong: fix → re-render → re-verify. Never ship a broken draft.

### MP4 preview (PREVIEW GATE 2 — MANDATORY)

```bash
npx serve renders -p 8080 -n
```

Do NOT use Python's `http.server` — it doesn't support HTTP Range requests, so scrubbing breaks.

Hand the user `http://localhost:8080/<slug>-draft.mp4`. **WAIT for explicit sign-off** on playback and audio sync.

### Final render

Before it: set `FFMPEG_ENCODE_TIMEOUT_MS=3600000` for a high-quality render over about 1:40 (the default limit killed one twice near frame 2,600, the reason buried in the log). Ship a full-quality master plus a share copy encoded two-pass at a bitrate computed from the size cap and duration; CRF 22 came out at 98 MB against a 30 MB cap. Confirm every voice, music and effect licence covers publishing: free-plan TTS carries no commercial licence, and a free stock-music account could not download at all.

```bash
npx hyperframes render --quality standard --output renders/<slug>-final.mp4
```

Report the output path. Done.

Full preflight + pre-delivery checklist: `Read: references/build-checklist.md`

---

## Non-negotiables (load-bearing — do not soften)

- **DO NOT skip PREVIEW GATE 1 (Studio) or PREVIEW GATE 2 (rendered MP4).** Two gates per build, always.
- **DO NOT claim a render is done** until frames have been extracted AND Read via the Read tool.
- **DO NOT build anywhere but inside a dedicated project folder.** Never put `index.html` at the workspace root.
- **DO NOT ask the user for assets** before inventorying their workspace.
- **DO NOT skip the `tl.to({}, { duration: SLOT_DURATION }, 0)` anchor tween** at the end of every sub-composition timeline. MOTION_PHILOSOPHY Law 11.
- **DO NOT use `Math.random()` / `Date.now()`** inside render logic. Seeded hashes only.
- **DO NOT add `class="clip"` to `<video>` tags.** It breaks them.
- **DO NOT impose a brand on the user.** Ask first; fall back to MOTION_PHILOSOPHY defaults only when they explicitly decline.

---

## References

- `references/interview-questions.md` — full question bank by Gate
- `references/style-intake.md` — style interview + MOTION_PHILOSOPHY defaults
- `references/catalog-intent-map.md` — "user says X → install Y"
- `references/storyboard-template.md` — beat-by-beat template + worked example
- `references/composition-scaffold.md` — scoped-styles + IIFE GSAP boilerplate
- `references/build-checklist.md` — preflight + pre-delivery gates

External (workspace-level):
- `MOTION_PHILOSOPHY.md` — the one external reference this skill assumes exists. Aesthetic baseline. Fallback lives in `references/style-intake.md` if the file is missing.

## Related skills

- `/hyperframes` — framework rules, invoke at Gate 6
- `/hyperframes-cli` — init · lint · preview · render · transcribe · tts
- `/hyperframes-registry` — installing catalog blocks
- `/gsap` — GSAP animation reference
- `/short-form-edit` — hand off at Gate 5 for 9:16 talking-head format
- `/website-to-hyperframes` — hand off at Gate 1 if the starting input is a URL
