---
type: corpus
aliases: ["Gap register: Jason Murray corpus (Layer 3)"]
corpus: jason-murray
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-10-03
---

# Gap register: Jason Murray corpus (Layer 3)

Written 2026-10-03. Every row is an `[A]` gap: something the corpus does not hold, or holds on one source only. Paths are relative to `knowledge/corpus/jason-murray/` unless they start with `skills/`.

"Lens" means the art direction lens at `skills/lens/lenses/jason-murray.md`. "Map" means the taxonomy map that reads `analysis/ingredient-map.json`.

Priority: High blocks a correct answer or a correct map node. Medium weakens one. Low is background.

## 1. Consumer wiring

| Gap | Why it matters for the lens and the map | What would resolve it | Source to try | Priority |
|---|---|---|---|---|
| Both consumers exist as of 2026-10-03: the lens at `skills/lens/lenses/jason-murray.md` (registered in `skills/lens/SKILL.md`, modes ask, classify, challenge, select) and the map at https://claude.ai/artifact/RECWGtHeMsDD2Ash5KCLQA, which reads `analysis/ingredient-map.json`. No `/lens jason-murray` answer has been run against the corpus yet, and the published page has not been opened and checked by Christian. | A lens nobody has run and a page nobody has opened are unproven. | One `/lens jason-murray classify` run on a real ad, and Christian opening the map once. Then update this row with the date. | `skills/lens/lenses/jason-murray.md`; `analysis/map/art-direction-map.html` | Medium |

## 2. His taxonomy tool and techniques

| Gap | Why it matters for the lens and the map | What would resolve it | Source to try | Priority |
|---|---|---|---|---|
| 11 of Iris's 39 technique names are unread. 6 more were read at low confidence from letters about 4 pixels tall. | The map cannot show his full taxonomy. The lens cannot say whether a technique is one of his 39. | A higher-resolution frame, or the tool itself. | Re-pull Short `2BYgOxYTE-0` at 1080p or higher and re-read the lower row; the October 2026 bootcamp, whose students get Iris first; his newsletter after 2026-10-02 | High |
| No per-technique example list. The tool shows counts ("Visual quotation · 15 examples") and a few hundred images, and none of the pairings are captured. | The map's promise is taxonomy with examples. Today only about ten techniques have even one example he named. | The tool's data, or a frame-by-frame read of each technique selected on screen. | Iris once public; future Shorts in the "Art Direction Techniques" series; MAD newsletter issues | High |
| The four Iris groups (Differentiate, Group, Sequence, Predict) have no published legend. The meaning given in Pass 2 is `[I]`. | The map's top-level grouping would rest on an inference. | His own description of the four filters. | The "About" link in the Iris top bar; bootcamp material; ask him | High |
| Visual literalism, figure-ground reversal and genre quotation are taught by name and are not among the 28 names read off Iris. | The lens may treat them as Iris nodes when they are named differently there. | Reading the 11 unread nodes. | Same as the first row | Medium |
| Visual rhyme, face schema, semantic compounding, body vector and most other read nodes have a name and no definition. | The lens can name them and cannot explain them in his words. | A definition and one example per node. | Iris; later newsletters | Medium |
| His 39 techniques and 61 menu lines are not mapped against Eyecandy's 136 technique categories in `.raw/mentioned/tools/eyecandy/`. | The map could borrow examples from a tool he recommends, and no crosswalk exists. | A crosswalk table, marked `[I]`. | `.raw/mentioned/tools/eyecandy/techniques.json`; `.raw/frames/art-direction-menu.md` | Medium |
| No ad in the Techniques video shows a Composition & Framing line, the longest menu heading. Motion & Editing, Constraints and Perspective & Intent have no named example either. | Four of eleven map headings would show lines with no example under them. | His examples for those lines, or examples tagged `[I]` from the campaign layer. | Bootcamp week 3 or 4; `.raw/mentioned/campaigns/_index.tsv`, column `dominant_ingredients` | Medium |

## 3. Paid and unscraped teaching material

