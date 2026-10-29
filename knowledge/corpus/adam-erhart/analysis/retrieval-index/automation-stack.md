---
type: corpus
aliases: ["Automation Stack"]
corpus: adam-erhart
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-19
---

# Automation Stack

How each productized service is built, demonstrated, priced and maintained. Source: `q03`, `q30`, `q31`, `q34`. Provenance `[S]`.

One file per question an operator actually asks: how do I build this, how do I show it to someone, and what do I charge.

---

## The platform

GoHighLevel, in use since 2019. The argument: it replaces 6 to 10 separate tools (ClickFunnels, ActiveCampaign, Zapier, Calendly) and drops software overhead from roughly $2,800/month to one platform fee, letting one operator run something that looks like a ten-person team.

| Plan | Price | What it unlocks | Who |
|---|---|---|---|
| Starter | $97/mo | Basic CRM, site builder, calendars, automations, 1–2 sub-accounts | A solo business owner, not an agency |
| Unlimited | $297/mo | Unlimited client sub-accounts, full white-label, prospecting audit tool | The agency tier |
| SaaS Pro | $497/mo | SaaS mode, automated signup, rebill and mark up phone/SMS/email/AI usage | Reselling software |
| White-label mobile app | +$497/mo | Branded app in the app stores | Skip as a beginner; use the free gray-labelled Lead Connector |

Because Unlimited is flat regardless of sub-account count, **the first client covers the entire stack** and every client after runs at 90%+ net. That flat fee is what makes the margin claim arithmetic rather than assertion.

**Warning:** avoid pure $97/month SaaS reselling as a beginner. It needs 50 to 100+ clients for a living, carries heavy support load and zero differentiation, and churns.

---

## The services

### Review engine
- **Does:** fires an SMS and email sequence after a job is marked complete, thanking the customer and linking straight to the Google review box. Auto-drafts replies to positive reviews.
- **Why it's the front door:** local businesses do not have a quality problem, they have a remembering problem. Staff forget to ask, so a solid business sits on 20 reviews while the competitor has 300. Results are visible in one to two weeks and it is nearly impossible to get wrong.
- **Build:** 10–20 minutes to connect the Google Business Profile and activate the snapshot.
- **Maintain:** 15–30 minutes a month reviewing negative feedback, approving responses, sending the client a progress note.
- **Price:** $197–$297/mo, sometimes $397.

### Missed-call text-back
- **Does:** instant SMS when an inbound call goes unanswered. "Hey, sorry we missed your call, we're currently with a client. How can we help you?"
- **Why:** 62% of calls to small local businesses go unanswered; 85% of callers hang up and call the next business rather than leave voicemail; 78% buy from whoever responds first.
- **Build:** 5–10 minutes. A tracking or forwarding number, a missed-call trigger, an SMS.
- **Maintain:** zero.
- **Demo:** call their line at night or over lunch, prove it goes to voicemail, then send a 2-minute Loom showing the missed call got no reply.
- **Price:** $100–$300 standalone, or bundled into $397–$497.

### AI receptionist / voice agent
- **Does:** 24/7 conversational voice agent answering on the first ring, or as after-hours and overflow backup. Answers FAQs, qualifies, collects details, books straight into the calendar.
- **Build:** HighLevel Voice AI module. Name the agent, pick a warm voice (he recommends female, citing human-factors and aviation research that callers are more articulate and compliant, the claim is his, no study is named). Train either by entering the business URL for the crawler, or by pasting a custom prompt. Assign a number, or attach to the existing line via carrier forwarding: `*71` Verizon, `*61` T-Mobile. Set it to take over after 3 rings, at lunch, and after hours.
- **Time:** 5 to 30 minutes depending on whether you refine the prompt and test the booking flow.
- **Maintain:** 10–15 minutes a month reading transcripts and booking logs, then a summary to the client.
- **Demo:** dial the demo number in front of the owner, or have them call it, and let them hear it book an appointment live. He calls this the Quiet Close, the owner goes silent calculating the missed calls.
- **Price:** $297–$497/mo plus an optional $500–$1,500 setup.
- **Guardrails:** an unbounded agent will state wrong prices. Point it at verified website data and configure fallback transfer to a human for complex calls.

