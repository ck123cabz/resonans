---
type: infrastructure-reference
aliases: ["Infrastructure Reference — Eric Nowoslawski Retrieval Index"]
corpus: eric-nowoslawski
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
last_updated: 2026-03-20
---

# Infrastructure Reference — Eric Nowoslawski Retrieval Index

Quick-reference for infrastructure constraints the Copywriter Agent needs when advising on campaign setup. These are hard rules that override methodology preferences.

---

## 1. Domain Management Rules (2025-2026)

| Rule | Value | Source | Provenance |
|------|-------|--------|------------|
| Domain extensions | `.com` and `.co` only | Q13 | `[S]` |
| Domain naming | Generic names acceptable if forwarded to main site | Q13 | `[S]` |
| Purchase source | Porkbun or Dynadot (buy during sales) | Q13 | `[S]` |
| Domain aging | 4-6 weeks before sending (critical for Outlook/Proofpoint) | Q38, LinkedIn 139 | `[S]` + `[V]` |
| Rotation system | Three-set: active / on-deck / aging | LinkedIn 139 | `[V]` |
| Insurance pool | 1:1 ratio (equal number of backup domains ready) | Q13, Q15 | `[S]` |
| DNS requirements | SPF, DKIM, DMARC perfectly configured. Custom tracking domains. | Q13 | `[S]` |
| Burn response | Cancel immediately. Dead inboxes never recover. Hot-swap from insurance pool. Purchase replacement same day. | Q13, Q14, Campaign doc | `[S]` + `[V]` |

### Three-Set Rotation System

```
SET A: ACTIVE — Currently sending campaigns
SET B: ON-DECK — Warmed up, aged, ready to swap in when Set A burns
SET C: AGING — Recently purchased, sitting unused to build domain age

Cycle: When Set A domain burns → swap in from Set B → move
replacement purchase to Set C → Set C graduates to Set B
after 4-6 weeks of aging
```

**Key evolution:** Domain aging is the "new secret weapon" in 2025. Standard warm-up alone is no longer sufficient. Buy during Porkbun/Dynadot sales, let domains sit unused for months before activating.

---

## 2. Inbox Setup Protocol

| Rule | Value | Source | Provenance |
|------|-------|--------|------------|
| Inboxes per domain | 2-3 | Q13, Campaign doc | `[S]` + `[V]` |
| Provider strategy | Gmail-first for 2-3 weeks, then swap aged domains for Outlook/Proofpoint | Q38 | `[S]` |
| Scale direction | Horizontal only (more inboxes), NEVER vertical | Q15, Q31 | `[S]` |
| Warm-up reserve | 50% of total capacity always in warm-up | LinkedIn 201 | `[V]` |

### Provider Launch Sequence

```
Week 1-3: Launch on Gmail (easier deliverability)
  └── Simultaneously: age backup domains for Outlook
Week 4-6: Swap aged domains into Outlook/Proofpoint
  └── Gmail continues sending
Week 6+: Both providers running
  └── Monitor deliverability per provider separately
```

**Rule:** Never scale vertically (sending more per inbox). Always scale horizontally (more inboxes). The 30/day/inbox limit is not negotiable for new Google inboxes.

---

## 3. Warm-Up Timelines

| Parameter | Gmail (SMB targets) | Outlook/Proofpoint (Enterprise targets) |
|-----------|--------------------|-----------------------------------------|
| Warm-up duration | 2-3 weeks | 4-6 weeks (up to 2 months for high-security) |
| Daily ramp | +5 emails/day | +5 emails/day |
| Daily cap | 50 warm-up emails/day | 50 warm-up emails/day |
| Response rate setting | 20-40% (Eric uses 32%) | 20-40% (Eric uses 32%) |
| Launch strategy | Send after warm-up | Gmail-first, then swap aged domains for Outlook at 4-6 weeks |

**Critical rules:**
- Never set 100% response rate -- looks unnatural when real cold emails get lower engagement
- Domain aging is now as important as warm-up: buy domains, let them sit unused, THEN warm up
- 50% of total inbox capacity should always be in warm-up (reserve ratio)

