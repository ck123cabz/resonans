---
type: tool
aliases: ["Channels (Telegram/Discord plugin)"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Channels (Telegram/Discord plugin)
provenance: M
lanes: [3, 5]
sources: [q19, q28, q29]
---

# Channels (Telegram/Discord plugin)

Official plugin that bridges the Claude Code terminal to Telegram or Discord: messages push into the active session, replies come back in-chat, and permission requests are relayed to the phone for remote approval of file edits and commands.

## The session-death limitation
Native Remote Control and Channels are tied to the local machine's awake state: laptop sleep, a Wi-Fi drop, or more than 10 minutes of inactivity kills the session and stops all work mid-task. They fail the dispatch-and-walk-away test on their own.

## The fix
Run Channels on a VPS inside tmux — the persistent server session lets you dispatch from the phone, close the app, and let the work finish. This combination (VPS ~$15/month + tmux + official Channels plugin) is Simon's winning remote setup: full security control, dynamic dispatch, and interactive Telegram chat drawing from the flat-rate Pro/Max subscription rather than API billing.

## Setup (from the VPS recipe)
Create a Telegram bot via BotFather `/newbot` and copy the token; install `bun` and `unzip` (plugin prerequisites); inside tmux run `/plugin install @claude-plugins/official`, then `/telegram configure` and paste the token, reload plugins; relaunch with `claude --channels-plugin telegram`; pair via the code the bot sends. After pairing, lock the bot down so nobody else can generate pairing codes or reach the server.

## When to skip
For purely scheduled (non-interactive) work, cloud Routines cover the hands-off case with zero setup; Channels is for ad-hoc interactive dispatch.
