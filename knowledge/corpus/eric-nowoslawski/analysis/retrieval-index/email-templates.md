---
type: email-templates
aliases: ["Email Templates — Eric Nowoslawski Retrieval Index"]
corpus: eric-nowoslawski
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
last_updated: 2026-03-20
---

# Email Templates — Eric Nowoslawski Retrieval Index

All complete or near-complete email templates extracted from the corpus. The Copywriter Agent pulls from these when generating email sequences.

---

## 1. Canonical GEX Template Structure (Message-Market Fit Sequence)

**Campaign type:** Standard outbound sequence
**When to use:** Default for all new campaigns. 3-4 emails unless TAM dictates otherwise.
**Provenance:** Campaign doc `[V]` + NotebookLM `[S]` (confirmed across all sources)

### Email 1: Initial Spear

**Line-by-line framework:**

```
Subject: {{internal_camouflage_subject}} (2-3 words, mismatched casing)

{{Line 1: "Why you, why now" — recency/relevance hook}}

{{Line 2: Enablement statement OR "poke the bear" question}}

{{Line 3: Social proof with quantifiable result (generalized, not named)}}

{{Line 4: Low-friction interest-based CTA}}
```

**Constraints:**
- Under 100 words (target ~75)
- 5th grade reading level
- Plain text only, no HTML
- Zero links including signature
- Zero images
- No tracking pixels
- CTA generates a reply, not a click

**Template example (Google Reputation Management):**

```
Subject: question about review

Hey {{first_name}},

I was looking at {{company}}'s Google reviews and noticed
you have a {{star_rating}} review from {{reviewer_name}} that
mentions {{specific_complaint}}.

We help businesses get negative reviews removed -- you only
pay if we succeed.

If getting that review taken down would be useful, would you
be open to hearing how it works?
```

**Anti-patterns for Email 1:**
- "Hope this email finds you well"
- "My name is [Name]"
- "Love what you're doing at [Company]"
- Calendly link as CTA
- HTML formatting
- Marketing-style subject lines

### Email 2: Context Bump

**Structure:** Threaded reply to E1. Provides valuable context, mechanisms, or case study details cut from E1.

```
Re: {{E1 subject}}

Hey {{first_name}},

{{Additional context that was too long for E1 -- mechanism detail,
specific case study outcome, or "flash roll" explanation of how
your product works}}

{{Repeat or rephrase CTA from E1}}
```

**Rules:**
- NEVER "just checking in" or "circling back"
- Content is pre-planned at E1 writing time (cut from E1, not generated fresh)
- Must add genuine value -- a new piece of information the prospect did not have

### Email 3: Value Flip & Friction Reducer

**Structure:** Net-new (new subject line). Pivot value angle. Take sales call off the table.

```
Subject: {{new_subject_line}}

Hey {{first_name}},

{{Pivot the value angle: if E1 was "save money," E3 is "save time" or "make more money"}}

{{Offer a friction reducer: free Loom video, lead magnet, free audit}}

If I were to {{low-friction deliverable}}, would you {{watch it / use it / want it}}?
```

**Three B2B value rotation axes:** save time, save money, make more money. E3 uses whichever E1 did not.

**CTA options:**
- "If I were to make a video going over our process for you, would you watch it?"
- "Could I send you access to try it out?"
- "Would it be useful if I sent those over?"

### Email 4: Status-Aligned Breakup

**Structure:** Threaded on E3. Uses data (headcount) and a named colleague.

```
Re: {{E3 subject}}

Hey {{first_name}},

I know there's about {{employee_headcount}} employees over at
{{company}}. Perhaps this isn't in your purview, should I reach
out to {{colleague_full_name}} given they lead the {{department}}?
```

**Rules:**
- This is the ONLY email where a "breakup" framing is acceptable
- Never "just wanted to check one last time" -- that is needy
- The named colleague creates internal routing pressure
- Use real data (headcount, colleague name from LinkedIn/Clay)

### Threading Pattern

| Email | Threading | Subject Line |
|-------|-----------|-------------|
| E1 | Net-new | Internal camouflage (2-3 words) |
| E2 | Threaded on E1 | Re: {{E1 subject}} |
| E3 | Net-new | New subject line (value flip) |
| E4 | Threaded on E3 | Re: {{E3 subject}} |

### Timing

- 3-5 day delay between emails (never 1-day)
- Avoid Friday afternoons and Monday mornings
- Small TAM: restrict to Tuesday-Thursday
- TAM-based length: >1M TAM = 1 email; 50K-100K = 2; <50K = 3

---

## 2. Creative Ideas Campaign Template

**Campaign type:** AI-generated value-first outreach
**When to use:** Default first test for new clients. Eric's single best-performing template across all customer types. Works as both signal-dependent and fallback (no signal required).
**Provenance:** Campaign doc `[V]` + LinkedIn 230 `[V]` + NotebookLM `[S]`
**Performance:** Won in 9-experiment comparison. Unseated competitor agencies.

