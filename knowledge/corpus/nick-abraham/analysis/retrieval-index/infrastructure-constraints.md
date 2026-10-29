---
type: corpus
aliases: ["Infrastructure Constraints: Nick Abraham"]
corpus: nick-abraham
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
knowledge_type: IN
provenance: mixed
last_updated: 2026-03-20
---

# Infrastructure Constraints: Nick Abraham

## Domain Setup Rules

**Domain selection.** Secondary .com domains only. No hyphens, no numbers. Forward to primary company site. "Aged" domains from providers are often a scam — prior reputation history cannot be reliably certified. [S→V]

**DNS configuration.** DKIM, DMARC, and SPF must be configured on every domain. Verify via MX Toolbox before any sending. [S→V]

**Density limits.** Maximum 2-3 inboxes per domain. Each domain in its own tenant. Google and Microsoft can see panels with 10+ domains and flag the entire organizational panel. [S→V]

**Providers.** Google Workspace and Microsoft Outlook only. Never private SMTP. Private SMTP networks work until they commercialize and get caught by enterprise filters (Mimecast, Proofpoint). Bad actors systematically destroy SMTP providers by ramming low-quality emails through new providers until they get flagged. [S→V]

**Cheapest acquisition.** Wait for Porkbun .co sales (domains at approximately $2.48 each), buy in bulk (2,000 at a time), set up Google/Microsoft inboxes. [V]


## Warm-Up Parameters

**Duration.** 14-day minimum. 6 weeks optimal. Warm-up stays on throughout live campaigns — never turn it off. [S→V]

**Volume.** 20-25 warm-up emails per day at 100% reply rate, plus 25 cold emails, equals 50 total per day per inbox. During the Summer 2024 crackdown, this dropped to 5 or fewer cold emails per inbox per day with reduced warm-up volume. [S→V]

**Pool.** Use Smartlead's warm-up pool. The agency runs approximately 130,000 inboxes through it. Smartlead spends multi-six figures monthly on 70M+ daily warm-up emails and would shut the network down if data showed it was ineffective. Private warm-up pools cost 3x without reliably yielding 3x results — seeds burn out in smaller pools. Anti-warm-up claims come from small-sample operators. [S→V]

**Holiday handling.** During sending pauses (if any), increase warm-up volume to create more positive engagement signals, improving deliverability heading into the new period. [V]


## The AB Flip

Buy double infrastructure: Set A and Set B. Run campaigns on Set A for 30 days. Switch to Set B for month 2. During Set B's active period, assess Set A's deliverability — delete and replace burned domains while idle. 45-day warm-up on the idle set before it rotates back in. [S→V]

This rotation prevents domain fatigue and ensures fresh sending infrastructure is always available. The cost (2x infrastructure) is the price of sustainable sending at scale.


## Hypertide Infrastructure

One Hypertide subscription provides: 4 domains, 25 inboxes per domain (100 inboxes total), sending 10K emails per month, from US IPs on Microsoft datacenters, individual tenants (unlike most resellers that share tenants). [V]

**Layover.** When a domain is burned, billing stops immediately but sending continues for 18 days. This grace period allows break-up emails and late replies to still be delivered. [S→V]

**Relay.** Late replies to deleted domains still reach the inbox. This prevents losing leads that respond after infrastructure has been rotated out. [S→V]


## Shared Infrastructure for New Clients

Launch new clients immediately on shared non-branded domains (200 purchased, rotated) while branded client domains warm in the background. Set A minimum 30-day warmup, Set B 60-day warmup. Transforms a fulfillment bottleneck (waiting weeks for domain warmup) into a sales advantage (Day 5 campaign launch). [V]

Keep emergency non-branded backup domains available at all times. [V]


## Domain Health Management

**The 40% Rule.** Flag any domain performing 40% worse than the client's average reply rate. That domain gets killed. [V]

**Bounce code monitoring.** Check bounce codes by domain, not just aggregate. Kill domains immediately when bounce codes indicate reputation damage. [V]

**Microsoft-to-Google transfer.** When a Microsoft-hosted domain burns, transfer to Google. Currently yields 3-5 extra weeks of sending life post-transfer. Effectiveness will likely diminish as providers share reputation data. [V]

**Inbox kill threshold.** Bounce rate greater than 10% on a specific inbox with at least 1,000 emails sent = that inbox is dead. [S]


## Sending Schedule

**Timing.** Monday through Friday, 9am-5pm. Smartlead API randomizes start and end times by plus or minus 30 minutes for variability. Mimics human sending patterns. [S→V]

**Weekends.** Saturdays work for SMBs and mid-market. Do not pause on weekends. [V]

**Holidays.** Valid sending days. Inboxes are less crowded because competitors pause. Senior targets still check email. People are in more relaxed moods. Expect approximately 50% of typical positive reply volume (still worth it given reduced competition). 150,000 emails over Thanksgiving Thursday and Friday met or exceeded typical weekday performance. 7+ leads generated per day through the December 23-31 period including Christmas. [S→V]


## Secure Email Gateways (SEGs)

Proofpoint, Barracuda, and Mimecast protect enterprise inboxes. Do not discard leads behind these gateways — push them to the bottom of the CSV so your domain builds age and positive engagement signals before reaching them (around day 40-50 of the campaign). Pair with LinkedIn or phone outreach as backup channels for these contacts. [S→V]


## Catch-All Email Handling

**Isolation.** Run catch-all campaigns in a separate campaign from primary SMTP-valid campaigns. If bounce spikes on catch-alls, pause without contaminating the main campaign's deliverability. [S→V]

