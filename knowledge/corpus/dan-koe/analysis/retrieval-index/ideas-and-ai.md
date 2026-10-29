---
type: corpus
aliases: ["Dan Koe Retrieval Index — Ideas and AI"]
corpus: dan-koe
layer: 2
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-29
file: ideas-and-ai
sources: q31–q35
built: 2026-07-28
---

# Dan Koe Retrieval Index — Ideas and AI

Layer 2 retrieval index. One item per `##` heading, each section self-contained: the method, its
numbers and its verbatim text all sit inside the same section. Context is repeated rather than
cross-referenced, so a single grep returns something usable.

**The verbatim rule.** Every line inside a `>` blockquote is reproduced exactly as the corpus
renders it, transcription errors included. The AI prompts in particular carry voice-transcript
artifacts ("direct challeng", "500 to 10,000word", "rank by project rank by projected engagement",
"review at my life plan"). A cleaned prompt is no longer the artifact, so none of them are cleaned.

**Two prompts here are not his.** The pair marked "Sourced from Signal's Post" in q33 are attributed
in their own headings. They must never enter a Koe prompt library unattributed. The corpus does not
say who or what "Signal" is.

**Provenance key.** `[D]` his own, with no source underneath · `[D+M:name]` his name over someone
else's architecture · `[M:name]` a straight relay under someone else's name · `[G]` backed by his
own reported outcome · `[I]` inferred · `[A]` a flagged gap.

**Source files.** q31–q35 in `knowledge/corpus/dan-koe/notebooklm/`.

---

## The idea generation system — the whole loop

Source q31, the framework file for this lane.

**The premise** `[PRN][D]` Creators are "idea junkies" or "mental blacksmiths" who mine reality for
raw material and forge it into valuable insight. The system is not waiting for random inspiration.
It runs on intentional consumption, systematic capture, and framework-driven development.

**The three inputs he names** `[TAC][D]`

1. **Cross-domain study.** Actively hunt ideas by consuming books, podcasts and long-form lectures
   across multiple disciplines (philosophy, psychology, business) to find intersecting patterns.
2. **Studying high-performing content.** Use Twemax or Tweet Hunter to study the most popular tweets
   of favourite creators, and filter YouTube channels by "most popular" to see which concepts the
   market has already validated.
3. **Personal problem solving.** Draw heavily on problems he has faced and solved, turning his own
   evolutionary journey into public content.

**The capture rule** `[WRN][D]` You cannot rely on memory. Without a dedicated capture system, ideas
vanish.

**Capture tooling** `[TAC][D]` Primarily his own software, plus **Apple Notes**. The corpus spells
his software two ways: q31 says "Cortex", q32 and q34 say "Kortex". **Kortex is correct** and q31's
is a transcription slip that should not become an alias.

**Capturing in motion** `[TAC][D]` Regular **30 to 45-minute** walks treated as "creativity blocks",
with an audiobook or in silence, phone pulled out only to capture ideas as the mind works through
problems.

**Outlines as idea magnets** `[TAC][D]` Instead of staring at a blank page, create the newsletter
outline early in the week. The outline acts as an anchor, so the brain automatically notices
information, conversations and ideas that fill in its blanks.

**The development step** `[FRM][D]` Every captured idea gets expanded through Cor Notes, which has
its own section in this file.

---

## The Dopamine Compass

**Provenance** `[FRM][D]`.

**What it is** The input filter. Pay close attention to what sparks excitement or a dopamine hit in
your own brain, and treat that reaction as the signal for what to capture.

**The test, verbatim** `[TPL][D]`, appearing word-identical in q31 and q34:

> "I wish I wrote that"

When a quote or idea produces that reaction, it will likely resonate with others and becomes
creative firepower.

**Where it sits in the loop** `[PRN][D]` You are not reading to memorise facts. You are hunting for
ideas that spark excitement or a dopamine hit. Only those get captured.

---

## The Idea Museum — the swipe file, and how to stock it

**Provenance** `[FRM][D+M:swipe-file]`. "Idea Museum" is his name for the copywriting tradition's
swipe file. The name is his; the object is not.

**What it is** A centralised note-taking system where quotes, random thoughts and links are logged
instantly so they can be resurfaced later. The fullest treatment is q34; q31, q32 and q35 all use
it.

