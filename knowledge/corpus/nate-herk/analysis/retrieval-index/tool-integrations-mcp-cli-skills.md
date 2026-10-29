---
type: tool
aliases: ["Integrations: MCP, CLI, APIs and skills"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: "Integrations: MCP, CLI, APIs and skills"
speaker: Nate Herk
provenance: D
sources: [q04, q12, q16, q41, q43]
videos: [every-level-of-claude-explained-in-21-minutes.md, this-is-the-most-powerful-tool-to-give-to-claude-code.md, 18-claude-code-token-hacks-in-18-minutes.md, 32-tricks-to-level-up-claude-code-in-16-mins.md, build-anything-with-claude-code-n8n-beginner-s-guide.md, build-sell-grok-bots-2-hour-course.md, a-week-of-grok-bot-lessons-in-10-mins.md, grok-bot-manages-my-inbox-and-has-its-own.md, build-sell-claude-code-operating-systems-2-hour-course.md, i-tried-100-claude-code-skills-these-6-are-the-best.md, this-one-plugin-just-10x-d-claude-code.md, claude-code-skills-just-got-even-better.md, master-95-of-claude-code-skills-in-28-minutes.md, build-sell-ai-saas-products-2-hour-course.md]
---

# Integrations: MCP, CLI, APIs and skills

How Nate Herk connects agents to outside services, and the third-party skills and plugins he uses. His order of preference is fixed from 2026-05-12: CLI, then API, then skills, then MCP. Token numbers behind that order are in `tool-claude-code-features-and-tokens.md`.

## Integration order: CLI, API, skills, MCP last
`[J] · [D] · uploaded 2026-05-12 · every-level-of-claude-explained-in-21-minutes.md · q12 · stable`

> the rule still holds cli first api endpoints second skills third and mcp only when nothing else fits (every-level-of-claude-explained-in-21-minutes.md)

Four tiers. q12 draws three (CLI, API, MCP); drop that version.

## Why CLI beats MCP: 35x and 72%, source unnamed
`[R] · [D] · uploaded 2026-05-09; 2026-05-12 · this-is-the-most-powerful-tool-to-give-to-claude-code.md; every-level-of-claude-explained-in-21-minutes.md · q06, q12 · version-bound`

He calls this "a real benchmark" and does not name who ran it.

> mcp used 35 times more tokens than the cli on the same task and reliability drops from 100% with the cli to 72% with mcp as tasks get harder (this-is-the-most-powerful-tool-to-give-to-claude-code.md)

A second, different figure is his reading of Anthropic's docs: CLIs "use 60 to 70% fewer tokens" than MCP. The two measure different things and he never reconciles them. q06's "~200 tokens per CLI call" was not found.

## Printing Press: a CLI factory
`[T] · [D] · uploaded 2026-05-09 · this-is-the-most-powerful-tool-to-give-to-claude-code.md · q06, q41 · version-bound`

A library of about 50 pre-built CLIs plus a way to generate new ones; commands carry the prefix "pp". He built a Skool CLI in about 10 minutes. On one call, pulling 10 community posts, about 132,000 tokens came back from Skool and stayed out of the context window; only a summary of about 2,000 tokens went in.

> the whole idea is that apis suck for agents mcps also suck for agents and a lot of times official clis suck for agents (this-is-the-most-powerful-tool-to-give-to-claude-code.md)

## Google Workspace CLI instead of the MCP
`[T] · [D] · uploaded 2026-04-02 · 18-claude-code-token-hacks-in-18-minutes.md · q12 · version-bound`

> rather than having the google workspace or google calendar mcp server which eats a lot of tokens just use the google workspace cli it's faster it's cheaper (18-claude-code-token-hacks-in-18-minutes.md)

The open-source GWS CLI covers Gmail, Docs, Sheets, Slides, Calendar and Drive. q12 adds that he has Claude write a local reference file (for example `gws_reference.md`) once so it stops fetching docs; that detail is [M].

## n8n MCP server and n8n skills
`[T] · [D] · uploaded 2026-01-16 · build-anything-with-claude-code-n8n-beginner-s-guide.md · q10, q12 · version-bound`

He gave Claude Code the n8n MCP server URL, his n8n API key, and the GitHub MCP server, plus n8n skills, so it can read node parameters and edit workflow JSON. In that build n8n stays the back end and Claude Code audits the workflow, switches it to a webhook and builds a front end. Full build: `build-n8n-agents-and-migration.md`.

## Context7 MCP for current docs
`[T] · [D] · uploaded 2026-04-27 · 32-tricks-to-level-up-claude-code-in-16-mins.md · q06, q41 · version-bound`

> hack number 32 is context 7 mcp this one's a game changer (32-tricks-to-level-up-claude-code-in-16-mins.md)

It fetches version-specific docs so the model stops suggesting renamed or deprecated functions. It is one of the MCPs he keeps despite the CLI-first rule.

## Composio inside Grok Bot
`[T] · [D] · uploaded 2026-08-31 · build-sell-grok-bots-2-hour-course.md; a-week-of-grok-bot-lessons-in-10-mins.md · q17 · version-bound`

One connection gives every bot in his Grok Bot org access to YouTube, Perplexity, LinkedIn and other apps. Connections are shared across bots; memory is per bot.

> every single agent that you spin up can use composio and can use everything that you've connected (build-sell-grok-bots-2-hour-course.md)

## AgentMail gives an agent its own inbox
`[T] · [D] · uploaded 2026-09-16 · grok-bot-manages-my-inbox-and-has-its-own.md · q26 · version-bound`

> we use a service called agent mail and it's completely free to start (grok-bot-manages-my-inbox-and-has-its-own.md)

He uses it so Grok Bot and Hermes can send and receive as themselves. It is not a cold-email tool.

## A dedicated bot account instead of your own key
`[R] · [D] · uploaded 2026-05-01 · build-sell-claude-code-operating-systems-2-hour-course.md · q12, q43 · stable`

> i created an account called up ai and now i give my uppai api key to cloud code rather than my own personal api key (build-sell-claude-code-operating-systems-2-hour-course.md)

The captions do not name the tool this account lives in. Keys go in a root `.env`, never in chat. He suggests the same pattern for QuickBooks.

## ClickUp, Slack, Stripe, Supabase keys
`[T] · [M] · no transcript · q12 · version-bound`

[M] Gemini's version only; no caption carries this text. q12: ClickUp through direct API tokens; Slack through channel webhooks and the API for alerts and error logs; Stripe with test and live keys for subscriptions and webhooks; Supabase with the `anon` public key and `service_role` secret. "ClickUp Brain 2" has no caption hit. Stripe checkout and Supabase are confirmed as parts of the Client Pack build (2026-08-10).

## Superpowers and GSD
`[T] · [D] · uploaded 2026-05-03; 2026-04-12 · i-tried-100-claude-code-skills-these-6-are-the-best.md; this-one-plugin-just-10x-d-claude-code.md · q04, q43 · version-bound`

Two third-party plugins he runs. Superpowers governs how Claude writes code. Its writing-skills meta-skill uses test-driven development for skills; he reads that off the plugin's docs, so TDD-for-skills is the plugin's method, not his.

> skill number three is called gsd which stands for get shit done and if superpowers is about how claude writes code then gsd is about the envir[onment] (i-tried-100-claude-code-skills-these-6-are-the-best.md)

GSD fights context rot by spawning fresh subagents instead of letting one long session degrade.

## Anthropic's skill-creator and the two skill types
`[T] · [D] · uploaded 2026-03-05; 2026-07-11 · claude-code-skills-just-got-even-better.md; claude-code-for-non-coders-6-hour-course.md · q04 · version-bound`

`skill-creator` is Anthropic's official skill for building, testing and refining skills; he invokes it as a slash command. Anthropic sorts skills into two types, which he reads out:

> there are two different types of skills we have a capability uplift skill which basically is a prompt so it teaches claude how to do something better (claude-code-skills-just-got-even-better.md)

The other type is encoded preference. Skill size, from the docs he quotes: keep `skill.md` under 500 lines; front matter loads at about 100 tokens (master-95-of-claude-code-skills-in-28-minutes.md, 2026-02-27).

## His own skill inventory
`[T] · [M] · no transcript · q04, q05 · version-bound`

[M] Gemini's version only; no caption carries this text. Skills named across his videos: `skill-builder`, `grill-me` (Matt Pocock's idea), `front-end-design`, `video-to-website`, `os-audit`, `level-up`, `session-handoff`, `morning-coffee`, `pulse-check`, `idea-mining`, `storm-research`, `roast`, `excalidraw-diagram`, `inbox-triage`, `repurpose-youtube-video`, `motion-reel`, `hyperframes`, `infographic-builder`, `gws-cli`, `nano-banana-image`. The list is Gemini's assembly; each name needs a grep before you cite it.

## Codex skills live in .agents/skills
`[T] · [M] · no transcript · q16 · version-bound`

[M] Gemini's version only; no caption carries this text. Project skills sit in `.agents/skills/<name>/skill.md`, global ones in `~/.agents/skills/`. The anatomy matches Claude skills, so folders copy between `.claude/skills/` and `.agents/skills/`. He keeps matching `claude.md` and `agents.md` at the repo root so both harnesses read the same rules.
