---
type: tool
aliases: ["Google Workspace CLI"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Google Workspace CLI
provenance: M
lanes: [7]
sources: [q40]
---

# Google Workspace CLI

Open-source CLI released by Google that gives Claude Code direct access to the entire Google ecosystem: Drive, Gmail, Calendar, Docs, and Sheets.

## How it works
- One tool replaces the need to set up multiple separate MCP integrations for Google products.
- Ships with over 100 built-in recipes.
- Talks to Google via bash commands rather than an MCP schema.
- Output documents arrive as properly formatted markdown — headers, images, links — not raw text.

## When to use
Any Claude Code workflow touching Google surfaces where you would otherwise stack several MCP servers. Worth weighing against the MCP cost rule elsewhere in this corpus: every connected MCP server loads a 10,000-20,000 token schema at session start even if unused, so replacing multiple Google MCPs with one bash-driven CLI is a context-budget win as well as a setup simplification.