**The premise** `[TAC][D]` If you are struggling to find good ideas, the answer is to change your
inputs, sourcing from places with high "idea density".

**The three steps** `[TAC][D]`

1. **Stop relying on the algorithmic feed.** Find **3 to 5 sources** of information that
   consistently make you envious of their writing.
2. **Sift through high-density sources.** Old, little-known books; curated intellectual blogs;
   or a highly curated list of **5 social media accounts** that consistently post great thoughts.
   **Farnam Street** `[CIT][D]` is the named example of a curated intellectual blog.
3. **Collect without judgment.** Put the ideas in the museum as future creative firepower rather
   than filtering them at capture time.

**The capture trigger** `[TAC][D]` from q35: when you read a sentence that profoundly impacts you,
stop reading immediately and do not read past it. Sit with the idea, reflect on why it resonated,
and capture it in the Idea Museum.

**Note on the "3 to 5" figure.** The corpus uses "3 to 5" for three different objects: inspiration
sources here, mentors elsewhere, and daily priority tasks in the productivity lane. Pass 2 says
explicitly not to merge them.

---

## Cor Notes — the component list, and the 6-versus-7 conflict

**Provenance** `[FRM][D+M:Zettelkasten]`. Also written "CorNotes" and "core notes", and called
"value notes" in q32. Pass 2 places it against the Zettelkasten and Smart Notes tradition, which
q67 does not cover.

**What it is** `[PRN][D]` The proprietary note system that transforms raw ideas into "mental Legos"
that hold persuasive weight. Once a note is broken into its components it is essentially "done":
writing a YouTube video or a Twitter thread becomes piecing predefined Legos together rather than
facing a blank page.

**The component list disagrees with itself across three files, and both lists are recorded here.**

**The 6-component list** (q31 and q34, word-for-word the same six), given as questions in q34:

1. **Problem.** What is the relatable pain point associated with this idea? How does it negatively
   impact people's lives?
2. **Goal.** What is the desirable end result people want to achieve by overcoming that problem?
3. **Example.** What is a personal story or tangible example that grounds the idea and helps people
   understand it?
4. **Benefit.** What are the benefits of overcoming the problem and achieving the goal?
5. **Process.** What is the step-by-step, actionable advice to get there?
6. **Concept.** Can you slap a unique word or name on this idea to package it into a memorable
   concept?

**The 7-component list** (q32, the fullest treatment): **Topic & Summary** (what the idea is, plus a
brief summary of his understanding) · **Problem** (the relatable pain point) · **Goal/Benefit** (the
positive outcome of overcoming it) · **Objections** (the limiting beliefs people hold about solving
it) · **Example/Story** (personal experience or anecdote that illustrates it) · **Process**
(step-by-step actionable solution) · **Concept** (a catchy unique name).

**The difference between the two lists:** q32 adds *Topic & Summary* and *Objections*, and folds the
separate *Benefit* into *Goal/Benefit*. q32 is the fullest treatment. q34 is the only one that gives
the selection rule.

**The selection rule** `[TAC][D]` from q34: do not use every component on every note. Pick **3 to 4**
of them to expand the thought.

**The three-step process** `[TAC][D]`

1. **Capture the "Golden Nuggets" (the aha moment).** While reading books, listening to podcasts or
   consuming content, take notes on nothing except the ideas, anecdotes or statistics that give a
   spike of dopamine. The test is the things that make you stop and think *"I wish I wrote that"*.
2. **Dissect the idea.** Do not leave it as a quote. Pick 3 to 4 of the building blocks above and
   expand the thought against them.
3. **Synthesise and write.** The dissected pieces are the "mental Legos". String them together to
   outline a comprehensive newsletter or a YouTube script, or extract individual elements to create
   tweets and short-form posts.

---

## The second brain — what he says it is, and what he rejects

Source q32.

**What it is** `[PRN][D]` He approaches note-taking and second-brain systems as "complete knowledge
workspaces" designed exclusively for creative output, and as a "search engine for your memories": a
highly curated space holding only the specific ideas, quotes or frames that caused a dopamine hit of
profound understanding.

**What it is not** `[WRN][D]`

- **Not a place to hoard information.** Against "tutorial hell" and hoarding theory without direct
  experience. If you are not building a project with what you capture, it is "soon to be forgotten
  brain fog".
