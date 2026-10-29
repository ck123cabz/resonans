---
type: campaign-evidence
aliases: ["Campaign Evidence — Eric Nowoslawski Retrieval Index"]
corpus: eric-nowoslawski
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
last_updated: 2026-03-20
---

# Campaign Evidence — Eric Nowoslawski Retrieval Index

All campaign case studies with metrics, organized by performance tier. The Copywriter Agent uses this to calibrate expectations, recommend approaches, and diagnose underperformance.

**Governing metric:** Contacts-per-positive-response. One number tells you everything about message-market fit.

**2025-2026 baseline:** 425 contacts/positive (degraded from 329 in 2023 due to hostile spam environment).

---

## Performance Tier Definitions

| Tier | Contacts/Positive | Meaning |
|------|-------------------|---------|
| Elite | <=150 | Scale immediately. Offer has strong market fit. |
| Above Average | 150-400 | Healthy campaign. Optimize but don't overhaul. |
| Average | 400-800 | Acceptable for some markets. Look for offer refinement. |
| Below Average | 800-1200 | Campaign is struggling. Diagnose: infrastructure, targeting, or offer. |
| Failed | 1200+ | Structural mismatch. Pivot offer, audience, or abandon category. |

**Decision rules:**
- Better than 1:300 = scale
- 1:1000 = pivot direction
- 1,000 contacts with zero positives = no fit, shift direction
- Should see replies within 1-3 iterations; 6 months of iteration with no results = fundamentally broken

---

## Elite Tier (<=150 contacts/positive)

### Forbes / Web Summit Free Listing

- **Industry:** Media / Events
- **Offer:** Free listing on Forbes or Web Summit directory
- **Approach:** Irresistible offer to a narrow, untouched TAM (<2K). Anti-scraping meant inboxes were clean. Minimal copy sophistication needed.
- **Metrics:** 1 positive response per 3 contacts sent (1:3)
- **Provenance:** Campaign doc Signal 205 `[E][G]`
- **Lessons learned:** The offer is the dominant variable. Copy is a multiplier on an offer that already has market fit. Eric: "I almost can't even take credit."
- **Agent instruction:** This is the north star. When an offer is truly irresistible and TAM is small/clean, even mediocre copy works. Do not over-invest in copy optimization when the offer itself is the differentiator.

### Google Reputation Management

- **Industry:** Local business (restaurants, hotels, service providers)
- **Offer:** "We'll try to get your negative Google review removed. You only pay if we succeed."
- **Approach:** Reference specific negative review by reviewer name. Performance-based pricing = zero risk. Publicly verifiable problem (anyone can check their Google reviews).
- **Metrics:** 1 positive response per 70 contacts (1:70)
- **Provenance:** Signal 116 `[E][G]`, LinkedIn 147 `[V]` (confirmed 1:70 with HubSpot+Smartlead+Clay stack)
- **Lessons learned:** Low-friction, publicly-verifiable, performance-based offers dramatically compress the contacts-per-positive ratio. "Doctor diagnosing" positioning at its purest -- you found the problem (their negative review), you show it to them, you offer to fix it risk-free.
- **Agent instruction:** This is the canonical "show don't tell" campaign. The email contains evidence of the problem (specific review) and a risk-free solution. Model new campaigns on this structure when possible.

### Social Listening Campaign

- **Industry:** Various (signal-dependent)
- **Offer:** Relevant outreach triggered by prospect's recent social media post
- **Approach:** AI summarizes their recent post in <8 words, connects to value prop
- **Metrics:** 1 positive response per 15 contacts (1:15)
- **Provenance:** LinkedIn 100 `[V]`
- **Lessons learned:** Signal-triggered outreach dramatically outperforms cold outreach, but only 5-15% of TAM will have signal triggers at any given time. Must pair with fallback campaigns for the remaining 85-95%.

---

## Above Average Tier (150-400 contacts/positive)

### Clay (Internal Campaign)

- **Industry:** SaaS (sales tooling)
- **Offer:** Creative Ideas campaign -- AI-generated use cases for how prospects could use Clay
- **Approach:** 3 constrained AI-generated bullet points per prospect. No signal required (works as fallback).
- **Metrics:** 1 positive response per 10.6 contacts (1:10.6) -- best in GEX leaderboard
- **Provenance:** Campaign doc Signal 205 `[E][G]`
- **Lessons learned:** This is Eric's internal campaign for a product he knows deeply. The extreme ratio (1:10.6) reflects both offer quality AND operator expertise. Do not use this as a benchmark for client campaigns.

### Taplio

- **Industry:** SaaS (social media tooling)
- **Offer:** Creative Ideas campaign with LinkedIn-specific use cases
- **Approach:** AI-generated ideas for how prospects could use Taplio for LinkedIn growth
- **Metrics:** Above average (specific number in Campaign doc leaderboard)
- **Provenance:** Campaign doc `[V]`
- **Lessons learned:** Creative Ideas template works especially well for tools where the use cases are varied and the prospect may not have considered all applications.

