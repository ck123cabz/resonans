---
type: index
aliases: ["Nate Herk retrieval index"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Nate Herk retrieval index
---

# Nate Herk retrieval index

Layer 2 of the Nate Herk corpus, written 2026-09-29 from `pass-2-reconciliation.md`, the four Pass 2 check files, `pass-1-extraction.md`, the q01–q51 answers and grep over the 299 transcripts. There are 45 files in four classes: 13 build, 9 script, 8 tool and 15 framework.

Each `##` section opens with a metadata line giving the type tag, provenance, upload date, source transcript file, the q## that raised it, and whether it is stable or version-bound. Caption quotes sit in blockquotes. A prompt that exists only in Gemini's answer sits in a code fence under a `[M]` line. Guest material sits under `[D:guest:<name>]` headings. Every value follows the Pass 2 corrections ledger, and Gemini's wrong figures appear only as labelled warnings.

## Builds

| File | Class | What it holds |
|---|---|---|
| `build-client-pack-saas.md` | build | Client Pack SaaS (2026-08-10): idea research, corrected stack, the 4-cent and 9-cent calls, 85 checks, $39/$390, the $29–$49 band. Also Agent Report Card: 16 tests, $499 × 168. |
| `build-appointment-setting-agent.md` | build | The $5,500 build told twice: $41,600 at 13% with $400 flat, and $38,400 at 15% with $550. Both kept open, with the arithmetic. |
| `build-invoice-processing-and-roi-cases.md` | build | Invoice processing ($78,000), construction errors at $12,000 a month in hard dollars, onboarding at $3,000 with a 5-month payback, and the $12,000 support case. |
| `build-early-agent-builds-ledger.md` | build | His priced builds from $1,200 to $12,000, the $6,000 live sales call, $23,650 against the "$23,000" title, and $240k in 6 months. |
| `build-outreach-and-lead-gen-agents.md` | build | The $1,650 outreach agent (about 2.9x), the Claude Code + Clay pipeline, and the 150,000-email discount incident. |
| `build-video-editing-pipelines.md` | build | The Remotion-to-Hyperframes switch, HeyGen avatar chunking, the Seedance scroll site and Higgsfield costs. |
| `build-grok-bot-org-chart.md` | build | The Klouse chief-of-staff prompt, the specialist bots, memory split, routines, the $5,000 setup project, and the Cursor Ultra → $30 price change. |
| `build-hermes-assistant.md` | build | Hermes: 5 pillars, VPS host, Codex login, Anthropic's consumer-login ban, nightly backup, least privilege, and the OpenClaw → Hermes dates. |
| `build-wat-workflows.md` | build | WAT builds: YouTube weekly report with 7 tools, the 622-job scraper, the "exactly 75" stop condition, and 90% per step down to 59%. |
| `build-agent-teams-and-subagents.md` | build | The Neuroflow agent team, a 2–5 teammate cap, max turns, storm-research, 41 Haiku scorers, four fleet models, and five guardrails. |
| `build-n8n-agents-and-migration.md` | build | n8n RAG, memory, reranker, inbox classifier, the orchestrator prompt, n8n verdicts, and the 2026-01-16 n8n-to-Claude Code migration. |
| `build-aios-second-brain.md` | build | Herkbrain LLM wiki, hot.md, the executive assistant role line, his ops skills, the Up AI account, and the channel-audit numbers. |
| `build-student-and-guest-cases.md` | build | One heading per person: student Christian, Sabrina, Brett, Azim, Jerome, CalAI, Devin Karns (guest), and unsupported or vendor cases. |

## Scripts

| File | Class | What it holds |
|---|---|---|
| `script-grill-me-and-95-confidence.md` | script | Pocock's grill-me as Nate reads it, his checkpoint upgrade, Sabrina's 95% prompt, the claude.md 95% rule, and the PRD prompt. |
| `script-claude-md-constitution.md` | script | claude.md as an "onboarding document": line limits by date, the Applied Learning rule, style rules, agents.md mirroring, and the q39 template marked [M]. |
| `script-discovery-call.md` | script | The call in order: opener, pokes, proxy questions, constraint questions, why this/now/me, the nephew and 2 am reply, and the "just tell me a price" reply. |
| `script-proposal-and-tiers.md` | script | Three client paragraphs, 10/25/50 tiers, the job-marketplace assumption line, payment terms by date, cutting scope instead of price, and IP ownership. |
| `script-10x-roi-pricing.md` | script | The $12,000 → $1,200 walkthrough verbatim, annualizing, the 10–20% anchor, 10x and his 7.5x admission, maintenance, margin, and the hourly on-ramp. |
| `script-cold-email.md` | script | Sav's emails, infrastructure, reply-rate tiers and funnel under `[D:guest:Sav]`, then Nate's own lines and the Clay output email. |
| `script-warm-outreach-trojan-horse-upwork.md` | script | The 7-day first-client plan, the Trojan Horse 20% pitch, the AI partner positioning, Upwork keywords, and his dated change of view on Upwork. |
| `script-agent-and-skill-prompts.md` | script | System-prompt shapes, which reactive rules are real, prompt vs tool permissions, skill prompts, session handoff, and the DRY and Codex mirror prompts. |
| `script-roast-council.md` | script | The six council seats verbatim, the judge's green light, reshape or kill verdict plus a 48-hour test, and ELEPHANT's 88% (third-party). |

## Tools

| File | Class | What it holds |
|---|---|---|
| `tool-harnesses.md` | tool | Claude Code, Codex, Antigravity, DeepSeek, Grok Bot, Hermes, OpenClaw and Cursor, each with price, limits and verdict. Also the Clawdbot scorecard and the owl vs Rottweiler labels. |
| `tool-harness-head-to-heads.md` | tool | Every numbered harness and model test, dated. The question of which harness uses fewer tokens stays open (B-C03). |
| `tool-models-and-prices.md` | tool | Anthropic, OpenAI, GLM, Fugu, Jev and Ollama: prices, which model for which job, release dates, and vendor claims labelled as such. |
| `tool-claude-code-features-and-tokens.md` | tool | Commands and modes, cache TTL, the reset rule over time (60% → 120k → 250k–300k), Cole's dumb-zone numbers (guest), MCP overhead, and the opusplan apology. |
| `tool-hosting-and-scheduling.md` | tool | Cloud Routines limits, Desktop tasks, Trigger.dev, Modal, Hostinger, Vercel and Supabase. |
| `tool-integrations-mcp-cli-skills.md` | tool | CLI > API > skills > MCP, the 35x benchmark, Printing Press, GWS CLI, n8n MCP, Composio, AgentMail, and third-party skills. |
| `tool-video-image-design.md` | tool | Hyperframes, HeyGen, ElevenLabs, Higgsfield, Seedance, Kling, key.ai, GPT Image 2 and Claude Design. |
| `tool-lead-gen.md` | tool | Clay, Instantly, Apify, Firecrawl, list hygiene, Vapi, Tavily, and Upwork's report figures (third-party). |

## Frameworks

| File | Class | Speaker | What it holds |
|---|---|---|---|
| `framework-wat.md` | framework | Nate | Workflows, Agent, Tools; the chef analogy; 90%^5; and a warning on Gemini's invented name for it. |
| `framework-aios-and-4-cs.md` | framework | Nate | AIOS ("AIS OS") and the 4 C's, built in order 1 to 4. |
| `framework-ai-service-ladder.md` | framework | Nate | Rungs 0–3 with the 2026-05-22 and 2026-08-11 prices, the Grok Bots version, and "earn each rung". |
| `framework-price.md` | framework | Nate | Prepare, Research, Identify ROI, Communicate, Expand; the 10% vs 10–20% anchor by date; and the $38,400 case. |
| `framework-share.md` | framework | Nate | Show, Hook, Attract, Recommend, Expand, the teaching stage of the 2025-10-03 start-over video. |
| `framework-build.md` | framework | Nate | Block by block, Understand, Install and imitate, Land, Document and duplicate: the freelancing stage. |
| `framework-scan.md` | framework | Nate | Study, Calculate, Architect, Narrate; the $5,000 audit then $20k–$100k. Devin's refund case sits apart under a guest heading. |
| `framework-grow.md` | framework | Nate | Get developers, Retain authority, Onboard sales, Win with brand. Devin's escalator sits under a guest heading. |
| `framework-lrp.md` | framework | Nate | Listen, Repeat, Poke; the 70/30 talk ratio, silence after the question, and the pivot. |
| `framework-4-rs.md` | framework | Nate | Result, Roadmap, Risk Reversal, Review (2025-11-17). |
| `framework-golden-ratio-60-30-10.md` | framework | Nate | 60% traditional, 30% AI-assisted, 10% human. 90/10 is not his. |
| `framework-5-step-agent-formula.md` | framework | Nate | His "five-step AI agent playbook" (2025-05-05), all steps quoted, with the five process-map elements. |
| `framework-6-step-skill-method-and-bike-method.md` | framework | Nate (Anthropic for skill types) | The six skill steps, the Codex variant list, the bike method, and bike-to-motorcycle. |
| `framework-other-named-methods.md` | framework | Nate | 3 M's, 3 Ps, 6 Ps, four blanks, doctor not pharmacist, default shift, vending vs slot, 10-minute rule, walk it down, integration order, and a list of names Gemini invented. |
| `framework-borrowed-and-guest.md` | framework | Various | Karpathy, Pocock, Stark, Devin Karns (guest), STORM, Anthropic, Cherny (speaker open), Nate B. Jones (guest), reason-act-observe, Superpowers TDD. |
