---
type: corpus
aliases: ["Gap Register: Adam Erhart"]
corpus: adam-erhart
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-19
---

# Gap Register: Adam Erhart

**Layer 3.** What this corpus does not know, why it matters, and what would resolve it. Consolidated from Pass 2 Section 5. Two gaps were closed during the pass by follow-up queries.

An agent working from this corpus should escalate rather than assert when a question lands in here.

---

## The structural limit

Everything in `core-knowledge.md` and `retrieval-index/` is Gemini's synthesis of video transcripts. There is no first-order Erhart writing in the corpus, so nothing reaches high confidence.

The practical consequence: an agent can say "Erhart teaches X" and be on solid ground. It cannot say "Erhart said X" and quote him, because what the corpus holds is a paraphrase of a transcript of a video, three steps from his keyboard. The quoted scripts are the exception worth watching, they read as verbatim and are probably close, but they have not been checked against a source video.

---

## Open gaps

### High priority

**1. No first-order source.**
Nothing Erhart wrote himself is in the corpus, so no `[S]` → `[D]` upgrade is possible and the ceiling stays Medium.
*Resolves by:* scraping adamerhart.com, his newsletter, X and LinkedIn, then confirming the named frameworks appear in his own words.

**2. Twenty statistics carry the pitch, unsourced.**
62% of local calls unanswered. 85% of voicemail-hitters never calling back. 78% buying from whoever responds first. A 391% conversion lift at one minute. A 100x drop past five minutes. 42–48 hour average response time. 76% agency churn at 90 days. 68% taking the pre-selected middle option. 90% of businesses failing. 82% of bankruptcies from cash flow. 0.7% cold email conversion. 25–30% cold email open rates. 40–60% of deals lost to no decision. 67% of "almost ready" prospects never returning. 80% of sales needing five follow-ups against 44% quitting at one and 94% at four. 97% of consumers checking reviews. 70–80% of routine questions handled by conversation AI. 95% SMS read rate within three minutes. 8–15% reactivation conversion. 38-month warm-water retention.

These carry the entire argument for the AI service stack, the audit method and the follow-up cadence. If any is wrong, the argument built on it is wrong.
*Resolves by:* tracing each to a primary source, or marking it unsupported wherever it is reused.

**3. Eleven `[G]` citations unverified.**
Carpenter's 2013 BYAF meta-analysis. Kahneman and Tversky on loss aversion. Iyengar's jam study. Rackham's SPIN research. Bandura's self-efficacy work and the 1991 Molton/Brown/Lent review. The GatherUp local AI study and the GatherUp recency finding. The Harvard Business School star-rating paper. Two Cornell lifetime-value papers. Stanford and MIT on cognitive half-life. Brehm on psychological reactance.

These are the corpus's only route above Medium confidence and are currently taken on trust. Erhart's characterisation of a study may not match what the study found.
*Resolves by:* reading the originals.

**4. No dates on any claim.**
The notebook exposes no per-video timestamps through query, so a 2019 claim and a 2026 claim read identically. Tool pricing and platform behaviour rot fastest: HighLevel plan prices, Meta ad settings, Ask Maps behaviour, what the AI models do with reviews.
*Resolves by:* pulling the notebook's source list with titles and publish dates, then re-anchoring every time-sensitive claim.

### Medium priority

**5. The AI receptionist's real price.**
Six values across the corpus, $247, $297, $397, $400, $497, $500, with barely a change in the service description. Most likely he raised it over a period the corpus cannot date.
*Resolves by:* dating the sources, or checking his current offer pages.

**6. Agency OS contents.**
Referenced across a dozen answers as the thing that makes the 48-hour launch work. The corpus describes the container: snapshots, workflows, scripts, a 90-day roadmap. It is a paid product, so the contents sit behind a paywall.
*Resolves by:* accepting it as out of scope, or buying it. Anything an agent generates about "the Agency OS" beyond the container description is invention.

**7. All client results self-reported.**
The landscaping client's 9 reviews in 6 days, the dental practice at #1 with bookings up 25%, the roofer passing 150 reviews in 90 days, the 500-customer reactivation, the 21.5-hour ranking claim, "$5 million closed without a proposal." No independent confirmation of any of it.
*Resolves by:* nothing available. Treat as claims, never as evidence.

**8. No visual material.**
HighLevel builds, ad account walkthroughs, funnel layouts and Figma-style screen work do not survive text synthesis. Where a build step is under-specified, the corpus cannot supply it.
*Resolves by:* targeted re-watch of the specific video.

### Low priority

**9. The single-variable rule against Dynamic Creative.**
He recommends testing one variable at a time and waiting for significance, and separately recommends Dynamic Creative varying three texts, three headlines and three visuals at once. He never reconciles it.
*Resolves by:* one follow-up query, or treating them as different phases (discovery versus isolation) and saying so.

**10. Nothing on pricing a first client with no case studies.**
The sliding scale says open at $197–$297 or a free trial and climb after three case studies. What he does not cover is how to handle a first prospect who asks for references, beyond the Systems Proof and Adventurer Frame moves.
*Resolves by:* a follow-up query.

**11. The two price ladders are never connected.**
Local retainers run $197–$1,191/mo. The Black Sand and choice-architecture tiers run $497 / $5,000 / $12,000. The second is clearly his consulting ladder rather than the agency service ladder, but he never says which prospect gets which, or how you move between them.
*Resolves by:* a follow-up query on how the consulting offer relates to the agency offer.

---

## Closed during this pass

**Nothing on failure rates**, closed 2026-09-16 by Q43. Returned ten of his own priced failures, four client campaigns that failed, the four causes of churn with the numbers, the 3/10/87 buyer-timing split, the real timelines against expected ones, and the survivorship-bias argument. Signals 126–130, written into `retrieval-index/agency-operations.md`.

**The email and nurture lane was compressed**, closed 2026-09-16 during Pass 3. The q37 material was already in the corpus but had only a pointer signal against it. Now extracted whole into `retrieval-index/email-sequences.md`: six sequence structures with intervals, four subject-line rules with examples, body structure per email type, three segmentation models, and all ten templates at full wording.

**Whether dentists and chiropractors are in or out**, closed 2026-09-16 by Q44. Returned runway versus destination: crowded niches are proven and profitable, wrong as a starting block, and enterable with prior domain background, post-runway proof, a drilled-down sub-niche, or warm relationships. Signal 131, written into `retrieval-index/niche-playbooks.md`.

---

## Where an agent should escalate rather than answer

- **Any specific number presented as fact.** The corpus holds the number; it does not hold the source. Say "Erhart cites X" and not "X is true."
- **Anything about the Agency OS beyond its container description.**
- **Anything time-sensitive**, platform pricing, ad manager settings, AI search behaviour. The corpus cannot date itself.
- **Client results.** Self-reported throughout.
- **Compliance in a jurisdiction other than the US.** The no-review-gating rule cites Google's terms and FTC regulations. Neither was checked, and neither is universal.
- **Anything requiring his own words verbatim.** The corpus is three steps from his keyboard.