### System Prompt (applied to all AI generation)

```
You are a senior copywriter who writes in a casual, direct tone.
Never use words like "leverage," "synergy," "innovate," "optimize,"
"disrupt," or "amazing." Write at a 5th grade reading level. Use
short sentences and concrete verbs. Do not mention that you are
writing a cold email. Do not use filler phrases.
```

### User Prompt (Creative Ideas generation)

```
You are given information about a company: {{company_description}}.
Your product/service does: {{your_product_description}}.

Generate exactly 3 creative, specific ideas for how this company
could use {{your_product}} to improve their business.

Each idea must:
- Be constrained to one specific feature/capability of {{your_product}}
- Be 1-2 sentences maximum
- Reference something specific about the prospect's business
- Sound like a smart colleague brainstorming, not a sales pitch

Here are examples of good outputs:
{{few_shot_example_1}}
{{few_shot_example_2}}
{{few_shot_example_3}}
```

### Email 1 Template

```
Subject: {{internal_camouflage}}

Hey {{first_name}},

{{Fallback first line OR recency hook}}

I had a few ideas for how {{company}} could use {{your_product}}:

- {{AI_idea_1}}
- {{AI_idea_2}}
- {{AI_idea_3}}

If any of these sound interesting, would it be worth connecting?
```

### Email 2 Template (net-new, if sending)

```
Subject: {{new_subject}}

Hey {{first_name}},

I shared a few ideas with your team about {{topic}} --
wanted to send one more that I think is particularly relevant
given {{specific_company_context}}.

{{AI_idea_4_deeper}}

Would this be useful to explore?
```

### Few-Shot Examples (from corpus)

**B2C Example (Finance Leaders):**
- "Run a TikTok campaign targeting first-time investors aged 18-24 showing how your app makes budgeting feel like a game, not a chore"
- "Partner with a personal finance podcast to sponsor a 'money makeover' segment where real users share their savings wins using your platform"
- "Create Instagram Reels showing side-by-side comparisons of 'budgeting the old way' vs. using your app, targeting millennial parents"

**B2B Example (US Pharma):**
- "Build a LinkedIn thought-leadership campaign targeting hospital procurement directors, positioning your drug delivery tech as reducing waste by 30%"
- "Launch a programmatic display campaign on medical journal websites targeting oncologists researching treatment alternatives"
- "Create a webinar series with KOLs comparing your molecule's efficacy data against the current standard of care"

**Rules:**
- Train with 3-5 manual examples before deploying
- Each bullet must be theme-constrained to a specific product feature
- This is the authorized exception to the "AI writes snippets only" rule -- AI generates 3 constrained ideas, not free-form copy
- The AI output IS the value, not a wrapper around a pitch

---

## 3. Fallback Templates (No Signal Required)

### 3a. Company Mission Fallback

**Campaign type:** Default when no recency signal found
**When to use:** First-line fallback in the recency waterfall when no LinkedIn post, job change, company news, or other signal is available
**Provenance:** NotebookLM `[S]` + Gap resolution

```
Subject: quick question

Hey {{first_name}},

I was on your LinkedIn company page and it looks like you're
focused on {{company_mission_6_words}}.

{{Core value prop -- one sentence}}

If helping with {{problem or quantifiable result}} would be
useful, let's find a time to connect?
```

**AI prompt for first line:**
```
Summarize what this company does in fewer than 6 words.
Start your output with: "I was on your LinkedIn company page
and it looks like you're focused on..."
Input: {{company_linkedin_description}}
```

### 3b. "Straight Down the Middle"

**Campaign type:** Offer validation against cold traffic
**When to use:** When testing whether an offer has any market fit before investing in personalization or targeting refinement
**Provenance:** Gap resolution (NotebookLM query)

```
Subject: question for {{first_name}}

Hey {{first_name}},

{{Fallback first line (company mission or "rando from LinkedIn")}}

{{Core value prop in one sentence -- what you do and the outcome}}

If that would be useful, would you be open to a quick conversation?
```

**Rules:**
- Three sentences maximum
- No personalization beyond first name and company
- Pure offer test -- if this gets zero responses, the problem is the offer, not the copy

### 3c. Lead Magnet Template

**Campaign type:** Demand generation for cold traffic
**When to use:** When standard CTA fails; when giving away something prospects know others charge for
**Provenance:** Campaign doc `[V]` + Gap resolution

**Email 1 (Announce):**
```
Subject: {{relevant_subject}}

Hey {{first_name}},

{{Context line -- why this is relevant to them}}

We built {{lead_magnet_description}} and I thought it might
be useful for {{company}}.

Would it be useful if I sent that over?
```

