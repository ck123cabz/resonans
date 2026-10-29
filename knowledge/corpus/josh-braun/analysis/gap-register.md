---
type: corpus
aliases: ["Gap Register: Josh Braun Corpus"]
corpus: josh-braun
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Gap Register: Josh Braun Corpus

**Date:** 2026-03-24
**Source:** Pass 2 gap analysis + Pass 2 temporal analysis (unique signals) + corpus profile review
**Extraction base:** 481 signals from 6,009 LinkedIn posts (July 2023 -- March 2026)

---

## Known Gaps

| # | Gap | Category | Why it matters for the agent | What would resolve it | Priority | Status |
|---|-----|----------|-----------------------------|-----------------------|----------|--------|
| G1 | Partially extracted carousels (5--8 decks, only 2--4 of 11--50 slides captured) | Media | Braun's most structured framework content lives in these carousels. "7 Ways to Make a Good First Impression" has 50 slides, "15 Rules of Selling" has 15, "Sales Mantras" has 11, "Poke the Bear" deck has 11, "10 Sales Mantras That Release Your Mind" has 11. The `[F]` layer is incomplete without them. | Re-run vision extraction on 5--8 partially extracted carousels. Estimated ~100 slides total. | P1 | Open |
| G2 | AI-generated copy anti-pattern depth (single FlashIntel example) | Agent-readiness | The Copywriter Agent's primary failure mode is generating structurally correct but soulless output. Braun identified this failure mode explicitly but provided only one specimen. One example is not enough to build a constraint layer. | Curate 5--10 examples of AI-generated cold emails and annotate them using Braun's framework. Build a graduated quality rubric (bad / mediocre / good / great) rather than the binary bad/good pattern that dominates the corpus. | P1 | Open |
| G3 | Video post transcription (454 posts, caption only) | Media | Cold call tone, pacing, and delivery live in the videos. Text signals describe these qualities ("smooth, calm, relaxed," "6/10 speed, 7/10 volume") but the agent cannot hear them. Affects the GTM Agent's ability to coach on delivery and evaluate call quality. The Copywriter Agent is less affected since it generates text. | Batch-transcribe top 50 videos by engagement via NotebookLM. Prioritize videos whose captions reference "cold call," "poke the bear," "role play," or "live." Check whether Braun has a YouTube channel with overlapping content first. | P2 | Partial: the top 50 by engagement were transcribed on 2026-10-20 (49 have speech, in `.raw/video/`); 404 remain caption only |
| G4 | Voice tag underrepresentation (6 `[VO]` signals out of 481) | Content | The profile identified Voice as a generation source for the Copywriter Agent. With only 6 explicit voice samples, the agent lacks sufficient Braun-specific voice patterns to generate from. The voice is implicit across hundreds of signals but was never consolidated because Braun's teaching style is consistent rather than variable. | Synthesize a voice profile during core-knowledge construction (Pass 3). Pull implicit voice patterns from the 481 signals: metaphor catalog, sentence rhythm, structural patterns, signature phrases, contrast-pair construction. This is synthesis work, not additional extraction. | P2 | Open |
| G5 | No quantified cold call outcomes | Content | Braun's cold call methodology is entirely qualitative. No connect rates, meeting-set rates, or A/B test results on openers/scripts anywhere in the corpus. The GTM Agent cannot optimize without empirical baselines. | Accept as permanent gap. Braun is a qualitative teacher, not a data operator. Cross-reference with Nick's operational data (7% connect rate baseline, 60K calls/month validation) during core-knowledge construction. Note provenance limitation explicitly. | P2 | Permanent |
| G6 | Industry breadth in annotated email examples | Agent-readiness | The ~20 annotated cold email breakdowns cluster in 4--5 verticals: SaaS commissions (CaptivateIQ), SDR tools (Phone Ready Leads), triathlon coaching, and real estate. The Copywriter Agent needs to generalize to the client's target industries. Eric's corpus fills some of this (staffing, fintech, cybersecurity benchmarks), but Braun's own examples are narrow. | During core-knowledge construction, map each annotated email to its underlying framework elements (which 4-T element, which psychology principle). Build a "framework to industry adaptation" guide showing how the anatomy would apply to verticals not in the examples. No new extraction needed -- this is synthesis. | P2 | Open |
| G7 | Named case studies vs. generalized proof (Braun/Eric contradiction) | Cross-corpus | Braun uses named customer proof in annotated examples (e.g., "Kevin Trosian, CFO at Extensiv"). Eric's 500K-email data says named case studies correlate with average or below-average performance. The Copywriter Agent needs a clear generation rule. | Build a reconciliation rule in core knowledge: named proof when TAM < 500 and the name is a genuine peer; generalized proof ("companies like yours") for all at-scale campaigns. Cite Eric's data as the governing constraint. Document that Braun's named-proof examples are 1:1 teaching context, not at-scale cold email. | P3 | Open |
| G8 | Post-discovery pipeline gaps | Content | Braun covers opener through discovery through qualification well. Proposal strategy, post-discovery nurture, and close mechanics are fragmentary -- a $57.5K negotiation transcript, the proposal-avoidance technique, and a micro-commitment ask, but no complete post-discovery playbook. | Accept as partial gap. Braun's expertise is the opening conversation, not the close. The GTM Agent should route post-discovery methodology to a different source when one becomes available. Flag as a known limitation in core knowledge. | P3 | Partial -- permanent |
| G9 | Offer evaluation absent from Braun | Cross-corpus | Braun assumes the product/offer is good. Eric and Nick both insist offer evaluation is the prerequisite to all campaign activity ("30% agency / 70% client offer" from Eric; "80% of results depend on the client's offer" from Nick). Braun's frameworks break down silently when the offer is weak. | Not a Braun gap to fill. Core knowledge should note that Braun's frameworks assume offer-market fit exists. The GTM Agent's offer-evaluation logic comes from Eric and Nick. | P3 | Accepted -- not Braun's domain |
| G10 | Pre-July 2023 content inaccessible | Media | LinkedIn API ceiling. Braun has been posting since at least 2017. The captured period shows fully formed methodology with high restatement density, suggesting core concepts pre-date the window. Earlier content likely contains formative versions but not new methodology. | Permanent gap. If Braun's "Badass B2B Growth Guide" or published courses surface publicly, they could fill pre-2023 foundations. Not worth pursuing actively. | P4 | Permanent |
| G11 | 704 unprocessed low-engagement image posts | Media | Below the 15% engagement threshold (sub-100 likes). Phase 3 keyword sweep on text posts below threshold yielded a 7% signal rate, almost entirely restatements. Image posts below threshold are expected to be motivational graphics or sketch illustrations of concepts already captured. | No action. The 124 high-engagement images already processed captured the annotated email breakdowns and framework diagrams. | P4 | Accepted -- no action |
| G12 | 26 unprocessed articles | Media | Promotional articles, not methodology content per the profile assessment during corpus setup. | No action. | P4 | Accepted -- no action |
| G13 | System 1 / System 2 questioning layers (single signal, P3-B1-6) | Content | Braun maps Kahneman's dual-process theory to cold call question sequencing -- start with easy questions (System 1) before moving to effortful ones (System 2). Appears once (July 2023), never referenced again. Provides a cognitive science foundation for the standard cold call flow (easy opener, then current state, then poke the bear) that the GTM Agent could use for call structure reasoning. | Investigate whether Braun develops this further in video content or external materials. If not, retain as a single-provenance signal in core knowledge with a note that it is unreinforced. Could be validated against general cognitive load literature. | P2 | Open -- investigation |
| G14 | "Reheat campaign" concept (single signal, P3-B1-12) | Content | Named campaign type: calling prospects who evaluated less than 3 months ago but did not buy, mapped to JTBD stage 4--5. Appears once (September 2023). Operationally valuable for pipeline management and has no equivalent in Eric's or Nick's campaign taxonomies. | Check whether the concept appears in video posts or Braun's paid materials. If confirmed as a Braun-originated campaign type, add to the framework layer with single-provenance flag. | P2 | Open -- investigation |
| G15 | Aristotle's Logos/Pathos/Ethos mapped to discovery (single signal, P3-B2-7) | Content | Most sellers over-index on Logos ("They sound like Spock"). This unique theoretical overlay explains why technically correct discovery calls still fail. The GTM Agent could use this for discovery call evaluation -- checking whether a rep is balancing all three persuasion modes. | Retain as a single-provenance signal. The concept is well-established outside Braun's corpus, so it can be validated against general rhetorical theory even without additional Braun reinforcement. | P3 | Open -- investigation |
| G16 | "I do / We do / You do" training framework (single signal, P3-B1-17) | Content | Applied to sales onboarding (December 2023). Most training skips straight to "You do." Named pedagogy framework from education research. Relevant if the GTM Agent ever handles rep onboarding or coaching sequences. | Retain as a single-provenance signal. This is a well-known education framework (gradual release of responsibility) that Braun applied to sales context. Low priority unless the GTM Agent's scope expands to training. | P3 | Open -- investigation |
| G17 | Edelman Trust Barometer stat -- 18% trust (single signal, P3-B4-17) | Content | Only 18% of 32,000 people surveyed trust a salesperson who says "We're here to help." A specific data point that validates the entire detached-seller methodology. Useful as cited evidence in core knowledge. | Verify the Edelman source. If confirmed, add as an evidence signal supporting the detached-seller framework. Strong anchor for the "why" behind Braun's anti-pitch philosophy. | P2 | Open -- investigation |
| G18 | Stanford milkshake/ghrelin study (single signal, P3-B3-20) | Content | Same milkshake, different labels, different biological ghrelin response. Evidence that mindset is not just psychological but physiological. Unique evidence type for the detachment principle. | Verify the study reference (Crum et al., 2011, likely). If confirmed, add as an evidence signal. Strengthens the "detached seller" framework by grounding it in biology rather than just coaching advice. | P3 | Open -- investigation |
| G19 | Altercasting (single signal, P3-B6-10) | Content | Named psychological technique: giving someone a positive label cues them to live up to it. Distinct from Voss labeling (which describes feelings) -- altercasting assigns roles. Appears once (January 2026). Could give the GTM Agent a distinct move beyond standard labeling. | Retain with single-provenance flag. The technique is established in social psychology literature. Braun's contribution is applying it to sales conversations. Check if it appears in his video content. | P3 | Open -- investigation |
| G20 | Four types of false "yes" (single signal, P3-B6-15) | Content | Taxonomy: peace-keeping yes, make-it-stop yes, pressure yes, no-tension yes. Diagnoses no-show meetings and pipeline that goes dark. Operationally useful for the GTM Agent's post-call evaluation. | Retain with single-provenance flag. This is a diagnostic framework the agent could use to flag weak commitments. Braun likely teaches this in more depth in paid content. Worth investigating in video posts. | P2 | Open -- investigation |
| G21 | Eric/Braun infrastructure constraint reconciliation | Agent-readiness | Braun's annotated email examples sometimes include links ("Here's a peek"), named case studies, and emails over 75 words. These violate Eric's operational rules (no links in E1, generalized proof, under 75 words). The Copywriter Agent needs a reconciliation layer so it does not generate Braun-style emails that break Eric's deliverability constraints. | Build a constraint reconciliation table in core knowledge: for each Braun practice that conflicts with Eric's infrastructure rules, specify which rule governs at-scale generation and under what conditions the Braun approach is permissible. | P1 | Open |
| G22 | Graduated quality examples (bad / mediocre / good / great) | Agent-readiness | Most Braun examples are binary: bad vs. good. The Copywriter Agent needs a quality gradient to calibrate its own output, especially the "mediocre" zone where an email checks structural boxes but lacks soul. This is the zone where AI-generated copy fails, and without graduated examples the agent cannot distinguish "correct but soulless" from "correct and human." | Construct graduated examples during core-knowledge synthesis using Braun's own annotated emails. Pick 4--5 emails and build a quality ladder: what makes this one bad, this one mediocre, this one good, this one great. Braun's annotation style already distinguishes elements; the graduation just needs to be made explicit. | P1 | Open |