**Verification.** Scrubby is the only reliable catch-all verification method. It physically sends a blank email from burner Gmail accounts and waits 48-72 hours to confirm bounce or delivery. Google People Chips produces a 17% false positive rate on known-invalid catch-all emails — never use it for this purpose. [S→V]

**Tools.** Catch-all verification tools that do not distinguish SMTP valids from valid catch-alls cause more bounces, not fewer — you cannot isolate what is bouncing, making it impossible to clean properly. The correct stack separates these categories at every stage. [V]


## Deliverability Failure Modes

Five deliverability failure modes at scale (from 9M+ emails in 6 months): [V]

1. **No inbox provider diversification.** Never all eggs in one provider.
2. **Using sketchy SMTPs instead of Google/Microsoft.** Quality checks: does the provider have enterprise filter bypass? Track record over 12+ months?
3. **Too many inboxes per domain or per tenant.** Signals automated operation to mailbox providers.
4. **No infrastructure rotation.** Domains fatigue. Without the AB Flip or equivalent rotation, performance degrades over 30-60 days.
5. **Catch-alls mixed with SMTP valids.** Cross-contamination makes diagnosis impossible when bounce rates spike.

Additional failure anti-patterns: free Gmail/Outlook accounts for sending, no proper DNS, all domains in same tenant, 20+ inboxes per tenant, 500+ emails per inbox per day, measuring deliverability via open rates (which are broken), skipping warm-up, single-channel dependency. [V]


## Provider Diversification Mandate

Name at least one backup vendor for every tool you pay for: inboxes, infrastructure, data, enrichment, verification, sequencing. Vendor dependency is an operational death sentence. [V]

In a 72-hour period in October 2025: Clay started charging per API call, an Apollo scraper on Apify shut down, and inbox reseller crackdowns hit. Agencies relying on non-compliant infrastructure saw entire operations paused. [V]

Agencies that built pricing on blackhat scrapers and cheap/non-compliant infrastructure had campaigns fully paused when those tools were shut down. [V]

The agencies that survive current industry consolidation will: (1) successfully delegate knowledge to account managers, (2) have AMs handling 15-25+ accounts with AI leverage, (3) have backup infrastructure for every fulfillment component. [V]


## Admin Panel Security

Use proxy tools (GoLogin, IPRoyal) to access Google/Microsoft admin panels from a consistent IP address. Mixed global IPs from offshore team members accessing the same panel trigger security flags and potential account suspension. [S]


## Copy as Deliverability Constraint

These are not style preferences — they are deliverability rules that directly affect inbox placement: [S→V]

- **No open tracking.** Tracking pixels are unreliable and actively hurt deliverability.
- **No links in first email.** Links trigger spam filters. Even in replies, a Calendly link triggers filtering on subsequent sends from that inbox.
- **No HTML formatting.** Plain text only.
- **No images, PDFs, or attachments.** These are spam signals.
- **No Calendly links.** Not even in follow-up replies.
- **Company names must be clean.** "Leadbird LLC" instead of "Leadbird" signals automated spray-and-pray.
- **No emojis or symbols in name fields.** Scraped LinkedIn display names often contain these — must be cleaned.
- **Email length matters.** Microsoft fingerprints email length. Shorter is safer.

Spintax is the deliverability cheat code — generates thousands of unique email variants preventing algorithmic fingerprinting. Word-level spintax is dying; sentence-structure-level spintax is required as Google/Microsoft detection improves. [V]


## Global Block List

Build a permanent list across all clients of people who mark cold emails as spam or threaten legal action. Never contact them again. Share across client campaigns. Over time this database protects the spam complaint rate and infrastructure health for the entire operation. [V]


## Prohibited Client Actions

Five things Leadbird prohibits clients from doing: [V]

1. Adding links or attachments (deliverability damage)
2. Tracking opens (deliverability damage)
3. Adding single individual accounts to a list (operational complexity that breaks campaign hygiene)
4. Sending without warm-up
5. Using non-approved infrastructure


## Tool-Specific Notes

| Tool | Role | Constraint |
|------|------|-----------|
| Smartlead | Sequencer + warm-up | Use their warm-up pool; API randomizes timing |
| Hypertide | Infrastructure provider | Layover + relay; $35K+/mo at scale |
| SmartSenders | Inbox provisioning | Budget option; combined with Smartlead |
| MillionVerifier | SMTP verification | Bulk purchase for 83.7% discount |
| Scrubby | Catch-all verification | Only reliable method; 48-72hr delay |
| ZeroBounce | Secondary verification | Used in bounce remediation flow |
| Apollo | Data source | Post-2025 API changes, unreliable as sole source |
| Mailreef | SMTP backup | Secondary to Google/Microsoft |
| GoLogin/IPRoyal | Admin panel proxy | Consistent IP for panel access |
| MX Toolbox | DNS verification | Pre-launch DNS check |


## Infrastructure Cost as Competitive Moat

Infrastructure is not a cost center — it is a competitive advantage. The 2024 deliverability crackdown massively increased infrastructure costs, which eliminated cash-poor agencies from the market. Cheap resellers fail during crackdowns. The agencies that survive invest in compliant, diversified, properly managed infrastructure at scale. $35K+/month on infrastructure is a feature, not a bug. [V]

Three forces ending the golden age of cheap lead gen agencies: (1) 2024 deliverability crackdown raised infrastructure costs; (2) 2025 Apollo API patch eliminated cheap data; (3) AI commoditized basic campaign execution, raising the quality bar. The surviving agencies are the ones who invested in infrastructure resilience before it became mandatory. [V]
