---
type: corpus
aliases: ["Core Knowledge — Simon Scrapes"]
corpus: simon-scrapes
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
---

# Core Knowledge — Simon Scrapes

**Layer 1 of the simon-scrapes corpus.** Distilled 2026-07-22 from 313 Pass-1 signals across 40 NotebookLM extractions of the @simonscrapes YouTube channel (Claude Code era, ~50 videos).

**How to read this document.** Every entry carries markers: `[P]` pattern, `[R]` rule, `[J]` judgment for knowledge type; `[M]` mediated (NotebookLM synthesis, the default), `[D]` direct quote, `[G]` grounded in a demonstrated outcome or external authority. Volatility: **(s)** = stable architectural principle, **(vb)** = version-bound feature behavior, pricing, or limits that can go stale. Claude Code changes monthly; treat every (vb) entry as "true when recorded, verify before relying on it."

**Standing warning (G1):** no settings key, env var, or install command in this corpus is trustworthy as spelled. They were shown on screen and reached us through phonetic transcripts. Verify against real docs at the moment of use.

Who Simon is, for context: runs The Agentic Academy (a Skool community teaching business owners to run their operations through Claude Code) and an automation agency. His audience is business operators, not developers. That lens explains the system's shape: business goals over code sessions, owned files over vendor features.

---

## 1. Context economy

The center of gravity. Nearly every other doctrine in this corpus justifies itself by pointing here.

- [P][D] "AI context is like milk: it's best served fresh and condensed." A community saying he adopts as the master framing. Everything the model sees competes for limited attention; stale content (failed attempts, old corrections, three tasks ago) actively degrades output. (s)
- [P][M] Context rot symptoms: slowness, drifting from prompts, quietly ignoring explicit instructions, declaring half-finished work done, losing the original objective, and self-bias: a rotted session asked to verify its own work favors its own results. (s)
- [R][M] Rot begins around 70–80% of the context window, while default autocompact waits until ~95% (one file says "85–100%"; the exact default is unresolved in-corpus). Set the autocompact override to ~75% so compression happens before quality degrades. (vb)
- [R][M] One task per conversation. `/clear` between unrelated tasks, always; `/compact` only to organize one long ongoing session. `/compact` accepts retention instructions ("keep the database schema") and needs them, because what it chooses to keep is otherwise unpredictable. (vb)
- [R][M] claude.md is the most expensive file in a project per word: it loads at session start and rides along with every message. Under 200 lines, ideally 60, some down to 20–30. One demonstrated strip from 3,847 tokens to 312 gave a 92% reduction in context overhead with zero measured quality loss. [G on the demo] (vb)
- [R][D] "Point, don't dump." The lean claude.md answers five questions (what is this project, how do I run things, what patterns do I follow, what's weird here, what's the workflow) and otherwise only points to detail files. Brand guides, client lists, example posts never live in it. (s)
- [J][M] The slimming test for any claude.md line: could Claude infer this by reading the codebase? If yes, cut it. (s)
- [R][M] Block junk reads twice over: a `.claudeignore` (node_modules, dist, build, coverage, lock files, vendor) as the advisory layer, and a settings permissions deny list as the hard layer; denied files can't be discovered or read even on direct request. Deny also `.env` and credential paths, and `git push` if publishing should stay human. (vb)
- [R][M] Hidden costs he itemizes: a bare "Hi" in a fresh session can burn ~37K tokens loading system prompt, skills, memory, and tool schemas; every connected MCP server adds a 10–20K-token schema at start even if unused. Disconnect unused servers; enable on-demand tool search. (vb)
- [R][M] Mermaid diagrams as compression: a few hundred tokens of diagram syntax can replace thousands of tokens of prose process description, and models parse structured diagrams more efficiently than paragraphs. Asserted, never demonstrated in-corpus (G7). (s)
- [R][M] HTML comments in claude.md are invisible to Claude, so they're a free channel for human-teammate notes. (vb)

