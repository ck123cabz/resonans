---
type: corpus
aliases: ["Retrieval Index — Numbers"]
corpus: rian-doris
layer: analysis
tags: [kairos, machine, psychology]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Retrieval Index — Numbers

Every figure in the corpus, with its unit, what it governs, the protocol it belongs to, and the
q-file it came from. Grep the figure or the thing it measures. One file answers "how much
L-theanine" without loading the physiology file.

Rules this file obeys, from Pass 2:

- Nothing is rounded or approximated. Ranges stay ranges, and a figure given in two units keeps both.
- Where the corpus states two values for one quantity, each value gets its own row and the "What it
  governs" column carries `⚠ conflicts`. Nine quantities are in that state (Pass 2 §3.4) and no
  winner was picked.
- `⚠ variant` marks a smaller divergence Pass 2 did not log as one of the nine: a second worked
  example, a rule stated at two intensities, a figure with two readings.
- `[D] ⚠ no source` marks a figure attributed to nobody anywhere in 44,047 words, q59's citation
  map included (Pass 2 §1.2). Seven of these exist.
- Four protocols are named for a number that appears nowhere in their content. They sit in the
  excluded section at the bottom and appear in no table above it.

Provenance: `[D]` Doris in his own voice · `[G]` backed by his own outcome · `[M:name]` attributed
to an outside authority · `[A]` a stated absence.

---

## Goals and planning

| Figure | What it governs | Protocol | Source | Provenance |
|---|---|---|---|---|
| 1 to 5 years | how long a High Hard Goal takes to achieve | Goal Stack | q01, q04, q60 | [D] |
| 7 levels: Purpose → High Hard Goals → Annual → Quarterly → Monthly → Weekly → Daily | depth of the goal hierarchy | Goal Stack | q01, q60 | [D] |
| 90 days per quarterly goal | milestone length between annual and monthly | Goal Stack | q01, q04 | [D] |
| $10M company in 3 years → $1M revenue plus initial funding in year one | worked example of reverse-engineering an annual goal | Goal Stack | q01 | [D] |
| 40 customer interviews in month 1 | worked example of a monthly goal | Goal Stack | q01 | [D] |
| 50 potential interviewees identified | worked example of a weekly goal | Goal Stack | q01 | [D] |
| maximum 3 goal-directed actions per week | weekly action cap ⚠ conflicts | Goal Stack, Goal Flywheel | q01, q04, q11, q16, q60 | [D] |
| 3 to 5 weekly actions overall | weekly action cap ⚠ conflicts, stated in the same file that caps goal-directed actions at 3 | Goal Flywheel | q02 | [D] |
| maximum 3 specific tasks per day | daily task cap ⚠ conflicts | Do Only 3 Things A Day | q01, q04, q16 | [D] |
| maximum 1 to 3 tasks per day | daily task cap ⚠ conflicts | Power Down Ritual, Goal-Directed Architecture | q03, q04 | [D] |
| 90 minutes, once a week, Sunday evening | weekly planning session length and slot | Goal Flywheel | q02, q11, q60 | [D] |
| 15 minutes of the 90 | time spent reviewing the goal hierarchy in step 1 | Goal Flywheel | q02, q04 | [D] |
| 5% of effort creates 95% of progress | the power-law claim behind action selection | Goal Flywheel, Do Only 3 Things A Day | q02, q16 | [D] |
| 10 to 30 minutes | Power Down Ritual length ⚠ conflicts | Power Down Ritual | q03 | [D] |
| exactly 10 minutes | Power Down Ritual length ⚠ conflicts, attached to planning specifically | Goal-Directed Architecture | q04 | [D] |
| about 30 minutes | Power Down Ritual length ⚠ conflicts | Power Down Ritual | q04 | [D] |
| 6 to 18 months | Certainty Window length ⚠ conflicts, macro scale | Certainty Windows | q05, q56, q60 | [D] |
| 10 to 30 minutes | Certainty Window length ⚠ conflicts, micro scale, identical term | Minimum Viable Certainty | q06, q33, q38, q41 | [D] |
| 5 to 10 years → 3 years → 18 months | the shrink ladder for finding your own window length | Certainty Windows | q05 | [D] |
| exactly 120 seconds | assessment step before committing to a micro mission | Minimum Viable Certainty | q06, q33 | [D] |
| start at 10 minutes, work up to 15 to 30 minutes | micro certainty-window block length | Minimum Viable Certainty | q06 | [D] |
| 90 seconds to clear a room | the Navy SEAL bounded-objective example | Minimum Viable Certainty | q06 | [M:NavySEALs] |
| 30-year horizon, or out to age 80 | how far to stretch the timeline when picking one pursuit | Temporal Audit | q04, q60 | [D] |
| 10 to 100 times longer than intuition expects | how long true compounding takes, against linearity bias | Defeating Dispersion | q04 | [D] |
| 20% more effort for exponential return, against an 80% good-enough threshold | which tasks to optimise and which to stop at | Optimization vs Good Enough | q60 | [D] |
| once every 5 years | deployment cadence for the extreme year | One-Year Decade | q11, q60 | [D] |

