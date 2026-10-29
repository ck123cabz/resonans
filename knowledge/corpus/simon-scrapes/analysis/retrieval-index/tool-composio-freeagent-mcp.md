---
type: tool
aliases: ["Composio / FreeAgent MCP"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Composio / FreeAgent MCP
provenance: M
lanes: [6]
sources: [q34]
---

# Composio / FreeAgent MCP

The two connector layers behind the finance automations: how Claude reaches accounting software and email inboxes that aren't native Claude partners.

## FreeAgent MCP
FreeAgent (the accounting software in the invoice-reconciliation build) is not a native Claude partner, so the system connects to it through a custom-hosted FreeAgent MCP server. The weekly routine uses this MCP to scan the accounting dashboard for unmatched or unexplained transactions lacking receipts, and later to upload the found receipt attachment to the correct transaction.

## Composio
The email side: the reconciliation routine searches across all of the user's connected inboxes, which connect via native integrations or Composio. In this corpus Composio appears as the connector option for wiring non-native email inboxes into a cloud Routine.

## When to use
When a Routine or workflow needs a tool outside Claude's native partner list: host a custom MCP server for the core system of record (the FreeAgent pattern), and use Composio or native integrations for commodity connections like inboxes.

## Caveat
Custom-hosted MCP servers are your infrastructure — the corpus doesn't cover their maintenance or auth details (on-screen content lost in transcript extraction).
