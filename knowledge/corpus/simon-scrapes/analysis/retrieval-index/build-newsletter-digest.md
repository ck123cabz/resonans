---
type: build
aliases: ["Strategic Newsletter Digest (inbox scout)"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Strategic Newsletter Digest (inbox scout)
provenance: M
lanes: [5, 6]
sources: [q30, q35]
---

# Strategic Newsletter Digest (inbox scout)

Daily pipeline that scans the inbox for AI newsletters and turns the best material into a scored morning digest plus drafted content.

## Pipeline
1. A reusable `tool-gmail` skill (Gmail MCP) scans the last 48-72 hours of inbox for AI newsletters.
2. A "curation brain" splits the newsletters into individual stories and scores each numerically against brand positioning and ICP — an explicit bar, not summarize-everything. In the demo only one item "truly clears the bar," scoring 16 out of 22.5 on the defined metrics; the rest are filtered out.
3. Output: a scannable morning digest of top content ideas and angles.
4. Downstream drafting: the digest chains into marketing copywriting and content repurposing skills, loads the brand voice, and drafts platform-specific content (short LinkedIn post, X thread) from the winning angles.

## Self-optimization
The system suggests adding recognized newsletter senders to a `senders.yaml` so later runs skip the whole-inbox search and save tokens.

## Scheduling
/goal defines done — check all emails, return the idea list, draft posts for the top three — wrapped in a cloud Routine or a local /loop cron firing daily. Full workflow, no human prompting.

## Origin
The component skills were themselves built by an Ultra Code run (the inbox skill builder demo): one agent designed the curation rubric, two parallel build agents made the Gmail tool and the newsletter digest, then integration and an adversarial review pass.
