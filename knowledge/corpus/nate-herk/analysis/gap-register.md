---
type: corpus
aliases: ["Gap Register — Nate Herk"]
corpus: nate-herk
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
---

# Gap Register — Nate Herk

Pass 3, Layer 3, written 2026-09-29. It consolidates the 30 `[A]` markers in `pass-1-extraction.md`, the 11 open contradictions and the gap table in `pass-2-reconciliation.md` (sections 4 and 6), and every UNSUPPORTED and UNRESOLVED verdict in `scratchpads/nate-herk-pass2/verify-a.md`, `verify-b.md`, `verify-c.md` and `round2.md`. Update an entry when its gap is filled; ids are stable and never reused.

Every filename below sits in `knowledge/corpus/nate-herk/video/` unless a path is given. Dates are YouTube upload dates from `sources.tsv`.

---

## Standing warnings

Seven rules the `nate-herk` lens obeys on every answer, before any entry below applies.

**W1 · Gemini credits guest speech to Nate.** Pass 2 found 7 guests across 7 interview files and tagged 28 rows `[D:guest]` (20 in verify-b, 1 in verify-c, 7 in round2). Cole Medin's per-model dumb-zone numbers (X-05), Devin Karns's mid-market advice (C11) and Nate B. Jones's "last mile" (R47-10) all reached Pass 1 as Nate's. Captions carry no speaker labels, so a line from an interview file counts as Nate's only when Pass 2 tagged it `[D]` without a guest tag.

**W2 · About a third of checked Gemini claims were wrong.** Of 526 rows checked, 125 were CORRECTED and 41 UNSUPPORTED, 166 in all, or 32%. An `[M]` claim that Pass 2 never checked gets a transcript grep before the lens states it as Nate's, and a phrase Gemini put in quotation marks is never quoted as his words (provenance Rule 1).

**W3 · Prices, limits and model names are version-bound.** Titles name Opus 4.7 (2026-04-16), Opus 4.8 (2026-05-28), Fable 5 (2026-06-12), GPT-5.6 Sol (2026-07-09), Fable 5.1 (2026-09-01), GPT-6 Astra (2026-09-03) and Opus 5.5 (2026-09-23). `/loop` went from 3 days to "like seven days" between 2026-04-27 and 2026-06-03, and Grok Bot access went from Cursor Ultra to $30 between 2026-08-12 and 2026-08-31. The lens states the upload date with every price, limit or model name it cites.

**W4 · The $500k cold-email student is Sav.** Captions spell him "Sav", "Savom" and "Savon"; "Sonam" appears only in the q26 question text (C10, B-C10). His volumes, reply rates and pipeline are `[D:guest:Sav]`, never Nate's agency numbers (how-a-college-student-made-500k-with-cold-email-exact-framework.md, 2026-02-14).

**W5 · Audience counts drift and carry no date of their own.** Counts in the corpus run from 150,000 (the discount-email list, B061) to 450,000 (the free community on 2026-09-23). The free community reads 230,000 on 2026-01-25 and "almost half a million" on 2026-09-09, and AIS Plus runs from "over 200" to "over 3,500". The only date a count has is its video's upload date, so the lens cites a count with that date or leaves it out.

**W6 · Course dates misdate positions.** build-sell-with-claude-code-10-hour-course.md (2026-03-12), claude-code-for-non-coders-6-hour-course.md (2026-07-11) and build-sell-with-codex-5-hour-course.md (2026-09-21) re-air older videos word for word. The non-coders course holds both "compact at around 60% capacity" and the `opusplan` apology, so the lens dates a position by the standalone video wherever one exists (G4).

**W7 · Captions spell by ear.** Claude is "cloud" or "claw", n8n is "NADN" or "naden", Anthropic is "Enthropic", Codex is "codeex" and Sol is "Soul". A caption spelling of a product or person wins over Gemini's only when a video title or description confirms it (G18).

---

## Index

