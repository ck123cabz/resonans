---
type: corpus
aliases: ["Tools Named — Dan Koe"]
corpus: dan-koe
layer: 2
tags: [machine]
source: analysis/pass-1-extraction.md (q70b roll-up + inline mentions across 24 files)
created: 2026-07-29
file: retrieval-index/tools-named.md
tools: 62 named products, apps and services
date: 2026-07-28
---

# Tools Named — Dan Koe

Every product, app and service named anywhere in the corpus, with what he says about each and
whether he backs it or rejects it.

**This file sits outside the type system on purpose.** The corpus taxonomy has eight tags and none
of them fits a tool name. Pass 1 tagged the q70(b) roll-up `[TAC][D]` for want of anything better
and flagged the problem. Forcing a tag onto a product name would put "Zapier" in the same bucket as
"send 30 DMs a week", so the tools are collected here instead. They are high-value retrieval keys:
a lens asked "what does he use for X" needs an answer, and none of the eight tags would return one.

**62 named things across 13 categories.** q70(b) is the corpus's own roll-up and lists roughly 45.
The rest are named in other files and never made the sweep. See the gap note at the bottom.

The tables below hold 65 rows for 62 products. Three rows are version labels rather than separate
things: Gemini Flash, Gemini 2.5 Pro and unversioned Gemini are one product he uses three ways, and
Claude 4.5 Sonnet is a model tier of Claude rather than a product of its own. Claude Code is counted
separately because he uses it for a different job.

## What he rejects, and why

Five explicit rejections and three partial ones. Each carries his stated reason, because the reason
is what transfers; the product is incidental.

| Tool | What he says | Reason he gives |
|---|---|---|
| **Notion** (as a second brain) | traditional note-taking apps are places where **"ideas go to get lost"** | They lack the streamlined workflow a writer or creator needs to turn ideas into daily content. He notes the apps are useful for their own use cases. **Split verdict: he rejects Notion as a second brain and ships Notion templates as products.** See the note below |
| **Obsidian** | same sentence, same verdict: **"ideas go to get lost"** | Identical reason. Named alongside Notion in q32 and again in the q70 tool sweep, with no separate argument |
| **ChatGPT / OpenAI** | he prefers Claude over it | ChatGPT's **default personality is too restrictive**. This is a preference stated as a rejection, and the alternative is named in the same breath |
| **Whoop** (and sleep trackers generally) | he threw it away | The number overrode the felt state: he would wake feeling perfectly fine, see a **red recovery score**, convince himself to "take it easy today", and then act tired. He reports **over six months without waking up tired** since |
| **YouTube AdSense** (as an income source) | do not rely on it to make a living | Use the platform to drive traffic to your own high-margin digital products instead. He earns about **$10,000 a month** from AdSense and still says this |
| **Claude 4.5 Sonnet** *(partial)* | he dislikes the newer models | When they **refuse to be "harsh"** in their feedback. The rejection is of the behaviour, not the product line: Opus 4.1 is his preferred model |
| **CapCut** *(partial)* | he attacks **"Walmart quality CapCut captions"** | The target is generic templated content, not the editor. The tool is named as shorthand for the aesthetic |
| **Facebook ads / paid ads for followers** *(a channel, not a tool)* | relying on paid ads for followers is **"the worst thing you can do"** | It attracts bottom-feeders and ruins audience loyalty. **He ran them anyway at the start**: "I tried it at the beginning and it works because my content was good", and q65 records $100 spent to make $2,500. He also lost $3,000 of his dad's money running ads with no audience, which is the origin of the whole audience-before-product model |

**The Notion split is worth stating plainly.** He rejects it as a second brain in q32 and sells
Notion assets in five other files: a "Focus Hub" template paired with the evergreen course (q07),
the **Notion Command Center** that is a named component of Digital Economics (q12), Notion templates
as free lead magnets (q09, q16), and implementation tools bundled with products (q10, q66). The
reconciliation he never states: the rejection is of Notion as a place to think, and the sales use is
of Notion as a place to execute a system somebody else designed.

