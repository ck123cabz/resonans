---
type: corpus
aliases: ["Core Knowledge: Jason Murray"]
corpus: jason-murray
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-10-03
---

# Core Knowledge: Jason Murray

**Layer 1, always in context.** Written 2026-10-03 for the `jason-murray` lens. It answers art direction questions the way Jason Murray teaches them: concept first, then craft, then taste, portfolio and career. Procreate tutorials, gear reviews and travel films are left out; look them up in the retrieval index (`analysis/` topic files on motion and gear).

---

## 0. How to read this file

**What the corpus is.** Jason Murray is an art director (Energy BBDO, Huge, Amazon Brand Innovation Lab), independent since January 31, 2025, YouTube channel @jason_swet, company Swet Studio. The raw layers under `.raw/` hold 75 video transcripts (about 214,000 words), 127 Shorts, 216 LinkedIn posts, 18 newsletter issues, 18 frame notes read off 77 video frames, 129 tools from thetoolbox.art, his site, blog, product and press pages, 24 files on people he cites and 44 on campaigns he cites. A NotebookLM notebook (96 sources, 72 indexed) answered 44 questions. Pass 1 turned those answers into 551 signals across three lane files and checked each against the first-order layers.

**Provenance markers.**

| Marker | Meaning |
|---|---|
| `[D]` | His words, from a transcript, Short, newsletter or post. Captions carry no punctuation; quotes keep that. |
| `[D:vis]` | Text read off a frame of his video: a slide, a FigJam note, an ad on screen. |
| `[D:guest:Name]` | A guest speaking on his podcast or writing in his newsletter. Not his. |
| `[X:Name]` | A cited person's own framework. Not his. |
| `[G]` | A fact from trade press or a product page: year, agency, price. |
| `[M]` | NotebookLM's wording with no first-order match. Medium confidence. |
| `[I]` | A pattern I drew across sources. He never states it. |

**Confidence ceiling.** `[D]` and `[D:vis]` are as good as this corpus gets. Three limits sit on top. Captions have no speaker labels, so podcast lines are split by context. His campaign readings are reverse-engineered ("that might have been Nike's insight"), so treat them as his teaching, and the `[G]` line as the record. His paid course and bootcamp lessons are outside the corpus.

**Source short names used below.**

| Short | File under `.raw/` |
|---|---|
| ADT | `video/art-direction-techniques-you-can-use.md` (frames: `frames/art-direction-techniques-you-can-use.md`) |
| MENU | `frames/art-direction-menu.md` |
| AD25 | `video/how-to-become-an-art-director-in-2025.md` |
| AD26 | `video/how-to-become-an-art-director-in-2026.md` (frames: `frames/how-to-become-an-art-director-in-2026.md`) |
| PIVOT | `video/how-to-pivot-to-art-direction-with-no-experience.md` |
| PORT | `video/how-to-craft-an-art-director-portfolio.md` (frames: `frames/how-to-craft-an-art-director-portfolio.md`) |
| LIVE | `video/art-director-reacts-to-portfolios-live.md` |
| PASSION | `video/turn-your-passion-projects-into-an-art-director-portfolio.md` |
| TOT | `video/the-theory-of-taste.md` |
| MOOD | `video/how-to-art-direct-your-mood-board-in-photoshop.md` |
| HOOK | `video/the-lost-art-of-the-hook.md` (frames: `frames/the-lost-art-of-the-hook.md`) |
| QA26 | `video/answering-every-aspiring-art-director-question-ye-concert-reaction.md` |
| BLUEPRINT | `video/my-exact-content-blueprint.md` |
| FINISH | `video/how-to-finish-every-project-you-start.md` |
| AI22 | `video/ai-will-steal-my-job-as-an-art-director.md` |
| EP2, EP4 | `video/building-my-2025-creative-empire-the-toolbox-podcast-ep-2.md`, `video/why-i-quit-my-art-director-job-at-amazon-the-toolbox-podcast-ep-4.md` |
| DREAM | `video/i-found-the-dream-creative-career-path.md` |
| IRIS | `frames/iris-taxonomy-of-visuals.md` and `frames/shorts-visual-tools.md` |
| MAD + date | the newsletter issue of that date under `newsletter/` |
| S + date | the Short of that date under `shorts/` |
| LI + number | the post under `linkedin/` |

---

## 1. What art direction is, in his words

### The definition
His slide, which he says is the first 20 minutes of the first bootcamp class: "An Art Director creates and develops concepts, and defines the look & feel of those concepts across channels and mediums. They are responsible for visual execution, often directing and collaborating with designers, photographers, filmmakers & more." On the slide "concepts" and "visual execution" are underlined and "look & feel" is in italics. Those are the three parts of the job. ([D:vis] AD26 frames)

### Concepts + craft
The next slide reads "CONCEPTS + CRAFT". The portfolio video repeats a text card four times: "IDEA + CRAFT". ([D:vis] AD26 frames, PORT frames)

He says half the job is ideas: "the other 50% of the role of art direction is the ideas Art directors are the bridge between the business the strategy the marketing and the creative execution the art that comes out of it". If you go down the route of craft alone, "you should just specialize as a designer in a certain field or as an executor". He never says "50/50" and never names a rule. ([D] PORT)

Which half is usually missing: "execution doesn't matter if you're executing a dumb idea". The idea is "usually the missing piece for most creative people that are thinking about art Direction". ([D] AD25)

Craft "is something you can learn on YouTube". He admits "I was a terrible designer at first" and "I never went to design school". ([D] AD25, AD26)

### Designer versus art director
His own contrast is attention against function: "a designer not always but often is more focused on the function the utility of what they're creating while an art director honestly function goes out the window and they're just so much more focused on attention". Slides: "Art Direction ≠ Design" and "Attention vs Function". ([D] AD26; [D:vis] AD26 frames)

An art director is not a senior designer by default. His Creative Pipeline slide shows why. Timeline: Strategy, Brief, Ideation, Concepts Sold, Execution. Creative director, copywriter and art director run from Brief to the end. Designers, producers, photographers, directors and DPs start at Concepts Sold. Side text: "Art Directors are not more senior by default. They can be more senior depending on the industry or company. But they are usually involved earlier in the pipeline." ([D:vis] AD26 frames)

The title changes by industry. His slide "Art directors across industries" has four columns: film and television (runs the art department under a production designer), fashion (shoot concepts and styling), design studios ("A senior role" managing designers) and advertising ("Idea-driven, responsible for visual execution", "Can be junior"). ([D:vis] AD26 frames)

The "architect of clarity" and "creative anarchist" lines are Sir John Hegarty's. See section 10.

### Art director, copywriter, creative director
"while the copywriter is focused on on handling the verbal and the written storytelling and messaging the art director is focused on the visual storytelling". Together they create and articulate a concept, under a creative director. In 2026 he adds that the pairing is no longer a given. He warns that the copywriter "is usually the one that's getting a lot of the credit for ideas because they're writing up a lot of the stuff". ([D] AD25, QA26)

Slide: "Art Direction ≠ Creative Direction". "creative director is more of a management role. You've got to have a lot of experience otherwise you won't be trusted". His advice to juniors who use the title: "if you're a creative director at the beginning of your career I would consider rethinking your title and rethinking your path". The route to creative direction is to work for a creative director. ([D:vis] AD26 frames; [D] QA26, AD26)

### Visually multilingual
"one big thing that I would emphasize about an art director is you need to be multilingual". The slide is a 4 by 2 grid: Photography + Cinematography; Environments, Styling & Props; Typography; Iconography & Illustration; Editing & Animation; Casting & Talent; Color; & more. A red loop circles a different subset each time, because each art director covers some of them and no one covers all. ([D] AD26; [D:vis] AD26 frames)

Newsletter: "Art Directors are creatively multilingual. You have to understand a bit of everything: design, photography, lighting, film, marketing, content creation." The extra language is the client's: "understanding our clients and the marketing objectives they are trying to reach". He splits learning into THINKING, which he teaches, and CRAFT, which "is a personal pursuit". ([D] MAD 2026-02-25)

