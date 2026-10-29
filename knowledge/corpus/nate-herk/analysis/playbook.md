---
type: corpus
aliases: ["Playbook: Nate Herk's AI video editing, ranked for the tournament"]
corpus: nate-herk
layer: analysis
tags: [machine]
source: first-order transcripts + hyperframes-student-kit files
created: 2026-10-01
---

# Playbook: Nate Herk's AI video editing, ranked for the tournament

Christian is making sponsor-pitch and promo videos for the Dumaguete tournament on
December 5-6, with no Kie.ai, Higgsfield or Wavespeed credits. Practices are ranked by
how much they help him with that, using his own footage, photos and screenshots.

**Sources.** V1 is "Opus 5.5 Just Changed Video Editing Forever", posted 9/25
(`7jHXoPGnA4c`). V2 is "Claude Video Editing Just Became Unrecognizable", posted 4/23
(`Aw3BkmhYu4I`). KIT is `nateherkai/hyperframes-student-kit`, installed at
`content-studio/` on 10/1. Every claim was checked against the raw transcripts in
`.raw/video/`, which have no timestamps, so each row cites a section of the video.
The NotebookLM pass did not run on 10/1 because the nlm sign-in had expired.

**Cost key.** FREE means local tools and his own footage. PAID means a generation
credit as he wrote it. SWAP means paid as he wrote it, but it works free once real
assets replace the generated ones.

## Ranked practices

| # | Practice | Source | Cost |
|---|---|---|---|
| 1 | Transcribe first, with a timestamp on every word, before any cut or graphic | V1 five steps; V2 transcript JSON | FREE: `npx hyperframes transcribe video.mp4 --model medium.en` runs local Whisper. ElevenLabs is his paid default |
| 2 | Anchor every beat to a spoken word, then review the plan in plan mode before any HTML gets built | V2 plan-mode section | FREE |
| 3 | Verification loop: the agent screenshots its own render, fixes it, and hands over version five or six | V1 step 5; V2 "verifying screenshots" | FREE |
| 4 | Event sizzle reel from a folder of raw event footage: "tell a story out of this" | V1 AIS Live section | FREE when the footage is real |
| 5 | Turn a reference video he likes into a skill, then update the skill after every run | V1 YouTube showreel + step 4 | FREE: KIT `analyze-reference.mjs` runs local |
| 6 | Say the feeling, not only the specs: "high energy, fast-paced, engaging, sync the music to the beats" | V1 Lululemon section | FREE |
| 7 | Cut silences and mistakes first, with each cut proposed for approval | V2 trim section; KIT `cut-silences`, `cut-mistakes` | FREE |
| 8 | Showreel grammar: one motif, 6-7 labelled chapters, cuts on a 120-130 BPM grid, logo lockup at the end | KIT `motion-showreel` | SWAP: the Suno music and Kling hero shot are paid; use a licensed track |
| 9 | Short form: the first three seconds are their own edit. Build three openings and keep the one that works muted | KIT `short-form-edit` | FREE |
| 10 | Readability: put a glass card or dark overlay behind any text and keep it off the speaker's face | V1 intro prompt; V2 revision | FREE |
| 11 | Finished videos are training data: after five of one type, write a design file for that type | V2 "all of these videos are training data" | FREE |
| 12 | Brand test: name the brand and require that the result reads as "unmistakable" | V1 YouTube showreel prompt; KIT brand test | FREE with logos he has the right to use |
| 13 | Real assets before generated ones: "use real assets and logos from our products when possible" | V1 AIS showreel prompt | FREE as written |
| 14 | Fix timing by hand in the HyperFrames Studio timeline; Claude Code reads the change back from the code | V2 timeline-editor section | FREE |
| 15 | Be specific up front, because one guided edit cost him about 238,000 tokens | V2 closing section | FREE (plan usage only) |
| 16 | Keep API keys in `.env` and never paste one into the chat | V2 ElevenLabs section | FREE |
| 17 | Run the model at high effort | V1 short-form section | FREE |

## Notes on the top ten

**1. Transcribe.** In V2 the word list said "you" starts at 11.199 seconds, so a graphic
can land on that exact frame. KIT needs `{text, start, end}` per word in seconds.
"Paragraphs, SRT subtitles, and segment-only transcripts do not supply the required word
timing" (`docs/TOOLS-AND-API-KEYS.md`). Its own helper only calls ElevenLabs, so tell
the agent to use local Whisper and normalize the output.

**2. Plan the beats.** In V2 the plan came back as four beats (0-5s, 5-12s, 12-20s, and
on), each with its trigger word. He read beat A, then clicked revise to add a fifth beat:
the thanks-for-watching crop in the last 5 seconds. KIT `hyperframes-video-beats` starts a beat 0.2-0.6 seconds
before its anchor word, and in a long video allows at most 20-30 seconds early on, or
30-45 seconds mid-video, without a visual beat.

**3. Verify.** In V1 he called this "probably the most important one". In V2 he said
that without screenshots the agent "will just come back and say hey I've done this but
it doesn't look good at all". KIT gates: `npx hyperframes lint`, Studio preview, a
draft render, then 10-frame strips across every transition with ffmpeg. The
`video-storytelling` skill says a zoom freeze passed every automated gate, and the
client caught it in one viewing.