| Gap | Why it matters for the lens and the map | What would resolve it | Source to try | Priority |
|---|---|---|---|---|
| Bootcamp and course lesson bodies are behind a login. The corpus has lesson titles and the four published week titles only. NEXT Art Director: $599 course, $1,199 bootcamp. | The lens reasons from public summaries of frameworks he teaches in full elsewhere. The first 20 minutes of class one, by his account, is the definition slide alone. | Buying the course and transcribing the lessons. | Teachable, NEXT Art Director; `.raw/products/teachable-next-art-director-the-course.md` for the lesson list | High |
| The Art Director Roadmap FigJam board is not scraped. It is free on Gumroad. Everything in the corpus about it is read off video frames while he screen-shares. | The Idea Sizing Chart, the Examples panel, the insight and platform notes and the project table all live on this board. Frames show parts of it at 720p, and the Advertising column of one slide is hidden by his webcam. | Opening the board and exporting its text. | Gumroad product "How to become an Art Director: The Roadmap" (`.raw/products/gumroad-agitc.md`); board URL figma.com/board/TDrBogrS8XreRY3QgGSGES | High |
| MAD Decks Vol 001 ($57) contents are not in the corpus: four deck templates and a mini course with two bootcamp lessons on insights and big ideas. | It is his closest answer to "how do you brief a photographer or a vendor". | Buying it. | `.raw/products/teachable-mad-decks-001.md` | Medium |
| Cut30's curriculum is absent. | He credits the course with changing his content. The lens cannot separate what he took from it. | The course outline. | cut30.com; `.raw/mentioned/people/cut-30-founders.md` | Low |
| Jason Bagley's Creative Megamachine lessons are paid. The "polarising portfolio" line and the "edge of madness" lesson are known by title and by Jason's retelling. | Two borrowed rules cannot be quoted in the owner's words. | The lessons. | theasap.com/creative-megamachine | Low |
| Luke Sullivan's platform tests are quoted from Jason's board note. The book text was not checked, and "Truth + Conflict = Platform" comes from a third-party summary. | The lens credits Sullivan for wording nobody has verified in the book. | Chapter 7 of Hey Whipple, Squeeze This, 6th edition. | The book | Medium |

## 4. Channels not scraped

| Gap | Why it matters for the lens and the map | What would resolve it | Source to try | Priority |
|---|---|---|---|---|
| Instagram and TikTok reels are not scraped. His About page links instagram.com/jason_swet as his content home. | Reels are where he posts first. Shorts carry some of them and the overlap is unknown. Series such as "Tools for LAZY Creatives" (5.8M views on one cover) are known from a frame only. | A reel scrape with captions and on-screen text. | Instagram @jason_swet; TikTok; an Instagram reel scraper | High |
| 48 of the 175 Shorts in `.raw/youtube-index.tsv` have no file in `.raw/shorts/` (127 present). The run brief counts 7 as failed downloads. From the files I could not tell which 7 failed and which 41 were skipped. Missing art direction titles from 2026: "Underrated Advice for Art Directors" (2026-04-06), "The Art Director VS The Result" (2026-06-30), "These images were completely captured in-camera?" (2026-08-20). | Three recent art direction Shorts may hold technique names or examples. | Re-running the caption pull for the missing ids. | `.raw/youtube-index.tsv`; ids `7LKLbSEuTKs`, `UhISkP3hEkE`, `u366uQNEPNg` | Medium |
| Theory of Taste coverage is uneven. The long video covers episodes 1 to 3. Episodes 4 (five taste types) and 5 (vision) exist only as Shorts and LinkedIn posts. The Short "The Shortcut to Taste" (2026-05-08) has no episode number. NotebookLM's q14 knows nothing of episodes 4 and 5. | The five taste types rest on one 2026-05-01 Short. The lens has one source for a core framework. | A longer treatment, if he publishes one, and frame notes for the episode 4 and 5 Shorts. | His channel; `.raw/shorts/2026-05-01-you-re-thinking-about-taste-wrong-bKjx0_m3zLM.md` | Medium |
| Three press appearances have show notes and no transcript: Air, "How to Level up Your Art Direction" (2025-04-17, 26 min); The Deeply Graphic Designcast, "Be The Creative Athlete" (2025-12-15, 82 min); Drew English, "The Lazy Creator Method" (2026-01-27, 46 min). | 154 minutes of him answering another host's questions, including one episode on art direction itself. | Pulling captions or transcribing the audio. | YouTube ids `OvH1ZFDIXKY`, `zLuNmtaZXw4`, `YkTDNtgIPN4` | Medium |
| The notebook indexed 72 of 96 YouTube sources. The other 24 are 2009 to 2018 clips with no captions. | Background films only. | Nothing needed for the lens. | None | Low |
| No frame notes exist for most Shorts. `frames/shorts-visual-tools.md` covers a handful. The Britannia out-of-home Short and the October 2025 "$1 vs $1M" Short have speech and no record of what was on screen. | On-screen ads are his examples, and captions do not name them. | Frame pulls for every art direction Short from 2025-10 onward. | `.raw/shorts/` ids; yt-dlp frames | Medium |