### Two rejections that are NOT in this corpus

**RescueTime and Screen Time appear nowhere in the Dan Koe corpus.** A full-text search of all 70
q-files and the Pass 1 extraction returns zero hits for either, in any spelling. Whatever the source
of that expectation, it is not this ingestion. The only tracker he rejects is the Whoop, and the
only screen-time position anywhere in the corpus is his account of 8-to-12-hour video game days as
biography rather than as a tool critique.

If a lens is asked about his position on time-tracking software, the honest answer is that the
corpus does not record one, and the Whoop reasoning is the nearest transferable argument: a metric
that overrides the felt state is worse than no metric.

## Spelling variants unified

Three products appear under two spellings each. The corpus is transcript-derived and the variants
are almost certainly ASR artifacts rather than real name changes.

| Variants in the corpus | One product | Where each spelling appears | Which to use |
|---|---|---|---|
| **Kortex** / **Cortex** | his second-brain software | Kortex: q32, q33, q34, q35, q65, q69. Cortex: q31, q66, q70, and "Cortex University" in q66 | **Kortex.** Record "Cortex" as a variant, never as an alias. Note that "Cortex University" is a product name and is only ever spelled with a C |
| **Twemax** / **Twemx** | a tweet-analysis tool | Twemax: q17, q31, q34. Twemx: q70 only | **Twemax**, on the 3-to-1 count. Pass 1 flags that no such product is publicly known and asks for verification before either spelling reaches a retrieval surface |
| **"Manis"** | almost certainly **Manus**, the agent platform | q70 only, one mention, for web scraping | Carry as "Manis (almost certainly Manus)". One mention is thin evidence and the correction is an inference, not a corpus statement |

A fourth name is misspelled but is a person rather than a tool, and is corrected in
`frameworks-index.md`: Susanne Cook-Greuter appears as "Suzanne", and Alex Soojung-Kim Pang as
"Alex Sujong Kim Pang".

---

## His own products and software

| Tool | What he uses it for, or says about it | Verdict | Source |
|---|---|---|---|
| **Kortex** (spelled Cortex in q31, q66) | His second-brain and knowledge workspace, built because Notion and Obsidian failed writers. Named mechanics: contextual capture with `@document`, the split-screen pane system, Elements (atomic notes from a highlighted paragraph), the Idea Museum with Readwise sync, and a "neural search" pane that listens to what you are writing and surfaces related notes | Endorses, and **disowns the original build**: he calls it **"a $3 million mistake"** — they moved too slowly, built their own auth and sync engines, and never shipped mobile for a note-taking tool | q31, q32, q33, q34, q35, q65, q66, q69 |
| **Eden** | The rebuild. An intelligent drive and canvas workspace: paste a YouTube video or Instagram Reel and it downloads, transcribes and analyses it frame by frame, drop PDFs onto a visual canvas, and AI agents reference all of it at once. Rebuilt from scratch **in three weeks** during a trip to Japan. Base features free, paid tiers for unlimited AI, 50% off the first month | Endorses | q33, q66, q69, q70 |
| **Kai** | The AI inside Kortex/Eden. Used as orchestrator and thought partner, never as a writer: deconstructing top-performing tweets, and acting as a "Clarity Coach" or "Strategic Advisor" that questions his blind spots | Endorses | q32, q33, q67 |
| **The Power Planner / Fosi Planner** | Free digital lead magnet mapping visions, anti-visions, long-term goals and daily priority tasks. Later produced as a physical notebook inside the Art of Focus Keepsake box. **Over 70,000 downloads** | Endorses | q09, q16, q65, q66, q70 |
| **7 Days to Genius Ideas** | A free 7-day creative challenge teaching his note-taking and ideation system. **Over 70,000 people** have taken it. Its system became CorNotes, which became the foundation of Kortex | Endorses, then **retires it** and replaces it with a free second-brain course inside the community | q09, q16, q34, q65, q66 |

