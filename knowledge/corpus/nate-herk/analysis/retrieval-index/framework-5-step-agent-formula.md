---
type: framework
aliases: ["5-step AI agent formula"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: 5-step AI agent formula
speaker: Nate Herk
provenance: D
sources: [q36, q37, q50]
videos: [my-proven-ai-agent-formula-explained.md]
---

# 5-step AI agent formula

Nate Herk's Era 1 method for building agents in n8n, from the video "My Proven AI Agent Formula (Explained)", uploaded 2025-05-05. He calls it his "five-step AI agent playbook". The steps are foundations, high-ROI opportunities, process mapping, workflows versus agents, and proof of concept with guardrails. Pass 1 logged it as never defined (gap A-05); the transcript defines it, and the gap is closed.

## The claim attached to it
`[F] · [D] · uploaded 2025-05-05 · my-proven-ai-agent-formula-explained.md · q36, q50 · stable`

> these are the five steps i always use when building ai agents and they've helped me generate over $240,000 in the past 6 months (my-proven-ai-agent-formula-explained.md)

The $240,000 is his own stated revenue, so it keeps `[D]`. No build list or client names come with it.

## Step 1: Foundations, don't run before you walk
`[F] · [D] · uploaded 2025-05-05 · my-proven-ai-agent-formula-explained.md · q50 · stable`

Learn the basics before agents: how an API call works, HTTP requests, how n8n handles data. He says too many people jump into complex agent systems without knowing how to set up an API call.

> starting with step one is the foundations don't run before you walk i see way too many people trying to jump into a very complex ai agent system but they still don't understand how to set up an api call (my-proven-ai-agent-formula-explained.md)

## Step 2: Identify high-ROI opportunities, four boxes
`[F] · [D] · uploaded 2025-05-05 · my-proven-ai-agent-formula-explained.md · q50 · stable`

A process worth automating ticks four boxes: repetitive, time-consuming, error-prone, scalable. He calls picking the right process "half the battle".

> the second step is actually identifying high roi opportunities so when you're looking for a process that you want to automate it should tick these four boxes which are is it repetitive is it timeconuming is it errorprone and is it scalable (my-proven-ai-agent-formula-explained.md)

## Step 3: Process mapping, the instruction manual
`[F] · [D] · uploaded 2025-05-05 · my-proven-ai-agent-formula-explained.md · q50 · stable`

Before opening n8n, write out every step of the manual process, however small. He calls this the step people skip most.

> our job here in the process mapping step is to build out the instruction manual and that means that we list every single step no matter how small (my-proven-ai-agent-formula-explained.md)

His worked map is a support-email flow: new email received (trigger), check if it is support, route, label the email, send the reply (data destination).

## The five things a process map looks for
`[F] · [D] · uploaded 2025-05-05 · my-proven-ai-agent-formula-explained.md · q50 · stable`

He names five elements that recur in every map: a trigger, data sources, data transformation, a decision point with its criteria, and a data destination. Round 2 (R50-03) confirmed four and could not find "data transformation"; a wider grep in this pass found it, so all five are spoken.

> there's kind of five main things that you're looking out for which is a trigger (my-proven-ai-agent-formula-explained.md)

> we have to do some sort of data transformation (my-proven-ai-agent-formula-explained.md)

> pretty much every process we have some sort of decision point and this helps us identify what do we actually use to make the decision what's the criteria (my-proven-ai-agent-formula-explained.md)

> whatever ends the process which is the data destination (my-proven-ai-agent-formula-explained.md)

## Step 4: Workflows versus AI agents
`[J] · [D] · uploaded 2025-05-05 · my-proven-ai-agent-formula-explained.md · q50 · stable`

Do not force an agent where a fixed sequence does the job. An unneeded agent adds latency, cost and inconsistent output. He points viewers to a separate workflows-versus-agents video.

> never force ai or never force an agent into a process that doesn't actually need it because all you'd be doing is increasing latency increasing the cost and increasing the risk of inconsistent outputs (my-proven-ai-agent-formula-explained.md)

His support-agent example ends with a 7-step workflow that "does the exact same thing as this ai agent over here but it's quicker and cheaper".

## Step 5: Proof of concept and guardrails, three bullets
`[F] · [D] · uploaded 2025-05-05 · my-proven-ai-agent-formula-explained.md · q50 · stable`

He gives three bullets. First, fail fast, debug often: errors come on every new workflow, and a quick path through them gets you to a proof of concept. Second, you don't know what you don't know: edge cases show up only when real users and prompts hit the build. Third, there is no finished product, because new models and new lessons keep changing it.

> the fifth step is about pc proof of concept and guardrails so there are three things that i like to say here the first one is fail fast debug often (my-proven-ai-agent-formula-explained.md)

He closes the step with two lines he still repeats in 2026:

> when it comes to automations predictable is better (my-proven-ai-agent-formula-explained.md)

> when it comes to automations boring is better (my-proven-ai-agent-formula-explained.md)

## Where the formula went next
`[I] · [M] · no transcript · q36 · stable`

The same video plugs "10 Hours to 10 Seconds", his AIS Plus n8n course: 11+ hours on picking the process, mapping the steps, n8n foundations, AI nodes and smarter workflows. Pass 2 lists it as a course. The steps reappear later in other forms: mapping in the 2026-08-01 pricing call, "boring is beautiful" in 9 files, workflows before agents in the golden ratio.

## Warnings: Gemini's spliced quotes
`[A] · [M] · no transcript · q50 · stable`

- R50-02: q50's "verbatim" step-2 quote ends with the step-3 instruction-manual line. Two steps were joined.
- R50-04: q50's step-4 quote ("quicker, cheaper, and better") is stitched from two separate sentences. Use the caption lines above.
- "The 5-Step AI Agent Formula" is Gemini's title. His words are "five-step AI agent playbook" and the video title "My Proven AI Agent Formula".