### Warm-Up Daily Ramp Schedule

```
Day 1:   5 warm-up emails
Day 2:  10 warm-up emails
Day 3:  15 warm-up emails
Day 4:  20 warm-up emails
Day 5:  25 warm-up emails
Day 6:  30 warm-up emails
Day 7:  35 warm-up emails
Day 8:  40 warm-up emails
Day 9:  45 warm-up emails
Day 10: 50 warm-up emails (cap reached)
...continue at 50/day until warm-up period complete
```

---

## 4. Email Validation Waterfall (Definitive Order)

```
Input: Raw email from data provider
  |
  +-- Step 1: DEBOUNCE (primary validator -- cheapest, broadest coverage)
  |     +-- Valid? --> PASS to campaign
  |     +-- Invalid? --> Continue
  |
  +-- Step 2: ZEROBOUNCE (secondary -- different methodology catches Debounce misses)
  |     +-- Valid? --> PASS
  |     +-- Invalid? --> Continue
  |
  +-- Step 3: INSTANTLY.AI VERIFIER (tertiary -- different infrastructure)
  |     +-- Valid? --> PASS
  |     +-- Invalid? --> Attempt to FIND correct email
  |
  +-- Step 4: LEAD MAGIC (primary finder -- highest coverage for new emails)
  |     +-- Found? --> Re-validate and PASS
  |     +-- Not found? --> Continue
  |
  +-- Step 5: PROSPEO (secondary finder -- good catch-all handling)
  |     +-- Found? --> Re-validate and PASS
  |     +-- Not found? --> Continue
  |
  +-- Step 6: ICPS (tertiary finder)
  |     +-- Found? --> Re-validate and PASS
  |     +-- Not found? --> Continue
  |
  +-- Step 7: KIT (quaternary finder -- last resort)
  |     +-- Found? --> Re-validate and PASS
  |     +-- Not found? --> SKIP contact
  |
  +-- CATCH-ALL DOMAIN DETECTED AT ANY STEP:
        +-- Stop waterfall. Trust Prospeo or BounceBan result.
        +-- Rationale: catch-all domains accept ALL emails during
            validation but may bounce during actual send. Only
            specialized providers can predict real deliverability.
```

**Rule:** Never trust raw email data from any single source. Bounce rate must stay under 2%. The waterfall order matters because each provider has different coverage strengths -- running them in sequence maximizes valid email recovery while minimizing cost (cheapest/highest-coverage first).

---

## 5. Scaling Formula (Canonical)

```
INPUTS:
  meetings_needed_per_month          (business goal)
  meeting_conversion_rate            (positive response to meeting -- use 20% as rough default)
  contacts_per_positive_response     (use 425 as 2025-2026 baseline)
  tam_size                           (total addressable market)

COMPUTE:
  positive_responses_needed = meetings_needed / meeting_conversion_rate
  daily_sends_needed = (positive_responses_needed * contacts_per_positive_response) / 22
  inboxes_needed = daily_sends_needed / 30          (2025-2026 rate per inbox)
  domains_needed = inboxes_needed / 2.5             (midpoint of 2-3 per domain)
  insurance_domains = domains_needed                (1:1 ratio)
  warmup_reserve = inboxes_needed                   (50% always warming)
  total_domains = domains_needed + insurance_domains
  total_inboxes = inboxes_needed + warmup_reserve

CONSTRAINTS:
  IF tam_size < 100K:  WARN -- may be insufficient for repeatable automated outbound
  IF tam_size < 20K:   cold email alone insufficient, must use omnichannel
  IF daily_sends > tam_size / 90:  WARN -- will exhaust TAM in <90 days (pace rule)
```

### Example Calculation

```
Goal: 10 meetings/month
Conversion rate: 20% (positive response to meeting)
Contacts/positive: 425 (2025-2026 baseline)

positive_responses_needed = 10 / 0.20 = 50
daily_sends_needed = (50 * 425) / 22 = 966
inboxes_needed = 966 / 30 = ~33
domains_needed = 33 / 2.5 = ~14
insurance_domains = 14
warmup_reserve = 33
total_domains = 28
total_inboxes = 66
```