- **Against Notion and Obsidian as second brains.** He calls them places where "ideas go to get
  lost", useful for their own use cases but lacking the streamlined workflow a writer needs to turn
  ideas into daily content.
- **Against clipping entire articles** and building complex webs of tags for the sake of
  organisation.

**The design goal** `[PRN][D]` A seamless transition from capturing a scattered thought, to
outlining a newsletter, to publishing a post.

**Provenance note** `[CIT][I]` "Second brain" is Tiago Forte's term from *Building a Second Brain*,
used here without attribution. What is his is the reframing to a search engine for memories, Cor
Notes, and the output-driven workflow. This is an inference and is marked as one.

---

## Kortex mechanics — five features, and the method each carries

Source q32. **The implementation named here is his own paid product.** Each feature carries a
transferable method claim, and the method is what a lens should use.

1. **Contextual Capture.** Capture feels like "texting yourself ideas", and a capture can be
   connected directly to a specific document on the go. The syntax, verbatim `[TPL][D]`: type `@`
   followed by the document name, for example `@YouTube video notes` or `@Week 2 December
   Planning`, and the idea is stored exactly where it will be needed in the future writing session.
   **Method: capture at the point of future use.**
2. **The Pane System (split-screen).** Open the idea dump or outline in one pane and the actual
   draft in another, dragging, dropping and referencing side by side instead of keeping 10 browser
   tabs open. **Method: reference while drafting.**
3. **Elements (atomic notes).** Highlight a good paragraph inside a document and turn it into an
   Element, a sub-note that can be independently tagged, searched and linked across the whole second
   brain. **Method: atomic reuse.**
4. **The Idea Museum and Deep Search.** Integrates with **Readwise** to sync Kindle highlights,
   accepts pasted YouTube links, tweets and articles, and automatically downloads, transcribes and
   tags media. The capability example, verbatim `[TPL][D]`: searching "pink sweater" pulls up the
   exact timestamp where someone wore a pink sweater in an uploaded video. **Method: search the
   media, not just the text.**
5. **Neural search.** A pane that automatically listens to what you are writing and continuously
   surfaces related notes, highlights and past ideas from the database to keep creative momentum
   flowing. **Method: ambient resurfacing.**

**AI inside the product** `[TAC][D]` Kai and Eden are used as orchestrator and thought partner
rather than writer: breaking down the psychological structures of top-performing tweets and
reverse-engineering their hooks, and acting as a "Clarity Coach" or "Strategic Advisor" that
questions his blind spots and challenges his thinking.

**Origin** `[BIO][G]` He built Kortex, which has evolved alongside his AI tool **Eden**, because
existing note apps failed writers and creators.

**The tension a lens should carry.** He warns against AI writing your content and sells AI software
in the same breath. The line he draws is director versus doer, and this is the sharpest instance in
the lane of the sell sitting adjacent to the teaching.

---

## Writer's block protocols

Source q31, under his own heading: what he does when he has "Nothing to Write About". He treats a
block as a structural or fatigue issue rather than a lack of creativity.

1. **Start with a pain point.** `[TAC][D]` The easiest and most potent prompt is identifying a
   relatable problem. Ask "What is a problem I've faced?" or write down **5** past problems. The
   kickstart phrases, verbatim `[TPL][D]`:

   > "Most people suck at..."

   > "If you struggle with..."

