---
type: build
aliases: ["AIOS and second brain builds"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: AIOS and second brain builds
speaker: Nate Herk
provenance: D
sources: [q01, q02, q04, q43, q49]
videos: [andrej-karpathy-just-10x-d-everyone-s-claude-code.md, build-sell-claude-code-operating-systems-2-hour-course.md, claude-code-for-non-coders-6-hour-course.md, i-turned-claude-into-the-ultimate-second-brain.md, master-95-of-claude-code-skills-in-28-minutes.md]
---

# AIOS and second brain builds

Nate's own AI operating system in Claude Code: an Obsidian-style LLM wiki called Herkbrain, an executive-assistant role, a set of ops skills, and the channel audits it produced. Dates run 2026-04-05 (the wiki video) to 2026-07-11 (the non-coders course). The framework (AIOS, 4 C's) is in `framework-aios-and-4-cs.md`.

## Herkbrain: a Karpathy-style LLM wiki over 36 videos
`[B] · [D][G] · uploaded 2026-04-05 · andrej-karpathy-just-10x-d-everyone-s-claude-code.md · q02 · stable`

He built a markdown vault from his 36 most recent YouTube videos. The layout follows Andrej Karpathy's LLM wiki idea: a raw folder for dropped inputs, a wiki folder the model writes pages into, plus an index. He keeps two vaults, Herk Brain and YouTube transcripts.

> what you're looking at right here is 36 of my most recent YouTube videos organized into an actual knowledge system that makes sense (andrej-karpathy-just-10x-d-everyone-s-claude-code.md)

> you've got a raw folder where you put all of the stuff and then you've got a wiki folder which is what the LLM takes from your raw and puts it into the wiki (andrej-karpathy-just-10x-d-everyone-s-claude-code.md)

q02's subfolder list (`/analysis/`, `/concepts/`, `/entities/`, `/sources/`, `log.md`) is Gemini's and unchecked.

## hot.md: a small cache of the latest context
`[B] · [D] · uploaded 2026-04-05 · andrej-karpathy-just-10x-d-everyone-s-claude-code.md · q02 · stable`

The Herkbrain wiki holds a `hot.md` that stores the most recent thing he said to his executive assistant. He hedges its size.

> this is basically just a cache of like 500 words or 500 characters that it saves which is like what is the most recent thing that Nate just gave me (andrej-karpathy-just-10x-d-everyone-s-claude-code.md)

Warning line: pass 1 gave "~500 words". Keep his hedge.

## The 95% token cut belongs to "one X user"
`[R] · [D] (third-party) · uploaded 2026-04-05 · andrej-karpathy-just-10x-d-everyone-s-claude-code.md · q06, q34 · stable`

He cites someone else's result for the wiki pattern. It is not his measurement.

> one X user turned 383 scattered files and over a 100 meeting transcripts into a compact wiki and dropped token usage by 95% (andrej-karpathy-just-10x-d-everyone-s-claude-code.md)

## Executive assistant role line
`[S] · [D] · uploaded 2026-07-11 · claude-code-for-non-coders-6-hour-course.md · q01 · stable`

The role line at the top of his assistant's `claude.md`. The verbatim form:

> you are Nate Herk's executive assistant your job is to help him spend less time on operations people management and admin so he can focus on learning AI tools and making YouTube videos (claude-code-for-non-coders-6-hour-course.md)

Warning line: q01's "spend less time on ops and ship faster" merges this with a different template's role line.

## Routing files under /context
`[B] · [M] · no transcript quote · q01, q02 · stable`

[M] Gemini's version only; no caption carries this text.

q02 lists `/context/` files for identity, business, team and priorities, with the `claude.md` routing to them. The `MI.md` filename and the routing sentence "If you need personal context read context/MI.md" are not in any caption; it may be `me.md` read off screen.

