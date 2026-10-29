---
type: corpus
aliases: ["Evidence & Benchmarks: Nick Abraham"]
corpus: nick-abraham
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
knowledge_type: E
provenance: V
last_updated: 2026-03-20 (v1.1 — incremental update with 2020-2023 signals)
---

# Evidence & Benchmarks: Nick Abraham

## Operational Scale Metrics

| Metric | Value | Source | Date |
|--------|-------|--------|------|
| Monthly email volume | 2M+ | E51 [V] 182-2025-04-03 | Apr 2025 |
| Active clients | 283 (goal: 1,000 by EOY 2026) | O61 [V] 085-2025-12-11 | Dec 2025 |
| Meetings booked/month | 800+ | M86 [V] 601-2024-10-11 | Oct 2024 |
| Monthly revenue | $350K+ | VO16 [V] 062-2026-03-15 | Mar 2026 |
| Total inboxes managed | ~130K | IN25 [V] 044-2026-01-27 | Jan 2026 |
| Infrastructure spend/month | $35K+ | IN37 [V] 232-2025-07-22 | Jul 2025 |
| Cumulative cold emails sent | 30M+ | M35 [V] 061-2026-01-07 | Jan 2026 |
| Cumulative spend on leads | $2M+ | M35 [V] 061-2026-01-07 | Jan 2026 |
| Total clients served | 500+ | O51 [V] 023-2026-02-23 | Feb 2026 |
| Cold calls/month | 60,000+ | M41 [V] 093-2025-12-04 | Dec 2025 |
| Case studies produced | 40+ | O102 [V] 596-2024-10-16 | Oct 2024 |
| Hires made (lifetime) | 60+ | O103 [V] 620-2024-10-01 | Oct 2024 |


## Campaign Performance Benchmarks

| Benchmark | Value | Context | Source |
|-----------|-------|---------|--------|
| Positive replies on Email 1 | 80%+ | Across 200+ clients sending 2M+/month | E26 [V] 273-2025-06-16 |
| Email 1 responsible for meetings | >90% | Nov 2023 data analysis (inflection point for 4→2 shift) | K99 [V] 666-2024-09-03 |
| Reply rate confirming inbox delivery | >1% | Universal minimum across all offers | E24 [V] 262-2025-06-26 |
| Solid B2B reply rate | 2-4% | Most B2B offers, clean infrastructure | E24 [V] 262-2025-06-26 |
| Contact-to-lead ratio (realistic) | 1 lead per 350-500 contacts | Across 200+ clients | E24 [V] 262-2025-06-26 |
| Catch-all campaign reply rate lift | 30-80% higher | vs. standard SMTP-valid campaigns | M60 [V] 304-2025-05-14 |
| Bounce rate ceiling | <2-4% | Pause and re-clean above 4% | E5 [S] q04 |
| Inbox kill threshold | >10% bounce | On specific inbox with 1,000+ emails sent | E8 [S] q22 |
| Campaign intervention trigger | 3% bounce | Triggers automated ZeroBounce remediation | E8 [S] q22 |
| "Stupid personalization" reply rates | >3% | In over-sold markets (agencies, ecom) | E32 [V] 606-2024-10-09 |
| Cold-traffic close rate | 19-25% | Standard benchmark for warm sales process | E10 [S] q31 |
| Website visitor campaign reply rate | 4.6% | Internal Leadbird benchmark | E41 [V] 006-2026-03-19 |
| Website visitor 24hr close rate | 3x | vs. visitors who act later | M113 [V] 009-2026-03-19 |
| Open rate utility | Zero | Confirmed by 520 days of data | K94 [V] 641-2024-09-19 |
| ETL ratio (2023 formulation) | Total emails sent / leads booked | Only metric that matters; goal is lowest number possible | M-new-61 [V] 1071-2023-08-03 |
| 2-step switch: single-day record | 55 meetings in one day | After switching from 4-step to 2-step | E-new-4 [V] 0909-2024-02-13 |
| Strong PMF campaign | 57 leads in 30 days | No advanced copy, personalization, or scraping — offer-market fit alone | M-new-43 [V] 0972-2023-11-29 |
| Rule-breaking copy performance | 58 meetings in 10 days | 5+ paragraphs, multiple links, bold/italic — offer was a no-brainer | E-new-14 [V] 1111-2023-06-19 |
| Competitor follower close speed | 1 client in 41 days | Scraping competitor LinkedIn followers + hyper-relevant offer | M-new-68 [V] 1122-2023-06-06 |
| Cold email for SaaS acquisition | 20-40 paying users/day | SaaS product acquired strictly through cold email | E-new-8 [V] 0793-2024-05-16 |
| Campaign case study | 3 clients in 30 days | 3,500 net new leads, 15,000 emails total | E-new-9 [V] 0789-2024-05-20 |
| 1 lead per 375 contacts | Good cold email benchmark | Below this, root cause is offer, targeting, or deliverability | E-new-6 [V] 0806-2024-05-06 |