**Email 2 (Deliver, sent 1 day after reply or after 1-day delay):**
```
Re: {{E1 subject}}

Here's the {{lead_magnet}} I mentioned:
{{link_or_attachment}}

Happy to walk you through how we put it together if that
would be helpful.
```

**Lead magnet types that work:**
- Custom list of 5,000 validated leads (redacted sample in E1)
- Free infrastructure setup
- Custom Loom audit of their current approach
- ROI calculator built with their brand colors
- Deep intelligence report on their market

**Lead magnets that fail:**
- Pre-recorded webinars
- Generic PDFs
- Whitepapers
- Anything prospects would not pay for

---

## 4. Multi-Threading Templates

### 4a. Weekend CEO/VP Escalation

**Campaign type:** Multi-threading (2 contacts, same company, same weekend)
**When to use:** No-brainer offer where mid-level contact is ignoring outreach
**Provenance:** LinkedIn 204 `[V]` + Gap resolution
**Performance:** "Getting positive responses from VPs AND CEOs" -- "nobody automates this"

**Email to VP (sent during week, Tuesday-Thursday):**
```
Subject: {{standard_internal_camouflage}}

Hey {{vp_first_name}},

{{Standard E1 template -- recency hook + value prop + CTA}}
```

**Email to CEO (sent Saturday or Sunday):**
```
Subject: contacting {{vp_first_name}} {{vp_last_initial}}

Hey {{ceo_first_name}},

I know it's a {{day_of_week}} and I'm just prepping for the week.

I reached out to {{vp_full_name}} on Tuesday about
{{one_sentence_offer}}. Is this actually a priority for
{{company}} right now?

If so, I'd love to connect with whoever owns this.
```

**Rules:**
- Weekend emails signal "real person who works on weekends" (founder energy)
- Multi-threading creates internal dialogue at start of work week
- Only for small TAMs where you can afford manual coordination
- Frame as casual prep ("prepping for the week"), not urgency

### 4b. Cross-Department Riddle

**Campaign type:** Pattern interrupt for C-level pairs
**When to use:** When targeting two executives at the same company who need to coordinate
**Provenance:** NotebookLM Signal 8 `[S]` + Gap resolution
**Performance:** "Tons of responses of people being like wow this was so cool" -- 1 negative vs. many positive

**Email to CEO:**
```
Subject: {{riddle_subject}}

Hey {{ceo_first_name}},

Here's a question: {{riddle_or_provocative_question}}.

I sent {{vp_first_name}} the answer. Ask them about it --
I think it's relevant to what you're building at {{company}}.

PS - {{vp_first_name}} has the answer to this.
```

**Email to VP:**
```
Subject: {{answer_subject}}

Hey {{vp_first_name}},

The answer to the question I sent {{ceo_first_name}} is:
{{answer_with_value_prop_embedded}}.

PS - I sent {{ceo_first_name}} the question.
Let me know if this is relevant to your team.
```

**Rules:**
- Forces internal conversation through information asymmetry
- The "riddle" must encode real value -- not gimmicky
- PS lines are the mechanism that drives internal routing

### 4c. Internal Name-Drop Breakup

**Campaign type:** Status-aligned breakup (E3 or E4 replacement)
**When to use:** When primary contact has not responded after 2-3 touches
**Provenance:** Campaign doc `[V]` + LinkedIn 204 `[V]`
**Performance:** Three reliable outcomes: "that's me" / "yes reach out to them" / "actually it's Bob"

```
Subject: {{thread_or_new}}

Hey {{first_name}},

I know there's about {{headcount}} employees at {{company}}.
Should I reach out to {{colleague_full_name}} instead given
their role in {{department}}?
```

---

## 5. Specialized Campaign Templates

### 5a. Social Listening Campaign

**Campaign type:** Signal-triggered outreach based on social media activity
**When to use:** When prospect has posted about a topic relevant to your product
**Provenance:** LinkedIn 100 `[V]`
**Performance:** 1:15 positive ratio

```
Subject: your post about {{topic}}

Hey {{first_name}},

I just wanted to reach out because I saw your post about
{{AI_summary_of_post_8_words}}.

{{One sentence connecting their post topic to your value prop}}

Would it make sense to chat about how {{your_product}} could
help with that?
```

**AI prompt for social post hook:**
```
Summarize this person's recent LinkedIn/TikTok post in fewer
than 8 words. Start your output with: "I just wanted to reach
out because I saw your post about..."
Input: {{post_content}}
```

### 5b. Free Test / Doctor Positioning Template

**Campaign type:** Risk-reversal offer
**When to use:** When you can deliver a meaningful free trial or proof of concept
**Provenance:** LinkedIn 057 `[V]` + LinkedIn 160 `[V]`