## 5. Attribution and speakers

| Gap | Why it matters for the lens and the map | What would resolve it | Source to try | Priority |
|---|---|---|---|---|
| Captions have no speaker labels. Podcast episodes mix Jason with guests, and Pass 1 split speakers by context. Five lines have no settled speaker: "the black hole that is Corporate America"; "every seven years you do take a beat to step off"; "the nicher you go the more you'll grow"; "it looked painterly"; the "Make It Count" line. | A guest's rule could enter the lens as his. q10, q17, q26, q27 and q30 already made that mistake. | Listening to the audio, or diarised transcripts. | Episodes 3 and 4 of The Toolbox Podcast; the Garrett King and Edward Sun episodes | High |
| The ep 3 guest who raises Nike FuelBand and Nike ID is not named in Pass 1. | The example is tagged `[D:guest]` with no name. | Checking the episode title and description. | `.raw/video/becoming-a-freelance-creative-director*.md` | Low |
| Names left unresolved: "Jeff Valet" (likely Jeff Vallee, unproven); Scott's, Brad's and Tyler's surnames; "Ashley", whose channel he links; Gap's "Mark Brightbard" (likely Mark Breitbard, from outside the corpus); the brand behind the chicken rocket ad and the two genre quotation stills; the "tools.app with six Os" site. | The resource and people lists carry names nobody can look up. | The original pages or frames. | The Roadmap board for Ashley's link; the reviewed portfolios' URLs in `frames/art-director-reacts-to-portfolios-live.md` | Low |
| The Hydro Flask spec campaign has two authors on record. Pass 1 names Abe Tullis from the link on his board (abetullis.com/10/). The campaign file found a team entry and Carly Garrett's page, and no single author. | The retrieval index would credit one student for team work. | Opening abetullis.com/10/ and the Young Ones entry and reading the credit lines. | `.raw/mentioned/campaigns/spec-hydro-flask-bottle-scars.md`; abetullis.com/10/ | Medium |

## 6. Facts that rest on one source