### Chef and orchestration
He asks what the art director's tool is. A photographer has a camera and a painter has a brush. His answers: "I often like to compare our direction to visual orchestration because yes you are conducting the visuals and that might involve multiple team members but it can also be a one-man band where you put on that hat". And the chef: "The chef might lead a team in the kitchen but they can also assemble these ingredients themselves And they have frameworks and tools and principles they can use over and over again". Captions write "our direction" for "art direction" throughout. ([D] ADT)

The chef comparison is why everything in section 3 is called an ingredient. He wants "something that feels concrete" so the work becomes "a more repeatable process". ([D] ADT)

### Describe the look in words
"Often the best way to define that visual language is to also describe it. That's right, through words." His creative directors made him add a short write-up to every mood board. It "removes the subjectivity that comes from looking at references and articulates clear boundaries". The failure case: "Without a clearly articulated vision, you get mismatch luggage." With no technical words, mash two worlds: "it's like a Wes Anderson film" but "shot on a flip phone". ([D] S 2025-03-17, S 2025-04-09)

---

## 2. Concept

### Insight
"an insight is a revelation or it's an unspoken human truth it's one of those things that when you say it it changes the way you see the world or it changes the way you see yourself". ([D] AD26)

The pink sticky on his Roadmap board, signed Jason: "The Insight is a revelatory or unspoken truth." The green note gives the long form: "An insight in advertising is a deep, human truth that explains why people think, feel, or behave. It reveals an unmet need, tension, or motivation that a brand can address in a meaningful way." ([D:vis] AD26 frames)

**Four traits of a strong insight**, from the board. Rooted in Human Behavior: "It taps into emotions, psychology, or cultural truths." Not Just a Fact: "It goes beyond observations and asks why something happens." Tension-Driven: "It highlights a gap, struggle, or contradiction in people's lives." Actionable: "It unlocks a powerful creative idea that the brand can own." Under them: "Great ideas are rooted in strong insights." ([D:vis] `frames/how-to-pivot-to-art-direction-with-no-experience.md`)

**His tests.**

- The template: "An insight is just that. It's a revelation. Something that doesn't just sound true, but it's insightful. People think X, but the reality is Y." ([D] S 2026-06-16)
- The reaction: great insights "often sound counterintuitive, uncomfortable, or like a contradiction at first", then you think "ah ha. I hadn't thought if it like that before." The typo is on the board. ([D:vis] AD26 frames)
- The contradiction check: "is that a truth that sounds like a contradiction". ([D] PIVOT)
- Write it plain first: "we're not going to dress it up yet like a tagline or campaign. We just want the truth." ([D] S 2026-06-02)
- Bad insights "sound more like observations. Obvious. Not very profound." His examples of an observation: "the sky is blue", "people get hungry in the mornings so they need their breakfast". ([D:vis] AD26 frames; [D] AD26)

**Observation to insight is one line.** "it's a spectrum from observations to insights it's about digging deeper into something that you know isn't being spoken". Board note: "One person's insight might be another person's observation." His hook video draws it: a horizontal line, "Observation" at the left end and "Insight" at the right, then "Idea" stepped above Insight and "Hook" stepped above Idea. The idea comes from the insight and the hook comes from the idea. ([D] PIVOT; [D:vis] HOOK frames)

**How to move right along the line.** Ask why. On Rachel Holmes's Coppertone line ("Research shows Gen Z is aware of the importance of wearing sunscreen, yet they still go without it regularly") he says: "that's a pretty great observation and that's what the research shows but if I wanted to make this even more intriguing I dig deeper". He has no name for this drill. The hook video has a one-word slide: "Why?" ([D] LIVE; [D:vis] HOOK frames)

**Borrowed sources he names.** Mark Pollard ("write it in a more savage way", and the slide "Insights are unspoken human truths"), Julian Cole, Luke Sullivan's *Hey Whipple, Squeeze This*, and Jason Bagley's eight-week class. Section 10 has the owners. NotebookLM's "five-step insight process" is its own assembly. ([D] AD26, PIVOT; [M] for the five steps)

### Idea
"Then the idea is what we do with that truth What is our creative formula that will help our audience experience that insight for themselves". ([D] ADT)

"his idea which I always describe as the verb what are we going to do with that insight". "Big ideas need verbs. We could dramatize something. We could contrast something. We could flip something." His students write it as an insight sentence followed by "So let's…". He uses idea and concept for the same thing. ([D] ADT, S 2026-06-16)

Once set, the idea is a creative formula: "every execution follows that same formula". He also calls it an organizing idea. NotebookLM's "If [Insight], then we will [Idea]" formula is nowhere in his words. ([D] ADT, QA26; [M])

### The Big Idea Pyramid
"that's what a big idea is It's your overarching creative formula that tells you what this project or this campaign is going to do". ([D] ADT)

Three bands, top to bottom. **Insight at the point**, "the smallest part of the triangle", one focused human truth. **Idea in the middle**, what you do with the truth. **Execution at the wide base**, "the largest part of the triangle cuz it has the most detail. It has the most variety." Every execution ladders back up. He calls it the big idea pyramid in the long video and "my big idea triangle" in June 2026. NotebookLM drew it upside down; ignore that. ([D:vis] ADT frames; [D] S 2026-06-02, S 2026-06-16)

Look and feel sits between idea and execution: "A great idea statement also starts to hint at the look and feel, the art direction". This is where the pyramid joins the menu in section 3. ([D] S 2026-06-16)

"Big" is about scale: "Not every big idea is a great idea. We're talking scale." "I like to separate quality from size". ([D] S 2026-06-16, PORT)

**Four traits of a Big Idea**, green note on the board: Simple & Clear; Emotional; Campaignable (works across channels and executions); Brand-Ownable. ([D:vis] AD26 frames)

**His worked example, Nike "Rip the Script" (2026).** Insight: "football is increasingly feeling more planned and strategic, maybe a little staged. But, the most beautiful moments are when players follow their instincts. You feel that tension? That's our insight." Idea: "we will rip up every playbook football is being told to follow and give players and fans the freedom to go off script." Executions: a hero film, athlete vignettes that each rip the script their own way, and content that only borrows the look. He is reverse-engineering Nike here. ([D] S 2026-06-16; [G] 2026, Wieden+Kennedy)

His board works four more: Snickers "You're Not You When You're Hungry", Dove "Real Beauty", Spotify "Wrapped", Nike "Winning Isn't for Everyone". The retrieval index has the text. ([D:vis] AD26 frames)

### The Idea Sizing Chart
A FigJam table on the Roadmap board. Eight rows, biggest to smallest, with three group labels in the left column. ([D:vis] AD26 frames; `frames/visual-maps.md`)

| Row | Group label beside it |
|---|---|
| Business Strategy & Positioning | |
| Branding | |
| Platform | Big Ideas |
| Campaign | |
| Execution | |
| One-off | Small Ideas |
| Tactics | |
| Crap | No ideas |

The chart has no job titles on it. The 2025 version showed Execution twice and had no Tactics row. Art directors, copywriters and most creative directors work at Platform and Campaign. Executions need every detail; a big idea fits on a Post-it. ([D:vis] AD26 frames; [D] S 2026-02-05)

A line can outgrow the Platform row: "just do it was such a big idea for Nike that it is part of their branding and positioning of the entire company um so it's larger than a platform". ([D] AD25)

### Platform, campaign, execution
- **Platform:** "it's just one level higher than a campaign where all it really is is a single uh message a single line". Board: "A platform is a type of 'big idea'". Snickers is his standard example. ([D] AD25; [D:vis] AD26 frames)
- **Campaign:** one big idea carried across touchpoints for a period. Rip the Script and Winning Isn't for Everyone are campaigns in his usage. ([D] S 2026-06-16)
- **Execution:** one piece. "what if we just put a sneaker in Time Square well that's not really a big idea that's just coming up with an execution". ([D] AD25)

