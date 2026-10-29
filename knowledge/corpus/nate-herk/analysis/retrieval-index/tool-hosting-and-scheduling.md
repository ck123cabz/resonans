---
type: tool
aliases: ["Hosting and scheduling"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Hosting and scheduling
speaker: Nate Herk
provenance: D
sources: [q11, q12, q38]
videos: [how-to-build-24-7-claude-agents-easy.md, how-to-deploy-your-claude-automations-3-methods.md, the-easiest-way-to-host-your-claude-code-agents.md, how-to-build-gpt-6-astra-automations-that-don-t-eat-your-usage-limit.md, claude-code-for-non-coders-6-hour-course.md, 100-hours-testing-clawdbot-vs-claude-code-honest-results.md, set-up-a-personal-hermes-in-14-mins-no-vps-or-mac-mini.md, build-sell-with-claude-code-10-hour-course.md, hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md]
---

# Hosting and scheduling

Where Nate Herk runs agents once they leave the terminal, and what each option costs. His 2026-05-15 video sorts them into three methods: local routines on your machine, Anthropic's cloud routines, and your own code on Modal or Trigger.dev. A VPS covers always-on assistants.

## The three deploy methods
`[J] · [D] · uploaded 2026-05-15 · how-to-deploy-your-claude-automations-3-methods.md · q11 · version-bound`

Method one is local: the Claude desktop app's routines, or crons in a session. Method two is Anthropic's cloud routines, which need nothing on your side. Method three:

> moving on to method three we have deploying to something like modal or trigger.dev which is kind of it's not your own cloud it's either modal or trigger.devscloud but it's not enthropic (how-to-deploy-your-claude-automations-3-methods.md)

His pick rule: cloud routines when the job needs the full agent loop with self-healing; Modal or Trigger.dev when the job is a fixed script that does not need an LLM on every run.

## Local routines in the desktop app
`[T] · [D] · uploaded 2026-05-15; 2026-03-12 · how-to-deploy-your-claude-automations-3-methods.md; build-sell-with-claude-code-10-hour-course.md · q11 · version-bound`

The desktop app lists routines as local or remote. Local ones start a fresh session on your machine, read local files, and need the computer on. If the machine was off, they catch up when it comes back. His example is the "morning coffee" skill:

> but now this can actually just run automatically at 6:00 a.m every morning (build-sell-with-claude-code-10-hour-course.md)

Included in Pro and Max, per q11 [M].

## Cloud routines: 5, 15 or 25 runs a day
`[T] · [D] · uploaded 2026-04-14 · how-to-build-24-7-claude-agents-easy.md · q11, q12 · version-bound`

Anthropic clones your private GitHub repo into a sandbox, runs `claude.md`, skills and tools, pushes changes back, and destroys the container. Triggers: schedule, API call, GitHub event. Secrets go in the cloud environment settings, never in the repo. He read the limits off the docs on camera:

> on pro you can have five runs a day on max you can have 15 runs a day and on team and enterprise you can have 25 routines a day (how-to-build-24-7-claude-agents-easy.md)

> minimum scheduled interval which is one hour ... every one of these routines in the cloud runs on four vcpus 16 gigs of ram and 30 gigs of disk space (how-to-build-24-7-claude-agents-easy.md)

He had guessed "3 or 5" for Pro before reading the page. Pro is 5. q12's "3 to 5" is the guess.

## Trigger.dev: TypeScript, free to start, start times can drift
`[T] · [D] · uploaded 2026-02-20; 2026-09-16 · the-easiest-way-to-host-your-claude-code-agents.md; how-to-build-gpt-6-astra-automations-that-don-t-eat-your-usage-limit.md · q11, q12 · version-bound`

Claude Code or Codex writes TypeScript under `src/trigger/`, pushes to GitHub, and Trigger.dev deploys it with queues, retries, logs and a dashboard. It can also run the Claude Agent SDK or Codex SDK in the cloud. His own schedules ran often:

> these two run every 2 minutes (the-easiest-way-to-host-your-claude-code-agents.md)

On the free plan a scheduled run can start late:

> delay a 6 a.m start by up to an hour ... as far as getting started you can start on the free plan (how-to-build-gpt-6-astra-automations-that-don-t-eat-your-usage-limit.md)

Whether the free plan itself covers 2-minute schedules is not stated.

## Modal: Python, about $30 of credits once
`[T] · [D] · uploaded 2026-07-11 · claude-code-for-non-coders-6-hour-course.md · q11 · version-bound`

Claude Code writes a Python script and runs `modal deploy`. Secrets live in Modal Secrets, and containers shut down after each run. Pricing is per second.

> you get five free bucks to start with and if you put in a credit card you'll get an extra 25 (claude-code-for-non-coders-6-hour-course.md)

That is about $30 total, one time. q11's "$5 a month plus $30, $35" is Gemini's.

## Hostinger VPS: KVM 2 at six to nine dollars
`[T] · [D] · uploaded 2026-01-28; 2026-08-27 · 100-hours-testing-clawdbot-vs-claude-code-honest-results.md; set-up-a-personal-hermes-in-14-mins-no-vps-or-mac-mini.md · q11, q38 · version-bound`

For always-on assistants: Hermes, OpenClaw, Clawdbot, self-hosted n8n. Ubuntu with Docker, reached over SSH, bridged to Telegram.

> you can go ahead and sign up here for you know six bucks a month n bucks a month and i use the kvm 2 (100-hours-testing-clawdbot-vs-claude-code-honest-results.md)

Hostinger's managed Hermes app starts at "about six bucks a month" (2026-08-27) and skips the server work. The coupon "Nate Herk" gives 10% off, and it is an affiliate link, so weigh q38's "S-tier" label with that in mind. Lock ports and set a password: 900 exposed Clawdbot servers leaked keys in January 2026.

## Vercel and Supabase
`[T] · [M] · no transcript · q38 · version-bound`

[M] Gemini's version only; no caption carries this text. q38: Vercel free Hobby tier, Pro $20 per user a month, one-click deploys from GitHub. Supabase free tier, Pro $25 a month, his default for chat history, relational data and pgvector. Client Pack's stack (2026-08-10) confirms he uses Supabase and a Vercel deploy; the prices are unchecked.

## Where the always-on assistant fits
`[J] · [D] · uploaded 2026-05-10 · hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md · q11, q14 · stable`

He keeps the desk work in Claude Code and puts the 24/7 assistant on a server. Claude Code is where "90% of my knowledge work" happens (2026-05-10); Hermes on a VPS covers voice notes, crons and messages while he is away. See `build-hermes-assistant.md`.
