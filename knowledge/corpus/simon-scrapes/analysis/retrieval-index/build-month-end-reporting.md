---
type: build
aliases: ["Month-end reporting routine"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Month-end reporting routine
provenance: M
lanes: [5, 6]
sources: [q27, q34]
---

# Month-end reporting routine

Cloud Routine that automates the spreadsheet labor of building an aggregated end-of-month financial summary.

## Trigger and schedule
Cloud-based scheduled task, fires automatically at the end of every month.

## Tools
Claude Code Routines, a bank account integration, and a spreadsheet.

## Steps
1. Pull live financial numbers by exporting all transactions directly from the bank account into a spreadsheet.
2. Replicate the human formatting steps — e.g. dragging down formulas in specific columns.
3. Analyze the transactions and add any previously unattributed names or vendors into a dedicated lookups field.
4. Aggregate everything to map exactly what money came in and what went out, generating a finished, clean P&L tab ready for the owner to review.

## Notes
The build's distinguishing move is step 2: the routine reproduces the exact manual formatting a human bookkeeper would do rather than inventing its own layout, so the output drops into the existing reporting workflow unchanged. Sibling routines: Friday invoice reconciliation and the 1st-of-month subscription catcher. Cloud-routine billing is contradicted within the corpus (plan usage vs API); verify before relying on it.