The size test is legs: "if that big idea could could have you know legs like a centipede have hundreds of mini ideas underneath it then it's a big idea". "Has legs" is the industry's phrase and the centipede is one simile from 2025. The Post-it test and "starts talking and won't shut up" are Luke Sullivan's; see section 10. ([D] AD25)

### The spec campaign process
Why spec: "You can't get hired without the work, and you can't get the work without getting hired." "You make spec work (fake work). It's the number one way creatives get into this industry." Reviewers want proof you can "think conceptually, think at scale, then translate that idea into visual solutions". ([D] MAD 2026-08-14)

Steps, in the order his bootcamp and videos run them:

1. **Pick a brand people already know**, "a globally recognized brand ideally so that you don't have to do a lot of the education". In 2025 he passed on other people's advice to skip Apple, "because you're never going to make fake ads that are better than the real ads". In August 2026 he wrote "you make fake campaigns for the biggest brands in the world". He does not reconcile the two. A fair reading: a known brand, yes; a brand whose real work you cannot beat, no. ([D] PORT, AD25, MAD 2026-08-14; reading is [I])
2. **Find the insight.** Write it plain. Push it right along the observation line by asking why.
3. **Write the idea as a verb sentence.** "So let's…"
4. **Name it.** "Give your project a title as in the idea has a name the campaign concept has a name That's going to show that you can distill an idea down to a single line It's going to make it memorable". ([D] PORT)
5. **Choose the ingredients.** Two or three standouts from the menu (section 3), and at least one that can travel across channels.
6. **Make a key visual or lockup** (section 3).
7. **Mock up the touchpoints.** His table says "Try for 4-10 different touch-points (social, OOH, TV, IRL, stunt, activation, print, non-traditional/unexpected, etc.)". His checklist says "4-6+". Four is the floor both share. ([D:vis] PORT frames)
8. **Lay out the page** in the order of section 6, with a line of thinking between touchpoints.
9. **If it can be done for real, do it.** His own student stunt, Venmo the Homeless, raised about $6,000 for a shelter. ([D] PIVOT)

Brief sources: The One Club Young Ones archive, D&AD New Blood, the One Show archive. Bootcamp students do the whole thing in 30 days. On volume: "just try not to come up with great ideas pour your subconscious out just come up with lots of ideas", in 15-minute sprints. ([D:vis] PORT frames; [D] QA26)

---

## 3. Craft

### Execution is ingredients
"Once we have our concept the art director's job is to bring it to life to actually execute it to guide the execution visually This is where art direction ingredients come in". The test for any ingredient: "what creative ingredients actually serve the idea what helps you feel and experience the insight for yourself". ([D] ADT)

### An Art Direction Menu
His slide, 11 headings and 61 lines. "even this menu doesn't encompass everything This is just to get your brain going". ([D:vis] MENU; [D] ADT)

1. **Color & Light:** color palette; contrast (high vs low); lighting (harsh, soft, natural, theatrical); texture (grain, gloss, paper, noise); depth of field (focus vs blur); grade or finish (film emulation, warm vs cool, faded vs punchy).
2. **Composition & Framing:** cropping; camera angle (eye-level, overhead, low); symmetry vs asymmetry; foreground / background; focal point (what the eye hits first); hierarchy of attention (what leads, what recedes); negative space; scale (how big or small things feel); density vs minimalism; repetition or pattern.
3. **Imagery:** photography vs illustration vs CG; stock vs shot (found vs bespoke); real people vs models vs characters; polished vs raw; literal vs metaphorical; close-up vs wide.
4. **Casting & Talent:** who's cast (age, look, energy, non-model vs model); expression and gaze (to camera vs away); gesture and body language; movement and direction of talent.
5. **Styling & Set:** wardrobe; props; set & location; era / time period; cultural references.
6. **Type & Graphics:** typeface (utility vs expressive); type hierarchy; type as image vs type as support; copy-driven vs image-driven; alignment; grid vs anti-grid; iconography; frames, borders, containers.
7. **Visual References & Influence:** genre or world you're borrowing from (film noir, 90s skate, editorial fashion, brutalist); era of visual style; homage vs originality.
8. **Motion & Editing:** pace and timing; hold vs movement; ease and weight; transitions vs hard cuts; camera movement; loops vs linear.
9. **Mood:** playful vs serious; clean vs chaotic; intimate vs epic; quiet vs loud; aspirational vs relatable.
10. **Constraints:** budget; location; format; timeline; platform norms; brand rules worth breaking.
11. **Perspective & Intent:** POV (first-person, observer, overhead); staged vs candid.

NotebookLM invented two ten-category menus; use this one. He gives no rule for choosing photography over illustration or CG. ([M] for the NotebookLM versions)

### Two to three standout ingredients
"there might be a lot of ingredients to make a dish but there's usually like two to three standout flavors standout ingredients". "You need to have some restraint". In his own examples the count runs one or two. On Polaroid: "I'm not in awe of the craft. I'm more so impressed by the decision making and the restraint." The rule is about a finished campaign. NotebookLM moved it onto mood boards, where he gives no count. ([D] ADT, MAD 2026-07-06; [M] for the mood board version)

### Visual Feeling ↔ Visual Solution
One line with five ticks, "Visual Feeling" on the left and "Visual Solution" on the right. He places each ad on it by speech. ([D:vis] ADT frames)

**Left, visual feeling.** "On the left side of the spectrum I write visual feeling Oftentimes concepts they just need supporting visual ingredients They need visual decisions that help support the message that's already being conveyed". Copy, dialogue or voice-over tells the message; the ingredients make you feel it. He also calls this the look and feel. ([D] ADT)

**Right, visual solution.** "sometimes it's best to convey that concept through the visuals themselves". There "the symbols and the pairing of certain images together become the message You don't need any supporting copy at all". He uses visual solution and visual device for the same end. ([D] ADT)

"There is no right or wrong". ([D] ADT)

**His test for a visual device.** "That's when it feels more like a visual device to me when there are endless subjects you could slot in". October 2025: "a visual mechanism where you could swap in any brand or theme, and the executions are endless." This is the legs test applied to a picture. ([D] ADT, S 2025-10-03; the link to legs is [I])

**Copy on the right side shrinks to a button**: "it might just be a tagline or a sort of button the punchline". ([D] ADT)

**The swap test for the left side.** Reset Polaroid's handwriting in Helvetica: "yes we would get the same message but we wouldn't feel it in the same way". ([D] ADT)

**Where his examples sit.**

| Example | Standout ingredients he names | Position | Source |
|---|---|---|---|
| Polaroid, "The Camera for an Analog Life" | the Polaroid prints; handwritten blue ballpoint | "a little bit more on that left side" | [D] ADT; [G] 2025, in-house |
| Oatly hand-lettered outdoor | the "big blocky font" | left | [D] ADT |
| Diesel, "Enjoy Before Returning" | flash photography; "super good-looking not normal models" in "a normalish high school setting" | left | [D] ADT; [G] 2019, Publicis Italy |
| Connor McLoughlin, Arc'teryx "Playdate" (student spec) | cut-out hand-coloured letters "collaged together like a child"; close-up photography | left | [D] ADT; [D:vis] ADT frames |
| Jaya Schreihart, EF Tours "Later Is Now" (student spec) | the boarding pass as medium: "there's really just one clear ingredient here" | the middle: "somewhere in between creating the feeling but also the medium itself" | [D] ADT; [D:vis] ADT frames |
| LEGO shadow ads | the product; a shadow that does not match it | right, "a visual device that just has endless possibilities" | [D] ADT; [G] "Imagine", 2006 to 2007, Blattner Brunner |
| LEGO "Build the future" | the product builds the child's future self | right | [D] ADT; [G] 2017, Ogilvy & Mather Bangkok |
| WMF knife, "Sharper than you think" | any food; the chopping board cut through with it | right; "It's not the most conceptually big idea" | [D] ADT; [G] 2004 to 2005, KNSK |
| Twitter hashtag out-of-home | the # symbol; an image standing for a topic | right | [D] ADT; [G] 2016, in-house |

He does not place Snickers, Hydro Flask or Dollar Shave Club on the line. His three type examples sit left and the hashtag sits right, so type has no fixed side. ([I])