## Time and scheduling

| Figure | What it governs | Protocol | Source | Provenance |
|---|---|---|---|---|
| 3 to 6 hours | daily deep-flow capacity ⚠ conflicts, "the upper limit for most people" | One Moment Workday | q10, q60 | [D] |
| 5 to 6 hours | daily deep-flow capacity ⚠ conflicts, "the absolute human biological limit" | four-stage flow cycle, Energy Arbitrage | q39, q42 | [D] |
| 7 to 8 hours daily, sustained 12 months | daily deep-flow capacity ⚠ conflicts | One-Year Decade | q11 | [D] |
| 11 hours in one day | daily deep-flow capacity ⚠ conflicts | One-Month Day | q09 | [D] |
| 1 to 3 hours | morning flow block length ⚠ conflicts | Wake Up and Flow | q14, q15 | [D] |
| 2 to 3 hours | morning flow block length ⚠ conflicts, stated as the pre-phone threshold | Flow Before Phone | q08, q18 | [D] |
| 11 hours of flow blocks (3 + 3 + 2 + 3) against 4 hours of in-day recovery | schedule arithmetic of the sprint day | One-Month Day | q09 | [D] |
| ~30 days of average knowledge-worker output, stated as ~46 hours of real work | the compression claim; his own arithmetic, no study offered | One-Month Day | q09 | [D] |
| 11 hours × 400% = 44 hours, against an average worker's 2.3 hours of real work a day | the same claim restated with different arithmetic ⚠ variant | One-Month Day | q60 | [D] |
| once a month (Acceleration) · once a week (Turbo) · 5 consecutive days once a quarter (Light Speed) | cadence modes, against the protocol's own "intentionally unsustainable" framing | One-Month Day | q09 | [D] |
| 5:00 am wake | the chronotype the published schedule assumes; a later type shifts the whole day forward | One-Month Day | q09 | [D] |
| 20% to 30% | baseline work efficiency of the average person | One Moment Workday | q10 | [D] |
| 90% or more | target work efficiency | One Moment Workday | q10, q60 | [D] |
| 14-hour day yielding 4 hours of real work = 28% | the Zurich worked example, which is also his own internship | One Moment Workday | q10, q57 | [G] |
| 5-hour window yielding 4 hours 50 minutes = 96.7% | the Hawaii worked example | One Moment Workday | q10 | [G] |
| 4 to 5 hours of real work → set a 3-hour block; 5 to 6 hours → set a 4-hour block | how to size your own compressed block | One Moment Workday | q10 | [D] |
| 8-hour day cut to 4 hours | Work Compression worked example | Work Compression | q16 | [D] |
| 400% to 500% productivity increase | claimed effect of compressing hours through scarcity tunnelling; restates the McKinsey figure with no separate basis | Work Compression | q56 | [D] |
| 12 months | duration of the compressed year | One-Year Decade | q11, q60 | [D] |
| 30 days of preparation | prep phase before the year starts | One-Year Decade | q11, q60 | [D] |
| first 6 weeks flawless | the strict-start window, sitting on the habit-automaticity curve | One-Year Decade | q11, q60 | [D], curve [M:Lally] |
| 4:30 am wake, zero caffeine, total isolation | his own three extreme guidelines for the year | One-Year Decade | q11 | [G] |
| 60 to 90 seconds from opening your eyes | how fast to be executing the day's top task | Wake Up and Flow | q14, q15, q30, q39 | [D] |
| 15-minute increments, tracked 24/7 including sleep | logging granularity | Temporal Architect | q12 | [D] |
| exactly 10 minutes at the end of an 8-hour workday | how long the retroactive log takes | 10-Minute Rule | q32 | [D] |
| $1,000/hr · $100/hr · $10/hr | the three work-task value tiers | Temporal Architect | q12, q60 | [D] |
| 50% flow · 25% execution · 25% off · 0% junk | target time allocation, the Workplace Olympian | Temporal Architect | q12, q60 | [D] |
| 50% execution · 40% junk · 0% flow · 10% off | the Hustler archetype | Temporal Architect | q12, q60 | [D] |
| 60% junk · 0% flow · 10% execution · 30% off | the Sloth archetype | Temporal Architect | q12, q60 | [D] |
| shrink by at least 25% | any meeting you cannot cancel | Calendar Choke Points | q13 | [D] |
| 15 to 30 minutes | the size of obligation that fragments a day | Calendar Choke Points | q13, q55, q60 | [D] |
| one 30-minute meeting | enough to create a choke point on its own | Calendar Choke Points | q39 | [D] |
| up to 70% of meetings | the share he calls unnecessary | Schedule Repair | q30 | [D] |
| 3 to 4 choke-point-free days per 10-day period; 3 to 5 in a row for "the real magic" | immersion target | Immersion Runway | q13, q60 | [D] |
| first 3 hours of every day | time reserved for the single business constraint | Scaling Blocker Protocol (3-Hour Rule) | q37 | [D] |
| 3, 6 or 18 months | how long breaking through a scaling blocker takes | Scaling Blocker Protocol | q37 | [D] |
| 14 days at 50% to 100% more output | duration and intensity | Temporary Overengagement | q60 | [D] |
| 14-hour days for 5 days | his own instance of it, during the thesis-removal scare | Temporary Overengagement | q57 | [G] |
| midpoint 3:30 am or earlier, roughly 10% of the population | Lark definition and share | Chronotypes | q42 | [M:Pink] |
| midpoint 3:30 am to 5:30 am, roughly 50% to 55% | Third Bird definition and share | Chronotypes | q42 | [M:Pink] |
| midpoint 5:30 am or later, roughly 25% | Owl definition and share; the three shares total 85–90%, not 100% | Chronotypes | q42 | [M:Pink] |
| natural sleep 1:00 am to 9:00 am → midpoint 5:00 am | worked example of the midpoint method | Chronotypes | q42 | [M:Pink] |
| ~4:00 or 5:00 am to 8:00 or 9:00 am | Lark peak window | Energy Arbitrage | q42 | [D] |
| ~8:00 am to 11:00 am | Third Bird peak window | Energy Arbitrage | q42 | [D] |
| ~4:00 pm to 9:00 pm | Owl peak window | Energy Arbitrage | q42 | [D] |
| ~8 hours after waking | when the trough hits Larks and Third Birds | Energy Arbitrage | q42 | [D] |
| ~3:00 pm | the Third Bird afternoon trough, used for task allocation and for meal timing | Energy Arbitrage, brain-fog protocol | q42, q44 | [D] |
| dip ~11:00 am, second wave 2:00 pm to 4:00 pm, full wind-down 4:30 pm | Lark secondary rhythm | Energy Arbitrage | q42 | [D] |
| wake ~10:00 am, peripheral tasks ~noon, massive evening peak | Owl rhythm | Energy Arbitrage | q42 | [D] |
| 1 hour in the chronotype zone = 4 hours in the trough (4:1) | the entire case for protecting the peak window | Energy Arbitrage | q42, q56 | [D] ⚠ no source; he states it is not peer-reviewed, only "in our experience having worked with thousands and thousands of clients" |

