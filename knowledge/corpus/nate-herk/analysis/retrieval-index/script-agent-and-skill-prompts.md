---
type: script
aliases: ["Agent system prompts and skill prompts"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Agent system prompts and skill prompts
speaker: Nate Herk
provenance: D
sources: [q04, q05, q08, q09, q16, q39, q43]
videos: [build-sell-n8n-ai-agents-8-hour-course-no-code.md, your-ai-agent-prompts-are-wrong-here-s-the-fix.md, 3-ai-workflows-step-by-step-beginner-s-guide-to-n8n.md, 5000-hours-of-building-ai-in-just-17-minutes.md, build-sell-with-codex-5-hour-course.md, anthropic-engineer-explains-what-to-build-instead-of-ai-agents.md, master-95-of-claude-code-skills-in-28-minutes.md, how-to-never-hit-your-claude-session-limit-again.md, build-sell-ai-saas-products-2-hour-course.md]
---

# Agent system prompts and skill prompts

Prompt text Nate uses inside agents and skills, from the n8n era (2025-02) to the Codex course (2026-09-21). Each section says whether the words come from a caption or only from Gemini. The claude.md template is in `script-claude-md-constitution.md`; planning prompts are in `script-grill-me-and-95-confidence.md`.

## n8n system prompt sections
`[S] · [M] with one [D] line · uploaded 2025-05-23 · build-sell-n8n-ai-agents-8-hour-course-no-code.md · q08, q09 · stable`

[M] Gemini's version only; no caption carries this text.

q09's four-part template:

```
OVERVIEW: You are [Role] for [Company]. Your job is [Goal].
INSTRUCTIONS: Step-by-step guidelines on what output to create.
TOOLS:
- Tool Name 1: what the tool does and WHEN to use it.
RULES & CONSTRAINTS:
- Negative constraints.
- Sign-off instructions.
```

q08 gives a different four-part list. This contradiction (A-C05) stays open: the captions never list the sections in order, and the structure was likely on screen. What he says aloud:

> this is like your overview and then if we need to get more granular we can give it different sections like output or rules or anything like that (build-sell-n8n-ai-agents-8-hour-course-no-code.md)

## Five-part structure (overview, objective, guidelines, tools, output)
`[S] · [M] · no transcript quote · q39 · stable`

[M] Gemini's version only; no caption carries this text.

```
# OVERVIEW & ROLE
# OBJECTIVE (take [input] into [deliverable])
# GUIDELINES & HARD CONSTRAINTS (no preambles like "Sure, here is your report"; "Do not add m-dashes or emojis")
# TOOLS AVAILABLE (tool plus when to use it)
# OUTPUT FORMAT (strict JSON schema or markdown)
```

q39 says he uses this across n8n, scripts and agent nodes. Treat it as Gemini's merge of several videos.

## Reactive prompting: add one line per observed failure
`[J] · [D] · uploaded 2025-02-26 · your-ai-agent-prompts-are-wrong-here-s-the-fix.md · q09, q48 · stable`

Start with a small prompt, run it, read the agent logs, and add a rule for the exact failure. He stopped using his own system-prompt generator for this reason.

> prompting needs to be done reactively I see way too many people doing this proactively throwing in a huge system message and then just testing things out (your-ai-agent-prompts-are-wrong-here-s-the-fix.md)

## Reactive rule examples: which are real
`[S] · mixed · q08, q09 · stable`

- "You must first use `get_emails` to get the message ID before calling `add_label`". [M] Not in captions; likely on-screen text.
- "When getting contacts, always check the email column first". [M] Not in captions.
- "Never issue refunds over $50 without human approval". [M] Not in captions.
- "You are a customer support agent designed to assist users with billing inquiries". [M] Not in captions.
- "Always sign off as Mr. Helpful". [D], below.
- "Never send emails, only write drafts". [D], below, as his example of a guard that fails.

## Sign-off line: Mr Helpful from Tech Haven Solutions
`[S] · [D] · uploaded 2025-04-07 · 3-ai-workflows-step-by-step-beginner-s-guide-to-n8n.md · q09 · stable`

> for the instructions I said your output should be friendly and use emojis and always sign off as Mr helpful from Tech Haven Solutions (3-ai-workflows-step-by-step-beginner-s-guide-to-n8n.md)

## "Never send emails, only write drafts" is a prompt guard that fails
`[J] · [D] · uploaded 2026-08-04 · 5000-hours-of-building-ai-in-just-17-minutes.md · q09, q33, q48 · stable`

Pass 1 and q09 list this as a constraint to copy. He uses it as the example of what does not work. His own team's agent read a to-do item, wrote a discount code and sent it to "about 150,000 people" on their list. A later video says "almost 200,000"; the count stays open.

> there's a huge difference between a prompt permissioning layer and a tool permissioning layer Because you can tell your agent never send emails only write drafts but if it still has a send email tool then it can still send emails (5000-hours-of-building-ai-in-just-17-minutes.md)

The fix he gives in the same video: "fix the access not the prompt". Remove the send tool or scope the key. The slogan "prompts are suggestions, tools are walls" has zero caption hits; his wording is "a rule that lives in the prompt is just a suggestion but a rule that lives in the tools is an actual restriction".

## Build it first, then "turn that into a skill"
`[S] · [D] · uploaded 2026-09-21 · build-sell-with-codex-5-hour-course.md · q05, q16 · stable`

Run the task by hand until the output is right, then ask the agent to make it a skill. That way the skill knows the target output. The pass-1 wording "Look back at what we just did and reverse engineer this process into a skill" is Gemini's; his words:

> it's so much easier to run the process get the output and say "Okay let's turn that into a skill." Rather than saying "Hey build me a skill for building a YouTube dashboard." (build-sell-with-codex-5-hour-course.md)

## Skill description example: LinkedIn carousels
`[S] · [D] · uploaded 2026-09-13 · anthropic-engineer-explains-what-to-build-instead-of-ai-agents.md · q04 · stable`

A description states what the skill does and when to fire, in the words a real person would type. Two overlapping descriptions ("help with content", "create marketing assets") leave Claude guessing. Verbatim:

> This skill creates LinkedIn carousels from a topic from a transcript or an outline Use this when the user asks for a carousel carousel slides or a LinkedIn document post (anthropic-engineer-explains-what-to-build-instead-of-ai-agents.md)

```
This skill creates LinkedIn carousels from a topic, from a transcript, or an outline. Use this when the user asks for a carousel, carousel slides, or a LinkedIn document post.
```

## skill-builder
`[S] · [D] for existence; [M] for contents · uploaded 2026-02-27 · master-95-of-claude-code-skills-in-28-minutes.md · q04 · stable`

He built a skill that builds skills and gives it away in the free community. q04 says it interviews the user through the six steps, writes `skill.md` with front matter, reference files and script folders, registers the skill in `claude.md`, and ships a pre-scraped `reference.md` of Anthropic's skill docs. Those contents are [M]. Anthropic's own `skill-creator` plugin sits alongside it.

> i have a skill that I built out called skilluer and this one I'll be giving away for free (master-95-of-claude-code-skills-in-28-minutes.md)

## Session handoff instead of /compact
`[S] · [D] · uploaded 2026-04-20; 2026-08-10 · how-to-never-hit-your-claude-session-limit-again.md; build-sell-ai-saas-products-2-hour-course.md · q02, q06, q39 · version-bound`

On 1M-token Opus he stops around 120,000 tokens, about 12%, asks for a summary, runs `/clear`, and pastes it back. He says he no longer uses `/compact`.

> if I cross around 120,000 tokens so about 12% then I will just say to Claude "Hey give me a full summary of everything that we've done and the current status of what we're about to do next." (how-to-never-hit-your-claude-session-limit-again.md)

```
Hey, give me a full summary of everything that we've done and the current status of what we're about to do next.
```

By the SaaS course he runs it as a `session handoff` skill that lists what was done and the files that matter.

> I'm going to use a skill called session handoff which is basically just going to give us a summary of what's been done files that are important so that I can clear the session and paste it back in (build-sell-ai-saas-products-2-hour-course.md)

q39's section list (Work Completed, Key Architectural Decisions, Open Questions, Immediate Next Step, saved to `./scratch/handoff.md`) and q02's `/tmp/handoff.md` are [M].

## DRY: save the proven script inside the skill
`[S] · [D] for the idea; [M] for the prompt · uploaded 2026-09-13 · anthropic-engineer-explains-what-to-build-instead-of-ai-agents.md · q43 · stable`

He relays an Anthropic example. Claude rewrote presentation-styling code each run with uneven results, until it saved the script inside the skill as "a tool for its future self".

> they had Claude save that script inside the skill as in their own words a tool for its future self So now the next time it needs to style a presentation it can just run the version that already was proven to work (anthropic-engineer-explains-what-to-build-instead-of-ai-agents.md)

[M] Gemini's version only; no caption carries this text:

```
Save the script you just used inside the skill's /scripts/ folder. Update skill.md... Then rerun the skill and verify.
```

## Codex mirror prompt: claude.md into agents.md
`[S] · [M] · uploaded 2026-09-21 · build-sell-with-codex-5-hour-course.md · q16 · stable`

[M] Gemini's version only; no caption carries this text.

```
Analyze this project and make it Codex-ready by mirroring claude.md into agents.md.
```

q16 says he keeps identical `claude.md` and `agents.md` at the repo root so either harness can run the project. The Codex course does teach `agents.md` as "concept number two"; the exact prompt line is unverified.
