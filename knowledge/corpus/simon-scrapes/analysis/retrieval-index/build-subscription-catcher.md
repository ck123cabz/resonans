---
type: build
aliases: ["Subscription catcher (recurring spend audit)"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Subscription catcher (recurring spend audit)
provenance: M
lanes: [5]
sources: [q27]
---

# Subscription catcher (recurring spend audit)

Monthly cloud Routine that audits recurring spend and emails the findings before sneaky charges compound.

## Trigger and schedule
Cloud-based scheduled task, 8:00 a.m. on the 1st of every month.

## Steps
1. Connect to the accounting software and pull all recurring bills and expenses.
2. Compare them against the previous month's data.
3. Flag three things: sneaky price increases, duplicate charges, and unused software subscriptions.
4. Immediately send an audit summary to email.

## Notes
One of the three demonstrated finance routines (with Friday invoice reconciliation and month-end P&L reporting). The month-over-month comparison is the mechanism — a single month's pull can't distinguish a price increase from a normal bill; the diff against last month is what surfaces the flags. Setup can go through the "Create it with Claude" path: a Co-work chat interviews you about the process, generates the prompt, and runs a historical test run to validate it before scheduling. Cloud-routine billing is contradicted within the corpus (plan usage per q27 vs API per q28); verify.
