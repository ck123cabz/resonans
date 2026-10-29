---
type: tool
aliases: ["GSD framework (Get Shit Done)"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: GSD framework (Get Shit Done)
provenance: M
lanes: [2]
sources: [q06, q13]
---

# GSD framework (Get Shit Done)

Metaprompting and context-engineering framework by Tash (Glitter Cowboy) that splits complex work into plan / execute / verify phases with specific task lists, built to prevent context rot on long builds.

## How it works
Breaks a complex task into detailed phases, each with its own task list, and keeps context strictly isolated between phases so a multi-day build doesn't rot a single window. In Simon's Command Center, dropping a goal in as a "deep build" automatically invokes GSD under the hood.

## Setup
Install: `npx get shit done CC`. Run: `/gsd new project`, `/gsd plan phase 1`, `/gsd execute phase 1`, `/gsd verify work`. Install commands in the source are phonetic transcript renderings — command/key name garbled in transcript — verify against the tool's real docs before use.

## When to use
Multi-day, full-application builds (a SaaS web app) requiring deep execution and human verification. For multi-hour projects, PRD Taskmaster is the lighter middle ground; below that, default plan mode.

## Verdict
The most powerful framework for complex projects. It costs more tokens and time upfront, but saves you from refactoring nightmares by keeping context strictly isolated.