| Gap | Why it matters for the lens and the map | What would resolve it | Source to try | Priority |
|---|---|---|---|---|
| Campaign credits for his own work rest on his site alone. No trade article, award entry or Amazon case study names him on Brooks, Kraft Heinz, Kellogg's or vitaminwater. On two credit lines he has no title. Champion was pitch work with no credit. | The lens presents him as an authority. His authority is real as a teacher and unverified as the art director of record on named campaigns. | A credit list naming him, or a colleague's page that does. | The One Club and Clio entries for the Amazon Brand Innovation Lab work; LinkedIn recommendations; Rath Ros's and Cyndi Walker's sites | High |
| His titles differ by source. About page: Associate Creative Director at Amazon and Senior Art Director for the whole Energy BBDO tenure. Speech: "ACD level art director", and a junior start at $55,000. | The lens should state one title per job, with its source. | His LinkedIn experience section. | His LinkedIn profile; `.raw/site/about.md` | Medium |
| Student spec work has no public page. The bootcamp pieces by Connor McLoughlin (Arc'teryx "Playdate") and Jaya Schreihart (EF Tours "Later Is Now") exist in the corpus as slides in his video. | These are his two fullest worked examples of insight, idea and ingredients. The map can show only cropped frames. | Portfolio URLs for both students. | Their names on LinkedIn; the bootcamp product page (`.raw/products/mad-next-art-director.md`) | Medium |
| "Venmo the Homeless", his own student stunt, has no outside record. His figures differ by telling: "$6,000" and "$5,000 $6,000", "30 50 people". The year is not given. | It is his one example of a spec idea done for real. | The Facebook video or a local news item. | Food and Care Coalition, Provo; BYU AdLab pages | Low |
| Campaigns he teaches with that have no record file: Spotify Wrapped, the Time red border ads, Google "Year in Search", LA28 "Super Bloom", Roland-Garros, Gap × Young Miko, OMODA 7 by Uncommon, the Britannia out-of-home work, the Nike federation kit shoots (Nike x Patta, Nocta x Nike), and the Heinz, Tinder, Midori and Sudafed ads on screen in Shorts. | The map would show his point with no year, agency or image for these. Spotify Wrapped is one of four examples on his board. | One record file each, in the format of the 44 that exist. | Ads of the World; The One Club; the makers' sites | Medium |
| LEGO "Imagine" has no settled year (2006 or 2007) and no agency or award-show page. WMF has one verified food execution, the carrot. | Two of his five right-side examples carry a weak record. | Lürzer's Archive entries. | luerzersarchive.com | Low |
| Claims of his with no source: Aristotle ranking taste near the bottom of the senses; David Hockney having died (LinkedIn, August 2026); the 1930s origin of macro texture as landscape. | The lens could repeat a factual error as his teaching. | Checking each against a reference. | A reference source for each | Low |
| Smith & Diction's tool being "trained on licensed data" is not confirmed. | Edward Sun's test for accepted AI work rests on it. | Visual Electric's own statement. | visualelectric.com | Low |

## 7. Topics he does not cover

| Gap | Why it matters for the lens and the map | What would resolve it | Source to try | Priority |
|---|---|---|---|---|
| He never defines "key visual" or "visual lineage" in one sentence. Both are defined by example. | The lens has to give a definition and mark it as assembled. | A sentence from him. | Bootcamp material; future newsletters | Medium |
| No rule for choosing photography, illustration or CG. No method for briefing a photographer. No rule on legibility or type over images beyond one portfolio-site preference. | NotebookLM invented all three. The lens should say he has not taught them. | Nothing, unless he publishes one. MAD Decks may hold the briefing method. | `.raw/products/teachable-mad-decks-001.md` | Medium |
| Nothing on interviews, soft skills or day rates. | Career questions on these have no answer in his words. | Nothing in the corpus. | The three untranscribed press episodes | Low |
| He does not reconcile visual literalism (2026-03-06) with "avoiding literal interpretations" (2026-04-08). | The lens will be asked which to use. His only guidance is the 2026-09-30 Short, which gives each technique a problem it fixes. | A statement from him on when each applies. | Later Shorts in the techniques series | Medium |
| A mood board image count, and a client board against a production-partner board. | Common questions with no answer of his. | Nothing found. | The mood board video's frame notes | Low |

## 8. Pass 1 items never checked

| Gap | Why it matters for the lens and the map | What would resolve it | Source to try | Priority |
|---|---|---|---|---|
| Lanes 1 and 2 left the AI video's conclusion unread, and lanes 3 and 4 did not read it at all. Lanes 5 to 7 quote it. | The 2022 position is the baseline for how his view of AI moved. | One full read of the transcript. | `.raw/video/ai-will-steal-my-job-as-an-art-director.md` | Medium |
| The two liquid logo tutorials, the Procreate Dreams verdict, the M1 iPad Pro and Crane-M reviews were not checked. | Background by the profile. | A read only if the motion lane is ever promoted. | `.raw/video/` Procreate files | Low |
| Four items in the older films (ESPLANADE, Assisted Mobility's narrator and diagnosis, the Māori film, the High Line foreground objects). | Background. | None needed. | `.raw/video/` | Low |
| The Photoshop recolour steps are `[D]` in lanes 3 and 4 and `[M]` in lanes 1 and 2. Pass 2 takes the lanes 3 and 4 reading; nobody compared the two step lists line by line. | A how-to the lens may quote. | One comparison. | `.raw/video/how-to-art-direct-your-mood-board-in-photoshop.md` | Low |
| Pass 1 dates the Techniques video to 2025. The index says 2026-09-15. Any Layer 1 line that says "2025" for the pyramid or the menu repeats the slip. | Wrong order in the "how his thinking moved" account. | A grep of Layers 1 and 2 for "2025" beside those two frameworks. | `.raw/youtube-index.tsv` | Medium |

## Count

42 gaps: 9 High, 19 Medium, 14 Low.