### Funded Companies (VC-Backed Startups)

- **Industry:** Various (startup-focused services)
- **Offer:** Services targeting recently funded companies
- **Approach:** Use funding announcement as recency signal. "Congratulations on your Series A" is the hook.
- **Metrics:** Above average range
- **Provenance:** Campaign doc `[E][G]`
- **Lessons learned:** Funding is one of the strongest recency signals because it creates budget and urgency simultaneously. However, every SDR in the world targets funded companies, so differentiation in the copy matters more here than in less crowded signal categories.

### Financial Services (After Pivot)

- **Industry:** Financial services / Tax advisory
- **Offer:** Tax strategy / depreciation advisory (pivoted from investment pitch)
- **Approach:** "Poke the bear" -- "How do you know your current tax accountant is using every legal loophole to get you the most money back?"
- **Metrics:** "Transformed results" after pivot from investment pitch
- **Provenance:** Signal 210 `[E][G]`, Signal 199 `[K][V]`
- **Lessons learned:** The controlled A/B test -- same list, same volume, same AI icebreaker, only value prop framing changed -- produced orders of magnitude improvement. This is the cleanest evidence that offer framing is the most important controllable variable.

---

## Average Tier (400-800 contacts/positive)

### Marketing Agency Campaigns (Typical)

- **Industry:** Marketing agencies
- **Offer:** Various agency services to B2B companies
- **Approach:** "Chunk up" to outcomes rather than selling services. Give massive upfront value.
- **Metrics:** 400-800 range (industry-dependent)
- **Provenance:** Campaign doc `[V]`
- **Lessons learned:** Agencies face the "commoditized service" challenge. Every agency says the same thing. The differentiator is either the lead magnet (5,000 free validated leads) or the flash roll (reveal the mechanism that makes your approach unique).

### SaaS (Mid-Market, Standard Offer)

- **Industry:** SaaS
- **Offer:** Standard product demo or trial offers
- **Approach:** Creative Ideas or standard GEX template
- **Metrics:** Average range when offer is standard; above average when Creative Ideas is deployed
- **Provenance:** Campaign doc + LinkedIn `[V]`
- **Lessons learned:** "Free trial" rarely works cold for SaaS because time-to-value is too long. Better to offer "knowledge arbitrage" -- insights, benchmarking data, or trends from your user base.

### Cleaning Equipment

- **Industry:** Industrial / Commercial cleaning
- **Offer:** Equipment for commercial cleaning operations
- **Approach:** Line-by-line annotated email with strategy notes for each section
- **Metrics:** Average range
- **Provenance:** LinkedIn 048 `[V]`
- **Lessons learned:** Even in unsexy B2B industries, the GEX template structure works. The key is finding the specific problem (e.g., equipment maintenance costs, compliance requirements) and "poking the bear" on it.

---

## Below Average Tier (800-1200 contacts/positive)

### Outsourced RevOps

- **Industry:** Revenue operations consulting
- **Offer:** Outsourced RevOps services
- **Approach:** Standard outbound
- **Metrics:** 1 positive per 1,858 contacts (1:1,858)
- **Provenance:** Signal 211 `[E][G]`
- **Lessons learned:** Eric says this "makes me scratch my head the most." The problem may be structural -- companies that need RevOps help often don't know they need it, making cold email a poor awareness channel for this category. Eric's "biggest blunder" category.

### Developer Tools (Targeting ICs)

- **Industry:** Developer tools
- **Offer:** Various dev tools
- **Approach:** Targeting individual contributors (developers) rather than decision-makers
- **Metrics:** 1 positive per 1,838 contacts (1:1,838)
- **Provenance:** Signal 211 `[E][G]`
- **Lessons learned:** ICs are the wrong target for cold email. Developers especially hate cold email and rarely have purchasing authority. Target engineering managers or VPs of Engineering instead.

### Staffing (Undifferentiated)

- **Industry:** Staffing / Recruiting
- **Offer:** Undifferentiated staffing services
- **Metrics:** 1 positive per 1,687 contacts (1:1,687)
- **Provenance:** Signal 211 `[E][G]`
- **Lessons learned:** Staffing is on Eric's explicit exclusion list. The category is too commoditized -- every staffing firm says the same thing, and hiring managers are bombarded with identical pitches. Eric will not take staffing clients.

---

## Failed Tier (1200+ contacts/positive)

### Cybersecurity

- **Industry:** Cybersecurity
- **Offer:** Security assessment / vulnerability scanning
- **Approach:** Creative -- scanned open ports, matched to breach data. Technically sophisticated targeting.
- **Metrics:** 1 positive per 5,121 contacts (1:5,121)
- **Provenance:** Signal 206 `[E][G]`
- **Lessons learned:** Buyers are unresponsive until an incident occurs. This is a structural category mismatch -- no amount of copy sophistication can overcome the fact that cybersecurity buyers do not respond to proactive outreach. Even the creative approach (scan ports, match breaches) failed completely. On Eric's exclusion list.

