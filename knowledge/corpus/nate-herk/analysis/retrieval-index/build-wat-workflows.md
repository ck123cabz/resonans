---
type: build
aliases: ["WAT workflow builds"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: WAT workflow builds
speaker: Nate Herk
provenance: D
sources: [q03, q01]
videos: [build-sell-with-claude-code-10-hour-course.md, how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md, agentic-workflows-just-changed-ai-automation-forever-claude-code.md]
---

# WAT workflow builds

The worked builds Nate runs inside his WAT layout in Claude Code, from 2026-01-25 to 2026-03-12. The framework itself is in `framework-wat.md`. This file holds the builds: the folder layout, the YouTube weekly report, the remote-jobs scraper, and the stop-condition example.

## Folder layout: /workflows, /tools, /temp
`[B] · [D] · uploaded 2026-03-12 · build-sell-with-claude-code-10-hour-course.md · q03, q01 · stable`

He has Claude Code create three folders before any build. `/workflows/` holds markdown SOPs, one per job. `/tools/` holds Python scripts, one action each. A temporary folder holds throwaway output such as test PDFs. API keys sit in a root `.env`, per q03. On camera he points at the empty folders the agent just made.

> we've got our temporary folder we've got our tools folder we've got our workflows obviously there's nothing in these yet besides just some read me and some basic stuff (build-sell-with-claude-code-10-hour-course.md)

In the same course the agent later drops a test PDF into that folder while fixing a tool:

> it made a test PDF just to see how that worked and you can see here it's stored as a temporary file so in our temp folder (build-sell-with-claude-code-10-hour-course.md)

## YouTube weekly report: one workflow, seven Python tools
`[B] · [D][G] · uploaded 2026-03-12 · build-sell-with-claude-code-10-hour-course.md · q03 · stable`

The workflow file is `youtube_weekly_report`. The agent pulls channel stats, analyses them, charts them, builds slides, and emails the report over Gmail. It plans seven Python tools, one action per script. q03 names the files `fetch_yt_data.py`, `analyze_yt_data.py`, `generate_charts.py`, `generate_slides.py`, `export_to_sheets.py`, `discover_channels.py`, `send_email_report.py`. The script filenames are Gemini's reading; the seven actions are spoken.

> we've got the workflow which is YouTube weekly report we've got the agent layer we've got different tools it's going to build out these seven different Python tools (build-sell-with-claude-code-10-hour-course.md)

> fetching YouTube data analyzing YouTube data generating charts generating slides sending the email report exporting to sheets and discovering channels (build-sell-with-claude-code-10-hour-course.md)

This is the cleanest example in the corpus of one action per script.

## Remote-jobs scraper: 622 social-media listings
`[B] · [D][G] · uploaded 2026-02-07 · how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md · q03 · stable`

Pass 1 called this a lead-scraping build. The captions show a job scraper. He searched a remote-jobs board for social media and got 622 listings over 21 pages. He goes into plan mode, pastes the URL, and asks Claude to build the workflow that logs them. q03 names the scripts `scrape_daily_remote_jobs.py` (Firecrawl), `generate_outreach.py` and `export_to_sheets.py`; no caption carries those names.

> what I've got is this list of remote jobs so I searched for social media there's 622 remote jobs and let's say I want to apply to all of these (how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md)

Warning line: q03 calls this "Lead Scraping & Enrichment" with lead criteria. The shown build collects jobs, not leads.

## Stop condition: "exactly 75" LinkedIn CEO profiles
`[S] · [D] · uploaded 2026-02-07 · how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md · q03 · stable`

In the same video he rewrites an open task into one with a count and a finish line. The open version is "search for LinkedIn profiles of CEOs at tech companies". The closed version names 75, the spreadsheet columns, and when to stop.

> I need exactly 75 LinkedIn profiles of CEOs at tech companies put them in a spreadsheet with their name company email their link to their profile and once you have 75 you're done (how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md)

Pass 1's wording, "Find exactly 75 verified LinkedIn leads and stop", is Gemini's paraphrase.

## Why the steps go in scripts: 90% per step, 59% after five
`[R] · [D] · uploaded 2026-02-07 · how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md · q03 · stable`

He gives the arithmetic for moving execution out of the model and into code.

> if each step is 90% accurate then you're down to 59% success after just five steps (how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md)

## Self-healing holds only while the agent is in the room
`[J] · [D] · uploaded 2026-03-12 · build-sell-with-claude-code-10-hour-course.md · q03 · stable`

He says self-healing is "partially true". It works while he runs the workflow himself inside Claude Code, because the agent can catch a break mid-run and edit its tools. q03 adds that a deployed run on Modal or Trigger.dev ships the workflow and tools without the agent, so nothing repairs itself there.

> that is partially true but only in a specific context at least right now cuz when you're actively working in a tool like Claude Code and you trigger a workflow yourself (build-sell-with-claude-code-10-hour-course.md)

His example of that local run is "go research these competitors and build me a report".

## Competitor intelligence report
`[B] · [M] · no transcript quote · q03 · stable`

[M] Gemini's version only; no caption carries this text.

q03 lists a third build: a `competitor_analysis` workflow that researches 5 competitor sites, pulls pricing, finds gaps, and lays out a PDF through scraping, synthesis and layout scripts. The only caption match is the one-line example above ("go research these competitors and build me a report"). Script names and the count of 5 are unverified.

## Where to look
- Folder layout, chef analogy, YouTube report: build-sell-with-claude-code-10-hour-course.md (2026-03-12)
- Jobs scraper, 75-profile stop, 59%: how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md (2026-02-07)
- First WAT naming: agentic-workflows-just-changed-ai-automation-forever-claude-code.md (2026-01-25)