### Sending Rates

| Parameter | 2025-2026 Value | 2023 Value |
|-----------|----------------|------------|
| Cold emails per inbox per day | 30 (new Google inboxes) | 50 |
| Conditional ramp | Start 30; push to 50 only after proven good response rate | Start 30; push 50 after good rate |
| Conservative / Hypertide rate | ~15/day (mimics human behavior) | Same |
| GEX scale (reference) | 71K inboxes, 3M emails/month | 5,562 accounts, 800K-1.55M/month |

**Critical update:** The drop from 50/day to 30/day on new Google inboxes means 67% more inboxes are needed for the same daily volume. This changes every infrastructure sizing calculation.

---

## 6. Kill Triggers and Diagnostic Protocol

### Kill Triggers (Immediate Action Required)

| Metric | Threshold | Action |
|--------|-----------|--------|
| Reply rate | <1% (excluding OOO) | Assume burned, rotate domains |
| Bounce rate | >2% (especially 550 errors) | Immediate kill |
| Warm-up health | <100% | Burn signal, investigate |
| Reputation score | <95% | Alert, prepare swap |
| Open rate (diagnostic) | <38% on 2-day test | Likely spam |
| Open rate (definitive) | ~10% on 2-day test | Definitively in spam, kill immediately |
| Negative sentiment | Any cursing/hostility in replies | Turn off campaign immediately, don't just swap |

### Diagnostic Protocol (Sequenced)

```
Step 1: Check reply rate
  +-- If <1% (excluding OOO) --> proceed to Step 2
  +-- If >=1% --> problem is messaging, not infrastructure

Step 2: Turn on open tracking for exactly 2 days
  +-- IMPORTANT: open tracking is diagnostic ONLY, never leave on

Step 3: Evaluate open rate
  +-- ~10% opens --> DEFINITIVELY IN SPAM. Kill inbox immediately.
  +-- 40-60%+ opens --> Inbox is fine. Problem is messaging.
  +-- 20-38% opens --> Borderline. Check Steps 4-5.

Step 4: Check MX Toolbox for blacklists (supplemental)

Step 5: Check bounce rate for 550 errors
  +-- >2% bounce rate --> Kill inbox, validation waterfall failed

Step 6: If inbox is healthy but messaging is failing:
  +-- Reframe offer (poke the bear)
  +-- Chunk up or chunk down
  +-- Move prospect higher up funnel (demand generation)
  +-- "Give it away free" test -- if free offer still refused,
      problem is core offer/market, not copy
```

### Diagnostic Hierarchy

When a campaign underperforms, diagnose in this order:
1. **Infrastructure** -- Are inboxes burned? (kill triggers above)
2. **Volume** -- Are enough Email 1s going out? (minimum 1,000 contacts per test batch)
3. **Messaging** -- Does the offer have market fit? (contacts-per-positive metric)

**Rule:** Do not optimize messaging if the infrastructure is burned. Fix infrastructure first.

---

## 7. Email Formatting Constraints

| Rule | Scope | Notes |
|------|-------|-------|
| Plain text only | All emails | No HTML formatting ever |
| Zero links in E1 | Including signature links | Links acceptable in E3+ for lead magnets |
| Zero images in E1 | Including signature images | Exception: image IS the evidence (negative review screenshot, bed bug meme) |
| No tracking pixels | All emails | Turn off open and link tracking entirely |
| No Calendly links | First touch | Acceptable ONLY after positive reply, paired with 2 manual time options |
| No unsubscribe link | Replace with text | "If this isn't relevant, let me know" (unless legally required) |
| No HTML signatures | All emails | Minimal or no signature in E1 |
| Custom tracking domains | If any tracking used | Required for deliverability |

---

## 8. Infrastructure Evolution Timeline (2022-2025)

