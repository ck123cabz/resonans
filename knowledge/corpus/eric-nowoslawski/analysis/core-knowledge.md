---
type: corpus
aliases: ["Eric Nowoslawski Methodology Bible"]
corpus: eric-nowoslawski
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Eric Nowoslawski Methodology Bible
## For: copywriter agent

**Corpus:** 1,035 files (40 NotebookLM extractions, 994 LinkedIn posts, 1 campaign playbook)
**Canonical period:** 2025-2026. Evolution from 2023-2024 noted where it changes the recommendation.

**Provenance markers on every entry:**
- `[V]` = Eric's direct voice (LinkedIn post, Campaign doc in his words). Highest confidence.
- `[G]` = Grounded in measurable evidence (A/B results, campaign metrics, 500K+ email analysis). Treat as proven.
- `[S]` = Synthesized by NotebookLM from Eric's YouTube content. Internally consistent with `[V]` frameworks but not directly confirmed in Eric's written voice. Use with appropriate caution.

---

## 1. Core Philosophy

**Cold email is a private ads network.** `[V]` You are optimizing impressions (sends/opens), targeting (waterfall enrichment), and messaging (copy). Meetings set is the only outcome metric but partly outside the operator's control. This framing shapes expectations, budgeting, and measurement. You are not writing letters. You are running ads where you control the audience.

**Offer beats everything.** `[V]` `[G]` The offer is the dominant variable. Copy, personalization, and infrastructure are multipliers on an offer that already has market fit. The data is unambiguous: Forbes/Web Summit free listing = 1 positive response per 3 contacts. Cybersecurity = 1 per 5,121. Same agency, same infrastructure, same team. That is a 1,700x spread, and it is almost entirely explained by offer quality. Eric puts it at 30% agency execution / 70% client offer. The agent must diagnose the offer before touching a single word of copy.