## Note-taking and workspace

| Tool | What he uses it for, or says about it | Verdict | Source |
|---|---|---|---|
| **Notion** | Rejected as a second brain: **"ideas go to get lost"**. Simultaneously sold as templates: the "Focus Hub", the Notion Command Center in Digital Economics, free lead magnets, and implementation tools bundled with courses | **Split.** Rejects as a thinking tool, ships as a product | q07, q09, q10, q12, q16, q32, q66, q69, q70 |
| **Obsidian** | Rejected on the same sentence as Notion, same reason, no separate argument | **Rejects** | q32, q70 |
| **Apple Notes** | Named as a capture destination alongside Kortex, for logging quotes and thoughts on the spot | Endorses | q31, q35, q70 |
| **Evernote** | Named in the tool sweep with no comment | Named only | q70 |
| **Roam Research** | Named in the tool sweep with no comment | Named only | q70 |
| **Google Docs** | Named in the tool sweep with no comment. Elsewhere he prescribes brain-dumping what you know into "a document or notes app" before starting a project | Named only | q70 |

## AI and coding

| Tool | What he uses it for, or says about it | Verdict | Source |
|---|---|---|---|
| **Claude** | His preferred LLM for building complex prompts and workflows. **Specifically Opus 4.1** | Endorses | q33, q35, q70 |
| **Claude 4.5 Sonnet** | Named as a newer model he dislikes when it refuses to be **"harsh"** in feedback | **Partial rejection** | q33 |
| **Claude Code** | Used for programming terminal applications | Endorses | q33, q70 |
| **ChatGPT / OpenAI** | Rejected in favour of Claude: its **default personality is too restrictive** | **Rejects** | q33, q70 |
| **Gemini Flash** | His reading companion for books and PDFs, because it processes large amounts of information incredibly fast | Endorses | q33 |
| **Gemini 2.5 Pro** | Used to research and digest dense books, specifically *Breakthrough Advertising*, which then became the source for his landing-page copywriting prompt | Endorses | q33 |
| **Gemini** (unversioned) | Named generally as a reading companion, and in the tool sweep | Endorses | q35, q70 |
| **Grok** | Named in the tool sweep with no comment | Named only | q70 |
| **Perplexity** | Named in the tool sweep with no comment. (Note for grep: "Perplexity" is also the name of phase 1 of his Cycles of Progress framework, which is unrelated to the tool) | Named only | q70 |
| **Cursor** | Recommended for "vibe coding" to turn digital products into interactive Micro-SaaS AI apps | Endorses | q33, q70 |
| **Replit** | Same use as Cursor, named alongside it | Endorses | q33, q70 |
| **Lovable.com** | Guides beginners through creating apps without coding from scratch. **Missing from the q70 sweep** | Endorses | q33 |
| **Bolt** | Named alongside Lovable.com for the same purpose. **Missing from the q70 sweep** | Endorses | q33 |

His standing rules for the whole category: act as a **director rather than a doer**; never outsource
your thinking, your creativity or the writing of your core ideas; never treat a model like a **"slot
machine"** by typing "write a viral tweet" and accepting what comes back. His stated philosophy for
the tooling: **"Automate yourself out of work by documenting your processes as prompts."** His
argument for why the human stays: AI lacks perspective, energy signature, sensemaking, trajectory
and evolving taste. The prompts themselves are in `templates-index.md`, T73–T84.

He names Claude by model tier and mentions Claude Code. **That is the only dating signal in 54,650
words**, and it places some sources in 2025 or later.

## Audience and content