## Attention and load

| Figure | What it governs | Protocol | Source | Provenance |
|---|---|---|---|---|
| 23 minutes 15 seconds | time to refocus after one interruption | Attention Recovery | q24, q30, q41, q55, q59 | [M:Mark] |
| detect drift within 3 seconds, recover within 30 seconds | the trained replacement targets | Attention Recovery (Boomerang Brain) | q24, q30 | [D] |
| 30 to 50 reps per 10-minute meditation | expected wander-and-return count | Attention Recovery | q24, q55 | [D] |
| a 10-minute rabbit hole shrinks to a 10-second glance | the stated end state, with no training timeline given | Attention Recovery | q24 | [D], timeline [A] |
| 4 to 7 items | working-memory limit ⚠ conflicts | Cognitive Load Dump | q17, q22, q59 | [M:Sweller] |
| 7 plus or minus 2 items | working-memory limit ⚠ conflicts, both values appear inside q59 | Cognitive Load Dump, the Flow No | q55, q59 | [M:Miller] |
| 10 minutes, then 3 to 5 minutes more after you feel empty | brain dump duration | Cognitive Load Dump | q17, q22 | [D] |
| under 2 minutes | do-it-now threshold when sorting the dump | Cognitive Load Dump | q17, q22 | [D] |
| 100% down to 20% to 30% | claimed mental RAM before and after the dump | Cognitive Load Dump | q17 | [D] |
| inhale 3 seconds, hold 2 seconds, exhale 10 seconds | the breath ratio | Flow State Breath (3-2-10) | q17, q22, q24, q30, q33, q46, q55 | [D] |
| 3 breaths | reps in the Cognitive Load Dump reset and the certainty-window reset | Flow State Breath | q17, q22, q33 | [D] |
| 3 rounds, stated as 9 total breaths | reps in the arousal-matching version ⚠ variant; "round" is never defined, so this reads either as 9 breath cycles (3 rounds of 3) or as 3 cycles labelled 9 breaths | Flow State Breath | q46 | [D] |
| 30 to 90 minutes of pull work | window before re-testing a return to push work | Salience Swap | q23, q60 | [D] |
| same sentence read 3 times, same email opened twice | the diagnostic counts for preoccupation | Salience Swap | q23 | [D] |
| 24 hours − 8 hours of sleep = 16 waking hours | the fixed equation the audit runs on | Life Maintenance Audit | q25 | [D] |
| 1 to 10 scale, cutoff 7 | autotelic value scoring; anything below 7 is flagged for elimination | Life Maintenance Audit | q25, q36 | [D] |
| every 6 months | audit repeat interval | Life Maintenance Audit | q25 | [D] |
| 5 scenarios | how many recurring decisions to convert into standing rules | Decision Recycling | q27 | [D] |
| alarm at exactly 7:30 am · always fly direct · socialise only on Wednesday nights | his worked examples of a recycled decision | Decision Recycling | q27, q60 | [D] |
| 5:00 am wake, exactly one pipe | the Kant example of a fully preset routine | Decision Autopilot | q27 | [M:Kant] |
| 1 hour to multiple days or weeks | incubation period, scaling with the size of the decision | DMN Method | q26 | [D] |
| 90% of decisions | share that do not need to be made immediately | DMN Method | q26 | [D] |
| 48 hours or more | minimum incubation he recommends | DMN Method | q26 | [D] |
| 1 to 2 minutes of writing | how long extraction takes before the answer pours out | DMN Method | q26 | [D] |
| 3 to 5 sentences maximum | script length for an avoided conversation | Social Rumination Purge | q38, q54, q55 | [D] |
| 2 to 3 hours before touching the phone | phone threshold, level 1 of 3 ⚠ variant, thresholds escalate across sources | Flow Before Phone | q08, q18, q56 | [D] |
| no phone until 12:00 pm | phone threshold, level 2 of 3 ⚠ variant | Phone Off Till Noon | q18 | [D] |
| flight mode from workday start to finish | phone threshold, level 3 of 3 ⚠ variant | Flight Mode to Finish Line | q60 | [D] |