**"Doctor, not used car salesman."** `[V]` Diagnose a specific problem found during research and ask if the prospect wants to solve it. Never pitch features. Ban "commission breath" (Oren Klaff's term, adopted by Eric). Anything that signals you are a salesperson kills the interaction. This is not a style preference. It is structural: the doctor positioning makes the prospect a patient seeking help rather than a target being sold to.

**"Those that give more make more."** `[V]` Central mantra, especially from 2025 onward. AI-generated lead magnets, free value upfront, Creative Ideas campaigns. The winning pattern is giving something genuinely useful before asking for anything. Reciprocity is the engine.

**"All conversion rates eventually average to zero."** `[V]` Channels degrade. What worked at 1:329 in 2023 averages 1:425 by 2025. AI spam saturation, tighter filters, prospect fatigue. The methodology accounts for this: you must keep testing, keep iterating, never assume a winning campaign stays winning. The math changes. You adapt or you die.

**Three B2B value propositions.** `[V]` Every B2B offer reduces to: save time, save money, make more money. Health and status are B2C only. Hormozi framework: "We help [audience] achieve [outcome] in [time frame] without [risk/problem]." Rotate value props between emails in a sequence and between A/B test variants.

**Demand Capture vs. Demand Generation.** `[V]` Cold email should tilt toward Demand Generation because cold prospects have no existing intent. Four quadrants for planning: Low Awareness + Capture = heavy documentation. High Awareness + Capture = volume + differentiation. Low Awareness + Generation = social proof. High Awareness + Generation = rock-solid personalization. This framework, credited to @cbwritescopy and @blackhatwizardd, determines strategy before a single word is written.

---

## 2. Sequence Architecture

### Current Standard: 2-3 Emails `[V]`

The standard "Message-Market Fit" sequence is 3 emails, trending down from 4 (2023) and still shortening. Eric now uses max 3. Some campaigns run 2.

**Threading pattern:** E1 net-new. E2 threaded on E1. E3 net-new (fresh subject line). If a 4th email is used, E4 threads on E3. Two threads because: threading reminds the prospect they ignored you (psychological pressure), and E3 as a fresh thread gives you a second first impression. E2 needs E1 context to function as a bump.

**Why short sequences win in 2025:** Long sequences generate approximately 10x more spam reports per late positive response `[V]`. Each positive response from E5+ costs 10 spam reports that damage domain health, and domain health takes weeks of warm-up to rebuild. The sequence limit is an infrastructure protection rule, not a best-practice suggestion.

### Per-Email Purpose and Formula

**Email 1 ("Initial Spear")** `[V]` has four lines, each with a distinct job:
1. **Subject line** = "internal camouflage" (Will Allred/Lavender concept). 2-3 words, lowercase. Must look like it could be from a colleague or customer without lying.
2. **Line 1** = "Why you, why now." Recency/relevance hook pulled from the personalization waterfall.
3. **Line 2** = Enablement or "poke the bear" question. Challenge the prospect's status quo.
4. **Line 3** = Social proof with a quantitative result. Generalized outcome, not named case study (see Section 6).
5. **Line 4** = Low-friction interest-based CTA. Formula: "If we could help you accomplish [X], would that be useful to you?"

**Email 2 ("Context Bump")** `[V]` is a threaded reply to E1. Provides valuable context, mechanisms, or case study details that were cut from E1 for brevity. Never "just checking in." The content for E2 is pre-planned when writing E1. If you cannot identify what E2 would add, the sequence should be 1 email.

**Email 3 ("Value Flip & Friction Reducer")** `[V]` is net-new with a new subject line. Pivot the value angle (if E1 was save time, E3 is save money). Take the sales call off the table. Offer a free lead magnet, async Loom video, or other low-commitment deliverable. Goal shifts from booking a meeting to getting a hand-raiser.

**Email 4 ("Status-Aligned Breakup")** `[V]` is threaded on E3, used only when TAM is small enough to justify the extra touch. Formula: "Hey [First Name], I know there's about [Employee Headcount] employees over at [Company Name]. Perhaps this isn't in your purview, should I reach out to [Other Colleague's Full Name] given they lead the [Department]?" This generates three reliable outcomes: "that's me," "yes reach out to them," or "actually it's [correct person]." Increasingly dropped as sequences shorten.

### TAM-Based Sequence Length `[V]`

Sequence length is a function of TAM size:
- TAM > 1M = 1 email
- TAM 50K-100K = 2 emails
- TAM < 50K = 3 emails
- TAM < 20K = cold email alone is insufficient, use omnichannel

For large TAMs (80K+), use shorter sequences and move capacity to new leads. You can always come back in 3 months with fresh messaging. No one actually remembers a cold email.

*Evolution: In 2023, the upper bound was 4 emails. By 2025, Eric trends toward 2 for large TAMs. For fully automated outbound with no SDR, the minimum TAM is >100K (LinkedIn 160).*

### Timing and Spacing `[S]` partial `[V]`

3-5 day delay between emails. 1-day follow-up delay is "definitely bad." Avoid Friday afternoons and Monday mornings. For small TAM, restrict to Tuesday-Thursday. Weekend sending still generates positive replies but is reserved for multi-threading and CEO escalation campaigns where the casual weekend energy is part of the play. End sequence, wait 3 months minimum, re-engage with a completely new campaign and fresh messaging.

---

## 3. Email Anatomy (Line by Line)

### Subject Lines `[V]`

The goal is **internal camouflage**: the subject line should look like a colleague or customer sent it, without lying or bait-and-switching.

**Rules:**
- 2-3 words max `[V]`
- All lowercase or mismatched casing (capitalize first word, lowercase rest). 500K+ email analysis: mismatched casing correlates with excellent performance `[G]`. All lowercase is Eric's personal preference. Default to mismatched.
- First name inclusion correlates with above-average rates `[G]`
- Never bait-and-switch. Subject line must cohere with body.
- Preview text is increasingly important as email clients display more of it.

**Working examples:** "pizza orders" = 88% open rate `[G]`. "quick question." "question for {{first_name}}." "{{first_name}} - quick thought." For multi-threading: "contacting {{VP First Initial Last Initial}}." For Flash Roll: the entire pitch goes in the subject line, body says "my subject line says it all."

**Banned:** "Don't Hire Your Next Accountant Until You Do This." Anything bombastic. Anything that gives away the pitch. Anything that sounds like a marketing email.

### Line 1: "Why You, Why Now" `[V]`

The recency waterfall, checked in strict priority order. Use the first hit:
1. Prospect's recent LinkedIn post
2. New hire or recently promoted
3. Company LinkedIn post
4. Company news
5. Company blog post
6. Product launch
7. Fallback line

*Evolution: In 2023, company news and job changes were the primary triggers. By 2025, LinkedIn post engagement moved to the top. Social signals are now the number one trigger.*

Even the fallback must demonstrate company understanding. Fallback formula: "Hey I know I'm some Rando from LinkedIn but I saw your company and how you help [Target Audience] [accomplish X]..." or the Company Mission variant: "I was on your site and it looks like you sell to [AI job titles]. I thought we should connect." `[V]`

### Line 2: "Poke the Bear" `[V]`

Challenge the prospect's status quo with a question that implies their current approach may be inadequate. Credited to Josh Braun. Eric calls it "the most difficult copywriting tool."

The mechanism: the question is not "do you have a problem?" It is "how do you know you DON'T have a problem?" Forces the prospect to confront uncertainty.

**Tax example** (Campaign doc, controlled A/B test `[G]`): "Are you looking for help to do your taxes?" = near-zero responses. "How do you know your current tax accountant is using every legal loophole to get you the most money back?" = 2-3 leads per day. Same volume, same list, same AI icebreaker. Only the framing changed.

**Prerequisite:** "You must have a razor sharp understanding about your prospects and their problems." Generic poke-the-bear questions are worse than no question at all.

### Line 3: Social Proof `[V]` `[G]`

Generalize outcomes. Do not name specific companies unless you have a massive case study library (100+ clients) with precise matching by industry and headcount band.

500K+ email analysis: named case studies correlate with average/below-average performance. Generalized outcomes correlate with above-average/excellent `[G]`. "We helped a company like yours increase revenue by 40%" beats "We helped Acme Corp increase revenue by 40%" because no one remembers cold emails, so the company name adds nothing. Exception: when the named company is a genuine peer the prospect would recognize (and you have the library to match precisely).

### Line 4: CTA `[V]`

Aim for a reply, not a click. Never force a cold prospect to click a link. Switching from calendar link CTA to interest-based question yields 5x increase in positive responses `[G]`.

**Default formula:** "If we could help you [accomplish X / reduce Y / achieve Z], would that be useful to you?" `[V]`

Calendar links in cold email are actively harmful. They are an identity signal that marks you as a marketer. Calendar links are acceptable ONLY in the response email after a positive reply, and even then paired with two specific manual time options.

---

## 4. Campaign Type Taxonomy

The agent selects campaign type based on TAM size, signal availability, offer strength, and whether standard messaging has already been tested.

### Standard Message-Market Fit (3 emails) `[V]`

The default. E1/E2/E3 threading pattern as described in Section 2. Start here for any new client with a reasonable TAM and a clear offer. Test in 1,000-contact batches.

### Creative Ideas (Best-Performing) `[V]` `[G]`

1-2 emails, net-new. Feed the prospect's company description into AI to generate 3 highly specific, theme-constrained creative ideas showing how they could use your product or service. Each bullet is constrained to a specific product feature to prevent hallucination. Train with 5 manual examples before deploying AI.

In a 9-experiment comparison, this campaign outperformed all other angles `[G]`. It is Eric's signature campaign and the closest thing to a universal default. It works because it gives genuine value (the ideas themselves trigger reciprocity), demonstrates understanding of the prospect's business, and inverts the pitch dynamic. This is also the **ultimate fallback** for prospects with no signal triggers. It does not require recency data.

### Lead Magnet / "Building It For You" `[V]` `[S]`

2-step sequence: E1 announces that you are building something specifically for the prospect's company (custom lead list, ROI calculator, intelligence report). E2 delivers it 1 day later. Lower friction from SQL (30-min call) to MQL (hand-raiser).

Golden rule: the lead magnet must be something the prospect knows others charge money for. Examples: custom list of 5K validated leads, free infrastructure setup, custom Loom audit. Enterprise fallback: "knowledge arbitrage" through proprietary benchmarking data.

**2025 fulfillment model** `[V]`: Cheap front-end (~$0.001/company for initial analysis) triggers expensive back-end (~$1/lead) only on positive reply. 5 minutes from reply to auto-delivered asset. Tool chain: Clay + Claygent for scraping, Make.com for orchestration, Lovable for micro-apps, Gamma for reports, Parallel.ai for intelligence reports.

Four lead magnet types with proven traction:
1. **Custom ROI Calculators** via Lovable (branded 1-page app with prospect's hex codes)
2. **Deep Intelligence Reports** via Parallel.ai dumped into Gamma presentations
3. **"New Hire" Custom Lead Lists** as continuously updated Google Sheet (62 leads in first hour)
4. **Agentic Free Trial** where AI sets up infrastructure, pulls list, writes copy, launches for the prospect

### Weekend Multi-Threading `[V]`

2+ simultaneous net-new emails to different contacts at the same company, sent Saturday or Sunday. Email to the IC below the DM says you reached out to their boss. Email to the CEO above says you had no success with the VP. Weekend CEO escalation: if the DM ignores, email the CEO Saturday asking "is this actually a priority?"

Three strategies with templates `[V]`:
- **Weekend CEO/VP Escalation:** VP during week, CEO on Saturday. "I reached out to [VP] on Tuesday about [offer]. Is this actually a priority?"
- **Cross-Department Riddle:** CEO gets the answer to a riddle the VP received. VP gets the riddle the CEO has the answer to. PS lines force internal conversation.
- **Internal Name-Drop Breakup:** "I know there's about [headcount] employees at [company]. Should I reach out to [colleague name] instead?"

### Riddle Campaign `[S]`

Coordinated riddle between CEO and VP. Operationally complex but generates high engagement. "Tons of responses of people being like wow this was so cool" with only 1 negative versus many positive `[V]`.

### Feedback / "I'm Lost" `[S]`

Takes sales completely off the table. Asks the prospect about their world instead of pitching. "We're trying to understand how companies like yours handle [problem]. Would you be open to sharing your perspective?" Phase 4 diagnostic campaign when all standard approaches fail.

### Flash Roll `[V]`

Entire message in the subject line. Body says "my subject line says it all" or "whole question is in the subject line." Oren Klaff attribution. The mechanism revelation variant: instead of high-level outcome, go deep on exactly HOW your product works at a level of specificity your competitors cannot match. "We built an email verification system that will actually send an email on your behalf to the email address and return the verification result" beats "we built an email verification service."

The Flash Roll sits in productive tension with the 5th-grade reading level rule. Resolution: go deep on mechanism but stay simple in language.

### Lookalike / Case Study `[S]`

Ocean.io ingests a case study URL and builds a lookalike list. "We literally just tell them the exact outcome." Works when the client has strong case studies to reference. Similarity-based shortcut that bypasses the need for broad targeting.

### "Straight Down the Middle" `[V]`

3-sentence email: fallback first line + core value prop + interest-based CTA. No frills, no elaborate personalization. Used specifically to test offer quality against cold traffic. If this gets zero responses, the problem is the offer, not the copy.

### Fallback (No-Signal) Strategies `[V]`

Signal-based targeting only covers 5-15% of TAM at any given time `[V]`. Fallback campaigns for the remaining 85-95% are not optional. They are the majority of volume.

Five fallback strategies:
1. **Company Mission Fallback:** "I was on your site and it looks like you sell to [target]. I thought we should connect."
2. **Creative Ideas:** No signal data required. The universal fallback.
3. **Lookalike targeting:** Start from proven case studies.
4. **"Straight Down the Middle":** Offer quality test.
5. **Massive Lead Magnet:** Give away something the prospect knows others charge for.

---

## 5. ICP & Targeting

### Segmentation Methodology: Waterfall, Not Static `[V]`

The ICP is not a fixed persona. It is a waterfall:
1. Define minimum threshold for an acceptable prospect.
2. Invert: find the BEST customer using waterfall enrichment (the "10 minutes of research" heuristic).
3. Move down the waterfall by removing criteria to expand volume while maintaining relevance.

Four situational data categories for the "Golden ICP":
- (a) Intent/recency triggers: job changes, posts, hires
- (b) Job description keywords
- (c) Technographics: software on the website (BuiltWith)
- (d) Public problems: negative reviews, Glassdoor complaints

*Evolution: In 2023, the Golden ICP used 5 trigger filters and multi-filter segmentation was the standard. By 2025, Eric simplified to 1-2 strong signals + broad fallback. Over-segmentation was abandoned (Signal 170). Dynamic messaging tiers replaced rigid binary qualification.*

### The "10-Minute Research Rule" `[V]`

The governing quality bar for all AI-assisted personalization. Automated emails should look exactly like the message you would manually send after 10 minutes of prospect research. "Think backwards from 10 minutes of research." Reverse-engineer what a human would find in 10 minutes of manual research, then automate that exact pipeline. This is not a tactic that evolves. It is the design principle.

### Signal Coverage = 5-15% of TAM `[V]`

At any given time, only 5-15% of your total TAM will have active signal triggers (recent LinkedIn post, job change, funding round). This means signal-dependent campaigns are the premium layer, not the strategy. Most volume runs on fallback campaigns. Plan accordingly.

### Fallback Campaigns Are Mandatory `[V]`

If you only run signal campaigns, you are reaching 5-15% of your market. The remaining 85-95% requires campaigns that work without recency signals: Creative Ideas, Company Mission fallback, Straight Down the Middle, or lead magnet approaches.

### Dynamic Messaging Tiers `[V]`

Segment prospects by how many targeting criteria they meet (3/2/1/0). Each tier receives different copy. Highest-signal prospects get the most personalized messaging. Lowest-signal prospects get the broadest campaign. This replaced the binary qualify/disqualify model from 2023.

**Range-based messaging** `[V]`: Segment by data ranges (0-10 employees, 11-20, 21-50) rather than binary thresholds. Each range receives different copy calibrated to their scale. "Hey, I know you're a 12-person team" hits differently than "Hey, I know you're a 200-person team."

### 4-Step List-Building Pipeline `[V]`

In strict order:
1. **Source** broad account list (Apollo, LinkedIn Sales Nav, D7 Lead Finder for local)
2. **AI qualification in Clay**: score fit, end workflow if fail. Do not waste enrichment budget on bad leads.
3. **Enrich** for situational triggers (intent data, technographics, job descriptions, public problems)
4. **Find decision maker** after the company passes checks. Person comes last.

**"Reverse" variant** `[S]` partial `[V]`: Analyze closed-won customer list with AI, identify exact commonalities, build TAM from proven data points instead of assumptions. Gaining emphasis as AI makes this practical at scale.

### Operating Exclusions `[V]` `[G]`

Some markets are structurally incompatible with cold email regardless of execution quality:
- **Cybersecurity:** 1:5,121. Buyers only look after an incident. `[G]`
- **Staffing (undifferentiated):** 1:1,687. No differentiation in commoditized category. `[G]`
- **Enterprise compliance:** 1:4,265 across 11 campaigns. Never take without existing sales team. `[G]`
- **Team culture:** 0 total positive responses across 12 campaigns. `[G]`
- **Web development:** 1:2,568. `[G]`
- **Benefits administration:** 1:2,966. "Nice to have" problem. `[G]`

Three failure patterns: (1) the problem is "nice to have" with no urgency, (2) no differentiation in a commoditized category, (3) enterprise targets require existing warm sales infrastructure that cold email cannot replace.

---

## 6. Copy Principles

### Length and Readability `[V]`

Under 100 words. Ideally around 75. 5th-grade reading level. Short sentences. Concrete verbs. No compound structures. No jargon. The email should look like a CEO text message, not a marketing brief.

**When this rule breaks** `[V]`: A customer wrote a 623-word email targeting CEOs running businesses 10+ years old. It outperformed. Why: the customer deeply knew the audience, each paragraph earned the next, the long personal format was what large buttoned-up competitors COULD NOT say, and capacity was limited so quality mattered more than volume. Eric's caveat: "Don't take this as outbound social bait that we are so amazing that we do this for our customers all the time. We are not." The rule breaks only when the sender has deep personal knowledge of the audience, long format itself differentiates from competitors, and TAM is small.

### Plain Text, No HTML, No Links in E1 `[V]`

No HTML. No embedded images. No tracking pixels. No Calendly links. No email signatures with logos. "The only people in the world that add a transparent 1x1 pixel to an email are just email marketers." Any element that signals "mass blast" kills deliverability and trust simultaneously.

Links acceptable in E3+ for lead magnets. Images acceptable only when the image IS the evidence (screenshot of their negative Google review, relevant meme about their actual problem), not decoration `[V]`.

### Relevance > Personalization `[V]` `[G]`

Eric's strongest conviction. Generic AI personalization ("I saw you sell to fitness coaches") generated 143% fewer replies than no personalization at all `[G]`. AI company analogies were tested and completely dropped with zero positive responses `[S]`. College-based personalization was so offensive the campaign was shut down in 2 days `[S]`.

Do not chase "triple double backflip" workflows when the offer has not been validated. Relevance (your message connects to something real about the prospect's situation) beats personalization (your message includes something scraped about the prospect's background) every time.

### "Poke the Bear" `[V]`

See Section 3 for full treatment. The single most impactful copy technique in the corpus. The tax campaign A/B result (near-zero vs. 2-3 leads/day on identical everything else) is the cleanest controlled experiment available `[G]`.

### Show Don't Tell / Flash Roll `[V]`

Two techniques under one umbrella:

**Mechanism revelation (Flash Roll):** Reveal HOW your product works at a level of specificity your competitors cannot match. Goes deep but stays simple. "What can you say in this email that your competitors can't say?" is the governing question.

**Evidence in the email:** Do not claim capability. Demonstrate it.
- Google Sheet of redacted leads (PE investors)
- Programmatic screenshots (screenshotapi.net)
- AI-generated use cases per prospect (Creative Ideas campaign)
- Quoting specific Google reviews (reputation management)
- Direct support doc links showing you did the research

### "Sell the Vacation, Not the Plane Ticket" `[V]`

Focus on what the prospect can do once the problem is solved, not the mechanism of solving it. Connected to "chunking up." The 9-experiment comparison winner (Creative Ideas) succeeded because it showed prospects what their life would look like using the product, not how the product works.

The tension: Flash Roll deliberately breaks this rule by revealing mechanism. Resolution: reveal mechanism only when the mechanism itself is the differentiator. If your mechanism is commoditized, sell the outcome.

### Chunking Up / Chunking Down `[V]`

"Chunking up" = strip the mechanism, talk high-level outcome ("$85K/month"). "Chunking down" = hyper-granular unique feature. Use chunking as a reframing technique when standard framing fails. Part of the diagnostic hierarchy for underperforming messaging.

### Handle Objections Before the Reply `[V]`

Do not wait for objections to come in. By Email 2, you have already lost the prospect if their primary objection was not addressed in Email 1. The poke-the-bear technique doubles as preemptive objection handling. It surfaces the objection as a question rather than waiting for it.

Eric's fire department sign example: "We are not looking for heroes, just neighbors!" speaks into the "I'm not qualified enough" objection before anyone voices it.

### Named Case Studies: When They Work and When They Don't `[V]` `[G]`

500K+ email analysis finding: named case studies correlate with average/below-average performance. Generalized outcomes correlate with above-average/excellent `[G]`.

**Exception:** When a client has 10,000+ past customers and uses Clay + ChatGPT to match the most recognizable case study in each industry + headcount band to each prospect, named case studies work. The matching must be precise (same industry AND same headcount range), and the named company must be one the prospect would recognize as a genuine peer `[V]`.

**Default:** Generalize. "We helped a company like yours achieve [X]."

---

## 7. AI in Cold Email

### AI Generates Variables, Not Emails `[V]`

The philosophy: human controls structure, AI fills data-dependent slots. In 2023, this meant 5-12 word snippets in human templates. By 2025, AI handles more through dynamic variable systems ($0.02 per email), but the constraint principle still holds. AI generates the personalization variables. Humans write the CTA, the social proof framing, and the overall structure.

Current snippet scope: 2-7 words per AI-generated variable (tightened from 5-12 in 2023) `[V]`. CTA and social proof are always hand-written `[S]`. AI only personalizes the relevance hook (Line 1) or offer-connect (Line 3).

### 4-Step Prompting Framework `[V]`

1. **Define goal.** What should the AI output?
2. **Provide reference data.** Company description, LinkedIn profile, job posting, news article.
3. **Constrain creativity.** Guardrails, jargon bans, word count limits. Specify what NOT to do.
4. **Provide 3-5 manual examples.** Step 4 is the most critical. The examples are the real prompt. Everything else is guardrails around the examples.

**Prefix technique** `[S]`: Force the AI to complete a sentence starting with a specific prefix. "I was on your LinkedIn company page and it looks like you're focused on..." The AI completes from the prefix, which controls tone and length.

### "Never Tell the Model You're Writing a Cold Email" `[V]`

Describe a persona instead: "You are a thoughtful VP of Sales who writes concise, direct messages to peers." The model produces more natural output when it does not activate its "cold email" training patterns. This is a meta-constraint on how to frame the task itself.

### Jargon Ban List `[V]`

Explicitly banned words for all AI-generated email snippets and cold email copy: **leverage, synergy, innovate, optimize, disrupt, amazing**. Explicitly banned phrases: **"Hope this email finds you well," "My name is [Name]," "Just checking in," "Circling back," "Love what you're doing at [Company]."**

Implicitly banned patterns: hyperbolic guarantees, exact scraped data stated as fact (decimal precision like "21.16% growth" sounds bot-written and invites factual disputes), marketing-style subject lines, calendar link language ("book a time here").

Eric explicitly recommends baking these bans into a reusable system prompt, not applying them as a post-generation filter: "Ask ChatGPT to draft a reusable system prompt that bans words like 'leverage,' 'synergy,' 'innovate,' etc." `[V]`

### Model Selection `[V]`

GPT-4o mini for most tasks. "Since we send so much, we do everything with 4o mini. Haven't seen a case where any of the others can really do something so much better that it's worth the expense." Lock the API key to prevent expensive model usage at scale. At $0.02 per email total enrichment cost and 3M emails/month, unnecessary AI calls are expensive. Gemini Flash noted for needle-in-haystack tasks (Alexander Han/Overjoy) `[V]`.

**Formula-over-AI threshold** `[V]`: Use deterministic enrichment (formulas, conditional logic, lookups) when possible. Reserve AI for unstructured data that cannot be handled deterministically. Decision hierarchy: formula, then conditional logic, then AI.

### Confidence Scores > Binary Classifications `[S]`

When using AI for lead scoring, return confidence scores (1-10) rather than binary yes/no classifications. This enables graduated messaging tiers (Section 5) and prevents the loss of borderline prospects.

### 6 Production Prompts `[V]`

Extracted from Eric's actual Clay workflows:
1. **System Prompt (Jargon Guardrails):** Universal tone/jargon filter banning the listed words
2. **Creative Ideas:** Generate 3 customized outbound use cases, each bullet constrained to a specific product feature, trained with 2+ few-shot examples (B2C + B2B)
3. **Company Mission First Line:** Summarize what company does in <6 words, prefix: "I was on your LinkedIn company page and it looks like you're focused on..."
4. **Social Post Hook:** Summarize prospect's recent LinkedIn/TikTok post in <8 words, prefix: "I just wanted to reach out because I saw your post about..."
5. **Job Openings Relevance:** Connect open role to company problem (two variants: job title inference + job description quoting)
6. **Deep Research AI Feature:** Determine if company uses AI + generate feature sentence with step-by-step reasoning and conditional output

---

## 8. CTA Design

### Reply > Click `[V]` `[G]`

Never force a cold prospect to click a link. Switching from calendar link to interest-based question = 5x increase in positive responses `[G]`. This is the single highest-impact tactical change in the corpus.

### Position-Mapped CTA Types `[V]`

| Position | CTA Type | Formula |
|----------|----------|---------|
| E1 (universal) | Interest-based | "If helping with [problem or quantifiable result] would be useful, let's find a time to connect?" |
| E3 (friction reducer) | Low-friction offer | "If I were to make a video going over our process for you, would you watch it?" |
| E4 (breakup only) | Routing/Right Person | "Should I reach out to [Full Name] instead given their role?" |
| When standard fails | Lead magnet offer | "Could I send you access to try it out?" / "Would it be useful if I sent those over?" |
| After positive reply | Post-reply scheduling | Two specific manual times + calendar link as fallback |
| Strong offer | Direct ask with value | "If we could help you reduce future OSHA violation fines with just 2 hours of implementation, would you take me up on that?" |

**CTA design question:** "How do we make this worth this person's time?" This question governs all CTA selection `[V]`.

**Soft vs. direct:** Interest-based CTAs are the default. Direct asks work when the offer is so clear and valuable that the prospect needs no additional context to say yes. Eric: "(I know soft CTAs are all the rage on LinkedIn but my customers need meetings.)" `[V]` The resolution is context-dependent, not dogmatic.

### Post-Reply Protocol `[V]`

After a positive reply:
1. Offer two specific manual times AND a calendar link: "Would Tuesday at 9am ET or Thursday at 2pm ET work? Or if easier, here's my calendar."
2. Follow up same day. Speed is your advantage.
3. Each follow-up adds value: ROI analysis, risk avoidance data, case study, new idea. After several tries, offer a gift card.
4. Do not stop until they book or say no. (Eric's own story: took 8 follow-ups from Rippling before booking.)
5. Follow up across channels: LinkedIn DM, phone call.

"Not interested" = add to global blocklist immediately. No objection handling. Generate "not interested" replies intentionally with language like "If this isn't relevant, let me know" because manual replies from reputable domains boost sender reputation `[S]`.

---

## 9. Subject Lines

### "Internal Camouflage" `[V]`

Will Allred/Lavender concept adopted by Eric. The subject line must look like it could plausibly be from a colleague or customer, without lying.

**Structural rules:**
- 2-3 words max `[V]`
- Mismatched casing (capitalize first word, rest lowercase) correlates with excellent performance in 500K+ analysis `[G]`
- All lowercase is Eric's personal preference `[V]`
- First name inclusion correlates with above-average rates `[G]`
- Preview text is increasingly important. Design for it.

**Categories:**
- **"Tried and True":** "quick question," "question for {{first_name}}" `[S]`
- **"Customer" approach:** "pizza orders" (88% open rate `[G]`), "question about review" `[V]`
- **Flash Roll:** Entire pitch in subject line `[V]`
- **Name-drop routing:** "contacting {{VP First Initial Last Initial}}" for multi-threading `[V]`
- **Media/feedback:** "request for quote" for demand-generation campaigns `[S]`

**Never:** Bait-and-switch. Marketing-style. All caps. Anything bombastic. The benchmark is: if creative cannot beat "quick question," use "quick question."

---

## 10. Message-Market Fit Testing

### Primary Metric: Contacts per Positive Response `[V]` `[G]`

This is the single governing metric. Not open rate (vanity metric, turn off tracking). Not click rate (you should not have links). Not reply rate alone (negative replies are noise). Contacts per positive response.

**Tiers** `[G]`:
- Excellent: 150 or fewer
- Above Average: 150-400
- Average: 450-800
- Below Average: 800-1,200
- Poor: 1,200+

**Baseline:** The cross-customer average was 329 in 2023 `[G]`, degraded to 425 by 2025 `[V]`. Use 425 as the current baseline for planning. The environment is harder. Adjust expectations accordingly.

### Test Batch Size `[V]`

Minimum 1,000 contacts per test. Testing on 286 is "far too low." You should see directional signal within 1-3 iterations. If you are 6 months in with zero progress, something is fundamentally broken.

### Scale/Fix Decision Rules `[S]`

- Better than 1:300 = scale
- 1:300-1:800 = iterate
- Worse than 1:1,000 = shift direction
- Zero positives in 1,000 contacts = no fit, major pivot needed

### Rapid Feedback Loop `[V]`

3-day positive response monitoring window. Check positive response rate within 3 days of campaign launch to determine initial health before waiting for the full 1,000 contacts to complete.

### 4-Phase Message-Market Fit Iteration `[S]` partial `[V]`

When initial messaging fails, iterate through phases (note: the 4-phase numbering may be NotebookLM's organization of Eric's more loosely described process):

**Phase 1:** Test the core offer with rotating value props (save time / save money / make more money). Same audience, different framing.

**Phase 2:** Test triggers and list segmentation. Same messaging, different audience slices.

**Phase 3:** Complete rewrite using static frameworks: poke the bear, extremely short (Flash Roll), weekend grassroots multi-threading.

**Phase 4:** Remove sales entirely. Feedback email, media template, aggregate into lead magnet. "If free offer still refused, problem is core offer/market" `[V]`.

### 4-Axis Testing Framework `[S]`

Do not apply website CRO tactics to cold email. Tests must involve significant changes, not button-color variations. Four orthogonal testing axes:
1. Test 3 core value props (save time, save money, make money)
2. Test chunking up vs. chunking down
3. Test demand capture vs. demand generation
4. Test audience segmentation (job title, company size)

Subject line testing: split-test standard lines ("quick question") against creative internal camouflage lines.

### Three Root Causes of Failure `[S]` partial `[V]`

Diagnose in this order:
1. **Inboxes burned** (infrastructure). Check deliverability metrics first.
2. **Not enough E1s** (volume). Are you actually sending enough?
3. **Messaging stinks** (copy). Only optimize copy after infrastructure and volume are confirmed healthy.

For messaging-specific diagnosis:
- (a) Address implicit objection via poke-the-bear
- (b) Chunk up or chunk down
- (c) Move prospect higher up funnel (demand generation)
- (d) "Give Away the Farm" test: if a free offer still gets refused, the problem is the core offer or the market, not the copy

The "Fake Domain" offer test `[S]`: unbranded domain, exact service offered for free, 500 prospects. If this gets zero responses, cold email cannot solve this market.

---

## 11. Infrastructure Constraints (What the Agent Must Never Violate)

These are hard rules that override methodology preferences. Violating them destroys the sending infrastructure that makes everything else possible.

### Sending Limits `[V]`

**30 emails per day per inbox** on new Google inboxes (2025, down from 50 in 2023). The drop from 50 to 30 means 67% more inboxes for the same daily volume. Conditional ramp: start at 30, push to 50 only after proven good response rate `[S]`. Conservative/Hypertide rate: ~15/day to mimic human behavior `[G]`.

### Domain Rules `[S]` `[V]`

- **.com and .co domains only.** No .io, .ai, or exotic TLDs.
- **2-3 inboxes per domain.**
- **Domain aging: 4-6 weeks before sending** (critical for Outlook/Proofpoint targets). Domain aging is now a "secret weapon." Buy during sales at Porkbun/Dynadot. Let them sit before activating.
- **Three-set rotation system** `[V]`: Active (currently sending), On-deck (warmed up, ready to swap in), Aging (newly purchased, warming up). When Active burns, On-deck takes over immediately. A new domain enters Aging. The machine never stops.
- **1:1 insurance ratio.** Equal number of backup domains ready at all times.
- **50% warmup reserve** `[V]`: Half of total sending capacity should always be in the warmup phase.

### Warm-Up Protocol `[S]` `[V]`

| Target | Duration |
|--------|----------|
| Gmail (SMB) | 2-3 weeks |
| Outlook/Proofpoint (Enterprise) | 4-6 weeks (up to 2 months) |

Daily ramp: start at 5 emails/day, increase by 5/day, cap at 50 warm-up emails/day. Response rate setting: 20-40% (Eric uses 32%). Never set 100%. It looks unnatural.

**Gmail-first launch strategy** `[S]`: Launch campaigns to Gmail recipients first for 2-3 weeks (easier deliverability). Let backup domains age. Swap them in for Outlook/Proofpoint at 4-6 weeks.

### Hot-Swap Protocol `[V]`

Dead inboxes do not recover. Burn signals:
- Reply rate <1% (excluding OOO)
- Bounce rate >2% (especially 550 errors)
- Warm-up health <100%
- Reputation score <95%
- Negative sentiment (cursing in replies) = turn off campaign immediately

**Diagnostic protocol (sequenced):**
1. Check reply rate. If <1%, proceed to step 2.
2. Turn on open tracking for exactly 2 days.
3. If opens ~10% = definitively in spam. Kill the inbox.
4. If opens 40-60%+ = inbox is fine. Problem is messaging, not infrastructure.
5. Check MX Toolbox for blacklists.
6. Check bounce rate for 550 errors.

Burn response: cancel immediately, hot-swap from insurance pool, purchase replacement the same day. "The cure is always the same: set up more inboxes" `[V]`.

### Email Formatting `[V]` `[S]`

Plain text only. No HTML. Zero links in E1 (including signature links). Zero images in E1 (including signature images). No tracking pixels. No Calendly links in cold email. Custom tracking domains required if any tracking is used. Replace unsubscribe link with "If this isn't relevant, let me know" (unless legally required) `[S]`.

### Excluded Tools `[S]` `[V]`

Do not use HubSpot, Mailchimp, Constant Contact, Outreach.io, or SalesLoft for cold email sending. These are marketing email or enterprise sales tools, not cold email infrastructure. HubSpot is acceptable as a $20/month data cache storing enrichment records `[V]`, but never for sending.

### Scaling Formula `[V]` `[S]`

```
INPUTS:
  meetings_needed_per_month
  contacts_per_positive_response (use 425 as 2025-2026 baseline)
  tam_size

COMPUTE:
  positive_responses_needed = meetings_needed / meeting_conversion_rate
  daily_sends_needed = (positive_responses_needed * 425) / 22 working days
  inboxes_needed = daily_sends_needed / 30
  domains_needed = inboxes_needed / 2.5
  insurance_domains = domains_needed (1:1 ratio)
  warmup_reserve = inboxes_needed (50% always warming)
  total_domains = domains_needed + insurance_domains
  total_inboxes = inboxes_needed + warmup_reserve

CONSTRAINTS:
  IF tam_size < 100K: warn — may need SDR complement
  IF tam_size < 20K: cold email alone insufficient, omnichannel required
  IF daily_sends > tam_size / 90: warn — will exhaust TAM in <90 days
```

Pace volume so it takes one quarter (90 days) to cycle through the entire TAM. Recontact minimum: 3 months with completely fresh messaging. "No one actually remembers a cold email" `[V]`.

---

## 12. Anti-Patterns (What to Never Do)

Every entry below includes WHY it fails, not just that it fails. The agent must understand the mechanism to avoid inventing new versions of the same mistake.

**"Hope this email finds you well"** `[V]` 4 sources. Identity signal. Marks you as a salesperson immediately. No colleague or customer writes this. It is the single most-confirmed ban in the corpus.

**Calendar link as CTA** `[V]` `[G]` 3 sources. Massive friction. "Only marketers do this." Tested repeatedly: "It always loses." 5x fewer positive responses versus interest-based question.

**Long sequences (5+ emails)** `[V]` 4 sources. ~10x more spam per late positive response. Data decays by E5 (job changes, company changes). Annoyance compounds. If they needed you, they would have replied by E2.

**Generic AI personalization** `[G]` 3 sources. "I saw you sell to fitness coaches" = 143% fewer replies than no personalization. AI company analogies tested and completely dropped. Zero positive responses. The AI is doing the wrong job.

**Fake/generic compliments** `[S]` 2 sources. "Love what you're doing at [Company]" is "level negative-2." Worse than no personalization because it actively demonstrates you did NOT research them.

**Robotic scraped data drops** `[S]` 2 sources. Exact numbers (540,000 visitors, 21.16% growth) sound bot-written. Prospects reply to argue the data instead of engaging with the offer. Round the numbers, use ranges, or drop them entirely.

**College-based personalization** `[S]` `[G]` 3 sources. Offended state school and community college attendees. Campaign shut down in 2 days. Demonstrates the danger of personalization that assumes shared context that does not exist.

**"Just checking in" / "Circling back"** `[S]` 2 sources. Status signals. Mark you as needy, not expert. Every follow-up must add new value or shift the angle.

**Traditional breakup emails** `[V]` 2 sources. "I can't think of anything else that looks more needy than a breakup email." If you must break up, use the status-aligned version (E4 routing to colleague), not "This will be my last email."

**HubSpot/Mailchimp for cold email** `[V]` 2 sources. Wrong infrastructure. Built for marketing email (opt-in lists, HTML templates, tracking pixels). Using them for cold outreach damages deliverability and violates platform ToS.

**Mentioning a competitor's post** `[S]` 1 source. "Never tell prospect you saw them liking a competitor's post." Signals surveillance, not research.

**Heavy spintax (15+ variations)** `[G]` 1 source. Hurts performance in 2025. Filters detect spintax patterns. Keep variation moderate.

**Threading all follow-ups** `[V]` 3 sources. "You're just reminding someone that they didn't respond to your other emails." Use the net-new / threaded / net-new pattern. Never thread the entire sequence.

**Bait-and-switch subject lines** `[V]` 2 sources. Destroys trust immediately. The subject line must make sense with the body. If it does not, you have lied in the prospect's inbox. They will never read another email from you.

**Sending from marketing email tools** `[V]`. This bears repeating because it is the most common infrastructure mistake. Outreach, SalesLoft, HubSpot, Mailchimp, Constant Contact. None of these are for cold email. Use Smartlead (advanced/agencies) or Instantly (beginners).

---

## Appendix: Industry-Specific Adjustments

Seven verticals with documented guidance `[V]`:

**SaaS:** Do not use "free trial" (time-to-value too long). Use Creative Ideas. Harmonic.ai/Ocean.io for targeting because LinkedIn industry tags are unreliable for SaaS companies.

**Marketing Agencies:** "Chunk up" to outcomes, not services. Give massive upfront value (5,000 free validated leads). Use SimilarWeb competitor data through Serper site: queries.

**Local Business:** No LinkedIn presence. Use Google Maps via D7/Apify. Hyper-casual copy. Reference specific Google reviews. Support@ emails are acceptable.

**Healthcare:** Strict compliance language. Target practice managers, not doctors. HIPAA-aware copy. Offer = audit of online patient reviews.

**Financial Services:** Investment pitch fails. Pivot to tax strategy/depreciation (proven A/B `[G]`). Target CPAs and financial advisors separately.

**E-commerce:** Google Shopping via Serper for AOV. Instagram/TikTok engagement data. "Show don't tell" with screenshots of their store.

**Professional Services (Law/Accounting):** Target first-time founders who do not have an existing advisor. Use Clay for "first-time position holder" detection (LLM-exclusive segmentation that no data provider can replicate).

---

## Appendix: Rule-Breaking Conditions

Rules are defaults, not absolutes. The agent must know when and why to break them.

| Rule | Break Condition | Evidence |
|------|----------------|----------|
| Under 100 words | Sender deeply knows audience + long format differentiates from competitors + each paragraph earns the next + small TAM | 623-word email outperformed `[V]` |
| No images in E1 | Image IS the evidence (negative review screenshot, relevant meme about actual problem), not decoration | Bed bug meme for pest control `[V]` |
| AI writes snippets only | Creative Ideas campaign: AI generates 3 constrained ideas as the email body. Still constrained (theme per bullet, trained on 5 examples) | Best-performing campaign across customer types `[G]` |
| Named case studies underperform | Case study library 100+, matching by industry AND headcount, prospect would recognize the company as a peer | 10K+ customer library with precise matching `[V]` |
| No weekend sending | Weekend multi-threading and CEO escalation campaigns where casual tone is the play | "I know it's a Sunday and I'm just prepping for the week" `[V]` |
| Interest-based CTA default | Offer so clear and valuable prospect needs no additional context to say yes | "If you have a negative Google review, we'll try to get it removed. You only pay if we succeed." `[V]` |

---

## Appendix: Post-Positive Conversion Reference

Eric intentionally does not track a global post-positive conversion rate. "If I could totally control the revenue, I might as well run your business." The three phases are: (1) get positive response (Eric's job), (2) book meetings (client's workflow), (3) close deals ("that's the part that'll punch you in the face").

Specific campaign data points (replies to opportunities) `[V]`:
- Campaign A: 122 replies, 27 opportunities (22%)
- Campaign B: 302 replies, 104 opportunities (34%)
- Campaign C: 859 replies, 77 opportunities (9%)
- Campaign D: 189 replies, 32 opportunities (17%)
- Campaign E: 642 replies, 225 opportunities (35%)

The agent should use contacts-per-positive-response as its primary metric and not attempt to forecast downstream conversion. This is a methodology decision, not a gap.
