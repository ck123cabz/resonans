---
type: script
aliases: ["claude.md and agents.md template"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: claude.md and agents.md template
speaker: Nate Herk (Anthropic for the TypeScript-strict example; Gemini for the full template)
provenance: D
sources: [q01, q16, q39]
videos: [claude-code-source-code-just-leaked-8-things-you-must-do.md, 18-claude-code-token-hacks-in-18-minutes.md, 32-tricks-to-level-up-claude-code-in-16-mins.md, generate-content-for-9-socials-on-autopilot-with-claude-code.md, every-level-of-claude-explained-in-21-minutes.md, claude-code-for-non-coders-6-hour-course.md, build-sell-with-codex-5-hour-course.md, build-sell-with-claude-code-10-hour-course.md]
---

# claude.md and agents.md template

The root file Claude Code (claude.md) or Codex (agents.md) reads on every turn. Nate's lines about it run from 2026-03-12 to 2026-09-21. The parts below are his spoken rules; the one full template is Gemini's assembly and is marked so.

## What the file is: an onboarding document
`[J] · [D] · uploaded 2026-04-01 · claude-code-source-code-just-leaked-8-things-you-must-do.md · q01 · stable`

On 2026-04-01 he framed claude.md as the onboarding document an employee gets on day one. Gemini's labels "System Constitution" and "Master Router" are not his; only "onboarding document" is in the captions.

> if Claude Code is an employee then claw.md is their onboarding document It tells them "Here's how we do things Here's what matters Here's what we never do and here's how this project is structured." (claude-code-source-code-just-leaked-8-things-you-must-do.md)

## Line limit: 150, 200, or 150 to 200
`[R] · [D] · uploaded 2026-03-17; 2026-04-02; 2026-04-27; 2026-05-12 · generate-content-for-9-socials-on-autopilot-with-claude-code.md; 18-claude-code-token-hacks-in-18-minutes.md; 32-tricks-to-level-up-claude-code-in-16-mins.md; every-level-of-claude-explained-in-21-minutes.md · q01, q39 · version-bound`

He gave three numbers in two months. All three are his. The reason each time: the file loads on every message, so every line costs tokens on every turn.

- 2026-03-17: under 150 lines.
- 2026-04-02: under 200 lines.
- 2026-04-27: between 150 and 200 lines max.
- 2026-05-12: under about 200 lines, with details pushed to files referenced by `@filename`.

> I think best practice is to keep it under 150 lines Otherwise you're just going to fill up your context much quicker (generate-content-for-9-socials-on-autopilot-with-claude-code.md)

> I like to keep it between 150 and 200 lines max If it starts getting longer than that then it's time to trim down some things (32-tricks-to-level-up-claude-code-in-16-mins.md)

## The Applied Learning rule, verbatim
`[S] · [D] · uploaded 2026-04-02 · 18-claude-code-token-hacks-in-18-minutes.md · q01, q39 · stable`

A self-updating section. Claude appends a one-line bullet when something fails twice, when Nate re-explains, or when it finds a workaround. Pass 1 dropped the workaround clause; the caption has it. He warns in the same breath to check it often so it does not bloat.

> applied learning when something fails repeatedly when Nate has to reexplain or when a workaround is found for a platform tool or limitation add a oneline bullet here keep each bullet under 15 words no explanations (18-claude-code-token-hacks-in-18-minutes.md)

## The 95% confidence rule line
`[S] · [D] · uploaded 2026-04-02 · 18-claude-code-token-hacks-in-18-minutes.md · q01, q39 · stable`

He said on 2026-04-02 that this line goes into all his claude.md files when Claude builds for him. Sabrina's prompt version is in script-grill-me-and-95-confidence.md.

> do not make any changes until you have 95% confidence in what you need to build ask me follow-up questions until you reach that confidence level (18-claude-code-token-hacks-in-18-minutes.md)

The same video lists what the file should hold: tech stack, coding conventions, build commands, the 95% rule, and pointers to where more data lives.

> include things like your text stack your coding conventions your build commands the 95% confidence rule only the most important things and you need to treat this like an index (18-claude-code-token-hacks-in-18-minutes.md)

## Role line: the executive assistant
`[S] · [D] · uploaded 2026-07-11 · claude-code-for-non-coders-6-hour-course.md · q01 · stable`

His pattern is a role plus one sentence of goal. Gemini's version ending "ship faster" merged this line with another template; the caption ends differently.

> you are Nate Herk's executive assistant your job is to help him spend less time on operations people management and admin so he can focus on learning AI tools and making YouTube videos (claude-code-for-non-coders-6-hour-course.md)

## Style rules: bullets, no m dashes, Oxford comma
`[S] · [D] · uploaded 2026-09-21 · build-sell-with-codex-5-hour-course.md · q01, q16 · stable`

In the Codex course (2026-09-21) he read his agents.md aloud: a role line, a few core operating rules, then a routing map that takes up most of the file.

> I use bullet points and don't use m dashes and you know use the Oxford comma but then I go into a routing map and that's the majority of my agents.mmd (build-sell-with-codex-5-hour-course.md)

"Use TypeScript strict mode" is a different source. On 2026-04-01 he read it as the kind of short, operational line the best users write, alongside tests-next-to-source, migrations before schema changes, and "use PNPM not npm". Treat it as Anthropic-leak example material, not his personal rule.

> Things like "We use TypeScript strict mode." Always Tests go in test folders next to the source file Never modify the database schema without running migrations Use PNPM not npm (claude-code-source-code-just-leaked-8-things-you-must-do.md)

## The routing map
`[S] · [D] · uploaded 2026-07-11 · claude-code-for-non-coders-6-hour-course.md · q01 · stable`

After the role line he lists where things live: business, team, strategy, corporate structure and tax, voice and style, course knowledge, projects. The specific line Gemini quotes ("If you need personal context read `context/MI.md`; if you need corporate structure look in `wiki/entities/`") is in no caption. It was probably on screen, so it stays [M].

> i've then given it a routing map so this is where things live if you want to find things about you know his business his team his OTAAS his strategy go here here's the path (claude-code-for-non-coders-6-hour-course.md)

## PNPM example: auto memory vs claude.md
`[J] · [D] · uploaded 2026-03-12 · build-sell-with-claude-code-10-hour-course.md · q01 · version-bound`

He uses "PNPM not npm" only as a generic example. In the 10-hour course (2026-03-12) it shows auto memory: Claude saves a stated preference to the global `~/.claude` folder, separate from the project claude.md.

> if you tell Claude always use you know PNPM not npm claude will save that to a global claude folder (build-sell-with-claude-code-10-hour-course.md)

## Mirroring claude.md into agents.md
`[S] · [D] · uploaded 2026-09-21 · build-sell-with-codex-5-hour-course.md · q16 · stable`

Codex reads agents.md. His instruction on 2026-09-21: copy claude.md, rename it agents.md. His own two files hold the same content. The prompt form in q16 ("Analyze this project and make it Codex-ready by mirroring claude.md into agents.md") is Gemini's wording and stays [M].

> literally what I would do is I would just copy your claw.md and then just name it agents.mmd it's the exact same thing (build-sell-with-codex-5-hour-course.md)

## What to keep out of the file
`[R] · [M] · uploaded 2026-09-21 · build-sell-with-codex-5-hour-course.md · q16 · stable`

[M] Gemini's version only; no caption carries this list. q16 says to keep out raw transcripts, long SOPs and full API docs, and to route to them instead. That matches his spoken rule from 2026-05-12 to push details into referenced files, which is [D] above.

## Full template, Gemini's assembly
`[S] · [M] · uploaded n/a · no transcript · q39 · version-bound`

[M] Gemini's version only; no caption carries this text. Gemini built it from several videos. Its pieces that carry a caption quote are above; the two example Applied Learning bullets and the "lead AI engineer" role line have none. Use it as a skeleton.

```markdown
# [Project Name] Constitution & Operating Context

## Primary Role & Goal
You are Nate's lead AI engineer for [Project Name]. Your goal is to help build, test, and maintain [Tech Stack/Application].

## Core Operating Rules
- 95% Confidence Rule: Do NOT make any code edits or execute multi-file changes until you reach 95% confidence in your approach. Ask follow-up questions until you hit that confidence level.
- Execution Discipline: Always use plan mode (`/plan` or `Shift+Tab`) before executing multi-step tasks.
- Token Efficiency: Use subagents (on lightweight/Haiku models) for any multi-file codebase research or file exploration. Only return summarized insights back to the main thread.
- Formatting: Direct and concise. No conversational filler, no pleasantries, no m-dashes, use Oxford commas.

## Self-Learning / Applied Learning Loop
Applied learning: When a tool fails repeatedly, when Nate re-explains a requirement, or when a platform limitation is found, add a 1-line bullet below. Keep each bullet under 15 words, no explanations:
- Always check if .env variables exist before initializing external API client instances.
- Never modify database schemas without generating a SQL migration script first.

## Directory & Context Routing Map
- Business Context: Refer to `./context/business.md`
- Brand Style Guide: Refer to `./context/style.md`
- Skill Recipes: Refer to `./.claude/skills/`
```
