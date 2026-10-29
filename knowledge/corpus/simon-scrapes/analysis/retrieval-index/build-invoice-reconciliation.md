---
type: build
aliases: ["Invoice reconciliation routine"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Invoice reconciliation routine
provenance: M
lanes: [5, 6]
sources: [q27, q34]
---

# Invoice reconciliation routine

Weekly cloud Routine that automates matching receipts to accounting transactions — the manual chore of hunting down receipts, eliminated.

## Trigger and schedule
Cloud-based scheduled task (Routines), fires every Friday at 4:00 p.m.

## Tools
Claude Code Routines; FreeAgent accounting software connected via a custom-hosted FreeAgent MCP server (FreeAgent is not a native Claude partner); multiple email inboxes connected via native integrations or Composio.

## Steps
1. At 4:00 p.m. Friday the routine wakes and uses the FreeAgent MCP server to scan the accounting dashboard for unmatched or unexplained transactions that currently have no attached receipts.
2. It searches across all connected email inboxes to hunt down the specific receipt corresponding to each unmatched transaction.
3. Once found, it grabs the file and uploads the attachment directly to the correct transaction in FreeAgent, reconciling the books autonomously.

## Notes
Runs entirely on Anthropic's cloud — laptop can be shut. Billing for cloud routines is contradicted within the corpus (plan usage per q27 vs API billing per q28); verify before scaling this up. Part of a trio of finance routines with month-end reporting and the subscription catcher.