```
Subject: quick question

Hey {{first_name}},

{{Recency or relevance hook}}

We {{what_you_do}} and I thought it might make sense for
{{company}}. We run a free test for new partners so you can
see the results before committing to anything.

If {{specific_outcome}} would be useful, would you take me
up on that?
```

### 5c. "Vending Machine" Analogy (Commoditized Industries)

**Campaign type:** Differentiation in crowded markets
**When to use:** When your service is in a category where every competitor says the same thing
**Provenance:** LinkedIn 164 `[V]`

```
Subject: {{internal_camouflage}}

Hey {{first_name}},

I know you probably get pitched by {{commodity_category}}
companies all the time.

The difference with us: {{flash_roll_mechanism -- 1-2 sentences
explaining HOW your product works at a level competitors can't match}}.

If seeing how that works for {{company}} would be useful,
I'm happy to show you.
```

### 5d. Flash Roll (Subject-Line-as-Body)

**Campaign type:** Extremely short, high-impact
**When to use:** When you have a single powerful insight or data point
**Provenance:** Campaign doc `[V]` + NotebookLM Signal 9 `[S]` (Oren Klaff attribution)

```
Subject: {{entire_pitch_in_subject_line}}

My subject line says it all.

If that's interesting, I'm happy to share more about how
it works for {{company}}.
```

---

## 6. Before/After Template Pairs

These pairs show the transformation from a bad email to an optimized one, demonstrating Eric's methodology in action.

### Pair 1: Generic AI Personalization to Constrained Relevance

**BEFORE (1:1500 performance):**
```
Subject: Quick chat about your business

Hi {{first_name}},

I saw that you sell to fitness coaches and thought our platform
could help you grow your business. We leverage AI to optimize
your outreach and drive synergy across your marketing channels.

Would you be open to a 15-minute call? Here's my Calendly:
[link]

Best,
[Name]
[Title]
[Company]
[Phone]
[LinkedIn]
```

**Problems:** Marketing subject line, generic AI personalization ("I saw you sell to fitness coaches"), banned words (leverage, optimize, synergy), Calendly link CTA, HTML signature, too many links, identity signals.

**AFTER (dramatically improved):**
```
Subject: fitness coaches

Hey {{first_name}},

I noticed you just posted about {{specific_post_topic}} --
{{2-5 word connection to their post}}.

We helped a company similar to yours add {{quantifiable_result}}
in {{timeframe}} without {{risk they care about}}.

If that would be useful for {{company}}, would you be open
to hearing how?
```

**Changes:** Internal camouflage subject, specific recency hook, generalized social proof, interest-based CTA, plain text, no links, under 75 words.

### Pair 2: Tax Campaign A/B (Offer Framing)

**BEFORE (near-zero responses):**
```
Are you looking for help to do your taxes in 2024?
```

**AFTER (2-3 leads per day, same volume, same list, same AI icebreaker):**
```
How do you know your current tax accountant is using every
legal loophole to get you the most money back?
```

**What changed:** Only the value prop framing. The "poke the bear" question challenges the status quo instead of asking a flat diagnostic question.

### Pair 3: CTA Transformation

**BEFORE (low conversion):**
```
Reply back with your address.
```

**AFTER (162% increase in meeting booked rate):**
```
I can show you how it works on a call by sending you a free box.
```

**What changed:** CTA bridges to meeting instead of stopping at physical delivery. The call becomes the mechanism for getting the free sample.

### Pair 4: Resource Offer to Call Bridge

**BEFORE (baseline):**
```
Here's a resource that might be helpful: [link]
```

**AFTER (3x meetings):**
```
I'll show you on the call how it applies to {{company}}.
```

**What changed:** The value is locked behind the meeting. Prospect must take the call to access the insight.

---

## Template Selection Decision Tree

```
START
  |
  ├── Does the prospect have a recency signal?
  |     ├── YES: Use GEX Standard Template (E1 with recency hook)
  |     └── NO: Continue
  |
  ├── Is this the first campaign for a new client?
  |     ├── YES: Use Creative Ideas Template
  |     └── NO: Continue
  |
  ├── Is the offer a no-brainer (free, risk-reversal, publicly verifiable)?
  |     ├── YES: Use Free Test / Doctor Positioning
  |     └── NO: Continue
  |
  ├── Is the industry commoditized (everyone says the same thing)?
  |     ├── YES: Use Vending Machine / Flash Roll
  |     └── NO: Continue
  |
  ├── Has the primary contact ignored 2+ emails?
  |     ├── YES: Use Multi-Threading (Weekend CEO or Name-Drop)
  |     └── NO: Continue
  |
  ├── Is this a pure offer validation test?
  |     ├── YES: Use "Straight Down the Middle"
  |     └── NO: Use Company Mission Fallback
  |
  └── At any point: if standard CTA fails, switch to Lead Magnet Template
```