## Motivation and dopamine

| Figure | What it governs | Protocol | Source | Provenance |
|---|---|---|---|---|
| work 45 minutes, break 5 minutes | the working cycle | Boring Breaks | q31 | [D] |
| 5 minutes | boring break length ⚠ conflicts | Boring Breaks | q31 | [D] |
| 1 to 10 minutes | boring break length ⚠ conflicts | Boring Breaks, inside the One-Month Day | q09, q60 | [D] |
| 5 to 10 minutes | boring break length ⚠ conflicts, as the Release step of the cycle | four-stage flow cycle | q39, q41 | [D] |
| a 20-minute nap | boring break length ⚠ conflicts, permitted in the same file that mandates 5 minutes | Boring Breaks | q31 | [D] |
| 50% to 70% drop in dopaminergic neuron firing | what happens when an outcome stops being uncertain | Defeating Dispersion, explore/exploit | q04, q37 | [D] ⚠ no source |
| 1 to 10 per motivator, +5 points a year, 50 total | scoring the five intrinsic motivators up to a maximum | intrinsic motivation scoring | q32 | [D] |
| 5 motivators: curiosity · mastery · autotelicity · purpose · autonomy | the full list | intrinsic motivation scoring | q32, q37 | [D] |
| 3 times per week for at least 6 months | dose for a high-flow hobby redirecting the novelty craving | Scaling Blocker Protocol | q37 | [D] |
| 2 to 3 books per week | the strategic-learning route for the same craving | Scaling Blocker Protocol | q37 | [D] |

## Discipline and habits

| Figure | What it governs | Protocol | Source | Provenance |
|---|---|---|---|---|
| an 8 or 9 out of 10 day | the test a candidate habit has to pass | Domino Habit | q35 | [D] |
| maximum 6 alarms a day | the cap; more than six makes the system too complex to adhere to | Temporal Landmarks | q34, q35, q60 | [D] |
| 5:00 pm work finishes · 6:00 pm finish eating · 8:00 AM reboot routine · 8:30 pm ready for bed · 9:00 pm in bed · 5:30 am wake | the full six-alarm example ⚠ variant; "8:00 AM" sits inside an evening sequence and is near-certainly a typo for 8:00 pm, preserved verbatim | Temporal Landmarks | q35 | [D] |
| 6:00 pm finish eating · 8:00 pm start winding down · 8:30 pm in bed · 5:30 am wake | the same example with different times ⚠ variant | Temporal Landmarks | q34 | [D] |
| 5:30 am wake and dive straight into flow | the worked Domino Habit | Domino Habit | q34, q35, q60 | [D] |
| reading for 60 minutes | one of the four qualifying-habit examples | Domino Habit | q35 | [D] |
| a tax return in 1 hour instead of a week | time-bounding a too-boring task upward | challenge-skills tuning | q30, q38 | [D] |
| 250 cold calls a day | the scale of task the "lower the hurdle" fix was built against | challenge-skills tuning | q30, q57 | [G] |