**4. Event sizzle reel.** He gave Claude Code a 105 GB folder of AIS Live recordings.
The result took one prompt, one round of notes and one fix, so he called it v2.1. It
pulled crowd quotes ("it was electric", "I had goosebumps") out of the call transcripts
and ended on the event logo with "your seat is in the middle". He listed what went
wrong himself: "awkward cut of the speech". This is the closest match to a
December 5-6 recap or a sponsor reel built from last season's footage.

**5. Reference into skill.** He downloaded a reel Ken posted on X and gave it to Claude
Code. He asked why it was so good, then said "turn that into a skill". The result was
`motion-showreel`. After each run he tells it "in this version I really liked this and I
really didn't like this" and has the skill updated. "If you ever find yourself repeating something just throw it in the
skill."

**6. Tone.** In V1 he said "sometimes you don't always know exactly what you want but
you know the emotions you want the video to create inside of you". For Lululemon he
gave only the vibe. KIT `short-form-edit` writes the hook, open loop, escalation,
evidence, payoff and call to action into `DESIGN.md` before any HTML.

**7. Cuts.** In V2 the cut took a 50-second take down to 32 seconds. The agent asked two
"taste calls" before cutting, and he answered "make this as punchy as possible". KIT
`cut-mistakes` proposes each cut with a reason and renders only the approved ones.

**8. Showreel grammar.** For a sponsor reel, the motif could be the ball, the court lines
or the paddle. At 129 BPM, 15 seconds is 32 beats: 4 for physics, 8 for type, three
4-beat chapters, a 4-beat flurry, then about 4 for the lockup. Nothing else in the
recipe needs paid generation. `music-grid.mjs`, `beatgrid.mjs`, `splice-music.mjs` and
`mix.mjs` all run on a track he supplies.

**9. First three seconds.** The gate in KIT: "In the first 3 seconds is someone convinced
they need to watch until the end?" Avoid a logo bumper or a flash that delays the
point. Check that the opening still reads with the sound off.

**10. Readability.** In V1 he said the card needs "some sort of liquid glass card behind
the element". In V2 the first render covered his face, and his fix was "scale this down
and then maybe crop off the right side a little bit".

## His prompts, verbatim (V1 and V2)

His words from the transcripts, lightly cut. Not linted.

- **V1 intro.** "edit this to be super engaging and clean with hyperframes … when I say powerful models like Fable 5.1 and GBD6 Astra I want you to have animations come in where I'm pointing … make sure there's some sort of liquid glass card behind the element … I want you to actually go off and get a B-roll screen recording and get a screenshot and pull in stuff because I want you to prove to the viewers"
- **V1 reference to skill.** "analyze this video which was created by Opus 5.5 and figure out why this is so good" → "Turn that into a skill." → "use that skill create me my own show reel about YouTube … Collect B-roll images any assets you need make sure the whole thing feels branded to YouTube typography design language colors branding … should be unmistakable in the show reel."
- **V1 AIS showreel, one shot.** "Make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are like it's your showreel for a resume go all out … Make it about our company AIS use real assets and logos from our products when possible you can also use kie.ai to generate any assets you need and use hyperframes or any other tools for motion design and music and sound effects" (PAID as written)
- **V1 AIS Live.** "look through all this and create me a sizzle reel tell a story out of this." (FREE)
- **V1 avocado, whiteboard.** "simple and clean whiteboard handdrawn style animation … as if you're trying to explain to a kid … some scenes should be a full screen whiteboard takeover and some scenes should just be the left half is the whiteboard and the right half is my face" (SWAP: he allowed kie.ai)
- **V1 avocado, course style.** "my camera will start off full screen and then I want it to be a rounded crop the background is going to be super simple super minimalistic … bullet points with important takeaways not too wordy and they should be big and then visual aids should just be AI generated images" (SWAP: use photos)
- **V1 avocado, short form.** "generate the assets you need have it be engaging have it be fast-paced easy to understand" (PAID as written)
- **V2 setup.** "look at these two GitHub repos and I want you to pull in the skills and pull in the important information that we need from these so that I could basically give you a raw video file and you would be able to edit it remove the filler words and then help me add motion graphics to it."
- **V2 trim.** "use the video use tool just to edit this video … remove any filler words or silences or retakes … your first task is just to edit out the mistakes and the filler words"
- **V2 closing direction.** "make sure that everything is syncing up to the exact second where it makes the most sense for that motion graphic or that text to pop in"
- **V2 end-card revision.** "in the last 5 seconds I want to transition i want to take the face cam and I want to vertical crop it with rounded edges and a drop shadow … on the left half of the screen I want there just to be text that says thanks for watching"

## Paid only, skip for now

- **Lululemon spec ad (V1).** The model videos were generated, so this needs credits.
- **YouTube showreel 3D play button (V1).** The images went to Kling to become video.
- **Course-style avocado visuals (V1).** He said "all of the images and videos in this
  video were AI generated". Swap in court photos and it is free.
- **KIT `kie.mjs`.** Each Suno track, Seedream still and Kling move costs a Kie.ai credit.
