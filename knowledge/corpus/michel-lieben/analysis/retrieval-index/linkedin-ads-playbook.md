---
type: corpus
aliases: ["LinkedIn Ads Playbook -- Michel Lieben"]
corpus: michel-lieben
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# LinkedIn Ads Playbook -- Michel Lieben

**Corpus:** michel-lieben
**Generated:** 2026-03-25

---

## Core Strategy: Thought Leader Ads Behind Proven Organic Posts

Michel's LinkedIn Ads strategy does not create net-new ad creatives. Instead, it identifies organic LinkedIn posts that already booked meetings, then puts paid ad spend behind those exact posts targeting lookalike prospects.

### The Process
1. Review which organic posts booked meetings (check which persona responded to which post)
2. Identify the exact job titles and industries of the prospects who booked
3. Run "Thought Leader" ads exposing that same post to more people matching that exact persona
4. Result: proven content + proven audience = high-converting paid distribution

### Performance Metrics
- **CPM:** $15 on Thought Leader ads
- **Time to impact:** "Massive impact" in meetings booked within three weeks of testing
- **Client ROI:** $472K at over 3x ROI across six months of combined outbound + LinkedIn Ads
- **Monthly spend example:** $5,100 in July 2025, generating 155,000 extra impressions at $33 CPM

---

## Three-Layer Ad Funnel

Michel warns against running the same "Book a Demo" CTA to every audience. The funnel has distinct layers:

### Top of Funnel (Awareness)
- **Document ads:** 5-8 page carousels packed with pure tactical value. 2-3x engagement vs. single image ads.
- **Single image ads:** Pain/fear hook paired with solution. Takes up maximum mobile real estate.
- **Thought-leader mini-demo videos:** 15-30 seconds, authentic and unpolished. Not production-quality ads.

### Middle of Funnel (Retargeting)
- Retarget people who engaged in the last 90 days
- Show proof content: client stories, results, testimonials

### Bottom of Funnel (Direct Response)
- Direct response CTAs to hot audiences only
- These people already know ColdIQ from organic content and retargeting

---

## LinkedIn Ads via API (Ivan Falco's Claude Code Workflow)

Ivan Falco automated LinkedIn Ads to bypass the platform's clunky native UI for bulk campaign management.

### Setup
- **Command hub:** Google Sheet with columns for campaign group, campaign name, targeting tags, landing page URL, ad copy, and Google Drive folder reference for creative assets
- **Engine:** Claude Code reads the Google Sheet, summarizes the proposed campaign, builds it from scratch via LinkedIn API
- **Targeting:** Uses saved audiences (bottom-of-funnel lists, ABM company tags built from outbound data)
- **Creative fetch:** Claude Code autonomously retrieves the correct visual asset from Google Drive based on a reference name

### Build Process
1. Input all campaign parameters in Google Sheet
2. Summon Claude Code in the campaign manager folder
3. Claude Code reads sheet, provides summary for human review
4. On confirmation, creates campaign via API
5. Campaign appears in LinkedIn Campaign Manager within seconds

### How Ivan Built This
- Used Claude Code's "plan mode" to figure out correct API calls through trial and error
- Each successful action saved as a reusable "skill" via checkpoint command
- Custom UI built on top of the scripts for non-technical team members
- API used for LinkedIn Ads; MCP available for Meta and Google Ads

### Scaling Uses
- Bulk updates to active campaign biddings
- Continuous updates to targeted account lists
- New campaign creation from spreadsheet in seconds
- Available to the broader team via custom UI (no terminal knowledge needed)

---

## LinkedIn Ads + Organic Synergy

The core insight: LinkedIn Ads and organic content are not separate channels. They compound.

- Organic posts test messaging and persona fit at zero cost
- Posts that book meetings prove which angle + audience combination works
- Thought Leader ads amplify proven posts to 10-100x the original organic reach
- The same visual and copy that worked organically works in paid because it already passed the market test
- Ivan goes through Alex's best-performing posts, identifies the ones that booked meetings, and boosts exactly those

**Warning:** Michel explicitly advises against broad Google or Meta ads. Ad platform algorithms will happily spend your budget bidding on your own brand name (making you pay for clicks you would have won organically). LinkedIn Ads work because the targeting is precise and the content is already validated.

---

## ABM Campaign Integration

LinkedIn Ads pair with outbound for ABM (Account-Based Marketing) campaigns:

- Build target company list via outbound tools (Clay, Ocean.io, Apollo)
- Upload company list as LinkedIn ABM audience
- Run Thought Leader ads targeting specific job titles at those exact companies
- Simultaneously run cold email and LinkedIn DM outreach to the same accounts
- Prospect sees organic content + paid ads + cold email = "ColdIQ is everywhere" effect
- ABM example: Ivan's AirOps campaign generated $3M pipeline, $500K closed-won in 6 months

**Provenance:** [S] (NotebookLM Q25) confirmed by [D] (LinkedIn posts 016, 143) and [P] (Blog article 018)