## Flow mechanics

| Figure | What it governs | Protocol | Source | Provenance |
|---|---|---|---|---|
| 14 triggers = 5 psychological + 4 environmental + 5 social | the complete trigger inventory as taught | flow triggers | q38 | [M:Kotler] |
| 4% above current skill level | where to set task difficulty | challenge-skills balance | q08, q16, q30, q38, q40 | [D] ⚠ no source; no measurement method and no account of how anyone detects 4%. The surrounding construct is [M:Csikszentmihalyi] |
| 4 stages: Struggle → Release → Flow → Recovery | the cycle | four-stage flow cycle | q29, q39 | [M:Kotler] |
| 5 steps, with Engage placed in front of Struggle | his own addition on top of the borrowed cycle | flow entry sequence | q41 | Engage [D], rest [M:Kotler] |
| ~15 minutes of sustained slogging | how long the struggle phase takes to push past naturally | four-stage flow cycle | q39 | [M:Kotler] |
| a few seconds up to a 5-to-10-minute break | Release phase length | four-stage flow cycle | q39, q41 | [M:Kotler] |
| 90 minutes to 4 hours | typical flow block length | four-stage flow cycle | q39 | [D] |
| up to 23 minutes to regain focus | the cost of breaking the struggle phase | four-stage flow cycle | q41 | [M:Mark] |
| 4 quadrants: Apathy · Boredom · Anxiety · Flow | the challenge-skills self-diagnostic | flow channel | q40 | [M:Csikszentmihalyi] |
| 10x or 100x current load, or the same goal in 1/10th the time | the Overload step | Exploding the Flow Channel | q04, q40, q56 | [D] |
| 3 to 6 months | how long to sustain the overload before deloading | Exploding the Flow Channel | q04, q40 | [D] |
| a 1,000% workload increase may cause only a 300% stress increase; after deload it takes 2,000% to feel that again | the stress-ceiling arithmetic | Exploding the Flow Channel | q04, q40 | [D] |
| 10 chapters in one week | worked example of an exponential commitment | High Consequences trigger | q04, q38 | [D] |
| 3 distinct physical work environments in rotation | the Novelty trigger, engineered | flow triggers | q38 | [D] |
| 6 preconditions for team flow: High Skill Integration · Collective Ambition · Open Communication · Psychological Safety · Joint Progress · Group Cohesion and Shared Control | what a leader has to engineer | team flow | q41 | [M:Kotler] |
| 5 social triggers | the same list one item shorter ⚠ variant; q38 omits Joint Progress | flow triggers | q38 | [M:Kotler] |
| 7 team-flow triggers, only 2 of them named | the cited count against what the corpus actually enumerates | team flow | q59 | [M:vandenHout] |
| 4 blockers: mismatched skill levels · failing to fire fast · the Musician Trap · poor role definition | team flow failure modes | team flow | q41 | [D] |
| 6 burnout triggers, none enumerated | the cited count against what the corpus enumerates | burnout | q59 | [M:Maslach] |

## Sleep

| Figure | What it governs | Protocol | Source | Provenance |
|---|---|---|---|---|
| 7 to 9 hours | sleep before a sprint day, and the night end of the recovery range | High Flow Sleep | q09, q39 | [D] |
| 1 to 2 hours of deep sleep, more than 2 hours of REM | nightly requirement for flow proneness | High Flow Sleep | q45 | [D] |
| 9 hours in bed for 8 hours of sleep | how to size the sleep container | High Flow Sleep | q45 | [D] |
| bedtime 11:00 pm, strict wake alarm 8:00 am | worked example of the container | High Flow Sleep | q45 | [D] |
| 33 decibels | noise level that already triggers cortical arousals | High Flow Sleep (Deaf) | q45 | [D] |
| 5 times more melatonin suppression | white LED lighting measured against incandescent | High Flow Sleep (Blind) | q45 | [D] |
| 2 hours | phone-free window before bed | High Flow Sleep (Blind) | q45 | [D] |
| at least 1,000 lux | direct morning sunlight to the eyes, to start the circadian clock | High Flow Sleep | q45 | [D] |
| 15 to 19°C (60 to 67°F) | bedroom temperature | High Flow Sleep (Cold) | q45 | [D] |
| exactly 4 hours before sleep | when to finish eating | High Flow Sleep (Hungry) | q45 | [D] |
| at least 10 hours before bed | alcohol cutoff, alongside the same cutoff for caffeine | High Flow Sleep | q45 | [D] |
| HRV at or above your 30-day average | the go/no-go check before a sprint day | One-Month Day, allostatic load | q09, q48 | [D] |

## Nutrition and fasting