### A device has to be airtight
"Visual shorthand must be airtight to be effective. Simple devices are difficult to execute because they require an immediate connection. If a viewer has to pause to decode the metaphor, the device has failed." Isolate "a specific detail within a larger scene". Use copy as the punchline. Iconic marks work best "because they already live in the viewer's head. The goal is to trigger a story that the audience finishes for you." His word for copy that repeats the picture is "see-say". ([D] MAD 2026-04-08, S 2026-03-25)

### Always have a reason
"a good art director always has a reason. Even when the honest reason is 'it just looks right,' you still gotta walk stakeholders through why." His Polaroid rationale: "Blue ink historically signals authenticity. You don't sign a contract in black." "You can say a thing, but it's HOW you say it that slices into your psyche." ([D] MAD 2026-07-06)

### Key visual or lockup
"I highly recommend always having a key visual or a lockup That's some sort of a key visualizing a single image that represents the entire campaign". From the live review: "what is the thing that tells the idea in a super clear way in in one image". His checklist marks it "(optional)". It goes at the top of the page, carries the idea's name, and proves "you can think big and and distill everything down into a single creative concept". ([D] PORT, LIVE; [D:vis] PORT frames)

Model: Nike's title "rip the script and they've got the cracked screen the digital cracked screen down the middle where it's like breaking You're visually hinting at the entire idea". Title plus one graphic gesture that acts out the verb. ([D] PORT)

The fix he gave Jairo Obando's Qdoba "Portion Pledge": show the pledge itself, signed and framed, or "lock it up with the kudoba logo" in strong type. The top image was only the brand logo, and the brand "is not the interesting part about this campaign your idea is". NotebookLM's three-step key visual formula is its own. ([D] LIVE; [M])

### Threading one ingredient across touchpoints
"You'll try to find an ingredient that can be threaded across these channels Ideally an ingredient that can live in an out of home ad and within an actual in-person IRL popup or some sort of activation". In both student campaigns the standout (cut-out letters, boarding pass) shows up in print, out of home, social and the activation. ([D] ADT)

Three tiers of consistency, from his Nike breakdown: the hero film states the idea; vignettes apply the formula their own way; "Some touch points or content might just borrow look and feel, but not spend the time hammering the message." Packaging and retail work the same way: "you'll pull in the look and feel You'll pull in colors the type". ([D] S 2026-06-16, PORT)

What holds it together when many people execute: "attached to that big idea, you can develop a sort of look and feel. You can decide on certain ingredients that will represent this campaign. So, there's a visual through-line as well." Nike's four repeating ingredients: "bts hollywood sets, cracked screens, SMPTE color bars, and digital glitching". ([D] QA26, MAD 2026-06-23)

### Music as an ingredient
"Now music is one of the most important creative ingredients And it's not even visual". It is not on the menu slide. How he picks: "I teach timeless art direction principles So I look for timeless music maybe a little nostalgic". He keeps to one artist so tracks pull "from that same world", and avoids "anything that feels generic or interchangeable". He says this inside a Musicbed sponsor read. ([D] ADT)

Three music techniques, framed as hooks: **the Mismatch** ("serene calm footage try pairing that with an aggressive track"), **the Amplifier** (match the emotion on screen and turn it up), **the Sonic Signature** (repeat motifs across videos so viewers "associate a sound with the value you bring"). ([D] HOOK)

---

## 4. Named techniques and Iris

In February 2026 he began numbering techniques ("Art Direction Techniques 001"). By September 2026 they sit in a tool he calls Iris. None of this is in the NotebookLM answers; every entry here is first-order.

### Techniques he has defined

| Technique | His definition | Example he attaches | Source |
|---|---|---|---|
| Visual literalism | "rendering the message as literally as possible. Word for word, what does the phrase or key message itself look like when translated to images?" | Sudafed, a man holding his own huge head; a KitKat bench; BMW mailer you tear to cut a road through snow | [D] S 2026-03-06 |
| Visual quotation | "references known genres, periods, or pieces of work. It allows the image to stand on the shoulders of its predecessors, as long as that reference is known (at least subconsciously) by the audience." | Szilveszter Makó's portraits quoting painting and Nosferatu | [D] MAD 2026-09-28 |
| Genre quotation | "If your visuals don't mean anything, try genre quotation. Reference something." It works "As long as your viewer understands that borrowed visual code." | period-drama and pirate stills with ad copy; 4x4 grid backgrounds in creator videos | [D] S 2026-09-30, S 2026-09-02 |
| Visible facture | "when the process can be seen in the final work ie when the hand of the maker stays present through painted surfaces, grain, brushwork, and constructed scenery" | Makó's painted props; Polaroid's pen | [D] MAD 2026-09-28 |
| Frame within a frame | "turns the portrait into a small stage. Scenes within scenes." | Makó's set-built portraits | [D] MAD 2026-09-28 |
| Scale disparity | "utilizes the contrast of sizes in order to accentuate a message" | Makó | [D] MAD 2026-09-28 |
| Figure-ground reversal | "Too obvious? Try a figure ground reversal. Turn the subtraction into the subject." | two posters for The Lobster, a figure embracing a cut-out | [D] S 2026-09-30 |
| Form substitution | "Too literal? Try form substitution. Use the shape of one thing to mean something else." | fried chicken shaped like a rocket plume | [D] S 2026-09-30 |
| Brand mark as a lens | "using a brand mark as a lens rather than a badge". "The formula is simple: Brand mark + Subject" | Time's red border; Twitter's hashtag; Google "Year in Search" | [D] MAD 2026-04-08 |
| Visual device | "a visual mechanism where you could swap in any brand or theme, and the executions are endless" | Rudy Willingham's paper cut-outs, his $1 tier | [D] S 2025-10-03 |
| Manipulate the medium | "Think how could you manipulate the medium itself." | a Britannia out-of-home campaign shaped by nature | [D] S 2025-10-03 |
| Hockney joiner (panography) | "a technique where you piece together a scene with separate photographs taken from different vantage points and moments in time. The very point of the technique is they aren't seamless." | sports ads showing motion in a still; Converse | [D] LI 010, S 2026-04-11 |
| Design through metaphor | "The LA28 work doesn't rely on flower illustrations; it uses color and patterns to suggest energy and growth." | LA28 "Super Bloom" | [D] MAD 2026-04-08 |
| Shipping the process | "Instead of hiding the effort behind a 'making of' video, bring those glimpses of the practical setup into the final execution." | OMODA 7 ads by Uncommon | [D] MAD 2026-04-08 |
| Anthropomorphism vs personification | "personification is a different way of abstracting human qualities, literal human, than anthropomorphism" | Apple's claymation Mac mini against "I'm a Mac" | [D] S 2026-08-31 |
| Reframe the familiar | "Take something people recognize and break up the pattern. You can borrow the association of those images." | 4x4 grid visuals | [D] S 2026-09-02 |

The September 30 Short gives three of these as fixes for named problems: too obvious, figure-ground reversal; visuals mean nothing, genre quotation; too literal, form substitution. Visual literalism (March 2026) and "Avoiding literal interpretations" (April 2026) point opposite ways and he does not reconcile them. ([D] S 2026-09-30; the contradiction is [I])

### Iris
"I call it, Iris™". Page header: "MODERN ART DIRECTION | A Taxonomy of Visuals". October 2026 bootcamp students get it first. No public URL as of 2026-10-03. ([D] MAD 2026-10-02; [D:vis] IRIS)

**Structure.** ([D:vis] IRIS)

- A filter row: All, **Differentiate** (red), **Group** (blue), **Sequence** (yellow), **Predict** (purple), "Any variable", Search, and the counter "39 of 39 techniques".
- Two rows of technique nodes. Lines run from each technique to every example image that uses it, in the group's colour.
- A few hundred example images: magazine covers, posters, print ads, photographs.
- Two-way selection. Pick a technique: "Visual quotation · 15 examples". Pick an image: "The shadow of Nosferatu, in an embroidered dress · 3 techniques".
- Variables per technique. Visual quotation carries four: genre code, period, format, work.
- A third layer in the newsletter image, **reference families**: historical portraiture, theatrical sets, painted backdrops, religious iconography. Families feed techniques, which feed images.

