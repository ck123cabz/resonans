---
type: build
aliases: ["Grok Bot org chart"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Grok Bot org chart
speaker: Nate Herk
provenance: D
sources: [q14, q17, q21, q38]
videos: [grok-bot-is-for-real-what-you-need-to-know.md, a-week-of-grok-bot-lessons-in-10-mins.md, build-sell-grok-bots-2-hour-course.md, every-grok-bot-concept-explained-for-normal-people.md, grok-bot-manages-my-inbox-and-has-its-own.md]
---

# Grok Bot org chart

Grok Bot is a multi-bot assistant app Nate covered in five videos from 2026-08-12 to 2026-09-16, peaking in "Build & Sell Grok Bots (2 Hour Course)" on 2026-08-31. He runs it as an org chart: one pinned chief of staff he talks to, specialists under it. Who makes the product is unsettled: the captions show both Cursor branding (the Ultra plan, "@cursor" in Slack) and xAI branding (Super Grok). Captions spell it "Grockbot".

## Klouse, the chief of staff: system description
`[S] · [D] · uploaded 2026-08-31; 2026-08-19 · build-sell-grok-bots-2-hour-course.md; a-week-of-grok-bot-lessons-in-10-mins.md · q17 · stable`

Each bot has a role and a description; the description is what tells other bots what it does. Klouse's is below, near-verbatim. Gemini's q17 version drops the last clause ("Only do the work yourself if no specialist fits") and the return step. The name is spelled "Klouse" in 59 caption hits, also "klaus" and "claus"; the real spelling is uncertain. Klouse started as his Clawdbot executive assistant in January 2026.

> for klouse this description is you are nate's chief of staff klouse is the only bot that nate talks to before doing any task check whether another grockbot owns it and delegate first only do the work yourself if no specialist fits (build-sell-grok-bots-2-hour-course.md)

## Grok Bot specialists and bot-to-bot messaging
`[B] · [D] · uploaded 2026-08-31 · build-sell-grok-bots-2-hour-course.md · q17 · stable`

Klouse can message every other bot, and they can message each other. The roster read on camera: Dan, Becky, Chandler, Dev, Eyes, Views, Minor, Motion, Money, Dash, Cal, Coffee. When he wanted email help, he told Klouse to spin up a separate email agent instead of doing it itself. Gemini's job labels (Motion for animation, Eyes for research, Coffee for daily planning, Money for Slack and media deals, Views for content strategy, Studio for image and video) are [M]; only the names are in this caption.

> klouse ... is able to talk to everyone else he's able to delegate work around to all of these bots (build-sell-grok-bots-2-hour-course.md)

## Grok Bot memory: global versus per-bot
`[B] · [D] · uploaded 2026-09-01 · every-grok-bot-concept-explained-for-normal-people.md; build-sell-grok-bots-2-hour-course.md · q17 · version-bound`

Every bot reads a shared global memory; each also keeps its own. He demos this by asking a bot what it knows about him that others do not. A copied template carries the bot's saved memories with it. Gemini's contents for global memory (company snapshot, CEO identity, quarterly goals, brand guidelines, Composio connections) and the auto-compaction claim are [M].

> the difference between all of your grockbot like global memory and individual bot memory (every-grok-bot-concept-explained-for-normal-people.md)

## Grok Bot routines: Inbox Watch every 30 minutes
`[B] · [D] · uploaded 2026-08-31 · build-sell-grok-bots-2-hour-course.md · q17 · version-bound`

Routines are written as step-by-step instructions with a schedule. His inbox routine runs every 30 minutes, midnight to 11:00 pm, and does nothing when no email fits the category. Routines run in the cloud with devices off [M]. The Friday 5:00 pm weekly report into Google Sheets and event triggers from Slack, Git commits or Teams are [M].

> it says when to run every 30 minutes so every single 30 minutes every day of the month between 12 a.m and 11 p.m (build-sell-grok-bots-2-hour-course.md)

## Teach a Task: record the browser, get a skill
`[T] · [D] · uploaded 2026-08-31; 2026-08-19 · build-sell-grok-bots-2-hour-course.md; a-week-of-grok-bot-lessons-in-10-mins.md · q17 · version-bound`

Bots share one computer with a browser. "Teach a task" records him doing something in that browser, and the bot turns the recording into a repeatable skill.

> there is this function in here called teach a task which basically means that i could record myself in this browser doing something (build-sell-grok-bots-2-hour-course.md)

## Share as Template: package a bot as a link
`[B] · [D] · uploaded 2026-08-31 · build-sell-grok-bots-2-hour-course.md · q17 · version-bound`

Every bot's settings carry a "share as template" button. It prompts the bot to make a shareable copy of itself, including its memories, skills, routines and plugins. Stripping credentials and private data is Gemini's description [M].

> there's a little button at the bottom that says share as template and when you click on that it basically just shoots off this prompt to your bot that says create a template of yourself (build-sell-grok-bots-2-hour-course.md)

## Grok Bot inbox with AgentMail
`[B] · [D] · uploaded 2026-09-16 · grok-bot-manages-my-inbox-and-has-its-own.md · q17 · version-bound`

He gave a bot its own email address through AgentMail, a native connector in the Grok Bot marketplace, free to start. AgentMail gives an agent an inbox; it is not a cold-email tool, whatever Gemini's q26 says.

> we use a service called agent mail and it's completely free to start (grok-bot-manages-my-inbox-and-has-its-own.md)

## Selling Grok Bot setup: a $5,000 project
`[R] · [D][G] · uploaded 2026-08-31 · build-sell-grok-bots-2-hour-course.md · q17, q21 · stable`

He places Grok Bot setup at the education and consulting end of his AI Service Ladder, or as a $5,000 project to set up a team. To pitch it, you must be your own proof first. Gemini's "foot in the door for $15k+ retainers" is in no caption.

> maybe you're able to package this into some sort of project like $5,000 to get you and your team set up with grockbot everyone personally (build-sell-grok-bots-2-hour-course.md)

## Grok Bot access price: Cursor Ultra, then $30
`[T] · [D] · uploaded 2026-08-12; 2026-08-31 · grok-bot-is-for-real-what-you-need-to-know.md; build-sell-grok-bots-2-hour-course.md · q17, q38 · version-bound`

On 2026-08-12 access required the Cursor Ultra plan. By 2026-08-31 it was $30 a month through Super Grok, down from $200 at launch. "Cursor Ultra at about $30" in Gemini's q17 merges two plans from two dates.

> in order to try this out you are going to have to be on the cursor ultra plan (grok-bot-is-for-real-what-you-need-to-know.md)

> you can get access to grockbot for just 30 bucks a month so it used to be when it first came out it was just the 200 bucks a month (build-sell-grok-bots-2-hour-course.md)

## Warning: the 8-metric scorecard and $80 day are Clawdbot's
`[R] · [D] · uploaded 2026-01-28 · 100-hours-testing-clawdbot-vs-claude-code-honest-results.md · q14 · version-bound`

Gemini's q14 labels a "Grok Bot vs Claude Code" scorecard. The scores and the $80, 8M-token day belong to Clawdbot (later OpenClaw) versus Claude Code, seven months before Grok Bot appears. Security: Claude Code 7, Clawdbot 3. See tool-harness-head-to-heads.md.

> for claude code i'm going to give it a 7 out of 10 and for clawbot we're giving it a 3 out of 10 (100-hours-testing-clawdbot-vs-claude-code-honest-results.md)