| Id | Gap | Fill method | Priority |
|---|---|---|---|
| G1 | Consumer wiring: the lens reads this file | none, wiring | High |
| G2 | Speaker tags missing in 7 interview files | video audio at caption timestamps; manifest marking | High |
| G3 | About 151 signals never checked one by one | transcript grep | High |
| G4 | 3 course files embed older videos | transcript grep, course against standalone | High |
| G5 | 49 UNSUPPORTED claims held in quarantine | none for most; video frames for 6 | High |
| G6 | 52 channel videos outside the notebook | yt-dlp on the 52, then a second notebook | Medium |
| G7 | 28 blank upload dates and undated events | dates: yt-dlp `--print upload_date`, sources.tsv join | Medium |
| G8 | On-screen content lost from captions | video frames; description links | Medium |
| G9 | Unnamed third-party numbers | transcript grep, then web search | Medium |
| G10 | No Nate-voiced agency metrics | targeted NotebookLM question; transcript grep; the 52 | Medium |
| G11 | Integration setup steps missing | targeted NotebookLM question per tool | Medium |
| G12 | Evaluation method thin | targeted NotebookLM question; transcript grep | Medium |
| G13 | No proposal, contract or SOW template | targeted NotebookLM question; description links | Low |
| G14 | Demand and price for his own products | targeted NotebookLM question; transcript grep | Low |
| G15 | Vendor prices never spoken | dated vendor pages at time of use | Low |
| G16 | Paid-course content behind the paywall | none short of course access | Low |
| G17 | S2ME69hra-k returned no content | yt-dlp | Low |
| G18 | Unsettled spellings | yt-dlp `--print description` | Low |
| G19 | Caption-garbled video prices | video frames | Low |
| G20 | The ~15 core n8n nodes never listed | targeted NotebookLM question; the 52 | Low |
| G21 | Karpathy's own statement of the 3 layers | web | Low |
| G22 | Whether `.claudeignore` exists | Claude Code docs | Low |
| G23 | Grok Bot owner | web, product page | Low |
| G24 | Open: A-C05 system-prompt sections | video frames | Medium |
| G25 | Open: B-C01 base and R42-15, the $5,500 build | dates | Low |
| G26 | Open: B-C03 which harness is token-lean | dates | Low |
| G27 | Open: B-C13 Max plan quota | dated vendor docs | Low |
| G28 | Open: X-12 Hostinger VPS price | video frames; vendor page | Low |
| G29 | Open: R44-12 Nate or Jonathan Stark | web; targeted NotebookLM question | Low |
| G30 | Open: R49-19 AIS Plus "over 200" vs 2,000 | dates | Low |
| G31 | Open: discount email to 150,000 vs 200,000 | none, his own drift | Low |
| G32 | Open: I-5 who speaks the Boris Cherny line | video audio at timestamp | High |
| G33 | Open: I-6 whose voice reads the Karpathy reel | video audio | Low |

---

## Consumer wiring

### G1 · The lens file reads this register
`skills/lens/lenses/nate-herk.md` names this file on line 8 (`gap_register: knowledge/corpus/nate-herk/analysis/gap-register.md`); the lens file is being written in this same session, 2026-09-29. The lens loads W1–W7 as refusal rules, answers "the corpus has no transcript for that" for any question about G6's pre-2025-02-22 window, and never quotes a G5 row as Nate's. When a gap is filled, the fix goes into this entry and into `core-knowledge.md`, and the lens picks it up on its next run because it reads this file by path and holds no copy.
- **Priority:** High. A lens that skips this file reads Pass 1 claims at face value, and 32% of checked ones were wrong (W2).

---

## High priority

### G2 · Speaker tags missing in interview files
Seven files mix Nate with a guest, and the captions never say who is talking: Sav (2026-02-14), Christian the Arizona student (2026-02-04), Devin Karns (2026-05-25), Cole Medin (2026-06-18), Nate B. Jones (2026-07-20), Mark Kashef (2026-09-11) and an Anthropic staff member (2026-08-12). B086's "10 meetings in 30 days" offer is tagged `[D:guest?]` because grep cannot say whether Sav or Nate says it. The two open speaker disputes are G32 and G33.
- **Why it matters to the lens:** `[D]` against `[D:guest]` decides what enters Nate's Layer 1, and 2 Pass 1 signals (X-05, C11) were guest speech credited to him.
- **Fill by:** listening to the YouTube video at the caption timestamp for each disputed line, and marking the 7 files as interviews in `manifest.json` so a grep hit there is never read as Nate by default.

