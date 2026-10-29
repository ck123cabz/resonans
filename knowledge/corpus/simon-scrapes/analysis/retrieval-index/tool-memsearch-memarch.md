---
type: tool
aliases: ["MemSearch (Memarch)"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: MemSearch (Memarch)
provenance: M
lanes: [2, 3, 4]
sources: [q13, q15, q16, q25]
---

# MemSearch (Memarch)

Open-source Claude Code memory plugin by Zilliz (the Milvus vector-DB team). Ports OpenClaw's memory architecture into Claude Code: markdown daily logs plus hybrid semantic search — dense vectors for meaning, BM25 for keywords ("payment processing" finds "Stripe").

## How it works
- Capture: a stop hook fires after every turn; a fast model (Haiku) summarizes the turn into bullets; summaries are chunked, embedded, and stored in a local Milvus vector DB running on CPU. Summaries also append to markdown daily log files organized by date and session anchors.
- Retrieval, three tiers: tier 1 returns semantic+keyword chunk matches; tier 2 (expand) adds surrounding summaries and metadata; tier 3 pulls the complete raw dialogue of the past session as last resort.
- Injection: a user-prompt-submit hook silently injects the top 3 semantic matches into every prompt, so no explicit "search my notes" is needed.
- Local vector DB means zero API costs for storage and retrieval (version-bound).

## Setup
`/plugin marketplace add` the Zilliz memsearch marketplace, then `/plugin install memarch`, then restart or `/reload plugins`. The marketplace name is rendered phonetically in the source ("zillastte mem search") — command/key name garbled in transcript — verify against the tool's real docs before use.

If running Memarch (or any custom memory system), turn native automemory OFF via /memory — otherwise Claude forks the entire context into a background memory-extraction call billed at full input prices.

## When to use
Simon's "80/20" memory fix and his "Level 3." Upgrade trigger is two conditions together: over a month of Claude Code use with memory files past a small handful of documents, AND native keyword recall has actually failed you on a past-information query.

## Verdict
The 80/20 solution for most business owners; fixes Claude Code's poor native recall. Returns raw chunks (top matches) for the agent to interpret — layer the GBrain reranking pattern on top if you want synthesized, cited answers.
