---
type: corpus
aliases: ["Operations: Market Selection & Industry Translation -- Christian Bonnier Retrieval Index"]
corpus: christian-bonnier
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
knowledge_type: "[O]"
provenance: "[D]"
last_updated: 2026-03-20
---

# Operations: Market Selection & Industry Translation -- Christian Bonnier Retrieval Index

The Copywriter Agent uses this file when entering a new vertical or adapting copy for a specific industry. Market selection is upstream of copy -- it determines what slang, personalization, and angles are available.

---

## Niche Selection Methodology

### Leverage Existing Case Studies

If you have proven results in a vertical, target that exact niche first. The case study becomes your CTA: "We did X for a company like yours." (NLM Signal 17)

### "Test and Trim" for Beginners

When you don't have case study data:
1. Cast a wide net across multiple verticals simultaneously
2. Monitor response rates by vertical
3. Strip away underperforming audiences
4. Focus entirely on the most receptive niche

This is a data-driven alternative to gut-feel niche selection. Let the market tell you where you belong. (NLM Signal 17)

### "Boomer Industry" Disruption

Identify verticals where all competitors use static images or outdated methods and enter with modern tactics (video ads, cold email, Loom pitches).

> "There are a lot of boomer industries out there that can be completely disrupted by a proper video ad campaign on Meta. Friend of mine showed me their ads + all of their competitors ads in (redacted) niche and they're ALL static images. Hop in with some direct response video ads and just dominate."
> -- X Signal 13 `[V]`

**Confirmed vertical:** Financial advisors. "All cookie cutter statics in the industry because they're all dinosaurs. And we're slinging video ads + VSL. Clients are printing." (X Signal 25, audience confirmation `[G]`)

---

## Niching Changes Copy in Two Ways

### 1. Mass-Personalized Openers

A tight niche enables openers that apply to everyone on the list without individual research.

| Niche | Opener Example | Source |
|-------|---------------|--------|
| Cosmetics brand | "shopping for my sister's birthday" | NLM Signal 17 |
| FFLs in Florida | "I was looking at FFLs in Florida and found your company's website" | NLM Signal 38 |
| Physicians | "Dr. [Last Name]" formal address | NLM Signal 45 |

### 2. Industry Slang Replacement

Generic marketing language kills response rates. Replace every generic term with the industry's own vocabulary.

---

## Industry Slang Translation Table

This is one of the most concrete, immediately automatable patterns in the corpus. Given an industry, translate generic terms to specific ones. (NLM Signal 31, confirmed `[D]`)

| Industry | Generic Term | Industry Slang | Source |
|----------|-------------|---------------|--------|
| Lawyers | "leads" | "contested divorce cases" or "child custody disputes" | NLM Signal 31 |
| Restaurants | "leads" | "weeknight dine-ins" or "beachgoer tourists" | NLM Signal 31 |
| Pest control | "leads" | "bed bug and termite jobs" | NLM Signal 31 |
| Pest control | "seasonal slowdown" | "winter slowdowns" (pain point) | NLM Signal 31 |
| Trucking | "leads" | "loads" and "shipments" | NLM Signal 31 |
| Trucking | "downtime" | "dead head miles" | NLM Signal 31 |
| Trucking | "full pipeline" | "keeping your board full" | NLM Signal 31 |
| Web design (startups) | "new website" | "raise capital" / "leave a great first impression on VCs" | NLM Signal 50 |
| Bookkeeping | "save money" | "Augusta Rule" / "$20K in personal tax savings" | NLM Signal 51 |
| Bookkeeping | "better accountant" | "Gen Z accounting firm with 24/7 Slack/text access" | NLM Signal 51 |
| Email marketing | "better emails" | "rewrote your welcome flow to optimize for more revenue" | NLM Signal 52 |
| Lead gen | "cold email" | "mix of LinkedIn, cold email, and SMS appointment setting" | NLM Signal 53 |

---

## The Deepseek Slang Injection Process

After writing a generic script, feed it to Deepseek with this exact prompt:

> "Do not make this script any longer or any shorter just change up the messaging to be hyper relevant for [Industry] companies using their lingo, pain points and desires."
> -- NLM Signal 10

This preserves the structure (word count, CTA, offer) while replacing vocabulary with industry-specific terms.

---

## The ChatGPT Pain Point Discovery Process

