---
type: build
aliases: ["Hermes personal assistant"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Hermes personal assistant
speaker: Nate Herk
provenance: D
sources: [q14, q16, q17, q33, q37, q38, q43]
videos: [hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md, set-up-a-personal-hermes-in-14-mins-no-vps-or-mac-mini.md, 100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md]
---

# Hermes personal assistant

Hermes Agent is an open-source, MIT-licensed assistant from Nous Research (captions: "Noose Research"). Nate set one up on a VPS, talked to it through Telegram, and taught it in "Hermes Agent: Zero to Personal AI Assistant (1 Hour Course)", uploaded 2026-05-10. A 14-minute setup without a VPS followed on 2026-08-27.

## Hermes: what it is and its 140,000 stars
`[T] · [D] · uploaded 2026-05-10 · hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md · q17, q38 · version-bound`

It runs on your own machine: a Mac Mini, a laptop, a VPS, a Docker container, even Android through Termux. It keeps memory, writes reusable skills, runs scheduled automations, searches past conversations and works through Telegram.

> it is an mit licensed like i said open source project right now it has 140,000 github stars and that is growing really fast (hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md)

## The 5 pillars of Hermes
`[F] · [D] · uploaded 2026-05-10 · hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md · q17, q37 · stable`

His teaching structure: memory, skills, soul, crons (things on a schedule), self-improving loop. He says his own Hermes agent helped him come up with it, then had Hermes draw the diagrams.

> i actually copied this exact five pillar structure which by the way my hermes agent helped me think of (hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md)

## Hermes pillar 1: memory in user.md and memory.md
`[B] · [D] · uploaded 2026-05-10 · hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md · q17 · stable`

Memory is the small, durable context carried across sessions. `user.md` holds who you are, your style, your likes and dislikes. `memory.md` holds the environment, projects and business context. Past sessions go into a SQLite database that Hermes can search. His beginner rule: save durable preferences and facts, never secrets or temporary task status.

> the first one is the user.md who you are your style your preferences and things that you don't like the second one is the memory md this is like the environment the projects you're working on (hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md)

## Hermes pillars 2 and 3: skills and soul
`[B] · [D] · uploaded 2026-05-10 · hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md · q17 · stable`

Skills install by command or by dropping a URL into chat. The soul file sets each agent's vibe, so six Hermes agents can each sound different. Gemini's claim that Hermes skills live in `.claude/skills/` was flagged doubtful in pass 1 and has no caption.

> pillar three is the soul now soulm basically shapes the assistant ... if you have six different hermes agents they all have basically a different vibe (hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md)

## Hermes pillar 4: the crons he runs
`[B] · [D] · uploaded 2026-05-10 · hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md · q17 · version-bound`

He listed his running crons: a daily AI news briefing posted to his Skool community, YouTube comment monitoring (an agent with his transcripts answers comments on his videos), Skool community engagement, morning business summaries, server checks. Gemini's 6:00 pm Fireflies ingest into `/meetings/` has no caption in the Hermes videos. The `--no-agent` flag for plain scripts is [M].

> a daily ai news briefing which is posted inside of my school community youtube comment monitoring so if you guys have noticed on my youtube videos lately i've had an ai agent that has access to the transcript (hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md)

## Hermes nightly GitHub backup
`[B] · [D] · uploaded 2026-05-10 · hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md · q17 · stable`

He calls the backup really important. Hermes creates a private repo and pushes updates every night, using a GitHub personal access token with read-write access to contents. He warns against pasting that token into chat. The exact 12:00 am time and the full restore-from-repo flow are Gemini's detail [M]; "every night" and the purpose are his.

> so it's really important that we're going to set up this automated backup it's completely free to set up go to github (hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md)

## Hermes on a Hostinger VPS
`[T] · [D] · uploaded 2026-05-10 · hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md · q17, q38 · version-bound`

Hostinger is his VPS provider for n8n, OpenClaw, Claude Code and Hermes. Hostinger offers a one-click Hermes deploy and daily auto-backups; code "Nate Herk" gives 10% off (an affiliate link). The KVM 2 at "six bucks a month, nine bucks" is from his Clawdbot video (2026-01-28). The 2026-08-27 video sets Hermes up with no VPS or Mac Mini.

> i'm going to be using hostinger for my hermes agent i have been using hostinger for hosting nadn and for openclaw and for cloud code (hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md)

## Hermes inference through a ChatGPT login
`[T] · [D] · uploaded 2026-08-27 · set-up-a-personal-hermes-in-14-mins-no-vps-or-mac-mini.md · q16, q17 · version-bound`

He signs Hermes into Codex with his ChatGPT account, so the ChatGPT subscription pays for inference instead of a per-token API bill.

> sign into your chatbt account copy in this code and then now your hermes agent will be powered by your chatbt subscription (set-up-a-personal-hermes-in-14-mins-no-vps-or-mac-mini.md)

## Anthropic's ban on consumer logins in third-party harnesses
`[R] · [D] · uploaded 2026-05-26 · 100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md · q16, q33 · version-bound`

This is why Hermes runs on a ChatGPT login and not a Claude one. Per his reading of the Agent SDK terms, a Claude subscription inside OpenClaw or Hermes is not allowed without Anthropic's approval. The OpenAI side and the Anthropic side do not conflict; the ban is Anthropic's.

> using your cloud subscription inside of a third party tool like openclaw or hermes isn't allowed unless anthropic specifically approves you (100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md)

## Hermes voice notes on Telegram
`[B] · [D] · uploaded 2026-05-10 · hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md · q17 · version-bound`

He asks by voice and Hermes answers with text plus a voice note; one reply ran 1 minute 16 seconds. Telegram's view is token-based, so auto-compaction runs as the context fills and slash commands are lost.

> you can see that it shot back an actual voice note as well as text (hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md)

## Hermes least privilege: one agent, one set of keys
`[J] · [D] · uploaded 2026-05-10 · hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md · q43 · stable`

Run separate agents for separate jobs and keep their keys apart. His example: a marketing Hermes has no need to read QuickBooks; a finance Hermes might.

> you can use the least privilege rule which is basically give each agent only the credentials and the tools needed for its job (hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md)

## Hermes versus Claude Code: desk versus always-on
`[J] · [D] · uploaded 2026-05-10 · hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md · q14 · version-bound`

Claude Code stays his daily driver. Hermes and OpenClaw are the always-on assistants he reaches from his phone.

> claude code is still my daily driver that's where i do 90% of my knowledge work throughout the day (hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md)

## OpenClaw to Hermes: the dates
`[J] · [D] · uploaded 2026-01-27 to 2026-09-28 · sources.tsv titles · q36 · version-bound`

Clawdbot videos 2026-01-27 to 2026-01-30; OpenClaw first named 2026-02-25; "Claude Code + Paperclip Just Destroyed OpenClaw" 2026-03-28; "I Gave OpenClaw $10,000 to Trade Stocks" 2026-04-09. Hermes is first named 2026-04-17, the course is 2026-05-10, the 14-minute setup 2026-08-27. OpenClaw and Hermes each appear in 33 captions. By 2026-09-28 he calls OpenClaw a past experiment ("i actually did this experiment before using open claw").
