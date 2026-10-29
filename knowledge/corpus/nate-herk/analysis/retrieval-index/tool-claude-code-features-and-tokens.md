---
type: tool
aliases: ["Claude Code features and token management"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Claude Code features and token management
speaker: Nate Herk (Cole Medin's numbers marked as guest)
provenance: D
sources: [q05, q06, q11, q33, q34, q41]
videos: [18-claude-code-token-hacks-in-18-minutes.md, 32-tricks-to-level-up-claude-code-in-16-mins.md, how-to-never-hit-your-claude-session-limit-again.md, give-me-10-mins-and-i-ll-save-you-millions-of-claude-tokens.md, every-level-of-claude-explained-in-21-minutes.md, i-tested-every-claude-code-feature-these-12-are-the-best.md, claude-code-clay-makes-lead-generation-actually-fun.md, i-tried-100-claude-code-skills-these-6-are-the-best.md, claude-code-just-added-what-everyone-wanted-remote-control.md, claude-code-for-non-coders-6-hour-course.md, claude-just-solved-session-limits.md, how-to-use-claude-code-better-than-98-of-people.md]
---

# Claude Code features and token management

The Claude Code commands and token rules Nate Herk teaches, February to September 2026. Most of this is version-bound: several rules changed with the move from a 200k to a 1M context window, and he says so on camera. Dates matter more here than anywhere else in the corpus.

## Why tokens compound: 500 to 15,500
`[R] · [D] · uploaded 2026-04-02 · 18-claude-code-token-hacks-in-18-minutes.md · q06 · stable`

Every message re-reads the conversation, `claude.md`, skills and MCP definitions.

> message one could be 500 message 30 could be 15,500 which is 31 times more (18-claude-code-token-hacks-in-18-minutes.md)

The 98.5% figure is a third party's single chat, which he cites:

> one developer actually tracked a 100 plus message chat and found that 98.5% of all the tokens were just spent rereading the old chat history (18-claude-code-token-hacks-in-18-minutes.md)

His closing line on the topic: "it's not a limits problem it's a context hygiene problem".

## When to reset: 60%, then 120k, then 250k to 300k
`[R] · [D] · uploaded 2026-04-02; 2026-04-20; 2026-07-11 · 18-claude-code-token-hacks-in-18-minutes.md; how-to-never-hit-your-claude-session-limit-again.md; claude-code-for-non-coders-6-hour-course.md · q06 · version-bound`

2026-04-02: compact at 60%, because auto-compact fires too late.

> compact at around 60% capacity autocompact triggers at like 95% by which point your context is already pretty degraded (18-claude-code-token-hacks-in-18-minutes.md)

2026-04-20: he explains the 60% was a 200k-window rule and drops `/compact`.

> when we only had 200,000 tokens in the context window i was basically always clearing and compacting when i got to about 60% which was about 120,000 tokens (how-to-never-hit-your-claude-session-limit-again.md)

On 1M Opus he stops near 120k (12%), asks for a full summary, runs `/clear` and pastes it back; his session-handoff skill packages that. A list video on 2026-04-27 still repeats "compact at 60%". By 2026-07-11:

> my best practice is basically if we get past 250,000 300,000 i'm going to do a session handoff (claude-code-for-non-coders-6-hour-course.md)

The token threshold is current; 60% is the old-window rule.

## "Dumb zone" is his term; the per-model numbers are not his
`[R] · [D] · uploaded 2026-05-12 · every-level-of-claude-explained-in-21-minutes.md · q33 · version-bound`

He uses "dumb zone" for a context window full enough that quality drops. Solo, he states it as a share of the window: 1M Opus 4.7 "gets sloppy past you know about 50% capacity".

## [D:guest:Cole Medin] Dumb-zone thresholds per model
`[R] · [D:guest:Cole Medin] · uploaded 2026-06-18 · how-to-use-claude-code-better-than-98-of-people.md · q33, q36 · version-bound`

On Nate's podcast Cole Medin gave the per-model numbers: about 250,000 tokens on Opus, about 200,000 on Opus 4.7, 100,000 to 125,000 on Sonnet 4.6.

> with opus right now it's usually around 250,000 tokens (how-to-use-claude-code-better-than-98-of-people.md)

Nate endorsed only the Opus figure: "that's my exact number too".

## Prompt cache: 1 hour on subscription, 5 minutes on API
`[R] · [D] · uploaded 2026-05-21 · give-me-10-mins-and-i-ll-save-you-millions-of-claude-tokens.md · q06 · version-bound`

Cached tokens cost 10% of normal input. Pause past the TTL and the next prompt pays full price for the whole history.

> if you're using claude via api or sub agents then the ttl or the time to live is only 5 minutes ... for cloud code inside of your terminal ... that's an hour (give-me-10-mins-and-i-ll-save-you-millions-of-claude-tokens.md)

Extra-usage (per-token) mode also defaults to 5 minutes.

## opusplan: recommended in April and May, retracted May 21
`[J] · [D] · uploaded 2026-05-12; 2026-05-21 · every-level-of-claude-explained-in-21-minutes.md; give-me-10-mins-and-i-ll-save-you-millions-of-claude-tokens.md · q06, q48 · version-bound`

> there's actually a hidden setting called opus plan ... opus does the planning and sonnet does the execution (every-level-of-claude-explained-in-21-minutes.md)

> i do want to apologize for something here because if you do model opus plan which is something that i've shown before in like token hacks videos (give-me-10-mins-and-i-ll-save-you-millions-of-claude-tokens.md)

Reason: each plan toggle is a model switch and starts a fresh cache. The recommendation also appears on 2026-04-09. Do not recommend `opusplan` from this corpus.

## Plan mode, and Boris Cherny's habit
`[J] · [D] · uploaded 2026-04-20 · how-to-never-hit-your-claude-session-limit-again.md · q06, q07 · stable`

> boris churnney the creator of claude code starts every single session in plan mode i do the same thing (how-to-never-hit-your-claude-session-limit-again.md)

Shift+Tab or `/plan`. He pairs it with the 95% confidence rule in `claude.md` (see the script files).

## Peak hours, then doubled limits
`[R] · [D] · uploaded 2026-04-02; 2026-05-07 · 18-claude-code-token-hacks-in-18-minutes.md; claude-just-solved-session-limits.md · q06, q34 · version-bound`

> during the peak hours which are 8 am to 2 p.m eastern time on weekdays (18-claude-code-token-hacks-in-18-minutes.md)

On 2026-05-07 Anthropic's SpaceX compute deal doubled the 5-hour limits on Pro, Max and Team and removed the peak-hour reduction.

> double claude code's 5-hour rate limits double whether you're on pro max or team (claude-just-solved-session-limits.md)

The peak-hour scheduling advice predates that change.

## MCP overhead: 18k per server, then tool search
`[R] · [D] · uploaded 2026-04-02; 2026-05-12 · 18-claude-code-token-hacks-in-18-minutes.md; every-level-of-claude-explained-in-21-minutes.md · q06, q12 · version-bound`

> one server alone might be something like 18,000 tokens per message (18-claude-code-token-hacks-in-18-minutes.md)

> enthropic shipped a feature in january called tool search that auto defers tool loading the moment your mcp overhead crosses 10% of your window so it cuts that overhead by 85% (every-level-of-claude-explained-in-21-minutes.md)

The 18k figure describes loading without tool search and was already stale when he said it.

## Convert documents to markdown first
`[R] · [D] · uploaded 2026-04-20 · how-to-never-hit-your-claude-session-limit-again.md · q06, q41 · stable`

> for html to markdown you're getting like 90% fewer tokens for pdf to markdown you're getting like 65 to 70% tokens reduction for docx files to markdown you're getting about 33% (how-to-never-hit-your-claude-session-limit-again.md)

He names "Dockling" (Docling) as one converter. The same video mentions a "cloud ignore file" to exclude folders. Whether Claude Code reads a `.claudeignore` is unverified; he said it, which does not make it a feature.

## /context, /cost, /statusline, /btw, /insights, output styles
`[T] · [D] · uploaded 2026-04-02; 2026-05-12 · 18-claude-code-token-hacks-in-18-minutes.md; every-level-of-claude-explained-in-21-minutes.md · q06, q41 · version-bound`

`/context` shows what fills the window; `/cost` estimates spend. A custom status line shows model, effort, context percent and tokens (captions say "/st status line"; the command is `/statusline`). `/btw` asks a side question without adding it to history:

> you can also do /btw which lets you ask claude a quick question mid task what does this function do again and it doesn't actually break the (every-level-of-claude-explained-in-21-minutes.md)

`/insights` reads a month of your sessions and reports habits worth turning into skills; he says to run it once a month. `/output style` swaps Claude Code's personality between built-in modes.

## Git worktrees for parallel sessions
`[T] · [D] · uploaded 2026-04-27 · 32-tricks-to-level-up-claude-code-in-16-mins.md · q06, q43 · version-bound`

> hack number 23 is to run parallel sessions with git work trees (32-tricks-to-level-up-claude-code-in-16-mins.md)

Each session gets an isolated copy on its own branch, so two agents do not overwrite each other. He runs "two three or four". The `claude-worktree` command name is not in the captions. He says Codex does worktrees more natively.

## /loop: 3 days, later about 7
`[T] · [D] · uploaded 2026-04-27; 2026-06-03 · 32-tricks-to-level-up-claude-code-in-16-mins.md; i-tested-every-claude-code-feature-these-12-are-the-best.md · q11 · version-bound`

`/loop` re-runs a prompt inside the open session and needs the machine awake.

> these actual loops will only last for 3 days (32-tricks-to-level-up-claude-code-in-16-mins.md)

> they should run for like seven days and then they'll automatically shut down (i-tested-every-claude-code-feature-these-12-are-the-best.md)

A product change between the two dates. Use it for short-term monitoring only.

## /goal: set an end condition
`[T] · [D] · uploaded 2026-07-12 · claude-code-clay-makes-lead-generation-actually-fun.md · q16, q19 · version-bound`

> a slash goal is basically what it lets you do is just set kind of like an end condition and then you can have claude keep working (claude-code-clay-makes-lead-generation-actually-fun.md)

His example on 2026-07-12: 50 enriched HVAC leads with personalized copy.

## /ultrareview: cloud code review
`[T] · [D] · uploaded 2026-05-03 · i-tried-100-claude-code-skills-these-6-are-the-best.md · q34, q47 · version-bound`

> / ultra review which launched alongside opus 4.7 now this one instead of running locally it uploads your branch to a cloud sandbox and spins up a fleet of reviewer[s] (i-tried-100-claude-code-skills-these-6-are-the-best.md)

`/review` is the local version. The agent-teams flag and team sizing are in `build-agent-teams-and-subagents.md`.

## Remote control: never share the link
`[T] · [D] · uploaded 2026-02-25 · claude-code-just-added-what-everyone-wanted-remote-control.md · q11, q33 · version-bound`

`claude remote-control` prints a QR code and URL that drive your local session from a phone.

> anyone could go to this link and then control your local files so just don't give that to people (claude-code-just-added-what-everyone-wanted-remote-control.md)

## Bypass mode fenced by a settings file; auto mode
`[J] · [D] · uploaded 2026-07-11 · claude-code-for-non-coders-6-hour-course.md · q33, q48 · version-bound`

He kept bypass permissions on, but only behind a `settings.json` that denies risky commands.

> i would put my cloud code on bypass permissions mode but i felt comfortable about it because it could never do anything that was actually risky (claude-code-for-non-coders-6-hour-course.md)

> auto mode was new so when i designed that settings file auto mode didn't yet exist (claude-code-for-non-coders-6-hour-course.md)

He tells viewers without that file to use auto mode. q48's "stopped using bypass" is wrong.