### Conversation AI (web chat and social DM)
- **Does:** one AI across the website chat widget, Instagram DMs, Facebook Messenger and SMS. Handles 70–80% of routine questions and books appointments.
- **Build:** paste the business URL so the bot crawls services, pricing, hours and FAQs. Activate autopilot with intent detection. Connect the channels.
- **Time:** 10–15 minutes.
- **Demo:** show the widget live on a test site, or trigger a comment-to-DM sequence in front of them.
- **Price:** $397/mo, sold as "AI Conversations" bundling chat, social DMs and missed-call text-back.

### Revenue website
- **Does:** replaces an outdated, slow, non-mobile site with a converting one carrying an AI chat widget and speed-to-lead follow-up.
- **Why:** most local sites are fancy business cards that talk visitors out of buying.
- **Build:** clone an industry template in HighLevel's builder, swap logo, colours, text and booking link.
- **Time:** 15–30 minutes.
- **Maintain:** ~10 minutes a month.
- **Price:** $497/mo, or $1,000–$2,000 upfront plus $297–$497/mo.

### Automated follow-up closers
- **Does:** instant SMS within 1–2 minutes of any opt-in, then value emails, social proof, objection prompts, booking nudges and ringless voicemail across days 1, 2, 3, 5, 7, 14, 30 and 90.
- **Build:** pre-built in the Agency OS snapshot, one click plus 5–10 minutes customising variables.
- **Demo:** submit a test lead on screen and show a response inside 60 seconds, or cite the 42–48 hour industry average.
- **Effect claimed:** responding under 5 minutes makes qualifying up to 100x more likely than waiting 30; closes move from 1-in-10 to 3-or-4-in-10.
- **Price:** included in $297–$497 retainers.

### Google Business Profile / Map Pack
- **Does:** completes categories, hours, description and photos; clears the review-response backlog; syncs directory citations.
- **Build:** HighLevel's Google Business integration plus the built-in Yext integration for citations.
- **Time:** 30–60 minutes setup, 15–20 minutes a month.
- **Price:** $297–$500/mo, or $500–$1,500 packaged with full local SEO.

### White-label SaaS
- **Does:** HighLevel under your own brand, domain and Stripe, sold as DIY dashboard access.
- **Build:** SaaS Pro plan. The client signs up through your branded checkout and the platform provisions the account automatically.
- **Time:** zero, ongoing and upfront.
- **Price:** $97–$497/mo per sub-account. Selling HighLevel directly as an affiliate yields 40% recurring.
- **Role:** the downsell when a prospect cannot afford full management.

---

## The stacking sequence

Never sell the menu. One front door, then rooms.

| Month | Service | Price |
|---|---|---|
| 1 | Google reviews, visible proof in one to two weeks | $297 |
| 2–3 | AI receptionist, once they trust you | $397 |
| 5–6 | Revenue website, the conversion layer | $497 |

$1,191/month per client. Ten of them is $11,910.

Three rules: one front door on day one, never two. No upsell before 60 to 90 days of proven results. Never a fourth or fifth room, three services is the whole house.

Stickiness is the reason for the cap. Cancelling three interlocked systems means shutting down reviews, call coverage and the lead engine at once.

---

## The 48-hour launch

