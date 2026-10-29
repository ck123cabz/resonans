---
type: tool
aliases: ["Lead generation tools"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Lead generation tools
speaker: Nate Herk; Sav (guest) for the cold-email infrastructure
provenance: D
sources: [q12, q26, q38, q45]
videos: [claude-code-clay-makes-lead-generation-actually-fun.md, how-a-college-student-made-500k-with-cold-email-exact-framework.md, beginner-s-guide-to-metadata-make-your-rag-agents-smarter.md, build-sell-n8n-ai-agents-8-hour-course-no-code.md, this-ai-agent-can-scrape-and-screenshot-the-web-with-no-code-n8n-tutor.md, learn-voice-agents-now-thank-me-later-full-beginner-s-guide.md, how-to-build-a-one-person-ai-business-using-claude-code.md, 3-hidden-data-table-hacks-for-smarter-ai-agents.md]
---

# Lead generation tools

Scraping, enrichment, sending and voice tools Nate Herk uses or shows for finding clients, 2025 to 2026. Every cold-email volume and reply-rate figure in this corpus comes from his guest Sav, a student, not from Nate's own agency; those sections carry the guest tag. The emails themselves are in `script-cold-email.md`.

## Clay: waterfall enrichment
`[T] · [D] · uploaded 2026-07-12 · claude-code-clay-makes-lead-generation-actually-fun.md · q12, q26 · version-bound`

Clay holds its own B2B data and has negotiated access to other providers. When enriching a contact it tries the top provider, then the next, until one hits.

> with the waterfall that number is going to increase somewhere up to more like 80 to 90% (claude-code-clay-makes-lead-generation-actually-fun.md)

The baseline he compares against is about 30% from a single vendor. q26's "250+ providers" was not checked. He drives Clay from Claude Code with a `/goal` prompt: 50 enriched HVAC leads with personalized subject lines and bodies.

## Clay: buy pre-warmed inboxes capped at 30 a day
`[T] · [D] · uploaded 2026-07-12 · claude-code-clay-makes-lead-generation-actually-fun.md · q26 · version-bound`

> you can buy domains right here in clay that are going to be warmed up for you and they're going to make sure that you're only sending 30 per day (claude-code-clay-makes-lead-generation-actually-fun.md)

## Clay: about $24 for 100 leads
`[R] · [D] · uploaded 2026-07-12 · claude-code-clay-makes-lead-generation-actually-fun.md · q26, q38 · version-bound`

> let's say you are converting about 1% of the people you're reaching out to this would cost you 24 bucksish to get 100 leads (claude-code-clay-makes-lead-generation-actually-fun.md)

His argument: one conversion out of 100 earns more than $24. q38 gives no Clay plan price. The Google-review cold email in this video ("4.7 stars across 4,100 reviews") is Claude's output from the demo, which he read aloud, not a template he wrote.

## [D:guest:Sav] Instantly as the sending platform
`[T] · [D:guest:Sav] · uploaded 2026-02-14 · how-a-college-student-made-500k-with-cold-email-exact-framework.md · q26 · version-bound`

> this is how i made half a million dollars in sales opportunities inside of instantly (how-a-college-student-made-500k-with-cold-email-exact-framework.md)

The half million is pipeline, not revenue. Sav's stack also included Clay, Apollo and n8n.

## [D:guest:Sav] Domains, inboxes and 30 a day per inbox
`[R] · [D:guest:Sav] · uploaded 2026-02-14 · how-a-college-student-made-500k-with-cold-email-exact-framework.md · q26 · version-bound`

Sav started on one domain with five inboxes, 150 sends a day. He says the usual advice is two or three inboxes per domain and five at most.

> you could put like five dom inboxes underneath each domain it's not advisable people typically recommend like two or [three] (how-a-college-student-made-500k-with-cold-email-exact-framework.md)

Scaling math spoken in the video: 3 domains, 15 inboxes, 450 a day, about 9,000 a month. He now runs "40 to 50 inboxes". The 450-a-day failure with no replies belongs to a different student, Christian, in the 7-day video; do not attach it to Sav. He skipped DNS setup (SPF, DKIM, DMARC) as "a massive rabbit hole".

## [D:guest:Sav] List cleaning: Million Verifier and Anymailfinder
`[T] · [D:guest:Sav] · uploaded 2026-02-14 · how-a-college-student-made-500k-with-cold-email-exact-framework.md · q26 · version-bound`

Captions read "mill million verifier or any mailinder". He builds lists from niche databases such as the American Institute of Architects, so the list carries no irrelevant contacts. His first personalization automation ran on Make.com, four modules long, feeding a Google Sheet.

## [D:guest:Sav] Reply-rate tiers
`[R] · [D:guest:Sav] · uploaded 2026-02-14 · how-a-college-student-made-500k-with-cold-email-exact-framework.md · q26 · stable`

Under 2%: infrastructure or list problem. 2 to 5%: copy problem. 5 to 10%: the golden zone. Over 10%: elite.

> anything above a 5% reply rate below a 10% reply rate i would say that's like the golden zone (how-a-college-student-made-500k-with-cold-email-exact-framework.md)

The funnel stops at 225 interested out of 9,000 sends. q26's "10 to 20 calls, 1 to 3 deals" is not in the captions.

## Apify: scraper marketplace, code "30 Nate Herk"
`[T] · [D] · uploaded 2025-05-23; 2025-07-23 · build-sell-n8n-ai-agents-8-hour-course-no-code.md; beginner-s-guide-to-metadata-make-your-rag-agents-smarter.md · q38 · version-bound`

> make sure to use code 30 nate herk for 30% off for 3 months (beginner-s-guide-to-metadata-make-your-rag-agents-smarter.md)

He uses Apify actors for YouTube, X and social scraping. q38's per-1,000 prices ($5.00 per 1,000 videos, $1.30 per 1,000 comments) are [M]. Affiliate code; weigh the praise with that.

## Firecrawl: scrape to markdown, code "herk10"
`[T] · [D] · uploaded 2025-05-23; 2025-06-03 · build-sell-n8n-ai-agents-8-hour-course-no-code.md; this-ai-agent-can-scrape-and-screenshot-the-web-with-no-code-n8n-tutor.md · q12, q38 · version-bound`

> use code herk10 to get 10% off the first 12 months on your firecrawl plan (build-sell-n8n-ai-agents-8-hour-course-no-code.md)

Turns pages and whole sites into clean markdown by API or MCP. q38's free trial of 1,000 credits and Hobby price of $16 to $20 are [M].

## Tavily and Perplexity as search tools in n8n
`[T] · [D] · uploaded 2025-09-26 · 3-hidden-data-table-hacks-for-smarter-ai-agents.md · q08 · version-bound`

> i'm going to change from use the perplexity tool to use the tavly tool (3-hidden-data-table-hacks-for-smarter-ai-agents.md)

"Tavly" in the captions is Tavily. Both sit as web-search tools on n8n agents.

## Vapi: $10 buys about 18.5 credits
`[T] · [D] · uploaded 2025-11-06 · learn-voice-agents-now-thank-me-later-full-beginner-s-guide.md · q38 · version-bound`

> you would just use $10 to get about 18.5 credits (learn-voice-agents-now-thank-me-later-full-beginner-s-guide.md)

The voice front end he pairs with an n8n back end for inbound and outbound calls.

## Upwork: the demand numbers are Upwork's
`[R] · [D] · uploaded 2026-08-11 · how-to-build-a-one-person-ai-business-using-claude-code.md · q45 · version-bound`

> upwork's 2026 in demand skills report came out in february they found that demand for ai integration work specifically grew 178% year-over-year ai enabled freelancers on the platform earn about 40% more per hour (how-to-build-a-one-person-ai-business-using-claude-code.md)

A third-party statistic he cites. He calls Upwork his second channel after the warm network, "so so so much easier than cold outreach" on 2026-08-11; on 2026-02-04 he had said it was "pretty much going to be similar to cold outreach". Search keywords and the proposal line are in `script-warm-outreach-trojan-horse-upwork.md`.
