---
type: tool
aliases: ["Open Brain"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Open Brain
provenance: M
lanes: [2, 3]
sources: [q13, q15, q18]
---

# Open Brain

Cross-tool memory infrastructure by Nate Jones: a Postgres database hosted on Supabase that Claude Code, ChatGPT, and Cursor all read and query as one shared memory in real time.

## How it works
- Single "thoughts" table where each row = text chunk + embedding vector + tags + timestamp.
- Supabase edge functions act as the front door any AI tool can call.
- The connection runs as an MCP server hitting the Supabase edge functions.
- Running cost: under $1/month (roughly 10-30 pence) on the Supabase free tier (version-bound).

## Setup
Notably heavier than local plugins: 30-45 minutes, AI-assisted, with a setup guide and companion prompts to migrate existing Claude Code memories. Simon calls it the hardest install of the memory options.

## When to use
When you heavily switch between tools — Claude Code on desktop, ChatGPT on the phone, Cursor for coding — and want one centralized memory. The portability argument: you own the Supabase project and can export the Postgres DB anytime; a new AI tool six months from now just connects to the existing brain with zero data migration. His "most future-proof" pick.

## When to skip
If you live mostly in Claude Code on one machine, skip it: every query goes to an external cloud DB (latency), and the setup complexity is overkill without a real multi-tool need. Stay with MemSearch or Mem Palace locally.