| Figure | What it governs | Protocol | Source | Provenance |
|---|---|---|---|---|
| 4 to 12 hours of eating per 24-hour cycle | the feeding-window range, fasting the other 12 to 20 | Chrononutrition | q43 | [D] |
| 6 hours eating, 18 hours fasted | the recommended compression | Chrononutrition | q43, q44 | [D] |
| 16:8, finish eating at 8:00 pm and break the fast at noon | the common starting protocol | Chrononutrition | q43 | [D] |
| 24 hours, once a week, dinner to dinner | the weekly fast | Chrononutrition | q43, q44 | [D] |
| 48 hours, twice a month | the monthly fast | Chrononutrition | q43, q44 | [D] |
| ~12,000 calories a month | what the two 48-hour fasts remove, assuming a 3,000 calorie/day baseline | Chrononutrition | q43 | [D] |
| fasted from waking until midday | the daytime rule | brain-fog protocol | q44 | [D] |
| 3 litres of water | the fasting cocktail, water component | brain-fog protocol | q44 | [D] |
| 3 to 5 apples | the plate-of-apples flow meal | Chrononutrition | q43 | [D] |
| 10,000 steps a day | step target for staying lean enough for clear cognition | Chrononutrition | q44, q59 | [M:JournalOfObesity] |
| a carnivore meal of steak or fish | his own flow meal, claimed to hold fasted-state cognition with no midday crash | Chrononutrition | q44, q60 | [D] ⚠ no source; he states it is a sample of one |
| 8 tiny meals a day of canned tuna, raw veggies or dry grilled chicken | the bodybuilding-forum regime from his teens that produced the binge loop | biography | q57 | [G] |
| 16 full-sugar Cokes a day | the never-drink-calories anecdote | Chrononutrition | q60 | [D] |

## Stimulants and supplements

| Figure | What it governs | Protocol | Source | Provenance |
|---|---|---|---|---|
| 100mg caffeine : 200mg L-theanine (2:1) | the standing pairing, never caffeine alone | Caffeine Commandments | q09, q43, q47 | [D] |
| 100 mg | caffeine baseline dose, about one regular cup of coffee | Caffeine Commandments | q43, q47 | [D] |
| 50 mg | caffeine floor, if 100 mg is too much | Caffeine Commandments | q47 | [D] |
| 300 mg | caffeine ceiling, the maximum sweet spot | Caffeine Commandments | q43, q47 | [D] |
| 100 to 200 mg | caffeine dose taken while fasted | brain-fog protocol | q43, q44 | [D] |
| 200 to 400 mg | L-theanine dose range | brain-fog protocol, Chrononutrition | q43, q44 | [D] |
| +50% on your normal dose | the Fatigue Multiplier, for rare instances only, never to cover poor sleep | Caffeine Commandments | q47 | [D] |
| at least 30 minutes after waking | the wake delay, letting natural cortisol wake you first | Caffeine Commandments | q47 | [M:Huberman] |
| from the moment of waking | caffeine timing ⚠ variant; the brain-fog protocol takes it immediately, head-on against the wake delay | brain-fog protocol | q44 | [D] |
| 2 cups of water for every cup of coffee | the hydration rule | Caffeine Commandments | q47 | [D] |
| at least 10 hours before bed | caffeine cutoff; a 10:00 pm bedtime puts it at midday | Caffeine Commandments | q45, q47 | [D] |
| 1 day off a week, plus 1 full week off a quarter | the tolerance reset | Caffeine Commandments (caffeine wash) | q47 | [D] |
| ~1 mg nicotine | dose for a pick-me-up | supplements inventory | q43, q60 | [D] |
| a 4-shot Americano | the largest single coffee dose named anywhere in the corpus | Chrononutrition | q43 | [D] |
| zero caffeine for 12 months | his own One-Year Decade guideline | One-Year Decade | q11 | [G] |
| no dose given | magnesium citrate, CBD, apigenin, salt/electrolytes, B-vitamins, taurine, ginseng, greens powders, prebiotics, probiotics: named in the inventory with no quantity anywhere | supplements inventory | q43, q60 | [A] |

## Environment and workspace