**Delta vs this system:** the author's own CLAUDE.md is well over Simon's cap and mixes pointer content with full doctrine (the AI filter rules live inline, for instance). His counterargument would be: move doctrine to reference files and point. The 12:30 chain's context discipline (fresh session per instrument) already matches his one-task-per-conversation rule.

## 2. The Agentic OS filesystem

His architecture for running a business through Claude Code. Convergent with this repo's layout to a striking degree.

- [P][M] Root ("Life OS" / "Work OS") holds a master claude.md (global rules and workflows) and a master memory.md (short-term important decisions). A hidden .claude/ holds execution: commands/ for single-file slash commands, skills/ for multi-file processes. (s)
- [P][M] Brand Context folder, the static business brain: voice_profile.md (voice rules, banned phrases, best-writing samples by platform), visual identity as tokens.json or markdown (hex palettes, typography, logo, layout rules), positioning.md (market angle, what you stand for and against), ICP.md (who it's for, pains, failed alternatives), body_of_work.md (a one-line thesis plus 7–12 strong opinions, so generators have a point of view instead of generic filler). (s)
- [P][M] Agent Context folder, the live layer: user.md (working-style preferences), soul.md (agent identity and behavioral priorities), a memory/ subfolder of daily logs, and learnings.md, a long-term ledger where the agent's own mistakes get logged for self-correction. (s)
- [P][M] Workstations are department folders (Content, Finance, Ops, Marketing), each with local claude.md, local memory.md, and resources/. Work happens in workstations; outputs save to a separate Projects folder organized by skill, each project with a brief. A routing-map table in the global claude.md lists every workstation and grows a row per addition. (s)
- [R][M] Inheritance mechanics: starting a session in a subfolder walks up the tree combining every claude.md found; the file closest to the working directory wins conflicts. (vb)
- [P][M] The inheritance is used in two directions. Workstations inherit global brand context and add local formatting rules (the Content workstation's "no em dashes" rule never costs tokens in Finance). Client folders invert it: local files own identity (each client's own voice, ICP, tokens, memory), while global methodology — the skills — stays inherited. Directory switching is the context switch. (s)
- [R][D] "Things like brand context will not be inherited": identity files must live in the folder being worked in; only process flows down. (s)
- [J][M] Never build brand-context files by hand. Use starter skills that interview you (10–15 minutes of extraction questions), then feed 3–5 real writing samples for pattern extraction; visual identity gets reverse-engineered from a website URL or admired references into tokens. (s)
- [P][M] Because every skill reads the one shared Brand Context folder, a voice or audience shift is a single-file edit that propagates everywhere instantly. (s)

**Delta vs this system:** near 1:1. soul.md/user.md ≈ identity/SOUL.md and USER.md; daily logs + master memory ≈ memory/daily/ and curated/MEMORY.md; Projects+briefs ≈ scratchpads/. What's genuinely absent here: **learnings.md** (machine-error ledger — the memory/ shards capture Christian's feedback to the machine, not the machine's own logged mistakes) and the **routing-map table** (one glanceable surface listing every skill-area; CLAUDE.md describes directories in prose instead). Body-of-work has no equivalent and matters only if a content lane opens.

## 3. Skill doctrine

The deepest-covered territory in the corpus (20–25 videos).

- [P][M] Skill anatomy: a folder with one required file, skill.md, plus optional references/ (deep knowledge), scripts/ (executable code), assets/ (templates, fonts). skill.md = YAML frontmatter (name, description) on top, a table-of-contents step list below. (s)
- [R][M] Progressive disclosure, three tiers: (1) every installed skill's frontmatter is always loaded; Claude continuously scans descriptions against a ~15,000-character budget for the whole menu; (2) the skill.md body loads only on trigger; (3) references/scripts/assets load only during the step that needs them, then offload. (vb)
- [R][M] skill.md under 200 lines, no exceptions worth keeping. The corpus's cautionary tale [G]: a Reddit dev's 1,131-line CloudFlare skill plus an 850-line UI skill and a 900-line Next.js skill loaded 5,000–7,000 lines into context when related skills activated together — slowness, ignored instructions, and undebuggable failures (process and reference data mixed, so you can't tell which caused a bad output). (s)
- [R][M] Description framework, three parts: explicit triggers ("trigger when the user says repurpose"), what it does, and explicit anti-triggers ("does not trigger for blog posts"). Bad descriptions collapse activation: too vague never fires, too broad fires on everything; he cites activation rates as low as 20%. (s)
- [R][M] Names kebab-case; the process file exactly `skill.md`, case-sensitive. (vb)
- [J][M] Curate 20–30 highly specific skills, not hundreds. The hoarding trap (installing generic marketplace packs) bloats the always-loaded menu; cannibalization (three overlapping SEO skills) makes Claude guess and produces day-to-day inconsistency. (s)
- [J][D] Skill vs subagent, his verbatim framing: "A skill is what Claude knows how to do and a sub agent is who does the work." And the decision rule: "if you want to isolate it keep that context separate then I'd use a sub agent But if you need the context of the actual actions taking place then we'd use a skill." (s)
- [J][M] Subagent triggers: heavy context that would flood the main session, different tools/permissions/model needs, parallel runs, or fully self-contained work ("go away, analyze, come back with findings"). Worked example: carousel planning and copy run as skills in the main window (the orchestrator needs the intermediate context); image generation hands off to a subagent so style references and scripts stay out of main. (s)
- [P][M] Skill systems: small skills wired through an orchestrator skill so one skill's clean output feeds the next; the value lives in the chain, and shared blocks (transcription, brand voice) get maintained in one place and reused across pipelines. The two failure extremes: mega-skills, and fully isolated skills where you become the manual middleman. (s)
- [P][M] Skill evals (Skills 2.0): define a task plus 1–3 binary criteria, the system runs the skill in parallel (e.g. 5 runs), grades true/false per assertion, and reports pass rates, token cost, and execution time per run. A/B use: 5 runs with a reference file vs 5 without proves whether the file earns its tokens. Iterate — failure-specific feedback, auto-edit, re-run — until the skill reliably scores 9/10. (vb)
- [J][M] Never write skills from scratch; use a skill-creator meta-skill so conventions and disclosure structure come free. (s)

**Delta vs this system:** the skills/ registry already sits in his 20–30 band, and the symlink-registration gotcha here is stricter than anything he describes. The real absence is **evaluation** — nothing in this repo tests a skill before production; failures surface in live runs (the instrument-fleet postmortems exist precisely because of that). His eval loop is the single most importable practice in the corpus.

## 4. The memory stack

- [P][M] Three pillars, each with its own failure mode: Storage (when and how information gets saved), Injection (what loads into context at session start), Recall (how you recover something from months ago). Evaluate any memory system by asking all three. (s)
- [R][M] Native baseline, per him: automemory captures almost nothing (often under 10 notes after months); injection is just claude.md plus a nearly empty index; recall is exact-keyword over ~30 days of session files, and compaction permanently destroys detail. Two recall death modes: vocabulary drift and compacted conversations. (vb)
- [J][M] His decision tree, six questions: verbatim vs summaries (verbatim → Mem Palace or claude-mem; summaries → MemSearch); how much to inject (never everything — a capped frozen snapshot: user profile plus recent decisions); keyword vs semantic recall (semantic finds "Stripe" from "payment processing"); raw chunks vs synthesized answer (a reranker pass that writes a cited answer and admits misses); cross-tool needs (Open Brain's Postgres if you span Claude/ChatGPT/Cursor; skip if single-machine); operational memory vs content consumption (wiki patterns are for reading, not running a business). (s)
- [J][M] His ladder, by escalating need: native → frozen-snapshot injection → MemSearch, the "80/20" fix (local Milvus vector DB, hybrid semantic+keyword, a stop hook summarizing each turn via a fast model, top-3 matches silently injected into every prompt) → Mem Palace for verbatim recall (SQL + Chroma, loci-style wings/rooms/drawers hierarchy) → Open Brain for cross-tool (Postgres on Supabase, under $1/month, the most portable — you own the database and a future AI tool just connects). (vb)
- [R][M] If you run a custom memory system, turn native automemory OFF; otherwise your context forks into a background extraction call billed at full input prices. (vb)
- [J][M] Upgrade triggers he names: adopt semantic search only after keyword recall has actually failed you on a real query; adopt verbatim only if exact phrasing keeps mattering; adopt cross-tool only with a real multi-tool life. (s)

**Delta vs this system:** the stack here already implements his ladder in local form: SessionStart injection of Chronos + BOOTSTRAP is his frozen snapshot; corpus-rag (LanceDB hybrid BM25+vector, local embeddings) is his MemSearch analog, applied to corpora rather than session history. The one open question his frame raises: session-history recall here still leans on Chronos entries and grep, which is his "keyword recall" rung. His trigger applies — upgrade only when it demonstrably fails.

## 5. Restart, don't correct

One philosophy expressed at two scales: interactive sessions and autonomous loops.

- [P][M] The slot machine principle (phrase attributed to Anthropic's data science team, retold): when a pull goes bad, don't argue with the machine; reset and pull again. Their retold workflow: save state, let Claude run ~30 minutes, then a binary accept-or-restart. Engineering teams checkpoint constantly and expect a first-try success rate around one in three. (s; the practices are retellings)
- [P][M] Why correction fails: every fix forces the model to hold the broken code, the failed attempt, and the correction in one window. Corrections compound pollution; the session drifts further with each round. (s)
- [J][M] The adoption barrier is sunk cost. Invested session time makes restarting feel like waste, but a clean restart beats arguing with a drifted context on success rate. (s)
- [P][M] Mechanically: Claude Code snapshots the codebase before every file edit; /rewind lists every prompt in the session and rolls back code, conversation, or both to any checkpoint. Roll back to just before the mistake, add slightly more specific instructions, spin again. (vb)
- [P][M] The autonomous-scale version is loop engineering: with strong models, stop writing longer step-by-step prompts. Give the outcome, the context, and what done looks like — goal, verification criteria, definition of done, and let the model's own plan-execute-verify loop close the gap. "The bottleneck is no longer the model; it's your ability to close the gap between what you asked for and what needs to happen." (s)
- [P][M] Ralph loop, the blunt instrument: a while-loop refeeds the identical prompt every iteration; state carries through the edited files, not conversation history, so each iteration starts fresh and cheap. Breaks on exactly two conditions: the done state, or a max iteration count. Always set the max: a stuck bug otherwise loops and burns without bound. Fits batch tasks with verifiable output and tight acceptance criteria (overnight content runs, rule-based refactors); vague criteria make it confidently build the wrong thing. (s)

**Delta vs this system:** the chain instruments already run headless-with-retry, but interactive work here has no checkpoint habit. Worth noting rather than adopting wholesale: the /rewind-first reflex directly conflicts with the natural instinct to patch, which is his point.

## 6. The autonomy ladder

From in-session repetition to full remote operation. This cluster contains the corpus's one unresolved contradiction.

- [P][M] The rungs: /loop + /goal for in-session recurrence (a smaller model checks the goal each turn; loops expire after 3 days, die with the terminal, and never catch up on missed firings) → cloud Routines for scheduled work (runs on Anthropic's cloud with the laptop shut; hourly/daily/weekly/monthly; a "create it with Claude" flow interviews you, generates the prompt, and validates it with a historical test run) → VPS + tmux + Channels for interactive dispatch → multi-agent patterns for scale. (vb)
- [R][M] **Unresolved (G2):** one video says Routines draw from Pro/Max plan usage; another says scheduled cloud work bills via API with only interactive chat riding the subscription. No dates to order the claims. Check current docs before building anything cost-sensitive on Routines. (vb)
- [P][M] The remote recipe: a ~$15/month Ubuntu VPS, tmux keeping the session alive (this is the piece that fixes the 10-minute session-death rule on native Remote Control and Channels), and the official Telegram/Discord Channels plugin relaying messages and permission approvals to the phone. Interactive traffic rides the flat-rate subscription. Security floor: never run as root, lock down bot pairing after setup. (vb)
- [J][M] His comparison verdicts: native Remote Control and Channels alone fail the walk-away test (tied to the laptop's awake state); Clell works but bills per-token through the SDK; OpenClaw and Hermes are 24/7 but highly technical with real security exposure (hundreds of malicious packages found on marketplaces); Routines cover scheduled-only. VPS+tmux+Channels wins on his rubric (secure, phone-accessible, always-on, business-context-aware, survives disconnect). (vb)
- [P][G] The multi-agent pattern set (from Anthropic docs): classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament, loop-until-done. His demonstrated deep-research run: 26 agents, 13 minutes, 670K tokens — the scale argument for reserving these for genuinely long, complex jobs. (s patterns; vb costs)
- [J][M] Agent teams (shared task list, direct inter-agent communication) versus ordinary subagents (isolated, report-only): teams burn dramatically more tokens; reserve for builds where frontend, API, and testing agents must continuously coordinate. (vb)

**Delta vs this system:** the launchd/cron fleet plus the 12:30 chain already occupies the "scheduled" rung locally, with a delivery contract Simon's stack lacks. His VPS rung is the one this system deliberately traded away when engine went local-primary; the trade was availability for control, and his own portability doctrine (section 9) argues for exactly that trade.

## 7. Model economics

- [J][G] Judge cost-per-finished-task, not cost-per-token. His demonstrated comparison: a pricing page at $0.25 on Sonnet plus two hours of human rework, versus $48 on the premium model with merge-ready output. (vb)
- [J][M] Three sanctioned uses of the premium tier: plan on it and build on Sonnet (plan.md as the handoff; "opus plan" preset automates the drop); a code-review subagent instructed to stay concise and never rewrite (kills output-token cost); loop engineering for long async tasks with clear success criteria. Casual chat on the premium tier is the named waste: ~$2–3 per half hour versus ~$0.15. (vb)
- [R][M] /effort at max is a trap per his testing: 20 rounds showed no correctness gain, only thousands of extra self-verification tokens. Default for routine, high for hard problems, almost never max. (vb)
- [R][M] Subagents inherit the parent's model: five parallel researchers on the premium tier all bill premium. Pin background workers to Haiku via the settings key (spelling unverified, G1). (vb)
- [R][M] Set Sonnet as the session default; he reports teams halving bills with no quality loss. Set a hard monthly spend cap so a runaway loop can't surprise you. (vb / s)

## 8. Production lines

How the architecture, skills, and context doctrine compose into shipping pipelines.

- [P][M] Universal shape: brand context as the single source of truth → an orchestrator skill chaining focused workers → heavy or expensive steps isolated in subagents → a human review gate placed *before* the expensive step → manual polish tooling for the last 5% → API publishing. Nothing auto-posts; drafts land locally and a human selects. (s)
- [P][M] Content repurposing engine: one source (URL, transcript, blog, podcast notes) fans out to platform drafts (LinkedIn, X, newsletter) in /drafts/date/platform/; chain = transcript extraction → trending research (Reddit/X angles) → repurposer → humanizer that strips AI tells (robotic transitions, banned words, em dashes). Platform formatting files load only while drafting that platform, then offload. (s)
- [P][M] The 18-skill social creator: idea in, brand-consistent carousel out. Notable moves: a designer subagent acts as art director (audits visual inventory, picks a narrative arc, writes a slide-by-slide plan); the review gate approves plan and copy before any image render spend; image generation runs fully isolated; flat outputs import into Canva Magic Layers, which converts them to editable layers so typo fixes are manual instead of re-prompted; Zernio API schedules the post. Style templates come from 3–5 admired references with their content stripped and your identity applied. Only ~8 of the 18 skills are named in-corpus (G6). (s)
- [P][M] The finance builds prove the same shape works off-content: a Friday routine reconciles receipts from email into accounting software via a custom FreeAgent MCP server; month-end pulls bank transactions into a spreadsheet, replicates the human formatting steps, and produces a P&L; a monthly "subscription catcher" diffs recurring bills and flags increases, duplicates, and unused subscriptions. (s)
- [P][M] The newsletter digest scores inbox stories numerically against positioning and ICP with an explicit bar (his demo: one item cleared at 16/22.5, the rest filtered), then chains into drafting skills — and self-optimizes by suggesting known senders be added to a senders.yaml so future runs skip the whole-inbox search. (s)
- [P][M] Visual consistency comes from codified tokens (tokens.json + design.md), not prompting; Skill UI reverse-engineers a live site's design system into a skill, and the Taste skill bans the recognizable AI tells (Inter, Roboto, generic gradients, teal, stock layouts) and applies deliberate imperfection as the final polish. (s)

**Delta vs this system:** the daily-news-digest skill already implements the scored-curation pattern (verify, dedup, rank, post). The humanizer role is the ai-filter skill. The importable idea is the senders.yaml-style self-optimization: instruments here log outcomes but don't yet feed narrowing hints back into their own next run.

## 9. Portability doctrine

- [J][D] Avoid features that only run "inside Anthropic's box" (managed agents, hosted environments): convenient now, but you inherit their pricing and ecosystem, and migration means rebuilding from scratch. (s)
- [J][M] His observed drift: Claude Code's features increasingly serve enterprise developers (he attributes 80% of Anthropic's revenue to that base) while the marketing says "no infrastructure needed", so business owners keep hitting containers, credential vaults, and env vars five minutes into "simple" features. (vb)
- [P][M] The four-step framework before adopting anything: (1) write down your actual system requirements; (2) strike everything a provider is ~95% likely to ship natively soon; (3) spend build effort only on requirements bespoke to your business; (4) where the model itself is weak, build an independent layer you own. His bespoke gaps turned out to be context management and codified processes; his owned layer is a local file-based memory system. (s)
- [P][M] His nine requirements (useful as a benchmark checklist): know who I am and how I work; know my business, clients, projects; recall sessions, decisions, learning; repeatable processes with consistent output; scheduled multi-step execution; planning matched to project size; per-client and per-person context separation; outputs in one predictable place; access from anywhere without a running computer. (s)
- [J][M] The n8n split as portability applied to tooling: n8n's license legally confines it to internal use [G: the license itself], so the customer-facing layer must be owned code; his stack keeps automation logic in n8n (visual execution history means non-technical people can debug it) and has Claude Code build the owned packaging — auth, dashboards, billing. The agency math: a $2K workflow becomes a $10K+ product when it ships with a branded front end and client logins. (s / vb on prices)

**Delta vs this system:** this repo is already his doctrine in practice: local-primary engine, file-based memory, owned instruments layered over model weaknesses. Checking his nine requirements against the running system: eight are met locally; "access from anywhere without a running computer" is the one deliberately unmet, and his own framework says strike requirements the vendor will ship (his step-2 example crossed off exactly that one).

---

## Cross-references

- Full signal inventory with per-file detail: `pass-1-extraction.md`
- Corroboration, contradictions, and the delta map in full: `pass-2-reconciliation.md`
- Tool profiles and build walkthroughs for retrieval: `retrieval-index/`
- What's missing and how to fill it: `gap-register.md`