| Dimension | 2023 State | 2025-2026 State | Change Driver |
|-----------|-----------|-----------------|---------------|
| Sending volume | 50/day/inbox | 30/day/inbox (new Google) | Gmail spam filter tightening |
| Warm-up duration | 3-4 weeks standard | 4-6 weeks standard, up to 2 months enterprise | Domain age critical for Outlook/Proofpoint |
| Domain management | Ad-hoc hot-swap | Three-set rotation (active/on-deck/aging) | Longer aging requirement demands systematic pipeline |
| Provider strategy | Google-only | Gmail-first, then swap aged for Outlook | Proofpoint specifically requires domain age |
| Open tracking | Used as delivery proxy | Turn off entirely; diagnostic-only 2-day test | Apple iOS inflation made open rates unreliable |
| Spintax | Acceptable, widely used | Heavy spintax (15+ variations) hurts performance | Spam filters detect spintax patterns |
| Sequence length | 3-4 emails standard | 2-3 emails, trending shorter | Worsened spam environment raises cost per touch |
| AI role | 5-12 word snippets in human templates | Dynamic full-variable emails ($0.02 each) | AI cost decrease + quality improvement |
| Scale reference | 5,562 accounts, 800K-1.55M/month | 71K inboxes, 3M/month | ~4x growth in 2 years |
| Golden ICP | 5-trigger multi-filter segmentation | 1-2 strong signals + broad fallback | Over-segmentation reduces volume without proportional quality gain |
| Seed testing | Not mentioned | Explicitly against: "never seed-test" | Live diagnostics preferred over synthetic testing |
| Unsubscribe | Standard link | Remove link; replace with "let me know" phrasing | Manual reply boosts sender reputation |
| AI snippet length | 5-12 words | 2-7 words | Constraint tightened over time |
| Contacts/positive baseline | 329 average | 425 average | 29% degradation from hostile spam environment |

---

## 9. Spam Word Avoidance

| Tier | Words/Patterns | Impact |
|------|---------------|--------|
| Immediate triggers | "Bitcoin," "Viagra," "Jesus," "Oprah" | Instant spam folder |
| Secondary "marketer" words | "Free," "guaranteed," "limited time" | Elevated spam scoring |
| AI-tell words | "Leverage," "synergy," "innovate," "optimize," "disrupt," "amazing" | Signals AI-generated or marketing copy |
| Identity-signal phrases | "Hope this finds you well," "Just checking in," "My name is..." | Marks sender as salesperson, not colleague |

**Reference:** HubSpot spam word list for comprehensive secondary triggers.

---

## 10. Tool Stack Quick Reference

### Required (Tier 1)

| Tool | Role |
|------|------|
| Clay.com | Enrichment orchestration + AI scoring |
| Smartlead.ai | Sending platform (advanced/agencies) |
| Apollo.io | Contact sourcing (270M+ contacts) |
| LinkedIn Sales Navigator | Intent signals + contact discovery |

### Email Validation (Tier 2, Waterfall Order)

| Order | Validation | Finding |
|-------|-----------|---------|
| 1 | Debounce | Lead Magic |
| 2 | ZeroBounce | Prospeo |
| 3 | Instantly.ai verifier | ICPS |
| 4 | -- | Kit |
| Catch-all | -- | Prospeo or BounceBan |

### Specialized Data (Tier 3)

| Tool | Market Type |
|------|------------|
| Harmonic.ai | SaaS company data |
| Ocean.io / Disco | Lookalike company finding |
| BuiltWith | Website technographics |
| D7 / Outscraper / Apify | Local business (Google Maps) |

### AI Models

| Model | Use Case | Cost |
|-------|----------|------|
| GPT-4o mini | Primary for all enrichment and snippet generation | Fractions of a cent per variable |
| GPT-4o / Claude | Complex reasoning (escalation only) | 10-50x more expensive |
| Gemini Flash | Needle-in-haystack tasks | Specialized use |
| Claygent | Unstructured web scraping | Per-call pricing |

### Explicitly Excluded Tools

| Tool | Reason |
|------|--------|
| HubSpot (for sending) | Marketing tool, not cold email. Damages deliverability. |
| Mailchimp | Marketing email, not cold outreach. |
| Constant Contact | Same category. |
| Outreach.io | Enterprise sales tools not optimized for cold email. |
| SalesLoft | Same as Outreach. |
| Zapier | Make.com preferred. Shift toward Cursor for direct API. |
