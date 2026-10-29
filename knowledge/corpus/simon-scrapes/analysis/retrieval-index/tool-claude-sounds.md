---
type: tool
aliases: ["Claude Sounds"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Claude Sounds
provenance: M
lanes: [2]
sources: [q13]
---

# Claude Sounds

Notification library by Dave Schumacer that replaces Claude's default alerts with custom sounds (example from the demo: "Yoohoo, hello is this thing on?").

## Setup
Clone the GitHub repo, add it to your path, and configure it as a notification hook in settings.json. Note the general corpus warning: exact settings.json key names were on-screen only and are transcript-mangled elsewhere — verify hook configuration against real docs.

## When to use
When you're letting Claude run autonomous background tasks and need to hear the moment it requires permission while you're away from the terminal. Fills the same gap as the mobile push setting (agent push notifications via remote control) but locally and audibly.

## Verdict
"Ridiculous but hilarious" and extremely useful for speeding up the workflow — the point is not the novelty sounds but never leaving an autonomous task silently blocked on an unnoticed permission prompt.