---

## Priority Summary

| Priority | Count | Gaps | Action |
|----------|-------|------|--------|
| **P1** | 4 | G1 (carousel re-extraction), G2 (AI-copy anti-patterns), G21 (Eric/Braun constraint reconciliation), G22 (graduated quality examples) | Resolve before agent build. G1 is extraction work. G2, G21, and G22 are synthesis work during core-knowledge construction. |
| **P2** | 8 | G3 (video transcription), G4 (voice synthesis), G5 (cold call outcomes), G6 (industry breadth), G13 (System 1/2), G14 (reheat campaign), G17 (Edelman stat), G20 (false "yes" taxonomy) | Resolve during agent build. G3 requires NotebookLM transcription. G4 and G6 are synthesis work. G5 is permanent. G13, G14, G17, G20 are investigation items. |
| **P3** | 6 | G7 (named proof contradiction), G8 (post-discovery), G9 (offer evaluation), G15 (Logos/Pathos/Ethos), G16 (I do/We do/You do), G18 (ghrelin study), G19 (altercasting) | Resolve if time permits. G8 and G9 are accepted limitations. G7 needs a reconciliation rule. G15, G16, G18, G19 are low-urgency investigation items. |
| **P4** | 3 | G10 (pre-2023 content), G11 (low-engagement images), G12 (articles) | No action planned. |