### Web Development

- **Industry:** Web development / Design agencies
- **Offer:** Web development services
- **Metrics:** 1 positive per 2,568 contacts (1:2,568)
- **Provenance:** Signal 212 `[E][G]`
- **Lessons learned:** Commoditized category with no differentiation. Every web dev shop says the same thing.

### Benefits Administration

- **Industry:** HR / Benefits
- **Offer:** Benefits administration services
- **Metrics:** 1 positive per 2,966 contacts (1:2,966)
- **Provenance:** Signal 212 `[E][G]`
- **Lessons learned:** "Nice to have" problem. No urgency. Companies only switch benefits providers at renewal time, and they have long contracts. Cold email is poorly suited for products without urgency.

### Enterprise Compliance

- **Industry:** Compliance / Regulatory
- **Offer:** Compliance software
- **Metrics:** 1 positive per 4,265 contacts (1:4,265)
- **Provenance:** Signal 212 `[E][G]`
- **Lessons learned:** 11 campaigns tested, FTSE 1000 targets. Eric's rule: never take enterprise compliance without client having an existing sales team. The sales cycle is too long and the decision-making process too complex for cold-email-only approach.

### Team Culture

- **Industry:** HR / Culture
- **Offer:** Team culture building services
- **Metrics:** 0 total positive responses across 12 campaigns
- **Provenance:** Signal 212 `[E][G]`
- **Lessons learned:** The ultimate proof that execution cannot overcome category mismatch. Zero responses across 12 separate campaigns means the category is fundamentally incompatible with cold email. This is Eric's most extreme failure data point.

---

## Category Exclusion List

Eric explicitly will not serve these categories:

| Category | Reason | Provenance |
|----------|--------|------------|
| Staffing (undifferentiated) | Commoditized, inbox overload | Signal 219 `[M][V]` |
| Payment processing | Commoditized | Signal 219 `[M][V]` |
| IT outsourcing | Commoditized | Signal 219 `[M][V]` |
| Cybersecurity | Buyers unresponsive until incident | Signal 219 `[M][V]` |
| Enterprise (Fortune 5000 / FTSE 1000) | Only with existing sales team | Signal 219 `[M][V]` |

### Three Failure Patterns

1. **"Nice to have"** = no urgency (benefits administration, team culture)
2. **No differentiation** in commoditized category (staffing, payment processing, web development)
3. **Enterprise-scale targets** require existing warm sales infrastructure (compliance, FTSE 1000)

---

## Key Evidence Links

### Offer Dominance

The 1,700x spread between best (Forbes 1:3) and worst (cybersecurity 1:5,121) campaigns run by the same agency with the same infrastructure proves the offer is the dominant variable.

- **Attribution split:** 30% agency execution / 70% client offer quality (Eric's estimate)
- **Copy quality multiplier:** ~3-5x band (good copy vs. bad copy on same offer)
- **Offer quality multiplier:** ~1,000x band (good offer vs. bad offer with same copy)

**Agent instruction:** Always prioritize offer diagnosis before copy optimization. If a campaign is performing at 1:1000+, the problem is almost certainly the offer, not the copy.

### CTA Impact

- Calendar link CTA to interest-based question: **5x increase** in positive responses
- "Reply with address" to "I'll show you on a call": **162% increase** in meetings
- "Here's a resource" to "I'll show you on the call how it applies": **3x meetings**

### AI Personalization Impact

- Generic AI personalization ("I saw you sell to fitness coaches"): **143% fewer replies** than no personalization
- AI company analogies: **zero positive responses** (tested and dropped)
- College-based personalization: campaign shut down in 2 days due to offensive responses
- Constrained AI snippets in human templates: **won 9-experiment comparison**

### Post-Reply Conversion Data Points

| Campaign | Replies | Opportunities | Rate |
|----------|---------|---------------|------|
| Campaign A | 122 | 27 | 22% |
| Campaign B | 302 | 104 | 34% |
| Campaign C | 859 | 77 | 9% |
| Campaign D | 189 | 32 | 17% |
| Campaign E | 642 | 225 | 35% |

Note: Eric intentionally does not track global post-positive conversion rates. "If I could totally control the revenue, I might as well run your business." The Copywriter Agent should use contacts-per-positive-response as its primary metric and not attempt to forecast downstream conversion.

---

## Temporal Degradation

| Metric | 2023 | 2025-2026 | Change |
|--------|------|-----------|--------|
| Average contacts/positive | 329 | 425 | 29% worse |
| Sending volume/inbox | 50/day | 30/day | 40% reduction |
| Sequence length | 3-4 emails | 2-3 emails | Shorter |
| Warm-up duration | 3-4 weeks | 4-6 weeks | Longer |
| GEX scale | 5,562 accounts | 71,000 inboxes | ~13x growth |

**Agent instruction:** Use 2025-2026 baselines for all recommendations. 2023 figures are historical context only.
