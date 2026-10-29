---
type: tool
aliases: ["Vibe Kanban / Pulsia"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Vibe Kanban / Pulsia
provenance: M
lanes: [1, 2]
sources: [q06, q13]
---

# Vibe Kanban / Pulsia

Two open-source Kanban UI wrappers that sit on top of Claude to manage agents from a board instead of terminal tabs.

## When to use
When you are a software engineer managing GitHub commits, branches, and coding agents — that is their design center.

## When to skip
For business operation. Both are strictly built for code sessions rather than tracking broader business goals; Vibe Kanban was rejected in the Command Center evaluation for exactly this (developer-focused: GitHub commits and PRs). The shared failure across these wrappers: bottom-up from code sessions with no underlying business context — brand voice, audience, content strategy — which is what output quality needs.

## Verdict
Beautiful UIs, wrong substrate for business goals. Simon's answer was to build the Command Center instead: the same Kanban surface, but sitting directly on top of the Agentic OS (brand context, project memory, chained skills) with columns for business outcomes, not code issues.
