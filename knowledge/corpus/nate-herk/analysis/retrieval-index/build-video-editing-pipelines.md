---
type: build
aliases: ["AI video editing pipelines"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: AI video editing pipelines
speaker: Nate Herk
provenance: D
sources: [q16, q30, q38]
videos: [claude-heygen-just-changed-content-creation-forever.md, claude-just-destroyed-every-video-editing-tool.md, claude-video-editing-just-became-unrecognizable.md, seedance-2-0-claude-code-creates-10k-websites-in-minutes.md, higgsfield-just-turned-claude-into-a-creative-agency.md, this-one-gpt-6-astra-skill-replaces-your-higgsfield-subscription.md, gpt-6-astra-finally-solves-ai-video-editing-full-guide.md, opus-5-5-just-changed-video-editing-forever-free-skills.md]
---

# AI video editing pipelines

Nate's video builds run a coding harness (Claude Code, later Codex with GPT-6 Astra) over video tools. Four pipelines: Hyperframes motion graphics, HeyGen avatar clones, Seedance loops for scroll-driven sites, and Higgsfield multi-model ad generation. The videos run 2026-04-11 to 2026-09-25. Model names below are the titles' spellings: Seedance 2.5 and Kling 3.0, which captions write "Cedance"/"Cance" and "Cling".

## Remotion to Hyperframes switch (2026-04-15 to 2026-04-18)
`[J] · [D] · uploaded 2026-04-15; 2026-04-18 · claude-heygen-just-changed-content-creation-forever.md; claude-just-destroyed-every-video-editing-tool.md · q30 · version-bound`

On 2026-04-15 his HeyGen pipeline used Remotion, a React video library, for motion graphics. Three days later he introduced Hyperframes as the stronger option. Hyperframes shows up in 19 captions from 2026-04-18 to 2026-09-25; Remotion's last caption mention (2026-05-05) is a dictation slip. Gemini's reason, that models iterate and visually check HTML/CSS faster than React, is [M]; the caption gives only "more setup but way more powerful".

> we have remotion which is what we're using to edit everything together and give us professional looking motion graphics (claude-heygen-just-changed-content-creation-forever.md)

> hyperframes which is kind of like a better version of remotion if you guys have seen that it's a little bit more setup but it's way more powerful (claude-just-destroyed-every-video-editing-tool.md)

## Hyperframes pipeline: transcribe, cut, plan beats, animate, check
`[B] · [D] · uploaded 2026-04-23; 2026-09-08; 2026-09-25 · claude-video-editing-just-became-unrecognizable.md; gpt-6-astra-finally-solves-ai-video-editing-full-guide.md; opus-5-5-just-changed-video-editing-forever-free-skills.md · q16, q30 · version-bound`

The agent writes HTML and animates it, renders to video, and screenshots scenes to check its own work. The steps Gemini lists (word-level transcript from ElevenLabs or Whisper, cut silences and fillers, plan scene beats, write timed HTML/CSS, screenshot QA loop, render through Puppeteer and FFmpeg) match what he shows; the captions confirm transcription, cutting, layout switching and screenshot checks. He prompts layout rules: full-screen facecam when nothing is on screen, a tutorial layout when he demos.

> i'm basically telling it to take screenshots of what's going on in the scene to make sure that it looks good (claude-video-editing-just-became-unrecognizable.md)

> it transcribes the audio and then it can cut o[ut] (gpt-6-astra-finally-solves-ai-video-editing-full-guide.md)

Skills named: `motion-reel`, `hyperframes-student-kit`, `motion-show-reel` [M]. By 2026-09-08 Codex with GPT-6 Astra drives the edits; on 2026-09-25 Opus 5.5 does, and he praises its taste.

## Hyperframes cost in tokens
`[R] · [D] · uploaded 2026-04-23 · claude-video-editing-just-became-unrecognizable.md · q30 · version-bound`

One edit in April took about 238,000 tokens. His advice is more specific planning to cut that. Gemini's range of 120k to 400k tokens, $7 to $18 via API, or 10% to 40% of a day on the $200 Max plan, is [M]. Local rendering is free.

> how many tokens did this cost this took us about 238,000 tokens so not too bad but not great either (claude-video-editing-just-became-unrecognizable.md)

## HeyGen avatar pipeline: chunked voice, Playwright workaround
`[B] · [D] · uploaded 2026-04-15 · claude-heygen-just-changed-content-creation-forever.md · q30 · version-bound`

Three pieces: HeyGen for the avatar clone, ElevenLabs for the voice clone, Remotion (later Hyperframes) for motion graphics. He chunks scripts for two reasons. HeyGen capped Avatar 5 generations at 3 minutes. ElevenLabs degrades past about a minute of audio, so 45 seconds to a minute is his sweet spot. Avatar 5 was not on the API at the time, so the script generated in Avatar 4 and a Playwright script opened his HeyGen dashboard and switched each clip.

> once you push past about a minute of audio it starts to degrade and it starts to sound less and less like you (claude-heygen-just-changed-content-creation-forever.md)

> i have the script generating all of these videos in avatar 4 and then i have a playwright script that opens up my hen dashboard and just changes it (claude-heygen-just-changed-content-creation-forever.md)

## HeyGen cost: about $4 a minute
`[R] · [D] · uploaded 2026-04-15 · claude-heygen-just-changed-content-creation-forever.md · q30, q38 · version-bound`

Each 1-minute clip cost about $4 on the API, so a 10-minute video runs almost $50. He weighs that against a couple of hours of his time. The Creator plan at about $30 a month and ElevenLabs Creator at about $22 are [M]; so is the "$300+ human editor" comparison. The 2–5 minutes of training footage for Avatar V5 is [M].

> each of these 1 minute clips are taking about four bucks so if you do a 10-minute video that's probably going to run you almost $50 (claude-heygen-just-changed-content-creation-forever.md)

## Seedance loop pipeline for scroll-driven websites
`[B] · [D] · uploaded 2026-04-11 · seedance-2-0-claude-code-creates-10k-websites-in-minutes.md · q30 · version-bound`

A start frame (Nano Banana 2 or GPT Image 2) goes into Seedance 2.0 with a loop prompt written by a skill. FFmpeg extracts the frames from the clip, and Claude Code binds each frame to a scroll position so scrolling plays the video. He generated at 720p, 25 credits a second; one run cost 615 credits through Key AI (probably kie.ai). The dollar range per clip, the 100–120 WebP frames and the 15-second / 30–40 MB web limit are [M].

> this is costing me 615 credits and if i go up here i'm generating this in 720p which is going to be 25 credits per second (seedance-2-0-claude-code-creates-10k-websites-in-minutes.md)

> it just basically extracted all of the frames from the video and then put them associated with a scroll pattern or a scroll position (seedance-2-0-claude-code-creates-10k-websites-in-minutes.md)

## Seedance loop prompt
`[S] · [M] · uploaded 2026-04-11 · no transcript carries this text · q39 · version-bound`

[M] Gemini's version only; no caption carries this text.

```
A seamless 10-second video loop starting from [reference image filename]. The camera
smoothly [zooms/pans] through [scene description], displaying large, bold white text at
second 3 that reads '[Headline Text]'. The motion transitions smoothly and fades back into
the exact original blueprint frame at second 10 with zero jumps, no shadows, no
reflections, and no hands.
```

## Higgsfield multi-model generation from Claude
`[B] · [D] · uploaded 2026-05-05 · higgsfield-just-turned-claude-into-a-creative-agency.md · q30 · version-bound`

Claude talks to Higgsfield through its MCP, researches products, then generates a product photo, an Instagram ad and a UGC video for each. Gemini adds brand-asset intake, Marketing Studio templates, a `generations.xlsx` cost log, the "76+ models" count and the `hypermotion` skill; those are [M].

> for each of them i want you to generate assets so a product photo an instagram ad and a ugc video and i told it to use the higsfield mcp for all of these generations (higgsfield-just-turned-claude-into-a-creative-agency.md)

## Per-clip costs: Seedance 2.5 $3.23, and the garbled ones
`[R] · [D] · uploaded 2026-09-18 · this-one-gpt-6-astra-skill-replaces-your-higgsfield-subscription.md · q30, q38 · version-bound`

Seedance 2.5 cost $3.23 a clip. It used to need a $60-a-month Higgsfield plan; Higgsfield's new API made it pay per use, and one batch cost $7.40 total. Kling 3.0 "$0.60", MiniMax "$1.10" and a $17.55 sizzle reel are caption garble ("60s", "a$110", "1755 based on my credits") and stay unresolved. "Seedance costs 5x Kling" is pass-1 arithmetic, never spoken.

> so this was cedance 2.5 and it was $3.23 here is cling 3.0 (this-one-gpt-6-astra-skill-replaces-your-higgsfield-subscription.md)

> if you wanted to use cedance 2.5 you had to be on a 60 bucks a month plan and you still had a limited number of credits (this-one-gpt-6-astra-skill-replaces-your-higgsfield-subscription.md)
