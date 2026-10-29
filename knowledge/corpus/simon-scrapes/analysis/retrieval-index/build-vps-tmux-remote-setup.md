---
type: build
aliases: ["VPS + tmux remote setup (12-step recipe)"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: VPS + tmux remote setup (12-step recipe)
provenance: M
lanes: [3, 5]
sources: [q19, q28, q29]
---

# VPS + tmux remote setup (12-step recipe)

Always-on remote Claude Code: dispatch from Telegram on the phone, close the app, work finishes on the server. Fixes native session death (Remote Control and Channels die on laptop sleep, Wi-Fi drop, or >10 minutes of inactivity) and avoids third-party frameworks like OpenClaw that force per-token API billing ($500–$1,000+/month reported). Interactive Telegram chat draws from the flat-rate Pro/Max subscription.

## Cost
~$15/month for Ubuntu on Hetzner (managed via ls.io), framed against a $600 dedicated Mac Mini. Caveat: scheduled cloud routines and cron jobs still bill via API even in this setup; only the Telegram chat interactions ride the subscription.

## Steps
1. Generate an SSH key pair.
2. Deploy an Ubuntu VPS with the public key.
3. Connect VS Code via Remote-SSH.
4. Create a non-root user and copy the SSH key to it.
5. `npm install -g @anthropic-ai/claude-code` and log in with the subscription account.
6. git clone the project repo for files/skills/brand context.
7. Create a Telegram bot via BotFather `/newbot` and copy the token.
8. Install `bun` and `unzip` (Telegram plugin prerequisites).
9. `tmux new -s agent`.
10. Inside tmux: `/plugin install @claude-plugins/official`, `/telegram configure` + paste token, reload plugins.
11. Relaunch with `claude --channels-plugin telegram`.
12. Pair via the code the bot sends, then lock down pairing.

## Security rules
Never run Claude as root on the server — use the dedicated user with granted permissions. After pairing, lock the bot down so nobody else can generate pairing codes or reach the server.

## Why tmux
tmux keeps the terminal session alive in the background, so closing Telegram or dropping the connection doesn't kill the running agent — it's the piece that makes dispatch-and-disconnect work. For purely scheduled work, cloud Routines now cover this with zero setup; the VPS route remains for ad-hoc interactive dispatch.
