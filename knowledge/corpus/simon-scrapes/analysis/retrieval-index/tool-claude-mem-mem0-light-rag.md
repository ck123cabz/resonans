---
type: tool
aliases: ["claude-mem / Mem0 / Light RAG"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: claude-mem / Mem0 / Light RAG
provenance: M
lanes: [2, 3]
sources: [q13, q15]
---

# claude-mem / Mem0 / Light RAG

Three memory layers Simon reviews and largely rules out for solo business use. Grouped here because his verdict on each is the same shape: capable, but wrong-sized.

## claude-mem
MCP-based plugin that auto-captures everything Claude does in the background. In the memory decision tree it sits on the verbatim-recall branch alongside Mem Palace. Simon calls it "overkill" and dislikes that it doesn't store memory in plain readable markdown.

## Mem0
Enterprise-grade cross-tool memory layer. Fits teams shipping AI products; the alternative to Open Brain for cross-tool memory. Trade-off: your data lives on their servers instead of infrastructure you own — Open Brain (self-hosted Supabase Postgres) is his pick when ownership matters.

## Light RAG
Enterprise knowledge graph built for heavy entity extraction. Verdict: complete overkill for 99% of business owners.

## When to use
Mem0 only if you're a team shipping AI products and accept vendor-hosted data. claude-mem and Light RAG: effectively never, in Simon's routing — MemSearch (Memarch) covers the summarized-semantic case, Mem Palace covers verbatim recall, Open Brain covers cross-tool.