| Figure | What it governs | Protocol | Source | Provenance |
|---|---|---|---|---|
| 21 to 25°C (69.8 to 77°F) | workspace temperature | Flow Dojo | q20 | [D] |
| up to 40% of productive time | claimed cost of context switching from disruptions | Flow Dojo, phone rules | q20 | [D] ⚠ no source |
| 50% standing / 25% walking / 25% sitting | claimed ideal positional ratio for flow | Flow Dojo (positional variance) | q60 | [D] ⚠ no source |
| 3 hours less sitting a day = 2 years of life expectancy | the case for positional variance | Flow Dojo | q60 | [D] ⚠ no source; stated as fact, no study, no controls |
| 6 design principles | suppression is active · anchoring bias · physiology of focus · eliminate friction · deter disruptions · condition the space | Flow Dojo | q20, q60 | [D] |
| 1 laptop, shut, plus 1 large monitor on adjustable arms | the screen setup | Flow Dojo | q20 | [D] |
| monitor's neutral middle at natural eye level | screen height | Flow Dojo | q20 | [D] |
| 0 to 4 apps visible | home-screen allowance | phone and device setup | q19 | [D] |
| 5:00 am to noon · 90 minutes before bed · 24 hours a day 7 days a week | recurring blocker session options | phone and device setup (Freedom) | q19 | [D] |
| no prices, brands or model numbers | the equipment list is generic apart from Moleskine and Apple | Flow Dojo | q20 | [A] |

## Recovery cadence

| Figure | What it governs | Protocol | Source | Provenance |
|---|---|---|---|---|
| 1 hour every day | daily active recovery: breathwork, sauna, cold plunge or a walk in nature | active recovery cadence | q48 | [D] |
| 1 full day every week | weekly, stacking protocols back to back | active recovery cadence | q48 | [D] |
| 3 days every month | monthly, ideally with a full digital detox | active recovery cadence | q48 | [D] |
| 10 days every quarter (one week plus two weekends) | quarterly reset | active recovery cadence | q48 | [D] |
| 2 weeks every year | annual reboot | active recovery cadence | q48 | [D] |
| 10 to 20 minutes | in-day active recovery break, the short end of the recovery range | four-stage flow cycle | q39 | [D] |
| 4 hours of in-day recovery | what the sprint day schedules against its 11 hours of blocks | One-Month Day | q09 | [D] |
| 4-7-8 | the named breathwork pattern in the active-recovery list | active recovery | q48 | [D] |
| HRV, no target value given | the objective measure of allostatic load | active recovery | q48 | [D], target [A] |
| 8:00 pm hard stop | when work ends on the sprint day, to give the glymphatic system its window | One-Month Day | q09 | [D] |

## Leverage and business

| Figure | What it governs | Protocol | Source | Provenance |
|---|---|---|---|---|
| 5 hours a week for 4 weeks = 20 hours | dose for real working proficiency in one new skill | Five for Four | q17, q50, q51, q53 | [D] |
| 1 hour/day across 5 weekdays · one 5-hour Saturday block · 5 hours/day for 4 days straight | the three permitted splits | Five for Four | q50, q51, q53 | [D] |
| done at least twice | the repetition threshold that triggers building a system | Process Leverage | q17, q50 | [D] |
| at least 1 new process a month | build rate | Process Leverage | q50 | [D] |
| 500 hours a year | claimed saving from automating repetitive work | Process Leverage | q50 | [D] |
| 5 years of struggle collapsed into 6 months | claimed effect of finding the one right person | People Leverage | q50 | [D] |
| 1 to 4 weeks | Leverage Sprint duration | Leverage Sprint | q17, q50, q51 | [D] |
| +30% to 50% total working hours | Leverage Sprint intensity | Leverage Sprint | q17, q50, q51 | [D] |
| at least 70% of those hours | share spent strictly on building people, process and proficiency leverage | Leverage Sprint | q17, q50, q51 | [D] |
| 3 vectors: Proficiency · Process · People | the trifecta | Leverage Trifecta | q17, q50, q56 | [D] |
| Eliminate → Automate → Delegate | the strict order of the hierarchy | Hierarchy of Leverage | q50 | [D] |
| 3 mock sales calls plus a follow-up email | Discovery Project for a salesperson | hiring | q52 | [D] |
| a 30-day plan to halve customer acquisition cost | Discovery Project for a marketing leader | hiring | q52 | [D] |
| 1-day project → 1-month period → full-time offer | the sequence for six-figure roles | hiring | q52 | [D] |
| up to $30,000 in cash | referral bonus for a senior role, paid only after the hire stays 3 months | hiring | q52, q58 | [D], amount [G] |
| $5 million run rate in under a year | FRC year-one revenue ⚠ conflicts | Flow Research Collective | q58 | [G] |
| 8-figure run rate within 12 months | FRC year-one revenue ⚠ conflicts, same file | Flow Research Collective | q58 | [G] |
| 3 years of singular focus | time to the 8-figure organisation before he allowed other projects | Flow Research Collective | q58 | [G] |
| 18 months | college student to CEO leading nearly 50 people | Flow Research Collective | q58 | [G] |
| ~$500,000 a month | payroll burden at the 50-person mark | Flow Research Collective | q58 | [G] |
| 60+ people, ~2,400 hours of work per week | later headcount and logged hours | Flow Research Collective | q58 | [G] |
| 15,000+ entrepreneurs and executives | customers trained, against an earlier "tens of thousands" in the same file ⚠ variant | Flow Research Collective | q58 | [G] |
| 16-hour workdays turned into 3-to-6-hour days | the claimed client result | Flow Research Collective | q58 | [D] |
| age 22 or 23 | how old he was at the co-founding; both readings appear ⚠ variant | Flow Research Collective | q58 | [G] |
| $600 a day, 8 hours a day, 80 days straight | the ice cream cart ceiling that taught him leverage | biography (Irish Ices) | q57 | [G] |
| 250 calls a day, 16 hours a day | the cold-calling period in Ireland | biography | q30, q57 | [G] |
| 50% of earnings spent on Uber rides | the LA internship | biography | q57 | [G] |
| six figures on a domain name, 400-person parties | hypomanic spending, the corpus's best-grounded warning | Stop Drop and Roll | q49, q58 | [G] |
| a 100-foot water slide at 13, a year mostly bedbound, 6 years debilitated | the injury behind the whole brain-fog material | biography | q57 | [G] |
| half a thesis written and submitted by 11:30 pm | the One-Month Day he actually ran, in New York | One-Month Day | q57 | [G] |