## Volume Math Model

At 1% positive reply rate, 80% meeting book rate, 15% close rate: [V] E28 [V] 476-2024-12-26

| Emails Sent | Positive Replies | Meetings Booked | Clients Closed |
|-------------|-----------------|-----------------|----------------|
| 2,500 | 25 | 20 | 3 |
| 5,000 | 50 | 40 | 6 |
| 10,000 | 100 | 80 | 12 |
| 15,000 | 150 | 120 | 18 |

Same conversion rates, more volume, linear scaling of revenue.


## $1M ARR Math Model

$1M ARR = approximately 112 clients/year (9-10/month) at $6K-$10K LTV with $1,500+ upfront. [S→V] O25/O99

Revenue math framework: LTV / goal revenue = clients needed / 12 = monthly new clients / 20% close rate = calls/month needed.


## Data Quality Benchmarks

| Metric | Value | Source |
|--------|-------|--------|
| Apollo raw pull → emails found | ~70% | E39 [V] 720-2024-07-19 |
| After verification → valid | ~20% of enriched (14% of original) | E39 [V] 720-2024-07-19 |
| Apollo/ZoomInfo raw pull validity (2023) | 40-50% valid | E-new-15 [V] 1194-2023-03-02 |
| NeverBounce breakdown (2023) | 41% valid, 42% risky, 17% invalid | E-new-15 [V] 1194-2023-03-02 |
| Scrubby risky-bucket recovery rate | 32% of risky → valid | E-new-15 [V] 1194-2023-03-02 |
| Lead list decay rate | ~9%/month | IN-new-20 [V] 1137-2023-05-17 |
| Scrubby pre-automation revenue | $70K before any app was built | IN-new-3 [V] 0826-2024-04-19 |
| Google People Chips false positive rate | 17% | IN12 [S] q24 / IN58 [V] 686-2024-08-16 |
| Google People Chips catch-all accuracy | Up to 40% invalid | M-new-6 [V] 0826-2024-04-19 |
| Auto-replies "no longer works here" | >15% of total replies | E36 [V] 690-2024-08-14 |
| Of those, new job on LinkedIn same day | 6/10 (60%) | E36 [V] 690-2024-08-14 |
| AI inbox categorization accuracy | 90% (10% failure fatal at scale) | O82 [V] 280-2025-06-09 |
| AI campaign creation error rate | 5% at 10K contacts = 500 wrong | M43 [V] 110-2025-11-13 |
| MillionVerifier bulk discount | 83.7% savings (100K vs 10M pack) | E21 [V] 139-2025-10-15 |
| Waterfall enrichment annual savings | ~$20K/year | M-new-67 [V] 1118-2023-06-09 |


## Infrastructure Benchmarks

| Metric | Value | Source |
|--------|-------|--------|
| Max inboxes per domain | 2-3 | IN1 [S→V] / IN67 [V] 302-2023-10-30 |
| Cold emails per inbox/day | 25 (+ 20-25 warm-up = 50 total) | IN10 [S→V] q21 |
| Summer 2024 crackdown limit | 5 cold/inbox/day | M107 [V] 715-2024-07-24 |
| Warm-up minimum | 14 days (6 weeks optimal) | IN10 [S→V] q21 |
| Warm-up start rate | 5 emails/day, increase 2-3/day | IN-new-13 [V] 0993-2023-11-03 |
| Warm-up target volume | 40-45/day after 14 days | IN-new-19 [V] 1048-2023-09-01 |
| Max total volume per inbox | 55-60/day (warmup + real) | IN-new-19 [V] 1048-2023-09-01 |
| Warm-up reply rate target (during) | 60% minimum | IN-new-13 [V] 0993-2023-11-03 |
| Warm-up reply rate target (post) | 80% after 14 days | IN-new-13 [V] 0993-2023-11-03 |
| AB Flip rotation | Monthly (30 days) | IN11 [S] / IN40 [V] 291-2025-05-28 |
| Idle set warmup | 45 days | IN40 [V] 291-2025-05-28 |
| Hypertide layover grace period | 18 days | IN24 [V] 042-2026-01-28 |
| Domain burn detection threshold | 40% worse than client average | IN24 [V] 042-2026-01-28 |
| Microsoft-to-Google domain transfer | 3-5 extra weeks of life | IN47 [V] 397-2025-02-20 |
| Shared infra Set A warmup | 30 days minimum | IN19 [V] 001-2026-03-19 |
| Shared infra Set B warmup | 60 days | IN19 [V] 001-2026-03-19 |


## Financial Benchmarks

