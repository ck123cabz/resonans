---
type: tool
aliases: ["/loop + /goal + cron tools"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: /loop + /goal + cron tools
provenance: M
lanes: [5]
sources: [q26, q31, q35]
---

# /loop + /goal + cron tools

Claude Code's native run-until-done pair: /loop is the scheduler, /goal is the completion checker.

## How it works
- /loop schedules a prompt or slash command to repeat on a defined interval (every 5 minutes, daily) instead of running once.
- /goal sets an explicit completion condition; after each turn a smaller faster model (e.g. Haiku) checks whether it's met, and if not, Claude spawns another agent and keeps iterating.
- Paired, they make run-until-done automation: the task fires on cadence and refuses to stop until the exact definition of done is achieved. Example: a daily inbox-filing loop connects to Gmail, triages the last hour's emails into category folders, with /goal hard stop = "inbox is empty" and every item filed. The newsletter digest uses the same shape: /goal defines done (check all emails, return the idea list, draft posts for the top three).
- Underneath, loops are standard cron jobs managed by three built-in tools: CronCreate (schedule), CronList (view active jobs), CronDelete (cancel by job ID).

## Limits (version-bound)
- Loops auto-expire after 3 days maximum, as a safety against forgotten processes.
- Loops are session-bound: closing the terminal window destroys the loop entirely.
- No catch-up behavior: a loop instance scheduled while the session was closed simply disappears and does not re-run on reopen.

## Vs Ralph Loop
/loop+/goal schedules against a time interval and stops when the interval's goal is met; Ralph is an immediate continuous cycle that hammers one intensive build to completion in a single sitting. For always-on scheduling that survives the laptop, wrap the workflow in a cloud Routine instead.