## Citation statistics

Every figure here is Doris quoting somebody else. None of them arrives with a study design, sample
size, paper title or link anywhere in 44,047 words. The corpus supports "he cites X". It does not
support asserting X.

| Figure | What it governs | Protocol | Source | Provenance |
|---|---|---|---|---|
| up to 500% | claimed productivity increase in flow | One-Month Day, Leverage Trifecta | q17, q59 | [M:McKinsey] |
| 490% to 500% | claimed increase in learning and skill-acquisition speed | Leverage Sprint, One-Month Day | q17, q59 | [M:DARPA] |
| up to 430% | claimed increase in creativity | Leverage Trifecta | q59 | [M:Sydney] |
| 96 times a day | claimed phone-check frequency | Phone Off Till Noon | q59 | [M:Asurion] |
| $650 billion a year | claimed cost of unnecessary interruptions to US businesses | Phone Off Till Noon | q59 | [M:Basex] |
| 400 billion bits/sec subconscious against 40 to 50 bits/sec conscious | the throughput claim the entire decision protocol rests on | DMN Method | q26, q28, q59 | [M:UPenn] |
| 40 bits/sec conscious | the same claim with a different conscious figure ⚠ variant | DMN Method | q59 | [M:UPenn] |
| 64% of waking hours | claimed share of waking life with the default mode network active | Upgraded Rumination | q27, q59 | [M:Hamilton] |
| 50,000 sleep patterns tracked over 10 years | the study size behind the chronotype taxonomy | Chronotypes, Energy Arbitrage | q59 | [M:Roenneberg] |
| 23 minutes 15 seconds, UC Irvine, 2004 | the only headline figure carrying both a year and an institution; the figure itself is indexed under attention and load | Attention Recovery | q59 | [M:Mark] |
| 9 of 56 authorities carry a date, 3 name a journal, 0 name a paper | measured citation quality across the whole corpus | citation map | q59 | [A] |

---

## Excluded: video-title figures with no content behind them

Four protocols are named for a number that appears nowhere in their own content. Indexing them
would invent a dosage the corpus never states. The real figure sits alongside each one. Per Pass 2
§3.6 they appear in no table above this line.

| Title figure | Protocol as titled | What the content actually says | Source |
|---|---|---|---|
| 56 seconds | "Give Me 56 Secs… I'll DELETE Your Procrastination" | **60 to 90 seconds** from opening your eyes to working. No 56-second step, threshold or measurement appears anywhere, and the name is never explained | q30 |
| 58 seconds | "Give Me 58 Secs… I'll REPROGRAM Your Brain" | resolves entirely to the **45/5 Boring Breaks cycle**: work 45 minutes, break 5. No 58-second figure appears | q31 |
| 8 minutes | "How To Get Addicted To Discipline In 8 Minutes" | **nothing in the three-step sequence is timed**, and the total is never stated as eight minutes | q34 |
| 11 minutes | "How To Enter Flow State In 11 Minutes" | verified by re-query on 2026-07-28: **the transcript never states 11 minutes anywhere**. Only **5 to 10 minutes** (the Release step) and **up to 23 minutes** (the refocus cost of breaking struggle) exist | q41 |

## Related

- [[04-resources/thinking-tools/flow.md|Flow]] — Doris puts a number on the challenge-skills balance the flow note describes, setting difficulty just above your current skill.
- [[04-resources/thinking-tools/the-pareto-principle.md|The Pareto Principle]] — Doris states the 80/20 split as 5/95 and uses it to pick which weekly actions to take.
- [[04-resources/thinking-tools/parkinsons-law.md|Parkinson's Law]] — His compression protocols are Parkinson's Law with numbers on them, halving the workday on purpose.
