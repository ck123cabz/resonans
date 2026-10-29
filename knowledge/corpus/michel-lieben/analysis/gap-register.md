---
type: corpus
aliases: ["Gap Register -- Michel Lieben"]
corpus: michel-lieben
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Gap Register -- Michel Lieben

**Corpus:** michel-lieben
**Generated:** 2026-03-25
**Input:** 112 signals from Pass 1, 8 clusters from Pass 2 (updated with 25-source notebook)

---

## P0: Critical Gaps

### Gap 1: Gated Copywriting Templates (Notion Document)
- **What's missing:** Michel references a curated Notion document containing tested copywriting frameworks and templates, previously reserved for ColdIQ team and clients, now shared behind LinkedIn engagement gates ("comment to get access"). The actual email copy structures, subject line formulas, exact body templates, and CTA wordings are not in the corpus.
- **Evidence:** NotebookLM Q10 explicitly states sources lack granular structural breakdowns. LinkedIn posts 440 (902 likes) and 476 (516 likes) reference this document.
- **Impact:** Without these templates, the agent has conceptual frameworks (hyper-relevant free value, irresistible offer, etc.) but lacks specific copy templates to generate from. The frameworks tell you what approach to take; the templates tell you exactly what to write.
- **Fallback:** Monitor for public sharing. Reconstruct partial templates from blog/019 (most concrete copy examples). Request from Michel directly.

### Gap 2: Claude Code Skill Architecture (Internal Detail)
- **What's missing:** Michel references "32 skills, 12 agents, 2,108 files" in ColdIQ's Claude Code GTM system. The expanded notebook (Q24) provides tool-level and workflow-level detail, but individual skill files, prompt structures, and agent configurations remain opaque.
- **Evidence:** LinkedIn post 016 (771 likes) and the live demo webinar mention the architecture. Blog/020 and Q24 detail workflows but not the underlying skill file structure.
- **Impact:** Agent can describe what Claude Code does and the general workflow but cannot replicate or reference specific skill implementations.
- **Fallback:** Access webinar recording (LinkedIn post 015). Check for GitHub repository. Extract from future ColdIQ publications.

---

## P1: Important Gaps

### Gap 3: Exact Sequence Timing
- **What's missing:** Day-by-day spacing between follow-up emails. Q14 mentions "two-day gap" between steps as one example but does not specify whether this varies by campaign type, audience, or industry.
- **Impact:** Agent can recommend 2-4 step sequences and 60-day re-engagement but cannot specify optimal inter-step timing for different scenarios.

### Gap 4: Client Case Studies with Detailed Metrics
- **What's missing:** Systematic case data across 70+ clients. Only a handful of specific cases: AirOps ($3M pipeline), HR SaaS Glassdoor play, $100K ACV client, $19/mo SaaS trap, recruiting firm lead list, luxury hotel outreach.
- **Impact:** Agent has powerful examples but lacks breadth for industry-specific recommendations.

### Gap 5: LinkedIn Infographic Content (Visual Methodology)
- **What's missing:** Visual methodology in tech stack breakdowns and system schemas. Caption text captured but visual content not extracted.
- **Impact:** Michel's visual frameworks may contain methodology not captured in text.
- **Fallback:** Run vision extraction on top-engagement infographic posts.

### Gap 6: Cold Calling SOPs
- **What's missing:** The Human Track (cold calling) methodology, scripts, talk tracks, training. Only mentioned as counterpart to Technical Track.
- **Impact:** Agent's outbound methodology is weighted toward email and LinkedIn; cold calling guidance absent.

---

## P2: Nice-to-Have Gaps

### Gap 7: Accelerator Curriculum Detail
- **What's missing:** Coaching program structure (200+ students, $300K+ revenue). Repositioned from GTM engineering to agency building based on market demand. Behind paywall.

### Gap 8: Competitor Analysis Methodology
- **What's missing:** Systematic tool evaluation framework beyond Clay tier list (Q8). The "G2 for sales" directory evaluation rubric is not detailed.

### Gap 9: Financial Operations & Unit Economics
- **What's missing:** Margin/profitability data. Unit economics per client. Infrastructure-as-a-service line ($60K+/mo) may have different economics than core agency but not broken down.

---

## P3: Contextual Gaps

### Gap 10: Personal Background Beyond ColdIQ
- Belgian, lives in Barcelona (Norrsken hub). Non-native English speaker. Failed 7 businesses. Sparse beyond professional narrative.

### Gap 11: Team Compensation and Economics
- Employee advocacy prizes documented. Base salaries, equity structures, and comp philosophy not disclosed.

### Gap 12: European Regulatory Considerations
- DMARC/spam regulations mentioned. GDPR compliance and European cold email regulatory details not covered.

---

## RESOLVED (from expanded 25-source notebook)

| Gap | Original Status | Resolution Source |
|-----|----------------|-------------------|
| Dan/Fivos departure story | Unknown | Q20: Complete narrative with betrayal details, competitor launch, "bulletproof business" lesson |
| LinkedIn Ads API workflow | Partial | Q25: Ivan's Google Sheet -> Claude Code -> LinkedIn API pipeline |
| AI coding stack | Referenced only | Q24: Conductor, Claude Code, Codex, Cursor (rejected), Lovable, Vercel, GitHub |
| Lempire/Lemlist comparison | Not covered | Q23/Q35: $29M ARR playbook, multi-product limits, focus tension |
| Clay feature tier list | Not covered | Q8: S/A/B/C/D rankings for 15+ features with rationale |
| Employee advocacy deep dive | Partial | Q3: Complete payout structure, quality gates, coaching sessions |
| Website visitor ID workflow | Partial | Q33: rb2b -> Slack -> Clay -> routing step-by-step |
| AI SDR position detail | Vague | Q26: Controversial bullish take, vertical limitation, human-AI hybrid |
| $0 to $6M timeline | Partial | Q9/Q19: Month-by-month growth arc |

**Total gaps:** 12 active (2 P0, 4 P1, 3 P2, 3 P3) + 9 resolved
