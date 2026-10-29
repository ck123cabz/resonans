---
type: corpus
aliases: ["Alex Vacca -- Gap Register"]
corpus: alex-vacca
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Alex Vacca -- Gap Register

**Generated:** 2026-03-24
**Input:** Pass 2 reconciliation (49 provenance upgrades, 20 clusters, 12 gaps identified), Pass 1 extraction (218 signals, 3 confirmed [A] gaps), ingestion profile (5 known gaps going in)

---

## Gaps by Priority

### P0 -- Critical (blocks agent function)

| # | Gap | Why It Matters | What Would Resolve It | Source to Try | Status |
|---|-----|----------------|----------------------|---------------|--------|
| 1 | 12 Claude Skill file contents | These are the literal files that encode ColdIQ's GTM methodology for Claude Code inside Clay. The 12 file names are known (L3, X218): Company Research Agent, Personalization Writer, ICP Scorer, LinkedIn Profile Analyzer, Data Cleaner & Normalizer, Objection Handler, Email Sequence Writer, Competitor Analyzer, Job Posting Analyzer, Technographic Qualifier, News & Signal Synthesizer, Account Brief Generator. The actual prompts, scoring rubrics, and templates inside each file are behind a lead magnet. Without these, the GTM agent must reverse-engineer generation templates from scattered corpus descriptions instead of using ColdIQ's battle-tested originals. | Acquire the lead magnet from the L3 LinkedIn post link, or reverse-engineer from corpus descriptions of each file's function | Lead magnet download from L3 post; Alex's future posts detailing individual files; ColdIQ Accelerator curriculum if accessible | Open |

### P1 -- High (degrades agent output quality)

| # | Gap | Why It Matters | What Would Resolve It | Source to Try | Status |
|---|-----|----------------|----------------------|---------------|--------|
| 2 | LinkedIn image/infographic methodology | Alex posts visual breakdowns of tech stacks, workflow diagrams, and funnel architectures. Carousel and infographic posts outperform all other formats (L38, N110). Caption text captures the framing but not the actual methodology in the image. Some of his highest-engagement posts are image-dependent, meaning the richest tactical content is invisible to text extraction. | Vision extraction on top-engagement image posts, or manual transcription of key infographics | Apify LinkedIn scraper with vision API on image posts; re-scrape top 50 image-heavy posts with GPT-4o vision | Open |
| 3 | ColdIQ copywriting training document (Notion) | Referenced in L19 as the master document used to train new hires on email writing. Contains battle-tested frameworks that get updated continuously. The corpus has scattered copy rules (50-80 words, relevance over personalization, give-first CTAs) but not the consolidated training artifact. Agent copy generation would be stronger with the structured source. | Acquire lead magnet from L19 post, or reconstruct from the ~29 Copy Craft signals already extracted | Lead magnet link from L19 LinkedIn post | Open |
| 4 | Specific Clay workflow configurations | NotebookLM describes Clay workflows conceptually (steps, tools, prompts) but the actual implementation details are lost in Gemini synthesis. Missing: exact column names, API configuration parameters, conditional formula syntax, Clay table structure. The agent can describe workflows but cannot reproduce them at the implementation level. | Detailed Clay table walkthroughs or exported Clay configurations | YouTube videos where Alex screenshares Clay tables (source videos behind the NotebookLM extraction); ColdIQ blog tutorials with Clay screenshots | Open |
| 5 | ICP scoring criteria specifics | N78 references a "scoring criteria markdown" with points for industry, employee count, funding stage, revenue, tech stack. L30 mentions ChatGPT + Claude scoring against ICP criteria. The exact point values, weights, and tier thresholds are not in the corpus. Without these, the agent can do ICP scoring but must invent its own rubric rather than using ColdIQ's proven one. | The actual ICP Scorer skill file (gap #1 dependency), or a detailed description of the scoring rubric from any source | 12 Claude Skill files (ICP Scorer specifically); ColdIQ Accelerator curriculum; future LinkedIn posts | Open |

### P2 -- Medium (nice to have)