**What is read.** 22 names read clearly, with the group inferred from line colour. Differentiate: scale disparity. Group: symmetry, face schema, visual rhyme, anthropomorphism, semantic compounding. Sequence: center placement, leading lines, gaze cue, size hierarchy, frame within a frame, body vector, reading path. Predict: closure, forced perspective, caricatural exaggeration, form substitution, visual quotation, pattern break, occlusion, crop at the edge, visible facture. Six more read at low confidence from 4-pixel letters: saturation blocking, simultaneous contrast, warm and cool split, semantic juxtaposition (red); common region, good continuation (blue). ([D:vis] IRIS)

**What is unread.** 11 nodes at the left of the lower row, with red and blue lines. Visual literalism, figure-ground reversal and genre quotation are not among the 28 read names. The four groups read as jobs a visual does for the eye (tell apart, tie together, order the reading, set up an expectation); he has published no legend, so that reading is inferred. ([I])

**What he says it is for.** "References become useful when you can name the technique." "we can break the image into reusable visual techniques. I'm building tools for my students so they can not only name techniques in the work they love, but reconstruct new visual solutions for their own work." The same techniques "don't create one monotonous look & feel. swap in different subjects, combine with different ratios of intensity, change other variables and those same techniques create vastly distinct and unique images." ([D] MAD 2026-09-28)

### Visual lineage
"Every visual idea carries baggage/associations, references, predecessors. And as art directors, we have a choice: we can utilize parts of that lineage intentionally, or we can accidentally plagiarize it." ([D] MAD 2026-02-17)

Method: "when you find a visual that inspires you, DONT STOP THERE. Trace it back." Three questions: "Who did this concept first?" "What photographer or artist established this visual language?" "How far back can you go before its something unusable?" Then branch from further back: "you reference Weston instead of the 2025 campaign everyone else saw". ([D] MAD 2026-02-17)

His worked tree runs from Decathlon's 2025 print ads back through Lurpak and Werner Bronkhorst to Edward Weston's 1930s peppers. ([D] MAD 2026-02-17)

The reasoning under it: "Smart art directors use these associations. They understand that certain visual ingredients come pre-loaded with meaning." "A close-up of fabric intuitively reads as terrain. A zipper becomes a road." The limit: "there's a fine line between leveraging visual shorthand and simply repeating what's been done". ([D] MAD 2026-02-17)

---

## 5. Taste

### His position
"the metaphor of taste is actually a pretty passive one consuming things and as an art director that's never been enough for me we have to visually cook we have to use our taste". "taste alone passive taste i truly don't think it's the moat everyone thinks it is". On LinkedIn, March 24, 2026: "People are saying that 'taste' will be your only moat. I think that's a little naive. I think VISION is a lot more powerful". He says "passive taste" and never says "active taste". ([D] TOT, LI 055)

"Taste judges what already exists. Vision imagines what doesn't." Stop asking "what do I like?" and ask "what would you like to see?" "You eventually got to stop tasting and start cooking." ([D] S 2026-06-03)

A second answer to the moat claim: "A lot of people talk about taste as your moat. I really think it's your Rolodex." ([D] `video/visuals-you-can-t-find-on-pinterest.md`)

### The three milestones
"there's three important milestones or techniques for you to learn to unlock your taste and the first one is broaden your inputs". ([D] TOT)

1. **Broaden your inputs, and capture them.** "nobody trusts the taste of someone who only eats fast food". Raise volume and variety. "I want you to replace scrolling with digging." Save in the moment with the Cosmos share extension, because "you can't articulate taste you haven't actually experienced and stopped to collect". ([D] TOT, S 2026-04-03)
2. **Express your taste.** The three levels below.
3. **Become visually literate through immersion.** "the best chefs don't just like sushi they move to japan". "Literacy is being able to critically read, comprehend, and express." ([D] TOT, S 2026-04-22)

The Shorts series ran five episodes from April 3 to June 3, 2026; the long video covers the first three. ([D] S 2026-06-03)

### The three levels of expressing taste
"this is the bridge between passively consuming and having taste you can actually use in your job in your career and there are levels to this". ([D] TOT)

1. **Know what you like or dislike.** "most people don't even get here intentionally". On every save, ask: why did I save that, do I actually like this, what about it do I like. Rejecting on purpose counts.
2. **Say how it feels.** A simile, metaphor or reference: "this maybe feels like a Michel Gondry film". Collection titles like "uncomfy", "dreamlike", "tense". "this level of language is actually really useful with clients because they don't need to know the technical words they just need a shared feeling".
3. **Name the ingredients.** "flashlighting a handdrawn mixed media effect that note of toasted oak you're not just saying how it feels anymore you're naming what made it feel that way". This is the level for talking to "the executors the partners or vendors". "You're filling a pantry." "Visual pantry" is NotebookLM's phrase. ([D] TOT; [M] for "visual pantry")

"learning to form an opinion and explain why you like or dislike something is the bridge between passive consumption and the kind of taste you can build a career on". ([D] S 2026-04-09)

### The five taste types
"everything I just talked about is a nuanced matrix of flavor profiles. There is no single monolith of taste." ([D] S 2026-05-01)

- **Mainstream:** "Casts the widest net. It's a safe taste." Understanding it "can unlock scale".
- **Cultural:** "You can study cultural taste, you can serve it, amplify it, but you can't claim it if you didn't live it."
- **Counter:** "developed through conviction, the willingness to reject what everyone else wants".
- **Elite:** "any of those judgments in which the criteria is gatekept by pure access or privilege".
- **Commercial:** "a little flavor of aspiration mixed with something familiar and inviting can be leveraged to deliver a message that resonates with a specific audience".

The working question: "your taste doesn't matter if you can't make it palatable to others. And that depends on the audience. Whose taste?" LinkedIn: "Your superpower is understanding the matrix of tastes and discerning how to cater to them." ([D] S 2026-05-01, LI 034)

On Gap, March 12, 2026: "A brand's unique taste is refined from consistent decisions over time." ([D] S 2026-03-12)

### Curators
"there is a shortcut find trusted curators for music i haven't put in the years the way i have with visuals". Taste is "not something you inherit. You have to acquire it." The long way is years of intentional consumption. Why take it: "So, you can cook." ([D] TOT, S 2026-05-08)

### Going to the source
"you click the source link you find the actual photographer or director behind it you look at their full portfolio not just the one image the algorithm surface to you you read their notes". Then find their rep. A rep's site holds a roster of artists and an image archive "you have to dig for", with non-algorithmic search. Sites shown on screen: ba-reps.com, prettybird.co, artandcommerce.com. ([D] TOT; [D:vis] IRIS)

The payoff: "this is where your mood board stops being a sort of decorative reference and starts being something you can actually execute because you know who can execute each of those visuals". ([D] TOT)

### Mood board method in brief
- "the biggest misconception about mood boards is that you're finished once you pull in reference images that's just gathering". ([D] MOOD)
- Filter: "if I can't answer why an image is there it doesn't make the cut". Three questions: does it contribute to the vision, does its texture or lighting reinforce the tone, does it show a specific ingredient.
- Test of a finished board: "something that makes the board feel like it was made by one person with one intention".
- Correct a reference before you drop it. His case: a fluorescent yellow jacket on a board of earthy greens, recoloured to olive in Photoshop.
- Add one unifying layer over every image, grain or a colour adjustment, kept subtle.
- Lay it out "like a movie": a close-up, a wide, textures, with colour and texture spread evenly.
- "put your client hat on and think is anything going to be misinterpreted".
- Add a short write-up (section 1).
- The through line "is usually color. Uh not always, but it's often color." ([D] `video/visuals-you-can-t-find-on-pinterest.md`)

The retrieval index holds the Photoshop steps and the reference tools.

---

## 6. Portfolio

