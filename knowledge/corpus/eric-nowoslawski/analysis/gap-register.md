---
type: corpus
aliases: ["Gap Register — Eric Nowoslawski Corpus"]
corpus: eric-nowoslawski
layer: gap-register
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
last_updated: 2026-03-20
gaps_total: 15
gaps_resolved: 10
gaps_remaining: 5
---

# Gap Register — Eric Nowoslawski Corpus

**Purpose:** Defines what the corpus does not cover after all extraction and resolution efforts. Informs agent confidence boundaries, human escalation rules, and future corpus collection priorities.

**Inputs:** Pass 2 gap analysis (15 gaps) + Gap resolution session (NotebookLM + LinkedIn deep search)

---

## Resolved Gaps

| Gap | Description | Resolution Method | Key Artifact |
|-----|------------|-------------------|--------------|
| **G1** | Client copy examples | LinkedIn deep search | 12 files with complete templates, 6 before/after comparisons. ~15 production templates across campaign types. |
| **G2** | Industry-specific methodology | NotebookLM query | 7 verticals covered: SaaS, agencies, local, healthcare, finance, e-commerce, professional services. |
| **G3** | Objection handling voice | LinkedIn deep search (reframed) | Eric's method is strategic (speed, CTA design, persistence), not scripted. 6-point post-reply framework from file 091. |
| **G5** | AI prompt templates | NotebookLM query | 6 production Clay prompts extracted: System Prompt, Creative Ideas, Company Mission, Social Post Hook, Job Openings, Deep Research AI Feature. |
| **G7** | Warm-up duration | NotebookLM query | Gmail: 2-3 weeks. Outlook/Proofpoint: 4-6 weeks (up to 2 months). Ramp: +5/day to 50 cap. Response rate: 32%. |
| **G8** | Counter-examples depth | LinkedIn deep search | 11+ failure stories: 4 data scraping fails, AI analogy abandoned, prompt cost waste, enterprise campaign shut down, 4000 inboxes lost. |
| **G10** | Multi-threading campaigns | NotebookLM query | 3 strategies with templates and performance notes: Weekend CEO/VP, Cross-Department Riddle, Internal Name-Drop. |
| **G12** | Post-positive conversion rates | NotebookLM query (definitively unknowable) | Eric intentionally does not track global post-reply conversion. 5 campaign-specific data points provided. Contacts-per-positive is the canonical metric. |
| **G13** | Fallback campaign guidance | NotebookLM query | 5 complete strategies: Company Mission, Creative Ideas (ultimate fallback), Lookalike, "Straight Down the Middle," Massive Lead Magnet. |
| **G15** | Lead magnet execution | NotebookLM query | Full fulfillment methodology: async model, Clay/Make.com/Lovable/Gamma/Parallel.ai toolchain, 4 concrete lead magnet types. |

---

## Remaining Gaps

### G4: 2024 Methodology (Transitional Year)

**Status:** Partially resolved

**Description:** The corpus covers 2023 (Campaign doc) and 2025-2026 (LinkedIn), but 2024 is represented only through retroactive references in 8 LinkedIn files. The GEX 2024 Wrapped doc exists externally but is not in the corpus.

**Why it matters for the agent:** The agent has the starting point (2023) and the current state (2025-2026), plus documented temporal evolution (sequence shortening, volume reduction, domain aging). It cannot determine whether these shifts were gradual or sudden. It also cannot reference 2024-specific tactics that may have been tried and abandoned.

**Agent behavior:** Generate using 2025-2026 parameters as canonical. When referencing historical evolution, present the 2023-to-2025 trajectory without claiming precision about intermediate steps. Do not fabricate 2024-specific claims.

**Resolution path:** Ingest the GEX 2024 Wrapped doc (`https://lnkd.in/ensEk6nd`). This would definitively close the gap.

**Priority:** Low. The 2025-2026 methodology is canonical for current campaigns. 2024 was transitional.