---

## Resolution Methods by Type

**Extraction work** (requires re-running tools on corpus data):
- G1: Vision re-extraction on 5--8 partially extracted carousels (~100 slides)
- G3: NotebookLM batch transcription of top 50 video posts by engagement

**Synthesis work** (requires reasoning over existing signals during Pass 3):
- G4: Voice profile construction from implicit patterns across 481 signals
- G6: Framework-to-industry adaptation mapping from annotated email breakdowns
- G7: Cross-corpus reconciliation rule (Braun named proof vs. Eric data)
- G21: Cross-corpus constraint reconciliation table (Braun practices vs. Eric infrastructure rules)
- G22: Graduated quality ladder built from existing annotated emails

**External curation** (requires sourcing material outside the corpus):
- G2: 5--10 AI-generated cold email specimens for anti-pattern annotation

**Investigation** (requires checking video posts, paid materials, or external sources):
- G13, G14, G15, G16, G17, G18, G19, G20: Eight single-provenance signals that may have deeper treatment in Braun's video content or paid courses

**Permanent / accepted**:
- G5: Braun does not produce quantitative data. Cross-reference with Nick.
- G8: Post-discovery is not Braun's primary domain.
- G9: Offer evaluation comes from Eric and Nick, not Braun.
- G10: LinkedIn API ceiling. Cannot be resolved.
- G11, G12: Below signal threshold. Not worth processing.