| # | Gap | Why It Matters | What Would Resolve It | Source to Try | Status |
|---|-----|----------------|----------------------|---------------|--------|
| 6 | Client case studies with metrics | ColdIQ references client results across the corpus (AirOps $3M pipeline, recruitment client 657 leads, HR SaaS 3x reply rate) but the data is scattered and inconsistent. No structured case study format with industry, deal size, timeline, and exact methodology applied. The agent can cite results anecdotally but cannot do pattern matching across verticals. | Structured case study extraction with consistent fields: industry, company size, campaign type, timeline, results | LinkedIn posts mentioning specific client results; blog case study articles; YouTube case study videos | Open |
| 7 | Michel Lieben's distinct methodology | Blog signals show Michel has his own frameworks (give-first elaboration in B2, tiered outreach in B1, signal-based lists in B24). Some may diverge from Alex's articulation. Scoped out of this corpus intentionally, but creates potential blind spots where the agent treats Michel's framing as Alex's. | Separate corpus ingestion for Michel, or at minimum a diff analysis of where Michel's and Alex's frameworks diverge | Michel's LinkedIn posts; YouTube appearances; blog articles under his byline | Open |
| 8 | Ivan Falco's LinkedIn Ads playbook details | Ivan built ColdIQ's ABM framework (B7) and LinkedIn Ads funnel (B8). Budget allocation (50-60% TOF, 20-30% MOF, 15-20% BOF) and the 25-40% reply rate lift are documented, but specific targeting parameters, creative testing protocols, and audience building workflows are summarized rather than detailed. | Direct extraction from Ivan's content, or detailed ColdIQ blog/video content about LinkedIn Ads operations | Ivan Falco's LinkedIn; ColdIQ YouTube featuring Ivan; LinkedIn Ads case study articles | Open |
| 9 | Pricing model evolution | First client $1,500/month, current payments $49,000 (L39). Revenue went from $0 to $507K+/month. But the pricing tiers, packaging logic, and what deliverables map to what price points are not documented. The agent can discuss ColdIQ's growth trajectory but cannot reason about service packaging. | Pricing page analysis, sales call transcripts, or direct documentation of service tiers | ColdIQ website; Qwilr proposal templates; sales call recordings via Attention | Open |
| 10 | Actual reply rates by industry/vertical | Corpus provides aggregate benchmarks (3-5% positive reply rate generic, 0.5-1% without enrichment, 20-30% with hyper-enrichment, 57% on inbound-triggered). Missing: which industries produce which rates, seasonal variation, B2B vs B2C service differences. | Campaign performance data broken down by industry segment | ColdIQ internal analytics; future LinkedIn posts with vertical-specific breakdowns | Open |

### P3 -- Low (completeness only)

| # | Gap | Why It Matters | What Would Resolve It | Source to Try | Status |
|---|-----|----------------|----------------------|---------------|--------|
| 11 | ColdIQ Accelerator curriculum | Referenced as $30K/month revenue stream (N99), 25 seats pre-sold. The curriculum would contain systematized versions of all ColdIQ frameworks, likely the most structured articulation of the methodology. Behind paywall. | Curriculum outline or participant notes | Public testimonials from accelerator graduates; any publicly shared curriculum outlines | Open |
| 12 | Reddit Intel Collector workflow details | Mentioned once in L33 as one of four n8n GTM agents. Described as "closest thing to reading your market's mind." No other source confirms or elaborates. | Full workflow architecture: Reddit API configuration, GPT prompt for ICP signal identification, output format, n8n node structure | Alex's future posts; n8n community templates; ColdIQ YouTube | Open |

---

## Summary

| Priority | Count | Description |
|----------|-------|-------------|
| P0 | 1 | Blocks agent function |
| P1 | 4 | Degrades output quality |
| P2 | 5 | Missing context |
| P3 | 2 | Completeness only |
| **Total** | **12** | |

### Dependencies Between Gaps

- Gap #5 (ICP scoring criteria) depends on gap #1 (12 Claude Skill files). The ICP Scorer is one of the 12 files. Resolving #1 likely resolves #5.
- Gap #3 (copywriting training doc) overlaps with gap #1. The Email Sequence Writer and Personalization Writer skill files may contain or reference the same training material.
- Gap #11 (Accelerator curriculum) could partially resolve gaps #1, #3, #4, and #5 if the curriculum documents the methodology in structured form.

### What the Agent Can Still Do

The corpus already contains enough to build a functional GTM agent. The 218 extracted signals cover all 8 knowledge types, and 49 provenance upgrades give high confidence on the core frameworks. The P0 gap (skill file contents) means the agent will generate from reconstructed templates rather than ColdIQ's exact originals. The P1 gaps mean the agent's copy generation, Clay workflow building, and ICP scoring will work but be less precise than ColdIQ's internal standard.