Before writing copy for a new industry, research pain points:

**Prompt:**
> "What are a few common pain points for [Target Audience] when it comes to marketing their [Business]?"
> -- NLM Signal 10

**Process:**
1. Ask the initial question
2. Drill deeper on the most interesting responses
3. Look for the single "golden nugget" pain point that's specific enough to use in copy
4. The pain point must be something the prospect would recognize immediately as their problem

---

## Specificity as the Primary Differentiator

All three source types converge on this principle:

> "If you want them to let their guard down and read your email, you need to be SPECIFIC."
> -- X Signal 5 `[V]`

> "In cold email, clarity will outperform creativity almost every time because prospects are scanning your email for relevance."
> -- LinkedIn Signal 12 `[V]`

> "Offer Anchoring: strip away marketing jargon, pitch tangible end-results with hyper-specific industry slang."
> -- NLM Signal 22 `[S]`

**Implementation:**
- Replace "leads" with the industry term for what the prospect actually wants
- Replace "growth" with a specific metric they care about
- Replace "results" with a number from a case study
- Replace "marketing" with the specific channel or tactic

---

## The "Use Their Language" Mechanism

> "We interview 100 of your customers and use their language in your email flows."
> -- LinkedIn Signal 8 `[V]`

This is both an offer angle and a market selection principle. The best copy uses the prospect's own vocabulary. Research their world, find their words, use those words in the email.

---

## Personalization Framework (Two Modes)

### Mass Personalization (for Email)

Build a highly segmented list. Write one opening line that applies to everyone on it. Call out job title, or combine location + industry. The line must bridge directly into the pitch, not sit as an isolated compliment.

**When to skip entirely:** If your offer is strong enough (a "no-brainer"), personalization is unnecessary. Jump straight to the pitch. (NLM Signal 14)

### Sniper Personalization (for DMs / Dream 100)

Genuine 1:1 manual research. Reference a specific video, product, or podcast. Aided by Manis for speed. 5-10 per day, never automated. (NLM Signal 14, 15)

**Old process:** 1 hour per prospect (15 min website, 20 min LinkedIn, 15 min case study hunting, 10 min message crafting).
**New process (AI-assisted):** 30 seconds per prospect. (LinkedIn Signal 9)

### Anti-Pattern: AI-Generated First Lines

AI frequently hallucinates (congratulating a prospect on working at a company they never worked for). If you can't verify it, don't include it. (NLM Signal 26)

---

## CTA-to-Persona Matching

Different prospect types respond to different CTA styles. (NLM Signal 30)

| Prospect Type | CTA Type | Reasoning |
|--------------|---------|-----------|
| Visual/creative services | Portfolio or Figma file | They want to see the work |
| Startups | Frame around fundraising ("raise Series A") | Their actual priority |
| Older demographics (lawyers, doctors) | Cell phone number, not Calendly | They don't use scheduling tools |
| Influencers | State payment rate + offer to write the post | They care about pay and minimal effort |
| Brick-and-mortar | Local coffee meeting | In-person is natural for them |

---

## Agency Scaling and Market Selection

As an agency scales, market selection strategy changes:

| Phase | Revenue | Market Strategy | Source |
|-------|---------|----------------|--------|
| Phase 1 | $0-$10K | Take anyone, wide services | NLM Signal 13 |
| Phase 2 | $10K-$50K | One offering, one business type | NLM Signal 13 |
| Phase 3 | $50K ceiling | Same niche, hire to scale | NLM Signal 13 |
| Phase 4 | $100K+ | Add complementary offer, cross-sell | NLM Signal 13 |

> "Finding the winning strategy is 90% of the battle."
> -- LinkedIn Signal 44 `[V]`

> "Once you find a winning marketing strategy you need to spam it until the wheels fall off."
> -- LinkedIn Signal 44 `[V]`

---

## Agent Instructions

When entering a new vertical:
1. Check the industry slang translation table above. If the industry is listed, use those translations.
2. If not listed, run the ChatGPT pain point discovery process and the Deepseek slang injection process.
3. Diagnose market level (1/2/3) before writing any copy. This determines CTA aggression.
4. Use mass personalization for email (job title or location + industry callout).
5. Reserve Sniper personalization for DMs and Dream 100 only.
6. Never use AI-generated first lines without manual verification.
7. Replace every generic marketing term with the industry-specific equivalent.
