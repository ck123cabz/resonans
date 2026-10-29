---
type: tool
aliases: ["Mem Palace"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Mem Palace
provenance: M
lanes: [2, 3]
sources: [q13, q15, q17]
---

# Mem Palace

Memory framework (by Me Palace Official) for verbatim word-for-word recall — Simon's "Level 4." Stores every conversation exactly as typed with no summarization compression, so exact detail survives.

## How it works
- Two databases: SQL for entities and relationships, Chroma DB for conversation chunks.
- Method-of-loci hierarchy: wings (people/projects/topics) > rooms (days/sessions/threads) > closets (narrower topics/bundles) > drawers (verbatim conversation text).
- A symbolic index acts as a dense dialect the LLM scans at a glance — claimed retrieval of specific information in as little as 42ms across thousands of drawers.
- Storage is hook-driven and silent: hooks fire at session end and right before context compaction, filing raw dialogue into the correct drawer with no manual effort.

## Setup
One-line install from mepalaceofficial.com. Auto-creates the palace directory structure and registers hooks in settings.json. A built-in `mine` function retroactively indexes previous conversation history.

## When to use
The upgrade trigger: you frequently think "I know we discussed this a few weeks ago, but I can't remember exactly what was decided." Beats semantic-search systems whenever exact phrasing matters — specific client phrasing, the exact wording of decisions.

## Verdict
Overkill for general business tasks. Limitation: locked to the local machine. In the memory decision tree, verbatim recall routes here (or to claude-mem); curated summaries route to MemSearch instead.
