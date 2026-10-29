---
type: build
aliases: ["Command Center"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Command Center
provenance: M
lanes: [1]
sources: [q06]
---

# Command Center

A visual Kanban UI Simon built on top of his Agentic OS. Problem: running autonomous Claude Code tasks meant five terminal tabs open at once, lost context, and managing terminal sessions instead of business goals.

## Rejected alternatives
tmux keeps you stuck in the terminal with no big-picture drag/progress view; the Anthropic desktop app manages one conversation at a time and makes env vars/MCP setup harder than the terminal; Vibe Kanban is developer-focused (GitHub commits/PRs); Paperclip forces corporate org charts (assign a CEO/CTO) for simple jobs. Their shared failure: all built bottom-up from code sessions with no underlying business context — brand voice, audience, content strategy — which is what output quality needs.

## Architecture
A UI wrapper sitting directly on top of the Agentic OS (brand voice, project memory, chained skills underneath). Runs locally and abides by Anthropic OAuth policy, so it works on Pro/Max subscriptions without separate API token costs.

## Features
- Kanban board tracks business goals, not code issues. Columns: "Your Turn" (needs human review), "Claude's Turn" (in progress), "Achieved".
- Goal scoping on drop-in: quick task, multi-deliverable campaign, or "deep build" — which automatically invokes the GSD planning framework under the hood.
- Task detail view: split conversation history + live-updating plan, plus rendered markdown previews of outputs (e.g. a LinkedIn post) for review and copy.
- Skills/docs management from the dashboard: search, view, and edit the markdown of 20+ skills and reference files, edits written back to the underlying codebase; includes a meta skill-creator that builds new skills using the system's conventions.
- Multi-client filter loads only that client's brand context and tasks; a scheduled-jobs view shows active background jobs (weekly digests, daily skill update checks) at a glance.

## Operating model
Owner as supervisor: type a business outcome, choose permissions, send. Claude works in the background and surfaces to "Your Turn" only when human feedback is needed; six or more goals run in parallel from one dashboard.
