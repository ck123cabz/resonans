---
type: script
aliases: ["Roast council"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Roast council
speaker: Nate Herk
provenance: D
sources: [q05, q07, q39, q47]
videos: [i-asked-claude-code-to-make-me-as-much-money-as-possible.md, how-to-build-claude-subagents-better-than-99-of-people.md, claude-code-for-non-coders-6-hour-course.md]
---

# Roast council

Nate's `roast` skill: a council of six AI seats that attacks a plan before he builds it. He presents the full version on 2026-06-25. An earlier one-agent version, the "roast my plan" subagent, is from the subagents video and the non-coders course. His stated reason is that models agree with whatever they are shown.

## Why he built it: models agree with you
`[R] · [D] (third-party study) · uploaded 2026-06-25 · i-asked-claude-code-to-make-me-as-much-money-as-possible.md · q47 · stable`

He cites a study called ELEPHANT: models fail to push back on the user's framing about 88% of the time, against about 60% for humans. He adds that researchers at MIT and Penn State found personalization and memory make a model more agreeable over a long conversation. Both are other people's numbers, not his tests.

> there's a study also called elephant which measures exactly this and they found that AI models fail to push back on the way you frame something about 88% of the time and for humans it's around 60% (i-asked-claude-code-to-make-me-as-much-money-as-possible.md)

## The six seats
`[S] · [D] · uploaded 2026-06-25 · i-asked-claude-code-to-make-me-as-much-money-as-possible.md · q39, q47 · stable`

The skill spins up a council that attacks the idea from six angles:
1. Contrarian: finds fatal flaws.
2. Expansionist: looks for the biggest upside.
3. First-principles thinker: no outside context, pure logic.
4. Deep researcher: pulls real market data and competitor pricing off the web.
5. Buyer: role-plays the customer and says whether they would buy.
6. Judge: merges the findings into one verdict.

> you've got a contrarian whose only job is to find fatal flaws we've got an expansionist who's looking for the biggest upside we've got a first principles thinker who's working with no outside context just pure logic (i-asked-claude-code-to-make-me-as-much-money-as-possible.md)

> we've got a deep researcher that actually goes in and pulls out a bunch of real market data and competitor pricing off the web and then we have the buyer (i-asked-claude-code-to-make-me-as-much-money-as-possible.md)

## The judge: green light, reshape or kill, plus a 48-hour test
`[S] · [D] · uploaded 2026-06-25 · i-asked-claude-code-to-make-me-as-much-money-as-possible.md · q07, q39 · stable`

The judge returns one of three verdicts and the cheapest test that fits in two days.

> the judge takes all of those findings and gives you one verdict you basically get green light reshape or kill and it also gives you the single cheapest test that you can run in the next 48 hours (i-asked-claude-code-to-make-me-as-much-money-as-possible.md)

A pasteable prompt built only from those spoken seats. It is our assembly of his words, not a file he showed:

```
Roast this plan. Spin up six seats:
- Contrarian: find fatal flaws.
- Expansionist: find the biggest upside.
- First-principles thinker: no outside context, pure logic.
- Deep researcher: pull real market data and competitor pricing from the web.
- Buyer: role-play the customer and say whether you would buy.
- Judge: merge the findings into one verdict (green light, reshape, or kill) and name the single cheapest test I can run in the next 48 hours.
```

## Roast my plan: the one-subagent version
`[S] · [D] · uploaded 2026-06-09 · how-to-build-claude-subagents-better-than-99-of-people.md · q05, q39 · stable`

Before the council, he made a single critic subagent. His creation prompt, in his own run-on words:

> create me a sub agent that criticizes all of my work i basically want to be able to hand it off ideas and I want it to not agree with me but I want it to um criticize it i want it to roast it (how-to-build-claude-subagents-better-than-99-of-people.md)

> i want it to play devil's advocate and look for every possible hole in the plan and what could go wrong and give me back basically that report i want this thing to be invoked whenever I say roast my plan or review my plan (how-to-build-claude-subagents-better-than-99-of-people.md)

He says the prompt is "pretty concise" and a real use case would want more detail. The same wording appears in claude-code-for-non-coders-6-hour-course.md (2026-07-11).

Warning line: q39's clean version ("Criticize all of my work. Do not agree with me. Play devil's advocate...") tidies his words. Use the caption text above.

## Persona lists that are wrong
`[S] · [M] · no transcript quote · q05, q07, q39, q47 · stable`

Gemini gives several other seat lists. None matches the 2026-06-25 video.
- q07's roast prompt: "a skeptic buyer, a senior engineer, and a contrarian". [M] composite; no caption.
- q39 and q47: five seats with "Target Buyer" and no judge. The seat is "the buyer", and the judge is the sixth.
- q05: Beginner, Software Engineer, Business Owner, Publisher, Executive, Critic. Those look like agent-team debate panels from other videos, not the roast skill.

When any file says four or five seats, the transcript says six.

## Where it sits in his planning order
`[J] · [M] · no transcript quote · q07 · stable`

q07 places the roast after the PRD and before build: plan mode, grill-me, PRD, roast, then build. The six-seat skill is the stress test in that chain. See `script-grill-me-and-95-confidence.md`.