## Ops skills: morning coffee, pulse check, level up, idea mining, inbox triage
`[B] · [D] for names; [M] for contents · uploaded 2026-05-01 · build-sell-claude-code-operating-systems-2-hour-course.md; claude-code-for-non-coders-6-hour-course.md · q04 · stable`

In the AIOS course he runs three agents at once: morning coffee plans his day, pulse check reviews projects and commitments, a third draws an Excalidraw diagram.

> I've got the skill that I called morning coffee that helps me plan my day every morning (build-sell-claude-code-operating-systems-2-hour-course.md)

> I'm asking it to run a pulse check on all my projects and commitments to see how things are going (build-sell-claude-code-operating-systems-2-hour-course.md)

The course kit ships three starter skills: audit, level up, and onboard.

> We have one called audit we have one called level up and we have one called onboard (build-sell-claude-code-operating-systems-2-hour-course.md)

Idea mining triggers on requests for content or video ideas. He uses it as his example of reference files kept outside the skill folder.

> here we have a skill called idea mining and so what happens in here is basically used when someone asks for content ideas video ideas what to make next (master-95-of-claude-code-skills-in-28-minutes.md)

Inbox triage is built live in the non-coders course, with references, scripts and a main markdown file. q04's job lists (morning coffee reads Calendar, ClickUp and priorities; level up scans for high-ROI automations; idea mining scores YouTube comments, competitor channels and X trends in parallel) are [M].

## A separate "Up AI" account for the agent's keys
`[B] · [D] · uploaded 2026-05-01 · build-sell-claude-code-operating-systems-2-hour-course.md · q43 · stable`

He created a bot user and gives Claude Code that account's API key, so the agent never holds his personal one. He suggests the same for QuickBooks. q43's "ClickUp profile" is not in the caption.

> I created an account called Up AI and now I give my uppai API key to cloud code rather than my own personal API key (build-sell-claude-code-operating-systems-2-hour-course.md)

## Channel audit: 75 videos in about 10 minutes
`[B] · [D][G] · uploaded 2026-07-11 · claude-code-for-non-coders-6-hour-course.md · q49 · version-bound`

His agent pulled analytics for 75 videos, color-coded and designed the report. The quarter is unnamed; q49's "Q2 2026" is Gemini's.

> how long would this have taken you to manually go pull out you know 75 videos put all the analytics in here color code it design it do all of this and this literally took my AI agent about 10 minutes (claude-code-for-non-coders-6-hour-course.md)

## Second-brain output: 41 and 261 videos, 620k stale vs 800k live, 13-person team
`[R] · [D] · uploaded 2026-06-10 · i-turned-claude-into-the-ultimate-second-brain.md · q49 · version-bound`

He reads figures off his AIOS output and corrects some on camera. It counts "41 videos in 2024 261 videos in 2025". It says 620,000 subscribers; he says that is wrong and he is at about 800k. It says a 13-person team runs the business at UPAI (captioned "AAI"), and he confirms that is his core team.

> right now I'm at um like 800k subscribers but it got this wrong ... it found that I had 620,000 subscribers (i-turned-claude-into-the-ultimate-second-brain.md)

> 13 person team is kind of the core team right now um my only job is to learn AI make videos delegate the rest (i-turned-claude-into-the-ultimate-second-brain.md)

Warning lines: 620k was never a milestone. sources.tsv holds 9 dated 2024 videos and 128 dated 2025 videos, so the 41/261 counts likely include shorts.

## Where to look
- Wiki, hot cache, 383-file stat: andrej-karpathy-just-10x-d-everyone-s-claude-code.md (2026-04-05)
- Course kit, ops skills, Up AI: build-sell-claude-code-operating-systems-2-hour-course.md (2026-05-01)
- EA role line, inbox triage, 75-video audit: claude-code-for-non-coders-6-hour-course.md (2026-07-11)
- 13-person team, 800k: i-turned-claude-into-the-ultimate-second-brain.md (2026-06-10)