| Tool | What he uses it for, or says about it | Verdict | Source |
|---|---|---|---|
| **Tweet Hunter** | Study the top-performing tweets of accounts you admire, deconstruct their structure, and find their "anomalies" — posts that did **2x** their normal engagement. The Training Wheels method runs on this | Endorses | q13, q17, q31, q34, q70 |
| **Twemax** (spelled Twemx in q70) | Named interchangeably with Tweet Hunter for the same job, every time it appears | Endorses, **pending verification of the name** | q17, q31, q34, q70 |
| **Hypefury** | Named in the tool sweep with no comment | Named only | q70 |
| **Substack** | His newsletter platform. He runs a **paid tier at $10 a month** carrying writing strategies, AI prompts and marketing lessons plus full access to the One-Person Business Launchpad, and gives away *Purpose and Profit* free there | Endorses | q17, q66, q70 |
| **Discord** | Hosts **Modern Mastery**, his private community: $5 for the first month, then $27 a month, with a library of **180+** strategies | Endorses | q66 |
| **Zoom** | Step 5 of Non-Needy Networking: "jump on Zoom just to talk shop and deepen the friendship". Also the mechanism behind the podcast-guest play, which he calls the ultimate **"trojan horse"** for getting a larger creator into a conversation | Endorses | q13, q17 |

## Email

| Tool | What he uses it for, or says about it | Verdict | Source |
|---|---|---|---|
| **Beehiiv** | Named in the tool sweep with no comment | Named only | q70 |
| **ConvertKit** | Named in the tool sweep with no comment | Named only | q70 |

He does not name an email tool anywhere he teaches the newsletter, which is the corpus's largest
tooling gap: the newsletter is called the only audience you own, and no platform recommendation is
attached to it beyond Substack.

## Commerce

| Tool | What he uses it for, or says about it | Verdict | Source |
|---|---|---|---|
| **Stan Store** | Build a simple landing page for pre-orders: problem, outcome, features, release date 3 to 4 weeks out. His stated reason it matters: you do not need a website, and once the first pre-order lands you have a deadline you cannot back out of | Endorses | q08, q70 |
| **Stripe** | Named in the tool sweep with no comment | Named only | q70 |

## Storage

| Tool | What he uses it for, or says about it | Verdict | Source |
|---|---|---|---|
| **Google Drive** | Named in the tool sweep with no comment | Named only | q70 |
| **Dropbox** | Named in the tool sweep with no comment | Named only | q70 |

## Video and design

| Tool | What he uses it for, or says about it | Verdict | Source |
|---|---|---|---|
| **Adobe Photoshop** | Biography: he spent **6 to 8 hours a day** in it making surreal composites for the digital art Instagram that failed. Also his standing example for "learn techniques, not skills": you do not learn "Photoshop", you learn how to mask an object | Endorses as a learning case | q42, q46, q64, q70 |
| **Adobe Premiere Pro** | Named in the tool sweep with no comment | Named only | q70 |
| **Adobe After Effects** | Named in the tool sweep with no comment | Named only | q70 |
| **Frame.io** | Named in the tool sweep with no comment | Named only | q70 |
| **Canva** | Paste a tweet screenshot into a **4x5 image template** for Instagram; also named in the sweep | Endorses | q17, q33, q66, q70 |
| **CapCut** | Named only inside the criticism of **"Walmart quality CapCut captions"** | **Partial rejection** of the generic use, not the editor | q69, q70 |
| **Figma** | The alternative to Canva for the same 4x5 template. **Missing from the q70 sweep** | Endorses | q17 |

## Support and forms

| Tool | What he uses it for, or says about it | Verdict | Source |
|---|---|---|---|
| **Intercom**, specifically **"Finn"**, its AI agent | Named in the tool sweep. The AI agent is named separately, which makes it the only support product he names to the feature level | Named only | q70 |
| **Typeform** | Named in the tool sweep with no comment | Named only | q70 |
| **Jotform** | Named in the tool sweep with no comment | Named only | q70 |
| **Google Forms** | The simple intake questionnaire for a first coaching offer. His argument: you need no website and no landing page, only a social profile as a storefront and a form | Endorses | q03, q70 |