---

### G6: Formal Client-Facing Voice Register

**Status:** Not resolvable from existing corpus

**Description:** The voice library covers Eric's public registers (anti-guru, confrontational, teaching, casual, empiricist, etc.) from LinkedIn and YouTube. No data exists on how Eric communicates in client kickoff calls, strategy presentations, or when delivering bad news about failed campaigns.

**Why it matters for the agent:** The Copywriter Agent writes cold email sequences, not client communications. This gap only matters if the agent's scope expands to client-facing deliverables (strategy decks, campaign reports, kickoff agendas).

**Agent behavior:** Do not attempt to generate client-facing communications. If asked to draft client-facing copy, flag: "This is outside the corpus. Eric's client communication register is undocumented. Recommend human drafting."

**Resolution path:** Fathom transcripts of Eric-client calls, or the client providing recordings/examples of Eric's formal register.

**Priority:** Low. Outside the Copywriter Agent's core function.

---

### G9: Per-Tool Enrichment Costs

**Status:** Not resolvable from corpus

**Description:** The corpus contains Eric's total enrichment cost ($0.02/email) and per-line fractions, but not a breakdown by individual tool (Clay, Lead Magic, Prospeo, ZeroBounce, etc.).

**Why it matters for the agent:** The agent cannot advise on cost-optimizing the enrichment waterfall or estimate per-campaign infrastructure costs for budget-constrained clients.

**Agent behavior:** Cite $0.02/email as the total benchmark. Do not attempt to decompose into per-tool costs. If asked for per-tool pricing, flag: "Per-tool cost breakdown is not in the corpus. This requires current vendor pricing data."

**Resolution path:** External vendor documentation. Not corpus-solvable.

**Priority:** Low. The Copywriter Agent writes copy, not infrastructure budgets.

---

### G11: Smartlead Platform Configuration

**Status:** Deferred

**Description:** Smartlead.ai is recommended as the primary sending platform, but no configuration details exist in the corpus (warm-up settings, campaign setup, inbox rotation, reply handling automation).

**Why it matters for the agent:** The agent cannot advise on platform configuration. This is relevant only if the agent expands to infrastructure setup guidance.

**Agent behavior:** Recommend Smartlead as the platform per Eric's methodology. Do not generate specific configuration values. If asked for setup details, flag: "Smartlead configuration details are not in the corpus. Recommend consulting Eric's tutorials or Smartlead documentation."

**Resolution path:** NotebookLM targeted query or yt-dlp extraction from Eric's Smartlead tutorial videos. Low effort if needed.

**Priority:** Low. Outside the Copywriter Agent's core function.

---

### G14: Outbound-to-Inbound Playbook (Newsletter Content Strategy)

**Status:** Partially resolved

**Description:** The cold-to-newsletter conversion funnel is documented (LinkedIn file 176). Lead magnet fulfillment is resolved (G15). But newsletter content strategy (frequency, topics, conversion checkpoints) remains thin.

**Why it matters for the agent:** If the agent's scope extends to full-funnel strategy beyond cold email, it lacks guidance on the inbound nurture layer. The agent can generate the initial cold email and the lead magnet delivery, but not the ongoing newsletter content that converts subscribers to meetings.

**Agent behavior:** Generate cold-to-newsletter conversion sequences using the documented playbook. For newsletter content strategy itself, flag: "Newsletter content methodology is not well-covered in the corpus. The cold-to-newsletter bridge is documented, but ongoing newsletter strategy requires human input."

**Resolution path:** Additional LinkedIn search for newsletter/inbound posts, or supplementary sources outside Eric's core teaching.

**Priority:** Low. Outbound-to-inbound is a funnel strategy question, not a copywriting task.

---

## Confidence Boundaries

### Generate with High Confidence

Areas fully covered by `[V]` (direct voice) and `[G]` (grounded evidence) provenance. The agent should generate without hedging.

