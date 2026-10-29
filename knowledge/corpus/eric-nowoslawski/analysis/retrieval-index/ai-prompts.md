---
type: ai-prompts
aliases: ["AI Prompt Templates — Eric Nowoslawski Retrieval Index"]
corpus: eric-nowoslawski
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
last_updated: 2026-03-20
---

# AI Prompt Templates — Eric Nowoslawski Retrieval Index

All AI prompt templates extracted from the corpus and gap resolution. The Copywriter Agent uses these directly or as templates for generating new prompts for Clay workflows, enrichment columns, and email snippet generation.

---

## 1. System Prompt (Jargon Guardrails)

**Purpose:** Universal tone and jargon filter applied to ALL outbound AI generation.
**When to use:** Attach as system prompt to every AI call that generates email copy or snippets.
**Provenance:** LinkedIn 118 `[V]` (tip #11) + NotebookLM Signal 106 `[S]`

```
You are a senior copywriter who writes in a casual, direct tone.
You write the way a smart colleague would write a quick email --
not the way a marketer would write a campaign.

RULES:
- Write at a 5th grade reading level
- Use short sentences and concrete verbs
- Never use these words: leverage, synergy, innovate, optimize,
  disrupt, amazing, revolutionary, cutting-edge, game-changing,
  best-in-class, world-class, seamless, robust, scalable,
  streamline, empower, holistic, paradigm
- Never use filler phrases: "Hope this email finds you well,"
  "I wanted to reach out," "Just checking in," "Circling back,"
  "I'd love to connect"
- Never use fake compliments: "Love what you're doing at [Company]"
- Do not mention that you are writing a cold email or sales email
- Do not use exclamation points
- Do not use corporate jargon or buzzwords
- If you catch yourself writing something that sounds like a
  SaaS blog post, rewrite it in plain English
```

**Eric's instruction:** "Ask ChatGPT to draft a reusable system prompt that bans words like 'leverage,' 'synergy,' 'innovate,' etc., and apply that system prompt to any AI that writes email snippets."

**Implementation note:** This should be baked into the agent's system prompt, not applied as a post-generation filter. The jargon ban is preventive, not corrective.

---

## 2. Creative Ideas Prompt (Full System + User + Few-Shot)

**Purpose:** Generate 3 customized outbound use cases per prospect for the Creative Ideas campaign.
**When to use:** Eric's single best-performing campaign template. Default for new clients.
**Provenance:** Campaign doc `[V]` + LinkedIn 230 `[V]` + Gap resolution (NotebookLM query)

### System Prompt

```
You are a senior business strategist who helps companies find
creative ways to use products and services. You think like a
consultant, not a salesperson. Your ideas are specific, actionable,
and grounded in what the company actually does.

RULES:
- Each idea must be 1-2 sentences maximum
- Each idea must reference something specific about the prospect's
  business (industry, audience, product, challenge)
- Each idea must be constrained to ONE specific feature or
  capability of the product being pitched
- Ideas should sound like a smart colleague brainstorming over
  coffee, not a pitch deck
- Never use words like: leverage, synergy, innovate, optimize,
  disrupt, amazing
- Write at a 5th grade reading level
```

### User Prompt

```
COMPANY INFORMATION:
Company: {{company_name}}
Description: {{company_description}}
Industry: {{industry}}
What they sell: {{what_they_sell}}
Target audience: {{their_target_audience}}

OUR PRODUCT/SERVICE:
Name: {{your_product_name}}
What it does: {{your_product_description}}
Key features:
1. {{feature_1}}
2. {{feature_2}}
3. {{feature_3}}

Generate exactly 3 creative, specific ideas for how {{company_name}}
could use {{your_product_name}} to improve their business.

CONSTRAINTS:
- Idea 1 must relate to feature: {{feature_1}}
- Idea 2 must relate to feature: {{feature_2}}
- Idea 3 must relate to feature: {{feature_3}}
- Each idea must be 1-2 sentences
- Each idea must reference something specific about their business

EXAMPLES OF GOOD OUTPUT:

Example for a marketing analytics company targeting e-commerce:
- "Track which Instagram Reels drive the most add-to-cart events
  for your skincare line, so you can double down on the content
  format that actually converts."
- "Set up automated alerts when your CAC on Facebook exceeds your
  target threshold of $45, so your team can pause underperforming
  ad sets before they waste budget."
- "Compare your email open rates against the beauty industry
  benchmark of 18.7% to see if your subject lines are
  underperforming relative to peers."

Example for a B2B sales platform targeting SaaS companies:
- "Auto-enrich your inbound demo requests with technographic data
  so your AEs know what tools prospects already use before the
  first call."
- "Score leads based on how closely they match your top 20
  customers by employee count and tech stack, so your SDRs
  prioritize the accounts most likely to close."
- "Track which LinkedIn posts drive the most demo requests so
  your content team knows what topics resonate with engineering
  leaders."

Now generate 3 ideas for {{company_name}}:
```

**Key rules:**
- Train with 3-5 manual examples before deploying (examples are the most important input)
- Each bullet must be theme-constrained to a specific product feature to prevent hallucination
- This is the authorized exception to the "AI writes snippets only" rule
- The AI output IS the value, not a wrapper around a pitch

---

## 3. Company Mission First Line Prompt

**Purpose:** Generate a fallback first line when no recency signal is available. Summarizes what the company does in <6 words.
**When to use:** Default fallback in the recency waterfall when no LinkedIn post, job change, or company news is found.
**Provenance:** Gap resolution (NotebookLM query)

```
Read this company's LinkedIn description and summarize what they
do in fewer than 6 words.

Start your output EXACTLY with this prefix:
"I was on your LinkedIn company page and it looks like you're
focused on "

Then complete the sentence with your summary.

RULES:
- Maximum 6 words after the prefix
- Use plain language, no jargon
- Describe what they DO, not what they ARE
- Do not use words like: leverage, synergy, innovate, optimize

EXAMPLES:
Input: "Acme Corp is a leading provider of cloud-based enterprise
resource planning solutions for mid-market manufacturing companies."
Output: "I was on your LinkedIn company page and it looks like
you're focused on cloud ERP for manufacturers"

Input: "FreshBites delivers healthy, chef-prepared meals to busy
professionals in the San Francisco Bay Area."
Output: "I was on your LinkedIn company page and it looks like
you're focused on healthy meal delivery"

INPUT:
{{company_linkedin_description}}
```

---

## 4. Social Post Hook Prompt

**Purpose:** Summarize a prospect's recent LinkedIn or TikTok post in <8 words for use as a recency hook in Email 1.
**When to use:** When the recency waterfall finds a recent social media post as the top signal.
**Provenance:** Gap resolution (NotebookLM query) + LinkedIn 100 `[V]`

```
Read this social media post and summarize the main topic in
fewer than 8 words.

Start your output EXACTLY with this prefix:
"I just wanted to reach out because I saw your post about "

Then complete the sentence with your summary.

RULES:
- Maximum 8 words after the prefix
- Capture the TOPIC, not the opinion
- Use plain language
- Do not editorialize or compliment
- Do not use words like: leverage, synergy, innovate

EXAMPLES:
Input: "Just wrapped up our Q3 planning session. Biggest takeaway:
we're doubling down on outbound and hiring 3 new SDRs. If you
know anyone great, send them my way!"
Output: "I just wanted to reach out because I saw your post
about hiring SDRs and doubling down on outbound"

Input: "Hot take: most companies waste 80% of their marketing
budget on channels that don't convert. Here's what we did
instead..."
Output: "I just wanted to reach out because I saw your post
about cutting wasteful marketing spend"

INPUT:
{{post_content}}
```

---

## 5. Job Openings Relevance Prompt

**Purpose:** Connect a company's open job posting to a business problem your product solves. Two variants: job title inference and job description analysis.
**When to use:** When the recency waterfall identifies a relevant job posting (e.g., company hiring for a role your product supports or replaces).
**Provenance:** Gap resolution (NotebookLM query) + LinkedIn 203 `[V]`

### Variant A: Job Title Inference (No Description Available)

```
A company called {{company_name}} in the {{industry}} industry
is hiring for the role: {{job_title}}.

Infer what business problem or priority this hire signals in
one sentence (maximum 12 words).

Start your output EXACTLY with:
"It looks like you're "

RULES:
- Infer the BUSINESS NEED, not the job duties
- Use plain language
- Maximum 12 words after the prefix

EXAMPLE:
Input: Company: Acme SaaS, Industry: Sales Tech, Role: "Senior
Data Engineer"
Output: "It looks like you're building out your data infrastructure"
```

### Variant B: Job Description Analysis

```
A company called {{company_name}} is hiring for {{job_title}}.
Here is the job description:
{{job_description}}

Our product does: {{your_product_description}}

In one sentence (maximum 15 words), explain how our product
connects to the priorities described in this job posting.

Start your output EXACTLY with:
"I noticed you're hiring a {{job_title}} and it looks like "

RULES:
- Connect our product to THEIR hiring priority
- Do not make claims we cannot verify
- Use plain language
- Quote specific phrases from the job description if relevant

EXAMPLE:
Input: Role: "RevOps Manager," JD mentions "cleaning up Salesforce
data and building repeatable pipeline reports"
Product: "Data enrichment platform"
Output: "I noticed you're hiring a RevOps Manager and it looks
like cleaning up your CRM data is a priority -- that's exactly
what we help with"
```

---

## 6. Deep Research AI Feature Prompt

**Purpose:** Determine if a company uses AI in their product and generate a feature-specific sentence. Used for technology-triggered campaigns.
**When to use:** When targeting companies that may use AI and your product/service relates to AI capabilities.
**Provenance:** Gap resolution (NotebookLM query)

```
Research this company and determine if they use AI or machine
learning in their product or service.

Company: {{company_name}}
Website: {{company_website}}
Description: {{company_description}}

STEP-BY-STEP REASONING (show your work):
1. Look for mentions of AI, ML, machine learning, artificial
   intelligence, neural networks, NLP, computer vision, or
   predictive analytics in their description
2. Check if their product features mention any AI capabilities
3. Determine confidence level: HIGH (explicit AI mention),
   MEDIUM (implied by product type), LOW (no evidence)

OUTPUT FORMAT:
If confidence HIGH or MEDIUM:
"{{company_name}} uses AI for {{specific_feature_in_8_words}}"

If confidence LOW:
"I couldn't confirm AI usage for {{company_name}} -- fallback
to company mission first line"

I am trusting you to be accurate here. If you are not confident,
say so. Do not hallucinate AI features that don't exist.

RULES:
- Maximum 8 words for the AI feature description
- Be specific: "product recommendation engine" not "AI capabilities"
- Show your reasoning before the final output
- If unsure, use the LOW confidence fallback
```

---

## 7. The 4-Step Prompting Framework

**Purpose:** Meta-framework for building any new AI prompt for Clay enrichment or email snippets.
**When to use:** When creating new prompts not covered by the templates above.
**Provenance:** NotebookLM Signal 100 `[M][S]` + LinkedIn 118 `[V]`

```
STEP 1: DEFINE THE GOAL
- What is the AI generating? (first line, value prop snippet,
  creative idea, lead score, etc.)
- What is the output format? (sentence prefix, word count,
  structured data)
- What is the one job this prompt does?

STEP 2: PROVIDE REFERENCE DATA
- What company/prospect data feeds into the prompt?
- What does the AI need to know about YOUR product/service?
- What context makes the output relevant?

STEP 3: CONSTRAIN CREATIVITY
- Word count limit (2-7 words for snippets, 1-2 sentences for ideas)
- Banned words (leverage, synergy, innovate, optimize, disrupt, amazing)
- Sentence prefix to force output format
- Jargon guardrails via system prompt
- Theme constraints (each output tied to specific feature/topic)

STEP 4: PROVIDE MANUAL EXAMPLES (MOST CRITICAL STEP)
- Write 3-5 "gold standard" examples by hand
- Examples define the tone, length, and quality bar
- Remove weak examples -- 3 excellent > 7 mediocre
- Examples are more important than instructions
```

**Eric's rule:** "Every AI in your workflow should do one task at a time." (LinkedIn 118, tip #7). Do not combine multiple generation tasks into a single prompt.

---

## 8. Confidence Scoring Technique

**Purpose:** Force AI to self-assess output quality and flag uncertain results for human review.
**When to use:** Any AI enrichment where false positives are costly (lead scoring, company classification, AI feature detection).
**Provenance:** NotebookLM `[S]` + LinkedIn 118 `[V]`

```
After generating your output, score your confidence:

CONFIDENCE LEVELS:
- HIGH: I found direct, explicit evidence for this claim
  (source: {{cite_source}})
- MEDIUM: I inferred this from related evidence but it's
  not explicitly stated
- LOW: I'm guessing based on limited information

OUTPUT FORMAT:
{{your_generated_output}} [CONFIDENCE: {{HIGH/MEDIUM/LOW}}]

If CONFIDENCE is LOW, append: "[NEEDS HUMAN REVIEW]"
```

**Agent instruction:** Use confidence scoring on any AI output that feeds directly into email copy. LOW confidence outputs should be filtered out or replaced with fallback content. Never send an email with a LOW confidence AI-generated snippet.

---

## 9. "Paralegal / Lawyer" Model Chaining Pattern

**Purpose:** Use cheap models (GPT-4o mini) for high-volume tasks, escalate to expensive models only for complex reasoning.
**When to use:** When building Clay workflows that process thousands of leads. Cost optimization at scale.
**Provenance:** LinkedIn 118 `[V]` (tip #10) + LinkedIn 244 `[V]`

### Architecture

```
STAGE 1: PARALEGAL (GPT-4o mini — $0.001/call)
  - High-volume, low-complexity tasks
  - Lead scoring (True/False or 1-10)
  - Simple enrichment (company mission summary, job title inference)
  - Email snippet generation (2-7 word constrained outputs)
  - Jargon filtering
  - Data validation

STAGE 2: LAWYER (GPT-4o or Claude — $0.01-0.05/call)
  - Only invoked when paralegal flags uncertainty
  - Complex reasoning (edge-case lead scoring, elaborate research)
  - Multi-step analysis (competitive displacement evaluation)
  - Creative Ideas generation for high-value prospects

DECISION RULE:
  IF paralegal_confidence >= HIGH → use paralegal output
  IF paralegal_confidence == MEDIUM → use paralegal output
    with human review flag
  IF paralegal_confidence == LOW → escalate to lawyer model
```

### Cost Math

```
At GEX scale (3M emails/month):
  GPT-4o mini at $0.001/call: $3,000/month
  GPT-4o at $0.03/call: $90,000/month (if used for everything)

Chaining saves ~97% by using expensive models only for
the ~3% of leads that need complex reasoning.

Eric's stated cost: "$0.02 total per email" (per-line enrichment)
```

**Eric's rule:** "Since we send so much, we do everything with 4o mini. Haven't seen a case where any of the others can really do something so much better that it's worth the expense." (LinkedIn 244)

**Exception:** Gemini Flash noted for "needle-in-haystack" tasks (LinkedIn 168, credited to Alexander Han at Overjoy) -- finding specific data points in large unstructured text.

---

## 10. Prompt Anti-Patterns

Do NOT build prompts that:

| Anti-Pattern | Why It Fails | What to Do Instead |
|-------------|-------------|-------------------|
| Ask AI to "write a cold email" | Output will be generic, bloated, and use every banned word | Describe the persona and tone. Never mention "cold email." |
| Generate full emails | AI cannot maintain the human-written template quality across a full email | Generate snippets (2-7 words) that slot into human templates |
| Use a single mega-prompt | "Long, 'all-in-one' prompts rarely nail everything" | Break into atomic tasks, one prompt per job |
| Skip few-shot examples | Without examples, the AI has no quality bar | Write 3-5 manual "gold standard" examples first |
| Provide 10+ weak examples | Quantity dilutes quality | 3 excellent examples > 7 mediocre ones |
| Include "per se" in instructions | Will confuse the model (Eric's misspelling, not the model's job) | Use correct spelling in prompts; voice matching is a different task |
| Set AI temperature too high | Increases hallucination risk in factual tasks | Use low temperature for enrichment, moderate for Creative Ideas |
| Use AI for tasks formulas can do | Wastes money and adds latency | "Formula-over-AI rule": use deterministic enrichment when possible |
