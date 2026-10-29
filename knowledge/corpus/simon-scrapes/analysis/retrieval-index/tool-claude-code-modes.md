---
type: tool
aliases: ["Claude Code modes"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Claude Code modes (Ultra Code, agent teams, worktrees, headless -p, auto mode)
provenance: M
lanes: [5, 7]
sources: [q30, q39, q40]
---

# Claude Code modes

The native execution modes for scaling beyond one interactive context window.

## Ultra Code
Claude steps outside a single context window and writes its own structured workflow harness for the problem: spins up a team of sub-agents, gives each a clean context slate and a single job, and coordinates their outputs. Use for long complex jobs where one window degrades — premature stopping, favoring its own results, or losing the objective to context rot. Demos: the 26-agent deep research run and the inbox skill builder.

## Agent teams
Standard sub-agents are isolated and only report to the orchestrator; agent teams share a task list and communicate directly with each other. The token burn is massive — reserve for complex app builds where frontend, API, and testing agents must continuously coordinate tests and verification. Enabled via an experimental agent-teams setting set to 1/true — command/key name garbled in transcript — verify against the tool's real docs before use.

## Worktrees (-w / --worktree)
Spins up an isolated workspace: a separate copy of the codebase on its own branch, so parallel tasks don't pollute each other's context. Multiple Claudes run simultaneously across worktrees; closing a session auto-cleans the worktree or merges the branch back.

## Headless mode (-p flag)
Fully autonomous: no conversation, approvals, or terminal window. Built for cron — e.g. a 7:00 a.m. job telling Claude to review yesterday's work and write a morning report that's waiting on wake-up.

## Auto Mode
Toggle with Shift+Tab twice. A background safety classifier auto-approves safe mundane actions (reading files, running tests, git operations) but still stops for genuinely risky ones (deleting files, pushing to main).

## Related settings
Force sub-agents onto Haiku via the sub-agent model setting so background workers don't inherit expensive premium models — command/key name garbled in transcript — verify against the tool's real docs before use.
