---
type: tool
aliases: ["PRD Taskmaster"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: PRD Taskmaster
provenance: M
lanes: [2]
sources: [q13]
---

# PRD Taskmaster

Planning skill by Anon byte 93: interviews you to generate a comprehensive Product Requirements Document, sets up the directory structure, and validates the plan against 13 automated checks.

## Setup
Clone the GitHub repo or install via `npx skills add ... -local`, then run the `./install.sh` script. Trigger with `/pd taskmaster` in Claude Code. Install commands in the source file are phonetic transcript renderings — command/key name garbled in transcript — verify against the tool's real docs before use.

## When to use
The middle tier of Simon's planning ladder: multi-hour projects that need better planning than Claude's default plan mode but aren't complex enough to justify the GSD framework. GSD takes over for multi-day full-application builds; default plan mode covers anything smaller.

## Verdict
A fantastic middle-ground planning framework, much more comprehensive than the built-in planning tools. The 13 automated validation checks are the differentiator over free-form PRD prompting.
