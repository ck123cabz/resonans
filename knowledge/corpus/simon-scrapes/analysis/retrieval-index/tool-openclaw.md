---
type: tool
aliases: ["OpenClaw"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: OpenClaw
provenance: M
lanes: [2, 5]
sources: [q13, q28, q29]
---

# OpenClaw

24/7 self-hosted messaging-first AI teammate by Peter Steinberger, connecting natively to Telegram, WhatsApp, and iMessage. Pitched as a full life assistant that can text you dynamically. (Distinct from Christian's own "OpenClaw" migration project name — don't conflate.)

## Setup
Requires a dedicated machine (Mac Mini or VPS), Tailscale for networking, Docker, and a WhatsApp business number.

## Risks
- Security: major concerns, including 386 malicious packages found on its marketplace.
- Billing: Anthropic blocked subscription tokens from working in third-party tools, so heavy agentic use routes through per-token API billing — reported runaway bills of $500–$1,000+/month, versus interactive use on a $20/month Pro/Max subscription via the VPS+tmux+Channels route.

## Verdict
Highly technical to set up with massive security exposure — "stick to Claude Code." The one piece worth salvaging is its memory architecture (daily logs plus semantic hybrid search), which Memarch ports into Claude Code directly.
