---
type: tool
aliases: ["Cloud Routines (Scheduled Tasks V2)"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Cloud Routines (Scheduled Tasks V2)
provenance: M
lanes: [5]
sources: [q27, q28, q29]
---

# Cloud Routines (Scheduled Tasks V2)

Feature in the Claude desktop app that runs scheduled workflows entirely on Anthropic's cloud — laptop shut, phone in pocket, the task still executes.

## Setup
Two paths:
- Manual form: name, description, custom prompt, frequency.
- "Create it with Claude": a Co-work chat interviews you about the business process and which tools/spreadsheets it touches, generates the description and step-by-step prompt, and runs a historical test run to validate the prompt before scheduling it.

Frequency options: hourly, daily, weekly, or monthly (e.g. 1st of every month at 8:00 a.m.).

## Billing — unresolved contradiction
The corpus contradicts itself: q27 says on Pro/Max/Team/Enterprise, Routines draw from normal plan usage rather than generating separate API bills; q28 says scheduled cloud routines still bill via API, with only Telegram chat interactions riding the subscription. Unresolved — verify current billing behavior before relying on either claim.

## When to use
Recurring scheduled workflows: the demonstrated builds are Friday invoice reconciliation, month-end P&L reporting, and the 1st-of-month subscription catcher. For scheduled tasks, Routines obsolete the DIY VPS+tmux+Telegram workaround — native cloud execution, zero technical setup.

## When to skip
Routines pass the hands-off test only for recurring scheduled work. They don't cover ad-hoc interactive dispatch from the phone — that still needs the VPS+tmux+Channels setup.