## Reading and research

| Tool | What he uses it for, or says about it | Verdict | Source |
|---|---|---|---|
| **Readwise** and **Readwise Reader** | Kortex integrates with it to sync Kindle highlights into the Idea Museum | Endorses | q32, q70 |
| **Z-Library** (and its Telegram bot) | Named in the tool sweep with no comment | Named only | q70 |
| **Hemingway App** | Named in the tool sweep with no comment. Adjacent to his stated 5th-grade reading level rule, though he never connects the two | Named only | q70 |
| **Farnam Street** | His named example of a curated intellectual blog, for step 2 of building an Idea Museum: sift old little-known books, curated blogs, or **5** highly curated social accounts, rather than the algorithmic feed | Endorses | q34 |
| **Udemy** | Two uses: market research for "sell what's already selling", and self-education. He learned a full college coding curriculum in **three weeks** from YouTube and Udemy, then dropped out | Endorses | q08, q63 |
| **Skillshare** | Market research: search your topic there and deconstruct what already sells | Endorses | q08 |
| **Reddit** | Market research, named alongside Udemy, Skillshare and YouTube | Endorses | q08 |

## Automation

| Tool | What he uses it for, or says about it | Verdict | Source |
|---|---|---|---|
| **Zapier** | Named in the tool sweep with no comment | Named only | q70 |
| **"Manis"** (almost certainly **Manus**) | Named for web scraping. One mention, one file | Named only, **pending verification** | q70 |

## Health, body and leisure

| Tool | What he uses it for, or says about it | Verdict | Source |
|---|---|---|---|
| **Whoop** | The sleep and recovery tracker he threw away, because a red recovery score would override how he actually felt and he would then act tired. **Over six months without waking up tired** since | **Rejects** | q41 |
| **Netflix** | "Normie nights", 7:00 pm to 9:00 pm: he watches *Lost* with his girlfriend and intentionally unplugs from self-improvement | Endorses as leisure | q40 |

The Whoop rejection is the corpus's clearest tracking argument and it is never applied consistently.
The same corpus tracks 10,000 to 15,000 steps, 4,000 to 4,500 calories, 220 grams of protein,
45-minute timers, 45-to-90-minute blocks and four priority rungs. The stated reason the tracker was
bad, that the metric overrode the felt state, applies unchanged to a step target. Pass 2 records
this as an unexamined asymmetry: anti-optimisation on the body, maximal on the mind.

## Games

Named as biography, not as tools. He was **heavily addicted, 8 to 12 hours a day, "to the point of
ruining his life"**, and the addiction is the grounding for his attention-economy critique and for
the Life-is-a-Video-Game framing he builds on Donald Hoffman.

| Game | What the corpus says | Source |
|---|---|---|
| **Halo 3** | Woke at **3:00 am** before school to hold his rank. Also unhooked a TV and played survival mode in the middle seat of his dad's truck on a family road trip to California | q63, q70 |
| **Call of Duty: Modern Warfare 2** | Home sick with pneumonia for a week, drank Dr. Pepper and played until he hit **10th prestige** | q63, q70 |
| **League of Legends** | "Countless hours" | q63, q70 |
| **Teamfight Tactics** | Named alongside League of Legends | q63 |
| **World of Warcraft** | Named in the addiction list | q63, q70 |
| **Flappy Bird** | Named in the tool sweep | q70 |
| **Temple Run** | Named in the tool sweep | q70 |

## Platforms, for grep

Distribution surfaces rather than tools, and their rules live in
`audience-and-distribution.md`. Listed once here so a tool search does not miss them:
**X (Twitter)** · **LinkedIn** · **Instagram** · **YouTube** · **TikTok** · **Threads** ·
**Facebook** · **Substack** (also a tool, above) · **Discord** (also a tool, above) · podcasts as a
category with no named host.