- **Core sequence architecture:** 2-4 email structures, threading patterns, email position roles
- **Email 1 line-by-line framework:** Subject line, recency hook, poke-the-bear, social proof, CTA
- **Follow-up email methodology:** Context bump (E2), value flip (E3), status-aligned breakup (E4)
- **Copy constraints:** Word limits, reading level, jargon bans, anti-patterns (17 cataloged)
- **CTA design:** Interest-based vs. calendar vs. resource CTAs, with performance evidence
- **Campaign type selection:** Creative Ideas, Message-Market Fit, Multi-Threading, Lead Magnet, Feedback, Media/RFQ, Social Proof, Riddle, Flash Roll, Lookalike, Misspelling
- **AI snippet philosophy:** 5-12 word constrained snippets, prefix locking, jargon guardrail prompts
- **Infrastructure constraints:** 30/day sending, 4-6 week warm-up, domain hot-swap, inbox health thresholds
- **Fallback campaigns:** 5 strategies for no-signal TAM coverage
- **Multi-threading campaigns:** 3 strategies with templates
- **Subject line rules:** Internal camouflage, all lowercase, 2-3 words
- **Personalization waterfall:** 7-priority recency signal hierarchy
- **Offer framing:** "Offer > everything," controllable variable, demand posture classification
- **Voice registers:** Anti-guru, confrontational, teaching, casual, empiricist, diplomatically direct, vulnerable, anti-complexity, competitive, terse
- **7 industry verticals:** SaaS, agencies, local, healthcare, finance, e-commerce, professional services

### Generate with Moderate Confidence

Areas covered primarily by `[S]` (synthesized/NotebookLM-mediated) provenance. The agent should generate but note internally that these claims lack direct voice confirmation.

- **~21 methodology signals** remaining at `[S]` provenance after Pass 2 upgrades
- **Tooling exclusion list:** HubSpot, Mailchimp, Outreach.io, SalesLoft (all `[S]` provenance)
- **Clay workflow patterns** beyond the 6 extracted prompts (described at `[S]`, not template-level)
- **ICP scoring nuances:** AI lead scoring methodology (described conceptually, few production examples)
- **Enrichment waterfall** tool ordering rationale (described but not all steps have `[V]` confirmation)

### Flag for Human Review

Areas where gaps exist, contradictions are unresolved, or the agent is operating at the boundary of corpus coverage.

- **Contradiction #5:** Enzo's 15/day vs. Eric's 30/day per Google inbox (unresolved, flagged for future testing)
- **Contradiction #4:** <100 words default vs. 623-word email outperforming (context-dependent, but the override conditions are imprecise)
- **Contradiction #7:** Images in email: "never" vs. screenshots boosting response 5x (context-dependent)
- **Long-form email decisions:** When does an email justify exceeding the 100-word default?
- **Named case study inclusion:** When is the audience hyper-targeted enough to override the "generalized outcomes outperform" rule?
- **Post-reply conversion forecasting:** Agent has 5 campaign data points but no global benchmark
- **Newsletter content strategy:** Bridge is documented, ongoing content is not

### Decline to Generate

Areas entirely outside the corpus. The agent should refuse and recommend human involvement.

- **Client-facing communications:** Strategy decks, campaign reports, kickoff agendas, bad-news delivery
- **Per-tool cost estimation:** Infrastructure budgeting, enrichment cost optimization
- **Platform configuration:** Smartlead setup, inbox rotation settings, warm-up configuration values
- **Legal/compliance guidance:** CAN-SPAM, GDPR, HIPAA-specific compliance language beyond "be aware"
- **Pricing/packaging:** How to price outbound services, package tiers, contract structures
- **Post-reply scripting:** The corpus explicitly establishes that post-reply is human/SDR work, not automatable copy
- **Industries not covered:** Any vertical outside the 7 documented (SaaS, agencies, local, healthcare, finance, e-commerce, professional services) should be flagged as requiring human input on vertical-specific adjustments