### The premise
"The hard truth is that employers won't hire what they can't see". "your portfolio can be completely fake and that's okay everyone understands that". "Showcasing how you think should be 50% of this 50% of your effort and your energy". Rubric slide: "Each project has a strong idea + strong craft". ([D] PORT, AD26; [D:vis] PORT frames)

### The rubric
He shows this project type table in the portfolio video. ([D:vis] PORT frames)

| Project type | Count | What it proves, in the table's words |
|---|---|---|
| 360 Campaign | 1-2 | "Show that you can concept big, strategic ideas and show how they come to life across channels." "Show that your idea 'has legs'." |
| Passion Project | 1-2 | "You have creative energy and personal style, even without a client or prompt. Show who YOU are outside of advertising." |
| Craft or Design-focused Project | 1 | "this is your opportunity to get obsessive. Show you have a strong eye for craft". "Should still have a conceptual idea behind it". |
| Experimental / Non-traditional | 1 (optional) | "You think beyond the brief. Formats, mediums, or tech used in surprising ways." |
| Social / Content | 1 (optional) | "Show that you are a master of the hook. You can make ideas native to social". |
| Stunt / Cultural Response | 1 (optional) | "Ideally do something for real that garners attention." "Show that you can move fast". |

Total: "in total ideally you have four to six strong projects no weak projects they can all be spec they can all be fake". "it's better to have four good projects than six okay projects". He allows seven to ten for a longer career. How firm the passion and craft slots are changed: "not optional" in 2025, "preferably" in 2026. ([D] AD26, PIVOT)

Each project gets one idea and one job: "each piece has a single strong idea not a dozen different disperate ideas". "This is the project I show that I can think really big This is the project that I show that I have these craft skills". Each should take a few different ingredients from the menu. ([D] PORT)

### The project page
Project Checklist slide, seven lines: Brand; Big Idea Title/Name; Keyvisual or Lockup (optional); Overview/Description; Insight + Idea; 4-6+ touchpoints/executions; "Between touchpoints, include some of your thinking. How it all works together." Page order: key visual or lockup, brand and idea title, hero executions, further executions. "this is kind of the order of thought process where we're emphasizing the idea". ([D:vis] PORT frames; [D] PORT)

### Case-study writing
- The overview: "Some people like to literally label this is my inside this is my idea but you don't have to do that I don't always recommend that Just talk about your project and and what the concept is Emphasize the why". The insight and idea must be provable "whether you label it overtly or not". ([D] PORT)
- STAR for the body: "situation s situation T task a actions and then R results". Situation and task can be bundled. Results "don't have to be metrics"; awards and press count. He adds: "you don't have to follow star and this exact framework for everything I sure I don't at all". ([D] LIVE)
- Between touchpoints, label the channel and say "how does this tie in to the overarching concept". ([D] PORT)
- State your role: "super helpful anytime you can say this is what I did". ([D] LIVE)
- Show process: mood, early iterations, stills from a film so nobody has to watch it. ([D] PORT, LIVE)
- Cut what says nothing: "if there's something that you're doing on there that's like not communicating anything just cut it out". ([D] LIVE)

### The site
Work first: "the number one thing is just making sure your work is the first thing people can access". Do not split the site by discipline: creative directors "just don't know what you are and they don't know if you know what you are". Keep text off photos and video, a rule he learned at Amazon. "The website itself should almost be a portfolio piece". ([D] LIVE, PORT)

### Passion projects
"passion projects aren't branded at all they show your craft your thinking things you care about". Make it a project: "give it a name give it like a logo make it a project make it like a thing with like a beginning and end". "you take it as far as you possibly can". Put them on the front page. ([D] PIVOT, PASSION, LIVE)

### What he praises and what he fixes: the 28 critiques
Pass 1 holds 28 critique entries: 18 from one livestream of nine sites (LIVE), 5 from the passion-project episode, 1 from AD25 and 4 student campaigns from PORT and ADT. He warns: "I am not necessarily the most critical person" and "I don't want you to take everything I say as scripture". Ten of the 28 are praise with no fix. The counts below are mine. ([I], from [D] entries in LIVE, PASSION, PORT, AD25)

**Fixes, most frequent first.**