2. **Use frameworks as "Legos".** `[TAC][D]` Fall back on **PAS (Problem, Amplify, Solution)** or
   his own **APAG** framework to force the ideas into narrative flow. When still stuck mid-piece,
   cycle through the mental Legos, inserting a personal story, a statistic, a metaphor or a quote to
   keep momentum going. (Note: PAS is rendered here as Problem-Amplify-Solution rather than the
   tradition's Problem-Agitate-Solution, the same substitution q20 makes.)
3. **Study structural outliers.** `[TAC][D]` Open the swipe file of high-performing posts from other
   creators, deconstruct the underlying structure (hook, bulleted list, punchline), and plug your own
   five-word ideas into that proven rhythm.
4. **Walk away and rest.** `[TAC][D]` A persistent block is overstimulation. Drop the work entirely
   for active rest, which activates the Default Mode Network protocol below.

---

## Intelligent Imitation and structural deconstruction

**Provenance** `[FRM][D+M:Kleon]`, with Wilson Mizner's aphorism behind it. Neither q67 nor q68
covers the borrowing where the tactic is taught.

**The premise** `[PRN][D]` You do not need to invent completely original concepts. You need to
explore proven ideas through your unique lens.

**The four steps** `[TAC][D]`

1. Choose **5 to 10 creators** whose articulation and ideas you admire.
2. Use **Tweet Hunter**, **Twemax**, or YouTube sorting to find their "anomalies": the posts or
   videos that performed **2x** better than their normal content.
3. Deconstruct *why* the idea worked. What psychological triggers were used? How was the hook
   structured?
4. Use that high-performing structure as "training wheels" and plug your own ideas and niche topics
   into that proven rhythm.

**Where else this appears** The same tactic runs through the corpus four times under different
framings: as the zero-follower growth move (q13), as the Tweet Hunter and Twemax move (q17), as the
same-idea-different-structures hook set (q22), and as an editing pass (q23).

**The contradiction to carry.** Originality is demanded across the philosophy lane while the growth
method here is copying validated structures. Pass 2 lists this as one of five philosophy-versus-
tactic conflicts, all running the same direction.

---

## Writing one idea 1,000 ways

**Provenance** `[PRN][D]`.

**The claim** Idea generation is often just taking your best concepts and changing their
architectural presentation. Originality is not inventing new things; it is exploring existing ideas
from fresh angles. Changing the structural format alone multiplies idea output infinitely.

**The worked example, verbatim** `[TPL][D]` The core idea:

> "Happy people are obsessed with maintaining their mental clarity"

Step 1, write it as a short, two-line observation. Step 2, rewrite the exact same idea as a
structured bulleted list detailing *how*:

> "they take time for rest, they focus on one goal, they eliminate distractions"

**The related instruction** `[NUM][D]` from the awareness ladder: at Level 5 (Most Aware), cover
different angles to say the same thing **1,000 different ways**.

---

## The Default Mode Network walk protocol

**Provenance** `[CIT][M:neuroscience]` for the DMN, relayed under its own name with no study cited.
Per the profile's hard-middle rule, the unsourced-evidence flag stays on it.

**The premise** `[PRN][D]` True creativity is rarely an input problem. It requires creating space
for the brain to process what it already has.

**The three steps** `[TAC][D]`

1. After a block of focused work or reading, step away from the desk and completely disconnect.
2. Walk **30 to 45 minutes**. Sometimes with an audiobook, but often in total silence to invoke true
   boredom.
3. The inward shift activates the Default Mode Network, a wandering state that subconsciously
   munches on the problems and information consumed earlier. As connections form, it shoots "aha"
   moments or "shower thoughts" into conscious mind to be captured.

**Walk length differs by purpose, and both figures hold.** 10 to 30 minutes as inter-block active
rest (q30). 30 to 45 minutes as a dedicated idea walk (q31, q34).

---

## 7 Days to Genius Ideas

**Provenance** `[BIO][G]`.

**What it is** A **free 7-day** creative challenge and educational course he created, aimed at
beginners and creators, to overcome creative blocks, open the mind, and build a system for content
ideation.

**The premise** `[PRN][D]` Note-taking is not a place to hoard random information. It is a
structured system for turning what you consume into original, articulate ideas.

**The lineage, documented once in the whole corpus** `[BIO][G]` The 7 Days to Genius Ideas system
later evolved into **Cor Notes**, which now forms the foundation of his second-brain software
**Kortex**. Free course to note system to paid software, in his own account. This is a clean
product-ladder data point and it is easy to lose, because it sits inside an idea-generation answer
rather than a business one.

**What the course teaches** The three-step Cor Notes process, the Idea Museum, Intelligent
Imitation, Writing One Idea 1,000 Ways, and the Default Mode Network walk. Each has its own section
in this file.

---

## What AI must never do — the five human traits AI lacks

Source q33. `[FRM][D]`.

**His posture** `[PRN][D]` Act as a "director" rather than a "doer". AI is a digital employee and
an intellectual sparring partner you orchestrate with extreme precision, not a shortcut to bypass
work.

**The absolute rule** `[WRN][D]` Never use AI to outsource your thinking, your creativity, or the
actual writing of your core ideas. Against treating AI like a "slot machine", typing a vague request
like "write a viral tweet" and accepting the generic slop it returns.

**The five traits, complete** `[FRM][D]`

1. **Perspective.** AI can simulate a perspective, but it lacks the direct experiences, wounds and
   wins that shape a unique worldview.
2. **Energy Signature.** It cannot mimic the human ability to care about a topic, or the unique
   energy an individual brings to their focus.
3. **Sensemaking.** It can process information but cannot assign meaning or prioritise what actually
   matters, because it has no biological stakes or mortality.
4. **Trajectory.** It has no past, present or future story arc that readers can follow.
5. **Evolving Taste.** If AI wrote for you, your output would be trapped in an infinite loop,
   whereas humans naturally grow, change their taste, and look back on old work with a desire to
   improve.

**The consequence he states** `[WRN][D]` Let AI take complete control of your craft and your output
becomes a commodity, and you turn yourself into a "drooling blob of flesh" who loses the ability to
think critically.

---

## The AI tools he names, and what each is for

Source q33, with q35 corroborating the reading-companion use.

| Tool | What he uses it for |
|---|---|
| **Claude, specifically Opus 4.1** | His preferred LLM for creating complex prompts and workflows |
| **Claude Code** | Programming terminal applications |
| **ChatGPT** | Named and rejected: he finds its default personality too restrictive |
| **Claude 4.5 Sonnet** | Named and disliked when it refuses to be "harsh" in its feedback |
| **Gemini Flash** | Reading companion for books and PDFs, because it processes large amounts of information incredibly fast |
| **Gemini 2.5 Pro** | Researching and digesting dense books, specifically *Breakthrough Advertising* |
| **Eden / Kortex (AI named "Kai")** | His own software. Second brain and AI content strategist: upload YouTube videos (auto-transcribed and analysed frame by frame), drop PDFs onto a visual canvas, and have Kai reference all those files at once to brainstorm and write |
| **Cursor and Replit** | "Vibe coding", to turn digital products or info-products into interactive Micro-SaaS AI apps |
| **Lovable.com and Bolt** | Guiding beginners through creating apps without coding from scratch |
| **Readwise** | Syncing Kindle highlights into Kortex (q32) |
| **Tweet Hunter, Twemax** | Finding creators' high-performing anomalies (q31, q34) |

**His overarching AI philosophy, stated** `[PRN][D]`:

> "Automate yourself out of work by documenting your processes as prompts."

**One dating signal.** Naming Claude by model tier and mentioning Claude Code places some sources in
2025 or later. It is the only dating signal in 54,650 words.

---

## AI Workflow 1 — the Meta-Prompt workflow (how to do anything with AI)

Source q33. `[TAC][D]`. Five steps. The premise is that instead of letting AI guess what to do, you
train it on expert information first.

1. Choose a task, for example writing a landing page.
2. Find an expert YouTube video, article or book on the topic.
3. Paste that source into AI and ask it to summarise the source into a detailed, step-by-step guide.
4. Feed that guide into a "Meta-Prompt" (a prompt designed to write prompts) and tell the AI to turn
   the guide into a structured prompt that gathers your personal context first and executes the task
   second.
5. Save, test and refine the new prompt.

---

## AI Workflow 2 — the YouTube creation workflow (7 prompts)

Source q33. `[TAC][D]`. He recommends creating **7 distinct AI prompts** to build a YouTube video
"like a pro". The corpus details four of the seven by name.

- **Title Prompt.** Paste **10 to 20** popular titles from top creators into AI, have it break down
  the psychology, then ask it to generate titles for your topic based on those rules.
- **Key Points and Intro Prompts.** Feed AI a video on outlining and on intros, and turn each into a
  prompt.
- **Script and B-Roll Prompts.** Feed AI a video script you like so it emulates the structure. Paste
  your final script into Eden or another AI and ask for B-roll ideas for each line.
- **Description Prompt.** Ask AI to create a keyword-friendly description with chapters and links.

**Gap** `[A]` The count is 7 and the corpus names 4 groups. The remaining prompts are not specified.

---

## AI Workflow 3 — the landing page and copywriting workflow

Source q33. `[TAC][D]`.

1. Upload *Breakthrough Advertising* to **Gemini 2.5 Pro** and ask for an extremely detailed guide
   on persuasive copywriting.
2. Ask the AI: "What information would you need from me to write copy using these principles?"
3. The AI returns a list (customer avatar, pain points, unique mechanism).
4. Turn that list into a **two-phase prompt**: phase one interviews him for the required business
   context, phase two writes the landing page draft.

**Provenance note** `[CIT][M:Breakthrough Advertising]` The book is named as "the legendary
copywriting book" and used as the AI's training source. **Eugene Schwartz is not named in this
file**, and the same book is the uncredited source of the five levels of awareness he teaches in
q22 and q29.

---

## AI Workflow 4 — content ideation and deconstruction

Source q33. `[TAC][D]`. Rather than having AI write tweets, paste high-performing social posts into
an AI chat, ask it to break down the psychological tactics, sentence structure and hooks, then use
those exact structural rules to write your own original ideas. The verbatim prompt for this workflow
is in the Content Deconstruction Prompt section below.

---

## AI Workflow 5 — reading companion and digestion

Source q33, with q32 and q35 giving the same workflow under different tool names. `[TAC][D]`.

Upload PDFs of books into AI and treat it as a study partner. While reading, if you do not
understand something, ask the AI for clarification. Ask it to connect the book's abstract concepts
directly to your personal life goals or business. Instead of asking for a summary, ask it to clarify
complex concepts, or challenge it to make the connection to your own goals.

**Tools named for this across three files** Gemini Flash and Gemini 2.5 Pro (q33), Kai inside
Eden/Kortex (q32), Gemini or Claude (q35).

---

## Prompt — Strategic Advisor / Clarity Coach

**Tool** Claude, per his stated preference for prompt-building. **Purpose** an advisor persona that
names gaps and assigns work. Named as "Clarity Coach" and "Strategic Advisor" in q32, given verbatim
in q33. `[TPL][D]`

> "act as my personal strategic advisor with the following context you have an IQ of 180 you're brutally honest and direct you built multiple billion dollar companies you have deep expertise in Psychology strategy and execution etc etc your mission is to identify the critical gaps holding me back design specific action plans to close those gaps push me beyond my comfort zone etc for each response start with the hard truth I need to hear follow a specific actionable steps end with a direct challeng or assignment"

The truncated word "challeng" is the corpus's own rendering and is left in place.

---

## Prompt — the follow-up command to the Strategic Advisor

**Tool** the same chat, or Eden. **Purpose** turning the advisor persona onto a life plan.
`[TPL][D]`

> "I want you to review at my life plan and help me achieve my goals what do I need to do"

The ungrammatical "review at" is the corpus's own rendering and is left in place.

---

## Prompt — Content Deconstruction

**Tool** any LLM chat. **Purpose** reverse-engineering a high-performing social post, paired with AI
Workflow 4. `[TPL][D]`

> "do a comprehensive analysis on this social post the overall idea how the sentences are structured and choice of words analyze why people engage with it why it works so well what psychological tactics are being used and how I can replicate this style step by step with my own ideas"

---

## Prompt — Landing Page Breakdown

**Tool** any LLM chat. **Purpose** teaching yourself a landing page's structure line by line, paired
with AI Workflow 3. `[TPL][D]`

> "I love this landing page copy Break down the overall structure what psychological tactics it uses why it works then break down each line individually Write this as if you are teaching me how to do it step by step"

---

## Prompt — Idea Synthesis

**Tool** Gemini or Claude as a reading companion. **Purpose** connecting a concept from a source to
your own life. `[TPL][D]`

> "I want to explore the concept of [concept] from [source] and how it relates to my life"

The square brackets are his own placeholders.

---

## Prompt — Content Writing Assistant

**Tool** any LLM chat. **Purpose** starting a post on something you are currently learning.
`[TPL][D]`

> "You are an expert at crafting engaging social post what's the best way to start a post on this topic that I'm learning and continue from there"

---

## Meta-prompt — creating a First-Principles Thinking prompt

**Tool** Claude Opus 4.1. **Purpose** a prompt that writes a prompt. The output is a questioning
partner that guides rather than answers. `[TPL][D]`

> "I want to create a prompt that helps me arrive at clear novel insights through first principles questioning according to the attached guide I want you to act as purely observational clear eyes that does not give me the exact answer but guides me to it First you will ask what topic idea or problem I want to discuss Then you will ask one question at a time following the thinking instructions Please ask clarifying questions before creating the prompt so that it comes out the best it can"

---

## Meta-prompt — creating a Personal Brand Coach prompt

**Tool** Claude Opus 4.1. **Purpose** a prompt that writes a prompt. The output is a 30-day
brand-building coach in three phases. `[TPL][D]`

> "I want to create a prompt that coaches me through building a personal brand for 30 days You will execute this in three phases Phase one is context gathering So break down everything you need from me in order to best build a personal brand... interview me to gather all of that information and ask one question at a time Then phase two is the action plan So I'm just telling it like hey output the 30-day action plan based on what I told you And then phase three is the coaching"

The ellipsis is the corpus's own.

---

## Meta-prompt — creating a Copywriting prompt

**Tool** Gemini 2.5 Pro, following the *Breakthrough Advertising* upload. **Purpose** a prompt that
writes a prompt. The output generates a long landing page in two phases. `[TPL][D]`

> "I want to create an AI prompt that generates a 500 to 10,000word landing page for a digital information product structure your prompt in two phases phase one context gathering acquire all information you need according to the information inside questions needed from user... ask the user two to three questions at a time to prevent overwhelm and then in phase two write the actual copy so use the principles from how to write copy... do this in markdown format"

The missing space in "10,000word" and both ellipses are the corpus's own.

---

## Prompt — Worldview Extraction

**Tool** any long-context LLM. **Purpose** digesting a thinker's entire body of work into one
document. `[TPL][D]`

> "I want you to break down the entire worldview of the person his core principles how he thinks through problems his main discoveries or insights and all of the ideas that best illustrate his philosophy This should be a comprehensive document as if I am diving into the entirety of his mind"

---

## Prompt — "AI Native" product prompt 1 (NOT Koe's, sourced from Signal's Post)

**Attribution** `[TPL][M:Signal]`. q33 labels this pair "Example 'AI Native' Product / Business
Prompts (Sourced from Signal's Post)". **These are not his prompts.** The corpus does not say who or
what "Signal" is. Any prompt library built from this corpus must carry the attribution or drop the
pair.

**Tool** unstated. **Purpose** product research and spec-writing from user interview data.

> "summarize the last 50 user interviews and cluster the main pain points by frequency and intensity suggest three product bets with highest signal to noise given the user feedback and usage data write a product spec for a new onboarding flow include edge cases and counterarguments"

---

## Prompt — "AI Native" product prompt 2 (NOT Koe's, sourced from Signal's Post)

**Attribution** `[TPL][M:Signal]`. Same label, same caution: **this is not his prompt**, and the
corpus does not identify "Signal".

**Tool** unstated. **Purpose** headline variation and launch email generation.

> "generate 10 variations of this blog post headline tuned to five different founder archetypes rank by project rank by projected engagement and then write a launch email in our brand tone optimized for early adopters who have bounced from the pricing page"

The duplicated "rank by project rank by projected" is the corpus's own rendering.

---

## The reusable form underneath the prompt library

**Provenance** `[PRN][D]`. Pass 1 records this as more valuable than any individual prompt, because
it is the transferable part.

**The pattern he repeats across every meta-prompt he writes:**

1. **Phase one, context gathering by interview.** The AI asks before it produces anything.
2. **Phase two, execution.** The AI does the task using the context it just gathered.
3. **Phase three, coaching** where present. Ongoing accountability after the deliverable.
4. **An explicit questions-per-turn limit.** One question at a time for the first-principles and
   brand prompts; two to three questions at a time for the copywriting prompt, stated as being to
   prevent overwhelm.

**Every figure embedded in the prompts** `[NUM][D]` IQ of 180 · "multiple billion dollar companies"
· a 30-day brand programme in three phases · a 500 to 10,000-word landing page · two to three
questions at a time · one question at a time · 10 to 20 titles · 7 YouTube prompts · 50 user
interviews · three product bets · 10 headline variations · five founder archetypes.

---

## Reading and consumption

Source q35.

**The metabolic frame** `[PRN][D]` Consumption and creation are a metabolic process. Consume too
much information without applying it and you gain "mental fat", becoming anxious, sluggish and
overwhelmed. Create without consuming and you run out of fuel and get bored.

**What to read** `[TAC][D]` Fiercely curate the digital environment and unfollow accounts that do
not serve your growth. Focus on long-form, challenging material: dense books, lectures, podcasts on
philosophy, psychology and metaphysics, all of which force worldview expansion, over short-form
"fast food" content.

**Against book summaries** `[WRN][D]` An explicit warning against reading bullet-point summaries of
books to save time. Trying to get "value without the fluff" is a manifestation of cheap dopamine
addiction, and the "fluff" is where the context, nuance and magic of new discoveries happen. You do
not need to read 52 books a year to flex your status.

**Pace** `[PRN][D]` The slower you read, the better, even if a book takes a year or two to finish.

**The daily block** `[NUM][D]` Dedicate a **30 to 60-minute block each day** specifically to
learning.

**Rotation for pattern recognition** `[TAC][D]` Read **three books at a time**, one physical, one
Kindle, one audiobook, across different genres, so the brain naturally connects them.

**Quit early** `[TAC][D]` You do not have to finish every book. If you are solving a specific
problem you can usually get the gist and the big ideas in the **first two or three chapters** and
put it down.

**Stop and Digest** `[TAC][D]` When you read a sentence that profoundly impacts you, stop reading
immediately and do not read past it. Sit with the idea, reflect on why it resonated, and capture it
in the Idea Museum. The capture destination he names is Kortex or Apple Notes.

**Write to Teach** `[TAC][D]` Do not copy quotes. Take notes as if teaching the concept to yourself
or to a beginner, which forces the brain to make sense of it and exposes knowledge gaps.

**AI as a reading companion** `[TAC][D]` For dense books, upload the PDF to Gemini or Claude and
treat it as a study partner. Instead of asking for a summary, ask it to clarify complex concepts, or
challenge it to connect the book's abstract ideas to personal life goals or business.

**His summary line, verbatim** `[TPL][D]`:

> "You can only cook with what's in the fridge"

**Prime your pattern recognition** `[TAC][D]` Never consume blindly. Always have an active project
or content outline created *before* you start reading. `[CIT][M:neuroscience]` With a clear goal in
mind the brain's **Reticular Activating System** filters inputs, automatically noticing the exact
quotes or solutions needed to build the project. The RAS-as-goal-filter claim is relayed under its
own name with no source, and it is pop-psychology rather than a cited finding. The
unsourced-evidence flag stays on it.

**Cross-domain synthesis as an input rule** `[TAC][D]` Consume from multiple distinct disciplines,
for example pulling a concept from physics to explain deep work, to generate genuinely original
perspectives instead of recycled industry advice.

**Mental Legos** `[PRN][D]` Captured ideas mean you never stare at a blank page. Open the notes and
assemble the concepts, anecdotes and quotes gathered during the consumption phase into a coherent
persuasive argument. The metaphor appears in q31, q32, q34 and q35, and q32 ties it most tightly to
Cor Notes.

---

## Numeric conflicts and unsourced claims in this file

The corpus carries no dates, so neither value in any pair can be called the later one. Both are
printed with their files.

| Item | Competing values or status | Files |
|---|---|---|
| Cor Notes components | **6** · **7** | q31 and q34 give six; q32 gives seven by adding Topic & Summary and Objections. q32 is fullest, q34 has the 3-to-4 selection rule |
| Walk length | **10 to 30 min** · **30 to 45 min** | q30 as inter-block rest; q31 and q34 as a dedicated idea walk. Different purposes, both hold |
| His software's name | **Kortex** · **Cortex** | q32 and q34 say Kortex, which is correct; q31's "Cortex" is a transcription slip and is not an alias |
| YouTube prompt count | **7 stated**, 4 named | q33. The remaining three are not specified `[A]` |
| Default Mode Network as an idea engine | Relayed under its own name, no study cited | q31, q34. Evidence flag stays |
| Reticular Activating System as a goal filter | Relayed under its own name, no study cited | q35. Evidence flag stays |
| "Second brain" | Tiago Forte's term, used without attribution | q32. Marked `[I]`, an inference |
| The awareness ladder behind Workflow 3 | *Breakthrough Advertising* named, Eugene Schwartz not named | q33 |