His per-platform verdicts in one line each: X is the testing ground and the foundation, because the
retweet button makes sharing low-friction. LinkedIn is lucrative and troll-free because users fear
losing their jobs. Instagram is top-of-funnel and should be fed repurposed text, never created
natively. YouTube is deep authority and too slow for beginners. TikTok, Reels and Shorts hold 10 to
30 seconds and are "shallow" and "entropic", useful only to capture and funnel. Podcasts are
notoriously hard to grow because their native search engines are "absolute trash", so start one as
an audio repository and a networking instrument rather than to get famous.

---

## Count, and what the corpus's own sweep missed

**62 named products, apps and services**, against roughly 45 in q70(b), the corpus's own tool
roll-up. Fifteen are named elsewhere and never made the sweep, and one category in the sweep is
under-specified.

| Missing from q70(b) | Where it is named | Why it matters |
|---|---|---|
| **Lovable.com** | q33 | A named no-code recommendation, absent from the AI category |
| **Bolt** | q33 | Same |
| **Figma** | q17 | The 4x5 Instagram template alternative to Canva |
| **Zoom** | q13, q17 | Carries two named tactics: the networking call and the podcast trojan horse |
| **Discord** | q66 | Hosts his own paid community |
| **Udemy** | q08, q63 | Appears twice, for market research and for the dropout story |
| **Skillshare** | q08 | Market research |
| **Reddit** | q08 | Market research |
| **Farnam Street** | q34 | The one named example of a high-idea-density source |
| **Whoop** | q41 | The corpus's clearest tracking rejection |
| **Netflix** | q40 | Names the show, *Lost*, and the ritual around it |
| **Teamfight Tactics** | q63 | Games list incomplete in q70 |
| **Kai** | q32, q33 | The AI inside his own software, named to feature level |
| **The Power Planner / Fosi Planner** | q09, q16, q65, q66 | Listed in q70 under "his own" but with no download figure or product history |
| **7 Days to Genius Ideas** | q09, q16, q34, q65, q66 | Absent from q70's "his own" row entirely, despite 70,000+ takers |

The pattern is consistent with the rest of this corpus. q70 is a sweep file answering "name every
tool", and like q67 and q68 it undercounts its own corpus by roughly a quarter. **Silence in the
sweep is not evidence a tool is unnamed**, which is the same working rule Pass 2 applies to the
citation map.

## Verification queue

Three items should be checked before any of them reaches a user-facing surface.

1. **Twemax / Twemx.** Pass 1 notes no such product is publicly known. Four mentions across three
   files, one of them a different spelling. Either the name is mis-transcribed from something else
   or the product is obscure. Do not recommend it until this resolves.
2. **"Manis" for web scraping.** Almost certainly Manus. One mention, one file, and the correction
   is an inference rather than anything the corpus states.
3. **Kortex versus Cortex.** Kortex is correct on the count and on q65/q69, which are the business
   files. "Cortex University" is a product name and may genuinely carry the C. Search any newly
   added source for both spellings.

Two structural gaps worth a re-query, both of them absences rather than errors:

- **No email platform is recommended where the newsletter is taught.** Beehiiv and ConvertKit are
  named once each in a list and never again, and the newsletter is the asset he calls the only one
  you own.
- **Twenty-two of the 62 carry a name and nothing else**, most of them from the q70 sweep: Evernote,
  Roam Research, Google Docs, Grok, Perplexity, Hypefury, Beehiiv, ConvertKit, Stripe, Google Drive,
  Dropbox, Adobe Premiere Pro, Adobe After Effects, Frame.io, Intercom (with Finn), Typeform,
  Jotform, Z-Library, Hemingway App, Zapier, "Manis", plus the two games named only in the sweep
  (Flappy Bird, Temple Run). A lens should say he mentions these rather than that he uses them, and
  should never present one as a recommendation.
