---
type: build
aliases: ["n8n agent builds and the Claude Code migration"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: n8n agent builds and the Claude Code migration
speaker: Nate Herk
provenance: D
sources: [q08, q09, q10, q38, q41]
videos: [n8n-just-leveled-up-rag-agents-reranking-metadata.md, multi-agent-systems-have-never-been-easier-to-build-n8n-no-code.md, from-zero-to-inbox-agent-full-beginner-s-course-no-code.md, build-sell-n8n-ai-agents-8-hour-course-no-code.md, building-an-ai-agent-swarm-in-n8n-just-got-so-easy.md, how-i-d-learn-n8n-if-i-had-to-start-over-in-2026.md, is-n8n-dead.md, build-anything-with-claude-code-n8n-beginner-s-guide.md, i-tested-openai-s-agentkit-against-n8n-what-you-need-to-know.md]
---

# n8n agent builds and the Claude Code migration

The n8n-era builds, 2025-02 to 2026-01, then the one migration build that moves an n8n workflow behind a Claude Code front end (2026-01-16). n8n titles fall from 32 in 2025-Q2 to 0 in 2026-Q2.

## RAG agent: ingestion and retrieval as two workflows
`[B] · [M] · no single transcript quote · q09 · version-bound`

[M] Gemini's version only; no caption carries this node list.

q09 splits RAG into two n8n workflows. Ingestion: Google Drive or webhook trigger, data loader and text splitter, `text-embedding-3-small` embeddings, insert into Pinecone or a Supabase vector store. Retrieval: chat or Telegram trigger, AI Agent, a vector-store tool with the same embeddings, and a chat model (GPT-4o-mini, Claude 3.5 Sonnet or Gemini Flash in that era).

## Supabase vector store with Postgres chat memory
`[B] · [D] · uploaded 2025-05-23 · build-sell-n8n-ai-agents-8-hour-course-no-code.md · q09 · stable`

Short-term memory goes to a Postgres chat memory node, keyed by the chat session. It writes to a Supabase table the captions call "Naden chat histories" (`n8n_chat_histories`).

> it's going to be storing it in a table in Subabase called Naden chat histories (build-sell-n8n-ai-agents-8-hour-course-no-code.md)

## Reranker: limit 20, keep the top three
`[B] · [D] · uploaded 2025-06-28 · n8n-just-leveled-up-rag-agents-reranking-metadata.md · q09 · version-bound`

He raises the Supabase vector-store limit from the default of 4 to 20 chunks, passes them through a reranker, and keeps the top three. An optional filter keeps only scores over about 0.7. The reranker vendor (Cohere in q09) is not in the captions.

> I gave it a limit of 20 and by default that's four (n8n-just-leveled-up-rag-agents-reranking-metadata.md)

> it will assign a relevant score and then it will grab just the top three most relevant answers and then those top three get fed into the agent (n8n-just-leveled-up-rag-agents-reranking-metadata.md)

## Vector databases are for unstructured text
`[J] · [D] · uploaded 2025-03-05 · 6-months-of-building-ai-agents-in-43-minutes-without-the-hype.md · q09, q48 · stable`

He admits he once put every kind of data into a vector store. q09 turns this into the rule: tables go in Postgres, n8n data tables or Airtable; vector stores hold PDFs, transcripts and policy text.

> I was taking all types of data no matter what it was and I was just chucking it into a vector database (6-months-of-building-ai-agents-in-43-minutes-without-the-hype.md)

## Inbox routing: text classifier into four branches
`[B] · [D] for the classifier; [M] for branch actions · uploaded 2025-10-29 · from-zero-to-inbox-agent-full-beginner-s-course-no-code.md · q09 · stable`

A Gmail trigger feeds a text classifier that reads subject and body. His four categories are customer support, finance and billing, high priority, and promotion. q09 adds the branch actions: support goes to an agent on a Pinecone FAQ that replies in thread; finance gets a label and a Slack or Telegram summary; promotions get marked read. q09 also puts an OpenAI node before the classifier to strip HTML. The branch actions are Gemini's list.

> we're going to do four generic categories which are customer support finance and billing high priority and promotion (from-zero-to-inbox-agent-full-beginner-s-course-no-code.md)

## Voice email assistant
`[B] · [M] · no transcript quote · q09 · version-bound`

[M] Gemini's version only; no caption carries this text.

q09: an ElevenLabs or Vapi webhook calls an n8n AI Agent, which looks up the contact in Sheets or Airtable, sends through a Gmail tool with "From AI" fields, and answers through Respond to Webhook with an audio-friendly line. Closest video: how-i-built-jarvis-with-no-code-tutorial-w-lovable-elevenlabs-n8n.md (2025-03-23).

## Orchestrator agent: the one-line fix for looping children
`[S] · [D] · uploaded 2025-06-10 · multi-agent-systems-have-never-been-easier-to-build-n8n-no-code.md · q09 · stable`

A parent agent routes to child workflows (email, calendar, contacts, research) through "Call n8n Workflow as Tool". q09's test query is "Find 4 YouTube videos, draft an email to Dexter, and schedule a calendar meeting". When the parent kept drafting emails itself, he added one system-prompt line. The verbatim line:

> overview you are an orchestrator agent your only job is to delegate the task to the correct tool no need to write emails or create summaries (multi-agent-systems-have-never-been-easier-to-build-n8n-no-code.md)

q09's wording ("pass the user query to the tool; do not summarize or draft emails yourself") is a paraphrase.

## The 25-tool debugging example
`[J] · [D] · uploaded 2025-06-10 · multi-agent-systems-have-never-been-easier-to-build-n8n-no-code.md · q09 · stable`

His case for child agents is debugging. One agent with 25 tools and a prompt explaining all 25 gives you nowhere to start when it breaks.

> if you tried to give that main agent access to 25 tools and in the prompt you have to say here's when you use all 25 tools and it wasn't working you wouldn't know where to start (multi-agent-systems-have-never-been-easier-to-build-n8n-no-code.md)

Warning line: q09 calls this the "dumb zone". He uses that term only for a full context window.

## Native agent swarm on one canvas
`[B] · [D] · uploaded 2025-07-25 · building-an-ai-agent-swarm-in-n8n-just-got-so-easy.md · q09 · version-bound`

n8n let several agents sit on one canvas without nested sub-workflows. He notes they can share one memory, though his six agents each do one-shot jobs and don't need it. q09's version number "1.103+" is not in the caption.

> what we can do is we can have all six agents hooked up to the same memory in this case I don't just because each of these sub agents jobs are super specific (building-an-ai-agent-swarm-in-n8n-just-got-so-easy.md)

## The 15 core nodes
`[R] · [D] · uploaded 2025-12-10 · how-i-d-learn-n8n-if-i-had-to-start-over-in-2026.md · q34, q09 · stable`

> About 90% of all workflows will rely on the same 15 or so core nodes and most errors fall into the same handful of categories (how-i-d-learn-n8n-if-i-had-to-start-over-in-2026.md)

q09's node table [M]: the triggers, AI Agent, chat model, Text Classifier, Structured Output Parser, Call n8n Workflow as Tool, vector stores, chat memories, Think Tool, Guardrails, Set, Code, Split Out, Aggregate, Merge.

## n8n shortcuts and the sheet backup
`[T] · [M] · no transcript quote · q41 · version-bound`

q41: `=` turns a field into an expression; `P` pins a node's output so tests don't re-fire paid calls; `D` deactivates a node; `Shift+S` adds a sticky note. A daily job clears a Google Sheet and rewrites all rows from an n8n data table as a backup. Unchecked against captions.

## n8n, AgentKit and Base44 verdicts
`[T] · [M] with one [D] · uploaded 2025-10-07 · i-tested-openai-s-agentkit-against-n8n-what-you-need-to-know.md · q38 · version-bound`

q38 [M]: n8n Cloud about $20 to $27 a month, self-hosted free; top pick for beginners, "graduated" for his own work. AgentKit suits simple OpenAI chat widgets and won't kill n8n. Base44 costs $20 a month for 100 credits. The "Canva" line is Sam Altman's, read out by Nate:

> here's a quote from Sam Alman saying "Agent Builder is like Canva for building agents (i-tested-openai-s-agentkit-against-n8n-what-you-need-to-know.md)

## The 10-minute rule and "is n8n dead"
`[J] · [D] · uploaded 2026-02-01 · is-n8n-dead.md · q41, q47 · stable`

Full entry in `framework-other-named-methods.md`. He answers a Plus-community post by saying the tools are "just fundamentally different", and keeps n8n for anything he can build there in 10 minutes or less.

> my 10-minute rule is basically if I have a use case and I could build it in 10 minutes or less in Nit I'm just going to do it there (is-n8n-dead.md)

## Migration build: n8n back end, Claude Code front end
`[B] · [D] · uploaded 2026-01-16 · build-anything-with-claude-code-n8n-beginner-s-guide.md · q10 · stable`

One build, one video. The n8n workflow stays as the back end. Steps as shown:
1. Install the n8n MCP server and n8n skills in Claude Code, so it can read node configs and workflow patterns.
2. Claude Code audits the workflow and makes it app-ready: the form trigger becomes a webhook, and the photo input, which now arrives as a base64 string, gets converted.
3. Claude Code builds the front end that calls the webhook.
4. Deploy to Vercel; his demo ran at a `.vercel.app` domain (a fitness coach app).

> cloud code having the ability to look at your workflow essentially audit it to make sure it's ready to go for an app and then make any of the changes ... before you build the front end (build-anything-with-claude-code-n8n-beginner-s-guide.md)

> cloud code actually realize that it's going to come through as a base 64 string when we send it over web hook and it has to convert that (build-anything-with-claude-code-n8n-beginner-s-guide.md)

Warning line: q12's version (move credentials into a root `.env` first, rebuild steps as `/tools/` scripts, deploy to Trigger.dev, Modal or a VPS) has no caption source. q10's "30+ steps" and "hundreds of nodes" break points are not spoken either.

## Bike to motorcycle
`[J] · [D] · uploaded 2026-01-25 · agentic-workflows-just-changed-ai-automation-forever-claude-code.md · q10, q47 · stable`

His answer to students who fear n8n was wasted time: n8n taught balance, Claude Code is the motorcycle. No training wheels in this analogy; those belong to his separate bike method for skills.

> learning to ride a bike i've got balance i know how to steer i know how to pedal but now we're going to be hopping on to like a motorcycle where we don't have to pedal (agentic-workflows-just-changed-ai-automation-forever-claude-code.md)