| Metric | Value | Source |
|--------|-------|--------|
| Minimum viable stack cost | ~$700/month | E43 [V] 150-2025-09-25 |
| Revenue achievable at that cost | $50K/month (with good offers) | E44 [V] 153-2025-09-09 |
| Minimum client revenue for DFY | $20K/month | O13 [S→V] / O21 [S] |
| VSL cost → revenue generated | $500 → $1M+ | O107 [V] 730-2024-07-11 |
| Offshore talent cost savings | 30-40% | O34 [V] q29 |
| Stripe dispute win rate | 99.9% | O133 [V] 156-2025-08-20 |
| Software replaced via Lovable/Replit | $10K+/year saved | E52 [V] 181-2025-04-12 |
| Content-to-demo CPA | ~$50 | O41 [S] q34 |
| Content demos/month achievable | 100+ | E49 [V] 326-2023-06-29 |
| Paid ads ROAS (Fazio case) | 5.5x ($432K → $2.36M) | E30 [V] 518-2024-11-29 |
| Paid ads burned without tracking | $80K | E55 [V] 122-2025-12-30 |
| Hiring burned without SOPs | $50K+ | O76 [V] 213-2025-08-07 |


## Channel Comparison Benchmarks

| Channel | Key Metric | Source |
|---------|-----------|--------|
| Cold email | 2M+/month possible, 1 lead per 350-500 contacts | E24/E51 [V] |
| LinkedIn DMs | 5x higher reply rates than email (late 2025) | E18 [V] 119-2025-11-05 |
| LinkedIn connections | 400 requests → 200 accept → 40 reply → 8 interested | E47 [V] 366-2022-06-15 |
| Cold calling | 2 AEs + 1 BDR = 3-9 extra appts/day | E45 [V] 210-2024-09-30 |
| Cold calling (novice) | 7% connect rate, 19 demos in 4 days | E27 [V] 451-2025-01-10 |
| Direct mail (pizza ABM) | $15K → 75 clients → $1M revenue | E50 [V] 191-2025-01-11 |
| Holiday sending | 7+ leads/day including Christmas | E42 [V] 193-2024-12-31 |


## Timeline / Revenue Trajectory

| Year | Revenue/Scale | Notes |
|------|--------------|-------|
| 2017 | $10/hr | Gas station |
| 2018 | $3K/mo | Instagram theme page |
| 2019 | $10K/mo | Agency, $0 profit |
| 2020 | $10K/mo | Leadbird founded |
| 2021 | $30K/mo | Growing |
| 2022 | $60K/mo | Growing |
| 2023 | 75 clients | Over-hiring disaster, recovery |
| 2024 | 150+ clients | Deliverability apocalypse, 200% YOY pace |
| 2025 | 200+ clients | Hardest year in lead gen |
| 2026 | 283 clients, $350K+/mo | Goal: 1,000 clients by EOY |

Source: E46 [V] 213-2024-09-30 and multiple corroborating signals


## Earlier-Era Benchmarks (2020-2023)

| Metric | Value | Context | Source |
|--------|-------|---------|--------|
| 2020 personalization benchmark | 76% open, 13% response, 4% booking | Outsourced research + personalization (VA model) | E-new-16 [V] 1219-2020-10-28 |
| 2023 per-client volume | 7,000 emails/month | 1,500 leads, 10 inboxes, 35/day/inbox, 20 sending days | E-new-12 [V] 1033-2023-09-19 |
| 2023 total monthly volume | 700,000 emails/month | At 105 clients | E-new-11 [V] 1032-2023-09-20 |
| 2023 growth rate | 25 → 110 clients (200% in 12 months) | Founder stayed in fulfillment | E-new-10 [V] 0960-2023-12-15 |
| 2023 scaling speed | 30 → 105 clients in 8 months | KPI input chains + client experience optimization | O-new-16 [V] 1056-2023-08-24 |
| 2024 agency growth | 400% in 2023 (30 → 120+ clients) | Primary driver: 4x more social proof | E-new-5 [V] 0924-2024-01-26 |
| 2024 2-step switch result | 800+ meetings/month | After cutting from 4-step to 2-step sequence | E-new-3 [V] 0904-2024-02-19 |
| Agency volume at scale | 1,000,000+ cold emails/month | Generating 500-800 leads | E-new-2 [V] 0835-2024-04-12 |
| Inbound compounding threshold | 90+ days | Consistent content before results appear | O-new-21 [V] 1100-2023-06-29 |
| Infrastructure failure cost | $10K+ in one week | Multiple systems down simultaneously (Aug 2023) | O-new-17 [V] 1062-2023-08-14 |

### Volume Math (2023 edition)

Per client: 1,500 scraped/verified leads → 10 inboxes → 35 emails/day/inbox → 20 sending days/month → 7,000 total emails/month. At 105 clients, this aggregated to 700,000 emails/month.

2-step sequence with 3,000 leads sends 7,000 total emails (Email 1 to all, Email 2 to all). Framework produces enough data for educated iteration decisions. [V]