1. **Day 1**, start the $297 Unlimited trial, one-click import the Agency OS snapshot.
2. **Day 1**, pick one local niche, swap agency name, logo and domain into the pre-built one-page site.
3. **Day 2**, use the built-in prospecting tool or Google Maps to find listings missing reviews or failing to answer calls.
4. **Day 2**, send 10 warm messages or 2-minute Loom audits.
5. **Demo**, show the AI receptionist or review engine live in a test sub-account.
6. **On a yes**, create the sub-account, connect their Google Business Profile and phone number, set forwarding after 3 rings, activate the review trigger.
7. **Monthly**, 30 minutes reviewing dashboards and sending a screen-share or note to prevent churn.

Setup and selling are the same motion: the demo account is the product.

---

## Reactivation (ACRC)

The highest-leverage single play in the corpus.

**Get the list.** Ask the client to export past customers from QuickBooks, booking software, spreadsheets or old contacts. 200 to 500 is enough; 1,000+ is a large campaign.

**SMS over email**, on a claimed 95% read rate within 3 minutes and ~90% open rate.

**Two message options** (full text in `scripts-library.md`): the $20 gift-card voucher bait, which he calls highest converting, or Dean Jackson's nine-word message.

**Logic.** Positive intent fires the booking link. Negative unsubscribes. No reply gets one nudge at 24 to 48 hours. Dripped in batches across 14 days.

**Build time:** 10–15 minutes.

**Claimed maths.** On 1,000 past customers: 900 open, 270 respond (~30%), 135 buy at a 50% response-to-booking rate, $300 service = $40,500 with zero ad spend. On 500 at a conservative 3%: 15 appointments, $7,500. *The 30% response and 50% booking rates are the most aggressive numbers in the corpus. Treat the $40,500 as illustrative arithmetic, not a reported result.*

**Four ways to monetise:**
1. Risk-reversal power offer: "I'll get you as many appointments as you want in 14 days with zero ad spend, or you pay nothing. Are you interested?"
2. Flat fee, $1,500–$4,500 per campaign.
3. Performance or revenue share, or a fee per booked appointment.
4. Free as a Trojan horse: run it for 7 to 14 days at no charge, generate thousands in quick revenue, convert to a $297–$497/mo retainer.

---

## The Bridge Method

The commercial thesis. You are a mortgage broker, a travel agent, a wholesaler. You do not create the solution.

**Step 1, find the gap.**
- Missed-call gap: phone a local business during lunch or after 5pm and hit voicemail.
- Review gap: 12 reviews on Google Maps against a competitor's 180.
- Speed-to-lead gap: submit a quote request and wait hours or days.

**Step 2, find the fix.** Missed calls → text-back or voice AI. Review gap → the review engine. Slow follow-up → speed-to-lead workflows.

**Step 3, connect them.** Show the gap in a 2-minute Loom ("I called your business at 5:15 PM and hit voicemail, here's how many jobs that leak is costing you"). Demonstrate the fix live in a test account. On a yes, import the snapshot, connect their profile and phone, swap the name: 10 to 20 minutes, never custom development. Charge $297–$497/mo to keep it running.

---

## White-label fulfilment

Hand off analytical, structured work where a deliverable can be judged right or wrong without the client's opinion: Google Ads, Maps rankings, citation builds, link building, local SEO. Partners such as AgencyPro.

Keep or avoid subjective creative work, custom web design, social content, ad copy, because revisions and taste disputes break the model.

---

## Agency OS

His one-click HighLevel snapshot: review workflows, missed-call triggers, AI receptionist prompts, lead follow-up sequences, reactivation campaigns, no-show reminders, landing page templates, 2-minute audit scripts, outreach sequences, pre-call intake forms, a 90-day roadmap, client reporting dashboards.

It is also a paid product, so the corpus describes the container without its contents. Gap register item.

---

## Delegation

The buyback rate: (annual income ÷ 2,000 hours) ÷ 4. At $100K/year that is $50/hr, giving a $12.50/hr threshold. Anything outsourceable below it goes immediately. VAs on Upwork or Fiverr at $5–$10/hr for admin, report compiling and technical setup.

Note this sits alongside the zero-employee stance. Contractors are apparently not headcount.