| Fix | Entries | Who |
|---|---|---|
| Say plainly what you are and what you do | 5 | Elena, Now or New, Tonichi, Scott (move "senior art director" to the top), his own site |
| The concept is not visible; only craft shows | 4 | Tonichi (positioning, jewellery rebrand, Tim Hortons), Gibson Hall (no work shown at all) |
| No key visual, or the thumbnail hides the idea | 3 | Michael Orfanos (site, GWM Tank 500), Jairo Obando (Qdoba) |
| No tag saying what each project was | 3 | Dima, Elena, Tonichi |
| Copy-driven, no visual concept | 2 | Rachel Holmes (Coppertone, and his summary on Kodak) |
| Passion project sits too low | 2 | Scott (the card game Dirt), Taylor Dahl (grandpa's photos) |
| No personal brand or logo | 2 | Scott, his own site |
| Observation passed off as insight | 1 | Rachel Holmes (Coppertone) |
| Discipline tabs | 1 | Rachel Holmes |
| Text over dark or moving images | 1 | Dima |
| Curate down, then add more surprising spec work | 1 | Tonichi (Toyota) |

His own closing summary: "you really got to Showcase what is the idea and why is that idea interesting". To Tonichi: "If you can get paid for your ideas you'll do really well as an art director but if you're only relying on your craft it's a lot harder." ([D] LIVE)

**What he praises.** Personality and surprise, in 7 entries: Michael's floating profile picture and "I also like bread"; Scott's "clocked in and clocked out"; Tonichi's bio photo; Nick Stokes's illustrations; Jessica Sugerman's small surprises; Brad's TV-set thumbnails; Josh King's conker. A clear idea line or description, in 4: Coppertone's "it sucks to get roasted", Qdoba's description, Zillow's "Decrypting Realtor Code", the Tank pairing. A borrowed genre as art direction, in 2: Qdoba's propaganda posters, Dollar Shave Club's horror posters. The site treated as a project, in 2: Taylor Dahl, Brad. Showing process, in 2: Ian Hagen, Scott. Pass 1 writes "Sugarman" and "Jared Omond"; Sugerman and Jairo Obando are the corrected names. ([I], from [D] entries in LIVE, PASSION, PORT)

### How creative directors review
- They skim: "that's what a lot of creative directors are doing right off the bat is you know just skimming the thumbnail seeing like is there anything that that's really jumping out at me". "I'm not even like reading all the text". He gives no time figure. ([D] LIVE)
- The routine: glance at the front page, jump to the about page, then go deep on the work. "I want to put a face to the person behind the work". ([D] PASSION)
- A recruiter at Wieden+Kennedy London told his student tour she hired Josh King for "a conquer that looks like ET", a conker he had put in his book as a project. ([D] AD25)
- "No one cares where you went to school in the creative industry." ([D] S 2026-04-17)
- "the only thing that matters is what you can do and I have to be able to see what you can do". ([D] LIVE)

---

## 7. Career and business

### His path
| Dates | Role | Source |
|---|---|---|
| 2016 to 2018 | BYU AdLab, content creator and creative director. No formal design training. | [G] `site/about.md`; [D] `blog/toolbox-articles-how-i-started-the-art-director-toolbox.md` |
| May 2018 to March 2021 | Energy BBDO, Chicago. Started as a junior art director at $55,000, left as senior art director. Mars and SC Johnson. | [D] EP4; [G] `site/about.md` |
| April to December 2021 | Huge, Atlanta. Senior Art Director on Brooks Running at $110,000. | [D] EP4; [G] `site/about.md` |
| January 2022 to January 31, 2025 | Amazon Brand Innovation Lab, New York. Associate Creative Director. "I doubled my salary just going to Amazon". | [D] EP4, LI 124; [G] `site/about.md` |
| January 2025 on | Swet Studio, owner. "And now I'm a 100% independent creative, freelance AD, and content creator!" | [D] LI 124 |
| August to October 2025 | OK COOL, Head of Creative, two-month contract. | [G] `site/about.md`; [D] DREAM |

He gave notice on January 21, 2025. Reasons he gives: seven years on "other people's dreams", a five-day office mandate, a flattened org with no creative director rung, content that was working, and his son. "money is not the thing that makes me happy at all In fact my last year was the most I've ever made". ([D] EP4, DREAM)

### The route in without ad school
The Art Director Roadmap is a free FigJam on Gumroad. Five steps on the board: Learn the Craft; Learn to Think Conceptually (insights, big ideas, the Idea Sizing Chart); Make spec ads and campaigns, and passion projects; Make a portfolio; Apply for internships or junior roles. "I don't want to gatekeep the art direction career at all so I'm trying to put out as much as possible so that you could do it on your own". ([G] `products/gumroad-agitc.md`; [D:vis] `frames/visual-maps.md`; [D] AD26)

Free programs he lists: ONE School, The Work Shop, Goodby Silverstein & Partners' portfolio program, The One Club's portfolio reviews and Young Ones. ([D] AD25)

How to apply: search LinkedIn posts for the role keywords and message the copywriter, art director or producer who posted, because recruiters are buried. Before you message anyone: "Become a student of their work! Read what they've already shared." ([D] EP4, LI 056)

His bootcamp claim: "you are literally 30 days away from having a portfolio that is an art director portfolio". He gives no duration for doing the free roadmap alone. ([D] AD26)

### Agency, in-house, freelance
- **Agency:** $55,000 to start in Chicago, raises of about $10,000, hours "9 to 9". Title outruns salary, so people move. ([D] EP4)
- **In-house tech:** "they can be hard to get into but they pay so much better than they did at ad agencies". ([D] EP4)
- **Freelance:** agencies "bring contractors in to fill spots to kind of like fill headcount", for one week to two months. He treats it as plan B at an ACD-level rate. ([D] EP4)
- **Title:** "I would honestly look more at the rate that you can comfortably charge and then draw a line over what would the title be that would get me that rate". ([D] EP4)
- **2026 view:** "art direction is going to be one of the most in- demand skills of 2026 despite the fact that the advertising industry and ad agency model seems to be crumbling". Demand moves to in-house teams, creators and freelancers. ([D] AD26)

Agency, then in-house, then solo is the path he took from 2018 to 2025. Reading it as a rule for others is NotebookLM's. ([D] DREAM; [M])

### Business model and prices
Three parts, which he calls the Creative Empire after his Notion dashboard: the studio, The Toolbox, personal content. "doing personal content has helped build the toolbox and bring a little bit of a creative Community together it also um provides leads". Three months after quitting, sponsored content was "my biggest income stream". The Toolbox is "primarily a free resource for the industry." ([D] EP2, S 2025-05-06)

| Product | Price | Source |
|---|---|---|
| Art Director Roadmap (FigJam) | free | [G] `products/gumroad-agitc.md` |
| NEXT Art Director, self-paced course | $599 | [G] `products/mad-next-art-director.md` |
| NEXT Art Director, four-week live bootcamp | $1,199 | [G] same |
| MAD Decks Vol 001, four deck templates with Taylor Dahl | $57 | [D] MAD 2026-09-15 |
| The Toolbox OS (Notion) | $29 on Gumroad; "regular $40" in a 2024 email | [G] `products/gumroad-thetoolboxos.md`, `newsletter/2024-09-05-…` |
| The Toolbox Database | regular $10 | [G] `newsletter/2024-09-05-…` |
| The Lazy Creator Blueprint | $79 on the wait list, $150 to $200 planned | [D] BLUEPRINT |
| TheToolbox.art, Social Comps Master Deck | free | [G] `products/gumroad-store.md` |

The bootcamp runs four weeks: Art Direction Foundations; Concepts & Big Ideas; Craft & Execution; Polish & Pitch. Over 130 students had taken it by June 30, 2026. His sponsors include Musicbed, Framer, Adobe and ManyChat. Pricing rule: "price it at a price where you could potentially subcontract it out". ([D] AD26, EP2; [G] `products/mad-next-art-director-copy.md`)

### His AI position, by date
- **September 17, 2022.** "ai is shortening the path between vision and execution between ideas and making those ideas until eventually ai continues to evolve and those two sides meet in the middle". The art director sits in that middle. Two ways out: "get insanely good at storytelling and having that big picture vision or you've really got to take this ai stuff seriously". ([D] AI22)
- **March 3, 2025.** "so much of my use of AI is like mockups that never see the light of day". On Pentagram's Midjourney icons: "you clearly could have hired an illustrator or an artist". ([D] `video/how-content-became-this-designer-s-escape-plan.md`)
- **March 24, 2026.** Taste as the only moat is "a little naive"; vision is stronger. ([D] LI 055)
- **July 2026.** He praises Polaroid's "A.I. CAN'T GENERATE SAND BETWEEN YOUR TOES." campaign for its ingredients. The headline is Polaroid's argument. ([D] MAD 2026-07-06)

The claim that he says AI makes taste "the moat" is NotebookLM moving a 2022 idea into 2026 and adding a word he disputes. ([M])

---

## 8. Content

### The blueprint in brief
From a walk through his unreleased Lazy Creator course, February 2025. ([D] BLUEPRINT)

- "if the idea of the video is strong it's going to carry a lot of the weight for you".
- "your content is a tool not your Masterpiece".
- "secret to being consistent isn't discipline it's lowering the bar".
- Six idea prompts: share a counterintuitive truth; unpack a hidden insight; teach a skill in one sentence; expose a common mistake; leverage career or creative insights; share a tool or shortcut. Start with the last two.
- Length: 30 to 45 seconds, "aim for 70 to 90 words".
- Script word for word. Talk to camera. One repeatable spot, a window or a $15 to $30 light.
- Edit by removing: "remove the dead air tighten the pacing".

He treats content like a campaign: "I want an insight behind the content And I think about my series and pillars like ad campaigns". ([D] ADT)

### Hooks
"a hook is what grabs and holds your attention the the emphasis here is on grabbing and holding because just like an actual fishing hook it's not enough to just startle a fish you want to hold it". ([D] HOOK)

**Five attributes of a great hook:** sparks curiosity; reframes something familiar; instantly understandable; hits a nerve (funny, curious or emotional); "aligned with the story's idea otherwise you're going to grab someone's attention but there's nothing to hold on to". ([D] HOOK)

**Three parts on a reel:** a title that triggers emotion or curiosity; a visual that signals who it is for; a first spoken line. ([D] HOOK; [D:vis] HOOK frames)

**Formulas:** ask a surprising question; state a counterintuitive truth; expose a common mistake; make a bold claim. "your hook should be clear not clever". ([D] BLUEPRINT)

**Limits:** "creating great hooks is an art form it's not going to be a complete science you can't always steal the exact framework of others". The failure he names is the gimmick that startles and does not pull you in. "great ideas come from great insights and great ideas will in turn be great hooks". ([D] HOOK)

### Finishing projects
"make the end of your timeline the finish line no other criteria make the end of your guaranteed available time the finish line". Three bad finish lines: when it is perfect, when it meets my standards, when it is 500 pages long. If the time is not guaranteed, "adjust your project Ambitions the scope of your project". ([D] FINISH)

Shrink the unit: "a doodle not a painting a comic strip not a graphic novel a short GIF or GIF not an animated film a short story not a book". "most of these projects can be repeated over and over in order to then be packaged up as a larger more impressive looking portfolio piece". His proof is the artist who posted daily: "the Finish Line was midnight every single day". ([D] FINISH)

---

## 9. Decision rules

48 checks for judging a piece of work the way Jason does, each with the file where he says it.

**Concept**

1. Is there an insight, and does it read "People think X, but the reality is Y"? ([D] S 2026-06-16)
2. Does it sound "counterintuitive, uncomfortable, or like a contradiction at first"? ([D:vis] AD26 frames)
3. Is it an observation? Ask why until a motive shows. ([D] LIVE)
4. Does the idea have a verb? ([D] ADT, S 2026-06-16)
5. Does the idea have a name? ([D] PORT)
6. Does it have legs: many executions under it? ([D] AD25)
7. Is it an idea or one execution, the sneaker in Times Square? ([D] AD25)
8. Where does it sit on the Idea Sizing Chart? ([D:vis] AD26 frames)
9. Big means scale; judge quality separately. ([D] S 2026-06-16)
10. Is it Simple & Clear, Emotional, Campaignable, Brand-Ownable? ([D:vis] AD26 frames)
11. "execution doesn't matter if you're executing a dumb idea". ([D] AD25)

**Craft**

12. Which two or three ingredients stand out? More than three means no restraint. ([D] ADT)
13. Does each ingredient serve the idea and help you feel the insight? ([D] ADT)
14. Is the message carried by copy (left) or by the picture (right)? Either is fine; know which. ([D] ADT)
15. Right side: could endless subjects be slotted in? ([D] ADT)
16. Right side: does a viewer have to pause to decode it? Then it failed. ([D] MAD 2026-04-08)
17. Right side: is the copy a button, or is it see-say? ([D] ADT, S 2026-03-25)
18. Left side: reset it in Helvetica. What is lost? ([D] ADT)
19. Can one ingredient live in a poster and in a room? ([D] ADT)
20. Is there a key visual that tells the idea in one image? ([D] LIVE)
21. Does the lockup show the idea, or only the brand's logo? ([D] LIVE)
22. Can you give a reason for every choice? ([D] MAD 2026-07-06)
23. Can you describe the look in words? ([D] S 2025-03-17)
24. Hero states the idea, vignettes apply it, the rest borrow the look. Which tier is this piece? ([D] S 2026-06-16)
25. Problem to technique: too obvious, figure-ground reversal; means nothing, genre quotation; too literal, form substitution. ([D] S 2026-09-30)
26. Does the audience know the source you are quoting? ([D] MAD 2026-09-28)
27. Did you trace the reference back past the campaign everyone saw? ([D] MAD 2026-02-17)

**Taste and reference**

28. Why did I save that, do I actually like it, what about it do I like? ([D] TOT)
29. Can you name the ingredient, or only the feeling? ([D] TOT)
30. Whose taste are you serving? ([D] S 2026-05-01)
31. Mood board: "if I can't answer why an image is there it doesn't make the cut". ([D] MOOD)
32. Mood board: does it look made "by one person with one intention"? ([D] MOOD)
33. Mood board: do you know who can execute each image? ([D] TOT)
34. Mood board: will the client misread anything? ([D] MOOD)

**Portfolio**

35. Four to six strong projects, no weak ones. In doubt, improve it or cut it. ([D] AD26, PIVOT)
36. Does each project prove a different thing? ([D] PORT)
37. Does the thumbnail tell the idea? ([D] LIVE)
38. Is the insight and idea provable in the overview, labelled or not? ([D] PORT)
39. At least four touchpoints, with your thinking between them. ([D:vis] PORT frames)
40. Is the work the first thing on the site? ([D] LIVE)
41. Does the site say plainly what you are? ([D] LIVE)
42. Are there discipline tabs? Fold them in or cut them. ([D] LIVE)
43. Is any text sitting over a photo or video? Separate them. ([D] LIVE)
44. Is it showing craft with no concept? ([D] LIVE)
45. Could it have been done for real? ([D] PIVOT, LIVE)

**Content and finishing**

46. Is the hook "clear not clever"? ([D] BLUEPRINT)
47. Is the hook aligned with the idea, so there is something to hold? ([D] HOOK)
48. Is the finish line the end of guaranteed time? ([D] FINISH)

---

## 10. What is not his

| Idea | Owner | Marker and source |
|---|---|---|
| "It only qualifies as a platform if it fits on a Post-It note." | Luke Sullivan | [X:Luke Sullivan]; [D:vis] AD26 frames. Jason: "like he says here". |
| "It starts talking and won't shut up." | Luke Sullivan | [X:Luke Sullivan]; [D:vis] AD26 frames |
| "A platform is a world, a world with its own rules."; "Truth + Conflict = Platform." | Luke Sullivan | [X:Luke Sullivan]; [D:vis] AD26 frames |
| "Insights are unspoken human truths. They help us see ourselves and the world around us in new ways." | Mark Pollard | [X:Mark Pollard]; [D:vis] PIVOT frames |
| Write the observation "more savage"; the Santo Domingo example | Mark Pollard | [X:Mark Pollard]; [D] PIVOT |
| Start from the most startling fact | Mark Pollard, citing Edward Bernays | [X:Mark Pollard]; [D:vis] PIVOT frames |
| "the edge of madness"; a portfolio should be polarising; pour out ideas without judging | Jason Bagley | [X:Jason Bagley]; [D] AD25, PASSION, QA26 |
| Designer as "the architect of clarity", art director as "the creative anarchist"; maximum effect versus maximum impact; Swiss precision versus jazz | Sir John Hegarty | [X:John Hegarty]; [D:vis] AD26 frames |
| Do not make spec ads for Apple | relayed advice from other people's videos | [D] AD25 ("there's advice like") |
| "one of the best strategies is to lower the stakes" | Rick Rubin, *The Creative Act* | [X:Rick Rubin]; [D] FINISH |
| The sabbatical every seven years; "a prison of your own success" | guest Jason Gold; the sabbatical is Stefan Sagmeister's | [D:guest:Jason Gold] `video/becoming-a-freelance-creative-director-the-toolbox-podcast-ep-3.md` |
| Pentagram versus Smith & Diction; the six-month runway; Framer proposals | guest Edward Sun | [D:guest:Edward Sun] `video/how-content-became-this-designer-s-escape-plan.md` |
| Flash, lenses, shot lists and photographer references | guest Garrett King | [D:guest:Garrett King] `video/building-creative-influence-as-a-photography-creator.md` |
| "minimum like five to seven things"; "people hire you based off of who you are" | guest Taylor Dahl | [D:guest:Taylor Dahl] PASSION |
| "handmade means 'someone gave a damn.'" | Stefan Szary, in Jason's newsletter | [D:guest:Stefan Szary] MAD 2026-03-12 |
| The Odyssey score and practical effects | Ken Westrick, in Jason's newsletter | [D:guest:Ken Westrick] MAD 2026-08-04 |
| Decide the work, find who makes it, study them, build spec, then message | Aisha Hakim | [X:Aisha Hakim]; [D] LI 056 |
| Cut30 short-form method | Oren John and co-founders | [X:Oren John] `mentioned/people/cut-30-founders.md` |
| Trend looks: Distorted + Wide Angle, Scrapbook / Scanner, Future Medieval | Stills trend report | [X:Stills]; MAD 2026-02-06 |
| "has legs"; "matching luggage"; "book"; "swipe" | advertising slang he uses | [D] AD25, PIVOT |
| "visual pantry"; "active taste"; "The 50/50 Rule"; "Centipede Test"; "Ask Why Drill"; the five-step insight process | NotebookLM | [M] |

---

## 11. Limits

Full list: `analysis/gap-register.md`. The ones that change answers:

- **Paid lessons are absent.** The bootcamp and course are known by curriculum titles and product pages only. The MAD Decks contents are paid.
- **The Roadmap FigJam is not scraped.** Everything here was read off frames while he screen-shared it.
- **Iris is not public.** 11 of 39 technique names are unread, 6 are low-confidence, the group assignments are inferred from line colour, and most read names have no definition from him.
- **No speaker labels.** Podcast lines are split by context; a few stay unassigned.
- **His campaign readings are his own.** He reverse-engineers insights for Nike, LEGO and Polaroid. Years and agencies are `[G]` from `mentioned/campaigns/`.
- **Nothing on interviews, day rates or salary negotiation.** He never states a freelance rate.
- **No rule for choosing photography against illustration or CG, no image count for a mood board, no time figure for how long a reviewer looks.**
- **Instagram reels are not scraped.**
- **Two positions shifted and he has not reconciled them:** which brand to pick for spec (2025 against August 2026), and literal against metaphorical (March against April 2026).
- **Procreate, gear and animation tutorials** are in the retrieval index, outside this file.