### G3 · About 151 signals never checked one by one
About 143 of the 475 Pass 1 signals were never checked against captions, including every numberless `[F]`, `[J]`, `[S]` and `[T]` in part A (verify-a's own note). Round 2 left 8 of its 194 signals unchecked (2 in q42–q44, 4 in q45–q48, 2 in q49–q51). All of them stay `[M]`.
- **Why it matters to the lens:** at the 32% error rate of W2, roughly 48 of the 151 are wrong in some detail.
- **Fill by:** transcript grep over the 299 files before any of them enters Layer 1 as Nate's rule or framework.

### G4 · Course files embed older videos
build-sell-with-claude-code-10-hour-course.md (2026-03-12), claude-code-for-non-coders-6-hour-course.md (2026-07-11) and build-sell-with-codex-5-hour-course.md (2026-09-21) repeat earlier videos word for word. No map says which standalone videos each course contains.
- **Why it matters to the lens:** a course date misdates a position, and one origin gets counted as two confirmations.
- **Fill by:** transcript grep, matching long word runs from each course against the standalone transcripts, then recording the contained videos per course.

### G5 · UNSUPPORTED claims in quarantine
Pass 2 counted 41 UNSUPPORTED verdicts, plus UNSUPPORTED clauses inside rows marked CONFIRMED or CORRECTED; the 49 lines below hold both, and no caption sentence backs any of them. Most are Gemini additions and have nothing to fill; 6 were probably on screen (marked "frames"). The lens never states any of these as Nate's.

| Row | Claim Gemini gave | What the captions hold | Fill |
|---|---|---|---|
| C12 (verify-a) | n8n breaks at 30+ steps, or at hundreds of nodes | Neither threshold, nor "spaghetti" | none |
| S06 | `context/MI.md` / `wiki/entities/` routing line | Not spoken; `MI.md` may be `me.md` read off screen | frames |
| S15 | "use `get_emails` before calling `add_label`" | Not spoken | frames |
| S16 | email column, refunds over $50, billing-inquiries role line | Not spoken | frames |
| R02 | 1,000-line file × 30 turns | The rule "keep it under 200 lines" only | none |
| R08 | Local docs 10x faster than web search | The only "10 times faster" is about agentic workflows | none |
| R37 | Memory in 70+ atomic files | Not found | none |
| R38 | Tier 2 at 2–3 endpoints | Not found | none |
| T15, T08, B21 | `claude-worktree`, "ClickUp Brain 2", "claude.ai/code" | Not spoken; the URL was on screen | frames (B21) |
| Glido | Glido is his own product | An affiliate link in the description | none |
| C04, B023 | Sol at $2/$10, "half the cost of Fable"; Terra and Luna prices | Astra $10/$50 only; half-cost is Astra vs Fable, $12 vs $26 | G15 |
| B010 | Source counts 26 vs 14 | Timings confirmed, counts not | none |
| B019 | Advisor pattern cuts cost 50–90% | No figure | none |
| B027 | Keeps Fugu for high-stakes checks | The test numbers only | none |
| B046 | Grok Bot setup leads to $15k+ retainers | $5,000 setup only | none |
| B072 | Maintenance 10–25% of build | "400 bucks a month"; $550 is one client at 10% | none |
| B076 | Add $100–$3,000 for test tokens | "client's account client's card" | none |
| B078, B107 | Workshop $1,000–$5,000 | No workshop price, Nate's or Devin's | G16 |
| B084 | SaaS band $29–$50, $390 a year | $39 a month only | none |
| B096 | $5,000 starter tier | $25k scale, $12k growth | none |
| B114 | $39 SaaS needs 2,136 customers | 168 at $499 only | none |
| B121 | Solo ceiling $10–20k a month, 90% margin | Not found | none |
| N01 | Sav is 20, University of Utah | Landscape architecture and Alexandra only | none |
| N16 | 10–20 calls, 1–3 deals | Funnel stops at 225 interested | none |
| C13 (verify-b) | Max plan "virtually unlimited" | Not in the Clawdbot video (G27) | none |
| X-04 | A $2,300 build | Six prices, none $2,300 | none |
| X-11 | 90% deterministic, 10% AI | 60/30/10 | none |
| C-132 | "Visual Agentic Workflow Framework" | Zero hits in 299 files; "the WAT framework" | none |
| Karns M&A | 1x–2x EBITDA | "like 5x" only | none |
| C-124 | "Another one of Nate's healthy mindset shifts" | Zero hits | none |
| C-016 | $10k salon MRR, "doubled reply rate" | The owner hit $10k; reply-rate line not found | none |
| C-022 | Dan's FP&A automation | No hit | none |
| C-002, C-003 | $3M partner perks; certification 9 pillars, 54 criteria | Neither spoken | G16 |
| C-037 | Claude Code and Codex write 40–60% of code | No hit | none |
| q27 | AIS Plus ~$300k a month | 3,500 × $89 arithmetic, never spoken | none |
| Q34-11, Q34-14, Q34-17 | Opus 4.8 "wise old owl"; Fable ~10x tokens; Astra 45% faster, 38% cheaper | Owl is Claude Code or Fable; per-task figures only | none |
| R42-25 | Shopify agency, 10 clients, $5,000 builds | No hit for "shopify" or "10 clients" | none |
| R43-04 | Karpathy layers shown with screenshot self-checks | Screenshot checks in another video, no Karpathy framing | none |
| R43-07 | DRY prompt text "Save the script… `/scripts/`" | Gemini's paraphrase | none |
| R43-14 | "Prompts are suggestions, tool permissions are walls" | Nearest line is Cole Medin's | none |
| R43-17 | UNIX "do one thing well" for skills | "unix" has zero hits | none |
| R44-18 | "immediate 7.5x to 10x return" | 7.5x now, 10x with lead growth | none |
| R45-04, R45-12 | 1–2 demo builds for Upwork; "which option do I choose" | Neither line spoken | none |
| R46-02, R46-05 | Agent Zero five modules; One Person AI Agency modules | Three-part blurb only; module order is paid | G16 |
| R46-04 | "Lego instruction manual" on Excalidraw | Map-first habit is his, the phrase is not | none |
| R47-09, R47-17 | 30/60/90-day check; "know 20% more" | No hits | none |
| R49-02 | Exit came "within his first year" | "almost 2 years", no exit date | G7 |
| R49-21 | Annual membership with locked-in rate | Not spoken; probably the pricing page | frames |
| R51-07 | $1,300 an hour on the $2,600 job | Gemini's division; he says $600 an hour only for the $1,200 job | none |

---

## Medium priority

### G6 · 52 channel videos outside the notebook
`sources.tsv` lists 352 videos and the notebook held 300, NotebookLM's cap. 52 videos have no transcript: 25 dated 2024-10-06 to 2025-02-19 and 27 with a blank date, all n8n-era tutorials by title. The full list is the table at the end. A second notebook, `d8087d26-…`, holds a near-duplicate 300 and covers none of the 52.
- **Why it matters to the lens:** Era 1 pricing and agent method rest on 116 transcripts, and 2024-Q4 has 0 of its 9 videos. Titles like "AI Agent Prompting Masterclass" (bwrAsnU2P88) and "5 n8n Tips You NEED to Know" (Ctr89Q2Nei8) likely hold early rules the lens cannot see.
- **Fill by:** yt-dlp auto-captions for the 52 video ids, then a second notebook built from those 52 alone, which fits under the 300 cap and answers the same q01–q51 lanes.

### G7 · Blank upload dates and undated events
28 videos have no upload date: 27 are among G6's 52, and 1 has a transcript (how-i-automated-faceless-shorts-with-ai-in-n8n-free-template.md). Model release dates in q34 were not spoken in the windows read (Q34-24, UNRESOLVED), no student case study carries a date (A-10), and no transcript dates the True Horizon exit (R49-02).
- **Why it matters to the lens:** titles place all 28 in Era 1, so only ordering inside Era 1 is lost; case studies and the exit cannot be put before or after a rule change.
- **Fill by:** dates. yt-dlp `--print upload_date` per blank video id; a join of each case-study filename against `sources.tsv` for A-10; video titles for release dates, which already give Opus 4.7 on 2026-04-16 and Fable 5.1 on 2026-09-01.

### G8 · On-screen content lost from captions
Captions hold what Nate says, and 9 gaps sit in what he showed. No full `skill.md` body is reproduced (A10), and the example `claude.md` files read as reconstructions (A13). The Client Pack deck names 7 of 10 slides and the PDF check names 4 of 5 defects (A02). The content-ops skills `packaging`, `idea mining` and `YouTube strategist` are named without their text (A-04). The Cohere reranker setup and several URLs are on screen only, and the q08 vs q09 system-prompt sections are G24.
- **Why it matters to the lens:** the profile says the lens generates from prompts, templates and builds, and these are the most copyable artifacts in the corpus.
- **Fill by:** video frames at the caption timestamps where he opens each file, OCR'd; the free templates linked in video descriptions.

### G9 · Unnamed third-party numbers
The 92% vs 78% retrieval figures, the 67% reasoning drop and the 6% to 34% edit-without-read rise carry no source (A03). The "35x fewer tokens" and "~72% MCP reliability" benchmarks are unnamed (A04), as are the 92% referral stat and "partner source deals close 46% faster". The AMD analysis of almost 7,000 Claude Code sessions is named and real (verify-c), so it is not in this gap.
- **Why it matters to the lens:** W1's rule applies to numbers too; a figure he cites is `[D]` for his words and never `[G]`, and the lens cannot say how strong it is.
- **Fill by:** transcript grep for the sentence around each figure, then a web search for the study or post.

### G10 · No Nate-voiced agency metrics
True Horizon's only figures are the $20,000 minimum retainer and "over $100,000 a month" before the sale (B125). No churn, close rate or pipeline-to-close number exists. Every cold-email volume and reply rate in the corpus is Sav's (W4), and Pass 1's q26 answer returned a copy of q25 (B122) until the Pass 2 re-run.
- **Why it matters to the lens:** "how would Nate sell this" gets answered with a guest's funnel unless the lens says so.
- **Fill by:** a targeted NotebookLM question on the-3-step-system-behind-my-20k-month-ai-agency-retainers.md (2026-08-25) and the pricing retrospective; transcript grep for "close rate" and "churn"; the 52 videos in G6.

### G11 · Integration setup steps missing
q12 was asked how he sets up Supabase, Stripe, ClickUp and Slack and returned key names only (A06). Sections 1 and 2 of q12 re-answer q10 and q11, so integration coverage is thinner than its length (A07).
- **Why it matters to the lens:** a build question that needs a Stripe or Supabase step gets no Nate answer.
- **Fill by:** one targeted NotebookLM question per tool, checked by transcript grep for "supabase" and "stripe".

### G12 · Evaluation method thin
Golden datasets and LLM-as-a-judge are named with no eval tool, rubric or scored run (A08). Pass 2 corrected the judge method to an n8n evaluation against a data table with a correctness score (R43-19, 3-hidden-data-table-hacks-for-smarter-ai-agents.md) and the dataset size to "100 or a few hundred" (R23).
- **Why it matters to the lens:** his verification pillar for agent loops has no worked scoring example.
- **Fill by:** a targeted NotebookLM question on evaluation, then transcript grep for "evaluation" and "correctness".

---

## Low priority

### G13 · No proposal, contract or SOW template
Only the proposal's top-paragraph rule ("none of them are about you") and the 10% / 25% / 50% tiers exist (B123).
- **Fill by:** a targeted NotebookLM question; templates linked in the descriptions of 18-months-of-pricing-ai-automations-in-21-mins.md (2026-08-01). It may sit in the paid tier (G16).

### G14 · Demand and price for his own products
Client Pack has a price and unit cost (4 and 9 cents a call) but no revenue, subscriber or conversion number (A01). Hermes is "packaged as an always-on AI OS" with no price, while Grok Bot has $5,000 (B126).
- **Fill by:** a targeted NotebookLM question on Hermes as a client offer; transcript grep for "subscribers" in build-sell-ai-saas-products-2-hour-course.md (2026-08-10).

### G15 · Vendor prices never spoken
Sol, Terra and Luna per-token prices are never spoken (B-C04, B023). Trigger.dev paid plans (A05) and Clay (A-08) carry verdicts and no price; Modal settled at about $30 one-off (A-C08).
- **Fill by:** vendor pricing pages on the day of use, dated; never stored as Nate's (W3).

### G16 · Paid-course content
AIS Plus syllabi, the Agent Zero module order (R46-02), the One Person AI Agency modules (R46-05), the Upwork bidding playbook ("I cover the Upwork bidding playbook in way more depth"), the certification's 9 pillars and 54 criteria (A-03, C-003), the $3M partner perks (C-002) and the coaching and AIS Live ticket prices (A-07) all sit behind the paywall or go unspoken.
- **Fill by:** nothing short of course access. Transcript grep recovers only the free blurbs.

### G17 · One transcript with no content
S2ME69hra-k, "Why Watching AI Videos Isn't Enough" (2026-06-24), returned nothing and is the only Era 3 hole.
- **Fill by:** yt-dlp auto-captions for S2ME69hra-k.

### G18 · Unsettled spellings
Key AI appears in 19 files and never as "kie", so kie.ai is probable but unconfirmed. "Jacob Coxin" is an Anthropic researcher whose real surname the captions cannot give (tweet dated September 8). Mark Kashef is probable from "Mark Cashup" and "Mark Cashef". Klouse is also captioned "klaus" and "claus", and "ultra code" (A09) is probably a mishearing of `ultrathink` or `ultraplan`; `/goal` is defined and closed.
- **Fill by:** yt-dlp `--print description` on the files that name them; on-screen names in video frames.

### G19 · Caption-garbled video prices
Higgsfield prices come through as Kling "60s", MiniMax "a$110" and a sizzle reel at "1755 based on my credits" (C-036, UNRESOLVED). Seedance 2.5 at $3.23 is clean.
- **Fill by:** video frames from this-one-gpt-6-astra-skill-replaces-your-higgsfield-subscription.md.

### G20 · The ~15 core n8n nodes are never listed
"About 90% of all workflows will rely on the same 15 or so core nodes" is confirmed (C-050, how-i-d-learn-n8n-if-i-had-to-start-over-in-2026.md), but the 15 are not named (A-06).
- **Fill by:** a targeted NotebookLM question; "n8n AI Agent Masterclass" (EzS2PIjyeQQ) in G6's 52.

### G21 · Karpathy's own statement of the 3 layers
Nate's version of Spec, Verifier, Environment is a reel of about 1 minute, so q43's depth is Gemini's.
- **Fill by:** Karpathy's original post, via web search.

### G22 · Whether `.claudeignore` exists
He says "a cloud ignore file" (F09, CONFIRMED as said); whether Claude Code reads one is unverified.
- **Fill by:** Claude Code docs.

### G23 · Grok Bot owner
Captions show Cursor Ultra, an "@cursor" Slack invite and "Super Grock" at $30 together (verify-b, UNRESOLVED).
- **Fill by:** the product page. The lens calls it Grok Bot, as he does.

---

## Open contradictions

Pass 2 left 11 contradiction rows open. G25 holds 2 of them (B-C01's base and R42-15), so 10 entries cover all 11.

### G24 · A-C05 · System-prompt sections differ between q08 and q09
Captions never list the sections; build-sell-n8n-ai-agents-8-hour-course-no-code.md (2025-05-23) says only "overview" then "sections like output or rules". Priority: Medium. **Fill by:** video frames from that course.

### G25 · B-C01 base and R42-15 · The $5,500 build, told twice
$38,400 at 15% with $550 maintenance on 2025-11-30 against $41,600 at 13% with $400 flat on 2026-08-01, same 20 leads a week at $40 an hour (R51-04). Captions cannot say whether it is one client or two. Priority: Low. **Fill by:** dates, already applied: the lens treats the 2026-08-01 telling as current and notes the $260 slip in the earlier one.

### G26 · B-C03 · Which harness is token-lean
"Codex wrote about 2 to 5x fewer output tokens" (2026-05-26), Codex ~11.5M output vs Claude 2M on a Typeform clone (2026-08-14), Codex 100,000 tokens and $20 vs Claude ~500k and $65 on design (2026-08-26). Q34-22's 2–5x range is part of this row. Priority: Low. **Fill by:** dates; the lens cites the dated test that matches the task and claims no general winner.

### G27 · B-C13 · Max plan "virtually unlimited" vs quota risk
"Virtually unlimited" is not in the captions; Claude Design took "about 6% of my session limit" on the $200 plan (2026-04-30), and limits doubled on 2026-05-07. Priority: Low. **Fill by:** Anthropic's plan docs, dated at time of use.

### G28 · X-12 · Hostinger VPS price
Only "six bucks a month n[ine] bucks" for KVM 2 is spoken (2026-01-28). Priority: Low. **Fill by:** video frames from that video, or Hostinger's page, dated.

### G29 · R44-12 · Why this, why now, why me: Nate's or Jonathan Stark's
18-months-of-pricing-ai-automations-in-21-mins.md credits Stark for hourly and the landscaper but is silent on the three buckets, and Stark's published "why conversation" asks the same three. Priority: Low. **Fill by:** a web search for Stark's version; a targeted NotebookLM question on where Nate says the buckets came from.

### G30 · R49-19 · AIS Plus "over 200" vs 2,000
"a community of over 200 members" appears in 15 files; it is either an early real count or a caption drop of 2,000. Priority: Low. **Fill by:** dates. If the 15 files all predate the first "1,100", the 200 is real.

### G31 · B061, C-064 · Discount email to 150,000 vs 200,000
"about 150,000" in the 2026-07-11 course and on 2026-08-04; "almost 200,000" on 2026-08-24 (everything-goldman-sachs-taught-me-about-ai-in-10-minutes.md). Priority: Low. **Fill by:** none; it is his own drift, and the lens gives both with dates.

### G32 · I-5 · Who speaks the Boris Cherny 6-month line
The line sits in the cold-open teaser of how-to-actually-choose-the-right-ai-agent.md (2026-09-11), which ends "all right so Mark thank you so much for joining us"; verify-c says Nate, round2 says Mark Kashef. B017's "only be loyal to my harness and my assets" is in the same teaser and carries the same risk. Priority: High, because the answer decides whether B017 enters Nate's Layer 1. **Fill by:** the YouTube video audio at the teaser timestamp.

### G33 · I-6 · Whose voice reads the Karpathy reel
The owner is settled as Karpathy; the voice in the reel Nate edits in gpt-6-astra-finally-solves-ai-video-editing-full-guide.md (2026-09-08) is not. Priority: Low. **Fill by:** the video audio.

---

## Where each input went

**`[A]` markers (30).** A01 → G14. A02 → G8. A03, A04 → G9. A05 → G15. A06, A07 → G11. A08 → G12. A09 → G18. A10, A13 → G8. A11 → closed by `sources.tsv` (324 of 352 dated), rest in G7. A12 → closed: LRP is Listen, Repeat, Poke in 6 files. A14 → closed: Capabilities and Cadence are defined in the 4 C's. B122 → closed by the q26 re-run, remainder in G10. B123 → G13. B124 → closed by `sources.tsv`, remainder in G26. B125 → G10. B126 → G14. A-01 → closed by the 299 transcripts. A-02 → closed by the q34 re-run, release dates in G7. A-03 → G16. A-04 → G8. A-05 → closed: the 5-step formula is defined, and the "Visual Agentic Workflow Framework" is Gemini's (G5). A-06 → G20. A-07 → G16. A-08 → G15. A-09 → G18, with Fable, Astra, Sol, Seedance, Kling, Wispr Flow, Docling, `/Ultra review` and the AMD analysis settled in Pass 2. A-10 → G7. A-11 → closed: Henry's House of Coffee and Vanisec are vendor copy he reads in the n8n course (C-024).

**UNRESOLVED verdicts.** verify-a C02 → closed by date (A-C02); C05 → G24. verify-b C01 base → G25; C03 → G26; C11 → closed by speaker (Devin Karns); C13 → G27; B061 → G31; Grok Bot owner → G23. verify-c C-016 → G5; C-036 → G19; key.ai and Jacob Coxin → G18; Q34-22 → G26; Q34-24 → G7. round2 R42-15 and R51-04 → G25; R44-12 → G29; R45-03 and R49-12 → closed by date; R49-17 → closed by caption (375,000); R49-19 → G30.

**Pass 2 gap table (17 rows).** The profile row is closed: `profiles/nate-herk.md` now names the 299 transcripts, Rule 1 and `[D:guest]`. The other 16 map to G2, G3, G4, G6, G7, G8, G9, G10, G25, G17, G16, G15, G23, G18, G21 and G22.

---

## The 52 videos outside the notebook

52 of the 352 videos in `sources.tsv` have no transcript in `video/`, 25 dated and 27 blank. Transcript frontmatter carries `url: None`, so the match ran on titles, with curly apostrophes and punctuation folded out. 299 of 352 titles matched, equal to the 299 transcripts, so no title failed on spelling. The 53rd unmatched title is S2ME69hra-k, which is inside the notebook with no content (G17) and is left out of the table.

| # | video_id | title | upload_date |
|---|---|---|---|
| 1 | R36bpNPPIMs | How to Build a Google Scraping AI Agent with n8n (Step By Step Tutorial) | 2024-10-06 |
| 2 | omw1MEvMCo0 | I Built a Personal Assistant AI Agent with No Code in n8n | 2024-10-12 |
| 3 | JUx2ZfNfD64 | I Built an AI Agent that Automated my Inbox with n8n (No Code) | 2024-10-15 |
| 4 | ZHH3sr234zY | n8n Masterclass: Build AI Agents & Automate Workflows (Beginner to Pro) | 2024-10-20 |
| 5 | gvldzucAoBo | Scrape Google for LinkedIn Profiles in Seconds with n8n | 2024-10-23 |
| 6 | DiCjeWKgNj0 | I Scraped, Researched, and Created Outreach for 16,846 Leads using Godmode HQ | 2024-11-10 |
| 7 | u2Tuu02r7QI | Build this Multi AI Agent System for Research and Content Creation in n8n | 2024-12-03 |
| 8 | ju9xk_QX990 | Understanding APIs in n8n (as a beginner) | 2024-12-11 |
| 9 | pYelCIqkm5Y | Everything I Learned About AI Agents in 2024 in 19 Minutes | 2024-12-14 |
| 10 | -uEDxBXsAnQ | Build AI Agents for $0.014 with DeepSeek V3 in n8n | 2025-01-10 |
| 11 | pJYm7MOyMH0 | Having an Actual Conversation with Data Using an ElevenLabs Voice Agent and n8n | 2025-01-13 |
| 12 | Je4EAscnKK0 | ElevenLabs Voice Agents Are So Easy to Build (No Code!) | 2025-01-15 |
| 13 | 6DLZK7XDOGo | How I'd Teach a 10 Year Old to Build AI Agents (No Code, n8n) | 2025-01-17 |
| 14 | HUdm3NXwk-w | I Built a Team of Research Agents for Newsletter Automation in n8n (No Code) | 2025-01-19 |
| 15 | 4JR-UrEZHQQ | The Ultimate n8n Starter Kit (2025) (Free) | 2025-01-20 |
| 16 | o69yGTxB8EE | Two Ways to Save 96% of Your Money Using DeepSeek R1 in n8n | 2025-01-23 |
| 17 | tjaD65OCoE8 | How to Actually Build Agents with DeepSeek R1 in n8n (Without OpenRouter) | 2025-01-24 |
| 18 | _DbZjllXDv8 | Best Model for RAG? GPT-4o vs Claude 3.5 vs Gemini Flash 2.0 (n8n Experiment Results) | 2025-01-30 |
| 19 | MGaR7i35KhA | How to Locally Host DeepSeek R1 for FREE in Under 10 Minutes in n8n | 2025-01-31 |
| 20 | 9FuNtfsnRNo | I Built the Ultimate Team of AI Agents in n8n With No Code (Free Template) | 2025-02-03 |
| 21 | nSQnJoqK4DQ | 4 Agentic Frameworks for More Efficient Workflows in n8n | 2025-02-10 |
| 22 | tr5_S1FGoUI | This Trick Helps me Build Agents 3x Faster (as a beginner) | 2025-02-12 |
| 23 | 5zhTxuuPc3A | I Built an AI Voice Travel Agent with ElevenLabs and n8n (Free Template) | 2025-02-16 |
| 24 | z-gDDajSSNE | I Built a Human in the Loop Calendar Agent in n8n with No Code | 2025-02-19 |
| 25 | TfqioNAP1W4 | Building AI Agents in n8n Somehow Got Easier (as a beginner) | 2025-02-19 |
| 26 | FcAAlOw6KZ8 | I Built a Human In The Loop Sales Team That Waits for Feedback and Approval in n8n | blank |
| 27 | IBaT-XQm_wE | OpenAI Fires Back at DeepSeek With a New Reasoning Model: o3-mini (n8n AI Agent) | blank |
| 28 | dooXxhGy5Ow | How I Built A Technical Analyst AI Agent in n8n With No Code | blank |
| 29 | KIJHRq_Tg6o | How I Built an AI Agent to Automate my Emails in n8n (Step by Step, No Code) | blank |
| 30 | Kvf-Pr1LRe4 | The Best RAG System On YouTube (Steal This!) | blank |
| 31 | skHe-qIRkM4 | This AI Agent Extracts Text From Images in n8n | blank |
| 32 | VBw5PEV-zKw | Vector Database Optimization with n8n: Metadata, Text Splitting, & Embeddings | blank |
| 33 | Ctr89Q2Nei8 | 5 n8n Tips You NEED to Know | blank |
| 34 | 3Ai1EPznlAc | Set up Google Credentials in n8n in 5 minutes (2025) | blank |
| 35 | ZP4fjVWKt2w | How to Build a Personal Assistant AI Agent in n8n (Step-by-Step, No Code) | blank |
| 36 | wEXrbtqNIqI | Step by Step: RAG AI Agents Got Even Better | blank |
| 37 | NzMNuuS5JbI | Step by Step: Scrape UNLIMITED Emails for FREE with n8n | blank |
| 38 | krHTtaud0CU | How to Build an AI Slack Assistant in 5 Minutes (Chatbase) | blank |
| 39 | bwrAsnU2P88 | AI Agent Prompting Masterclass: Beginner to Advanced | blank |
| 40 | l8NoMgd8lG4 | The Best Way to Give AI Agents Tools in n8n | blank |
| 41 | 9G-5SiShBKM | AI Personal Assistant 2.0 / This Agent Calls Other Agents (No Code) in n8n | blank |
| 42 | EzS2PIjyeQQ | n8n AI Agent Masterclass / AI Nodes Made Simple | blank |
| 43 | fWtXJswvUcA | Step By Step: Automating Lead Nurturing with No Code in n8n | blank |
| 44 | iT9xpiUwVbI | Step-By-Step: Add 100+ Files to Pinecone for RAG AI Agent with n8n | blank |
| 45 | B15e_9_fCyE | Build a No-Code AI Chatbot (Step-by-Step Tutorial) | blank |
| 46 | Wpwbm3zCymk | How to Build a Client Onboarding AI Agent with n8n (Step-by-Step Tutorial, No Code) | blank |
| 47 | x1tam0Fhymc | *LIVE BUILD* Inbox Management AI Agent with n8n (NO CODE, Step-by-Step Tutorial) | blank |
| 48 | fz1RduhHeks | *LIVE BUILD* Personalized Outreach AI Agent in n8n (No Code) | blank |
| 49 | otUBuV1foLY | Build your first NO CODE AI Agent in n8n (for beginners) | blank |
| 50 | 6w0MshwAqBQ | How to Create an RAG Chatbot AI Agent with n8n (No Code, Step-by-Step Tutorial) | blank |
| 51 | YFrej2oSldo | How to Create an AI Email Agent with n8n (No Code, Step-by-Step Tutorial) | blank |
| 52 | w4qtnXRd8nU | How I Wish Someone Explained AI Agents To Me (as a beginner) | blank |
