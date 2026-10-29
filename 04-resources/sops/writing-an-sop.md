---
type: sop
kind: field
aliases: ["Writing an SOP"]
category: operations
owner: Christian
project: 
pack: knowledge/learning/sop-craft
follower: Sai, first run; an agent through the write-sop skill
mode: read-do
trigger: a task reaches its owner a second time, or goes wrong once
runs: a few times a month
miss-costs: the task stays in one head, and the next person or agent does it wrong
last-updated: 2026-10-20
summary: "How to turn a task into an SOP a person and an agent can both follow cold, from deciding whether it deserves one to the first cold run."
---

# Writing an SOP

**Use this when:** a task reaches you a second time, or a task went wrong once.

**You're done when:** someone who has never done the task followed the SOP with nobody to ask, and
every question they asked is now answered in the text.

> [!info]+ Header
> - **Kind:** field. **Follower:** Sai on a first run, or an agent through the write-sop skill.
> - **Mode:** read-do. **Runs:** a few times a month. **A miss costs:** the task stays in one head, and the next person does it wrong.

> [!quote]+ Source
> The SOP-craft immersion pack, `knowledge/learning/sop-craft/`, above all `judgment.md`. Behind it:
> Degani and Wiener's NASA checklist report (1990), Boorman's checklist rules as Gawande reports them
> (2009), and the field's agency and VA operators (Deiss 2025, Lequiron 2026).

> [!todo]+ When a task reaches you a second time
> **10 min · the task's last run open in front of you**
>
> **Do:** decide whether this task earns an SOP, and who will follow it.
>
> **Why:** Ryan Deiss shut his company for a month to write binders nobody used, and now caps it at
> 10 to 20 SOPs (judgment 1).
>
> **Stuck:** [[knowledge/learning/sop-craft/judgment|SOP-craft judgment]], calls 1 to 3
>
> 1. **Write the task, how often it runs and what a miss costs, on one line.** Because a rare task
>    with a cheap miss costs more to document than to redo. Check: a line like "send the welcome
>    pack · 6 a month · a client waits a day".
> 2. **Pick one: SOP, automate, or nothing.** Because a fixed list of commands belongs in a script.
>    Check: one word written under the line; stop here unless it says "SOP".
> 3. **Name the follower and the failure the SOP guards against.** Check: a line like "Sai, first
>    run · guards against unknown steps".
> 4. **Pick the mode.** Read-do when the follower could not do it without the page, do-confirm when
>    they could. Check: "read-do" or "do-confirm" in the `mode` field.
> 5. **Find the pack for the task's field.** Check: a path under `knowledge/learning/` in the `pack`
>    field.

> [!todo]+ When the person who does the task can walk through it
> **30 min · that person doing one real run, you writing**
>
> **Do:** write the steps while the work happens, never from memory.
>
> **Why:** drafts written by the person who does the work were followed more than drafts written by
> managers (Lequiron 2026, judgment 13), and first drafts written from memory fall apart.
>
> **Stuck:** [[knowledge/learning/sop-craft/incidents|SOP-craft incidents]]
>
> 1. **Copy the template from `04-resources/templates/sop.md` into `04-resources/sops/`.** Check: a
>    new file whose `kind` reads "field".
> 2. **Write each step as the person does it: one exact verb, one exact object.** Check: no step
>    reads "make sure", "clean up", "handle" or "the usual".
> 3. **After each step, write what the screen or record shows when it is right.** Check: every step
>    ends in "Check:" and a value, such as "invoice 1042, $300, in Sent".
> 4. **Add a "because" clause only to a step that looks arbitrary.** Because the reason, not the
>    case's label, tells the follower whether the step applies. Check: each clause is one line.
> 5. **Split the steps at events that happen on every run.** Check: each group is a callout titled
>    "When <event>" with nine steps or fewer.
> 6. **Write the priming block for each group.** Check: each callout opens with time · setting, Do,
>    Why with a source, and Stuck.

> [!todo]+ When the draft has every step
> **20 min · the draft and the checker**
>
> **Do:** close the ways the SOP can fail without anyone noticing.
>
> **Why:** Amazon's 2017 S3 outage and Replit's 2025 deletion were both fixed in the tool, not in the
> text (judgment 12).
>
> **Stuck:** [[knowledge/learning/sop-craft/fights|SOP-craft fights]]
>
> 1. **Write each never-rule with the gate that enforces it.** Check: every Never line holds "Gate:"
>    or "No gate:" and a reason.
> 2. **Write the exits: solve it, escalate to a named person with named facts, or pause and log.**
>    Because the person escalating knows the most at that moment, the escalation carries their
>    recommendation and a note in the record. Check: every escalation names a person, the facts to
>    bring, and the recommendation.
> 3. **Run `scripts/sop_check.py` on the file, or ask Christian to run it.** Check: the file's line
>    prints with no problem lines under it.

> [!todo]+ When the checker prints no problems
> **30 to 60 min · a follower new to the task, you watching**
>
> **Do:** watch someone follow it cold and say nothing.
>
> **Why:** a tester who already knows the work fills the gaps without noticing (judgment 13).
>
> **Stuck:** [[knowledge/learning/sop-craft/roles|SOP-craft roles]], the follower
>
> 1. **Hand the SOP to someone who has never done the task, with nobody to ask.** Check: their name
>    and today's date written in the Runs callout.
> 2. **Write down each question they ask and each place they stop.** Check: the Runs line lists them
>    after "questions:", or reads "questions: none".
> 3. **Answer each question in the text and run it cold again with someone new.** Check: the latest
>    Runs line reads "questions: none".

> [!danger]+ Never
> - **Never count a warm run as the test.** Gate: `scripts/sop_check.py` reads only lines marked cold.
> - **Never write the steps from memory alone, or have an AI write them from nothing.** No gate: the
>   draft has to come from a real run, so the second pause point starts with one.

> [!tip]+ Exits
> - The task changes every week: pause and log the gap in Runs, and write the SOP once it holds still.
> - Nobody who does the task can walk through it: escalate to Christian with the task name and the
>   date it was last done.
> - The field has no pack: escalate to Christian with the field name, so he can run `/immerse`.
> - The cold follower cannot finish: pause and log where they stopped in Runs, then rewrite from the
>   second pause point.

> [!example]+ Worked example
> None yet. The first is due at the 1 Nov Sunday review, when Sai follows a video SOP cold.

> [!warning]+ Where it goes wrong
> - The library outgrows its owner: Chris Jones wrote 250 processes and one software update broke
>   half of them (roles.md).
> - The checks get answered from memory: on Delta 1141 the crew answered in under a second
>   (incidents.md §2).
> - The tester already knows the work, so the gaps never show (judgment 13).

> [!note]+ Runs
> One line per run: `- YYYY-MM-DD · who · cold|warm · questions: none|<asked> · changed: <what>`

> [!note]+ Related
> [[pass-conditions|Pass conditions]] · [[done-conditions|Done conditions]] ·
> [[first-real-use|First real use]]
