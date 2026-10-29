---
type: tool
aliases: ["Hermes"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Hermes
provenance: M
lanes: [2, 3, 5]
sources: [q13, q15, q19, q29]
---

# Hermes

Open-source agent framework known for two behaviors: injecting a frozen memory snapshot at session start, and running self-learning skill loops. Installed off-the-shelf as an independent system; has the fastest adoption rate of the frameworks Simon reviews.

## The frozen-snapshot pattern
The part worth keeping. In the memory decision tree, the recommended session-start injection is Hermes-style: a capped, curated snapshot (a user.md profile plus a memory.md of recent decisions) rather than injecting everything (context rot) or nothing (the human becomes the memory, re-explaining background every session). Hermes-style keyword recall works out of the box but fails on vocabulary drift — MemSearch's hybrid search is the fix for that half.

## Risks
You inherit the creator's assumptions, including no guardrails on the self-learning loop. In the dispatch-and-walk-away comparison it's grouped with OpenClaw: a 24/7 agent, but highly technical to set up with major security exposure — hundreds of malicious packages found on their marketplaces.

## Verdict
Simon prefers rebuilding its best features, memory injection above all, natively inside Claude Code rather than adopting the framework wholesale.
