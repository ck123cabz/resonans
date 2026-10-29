---
type: corpus
aliases: ["Core Knowledge: Nate Herk"]
corpus: nate-herk
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
---

# Core Knowledge: Nate Herk

**Layer 1 of the nate-herk corpus**, distilled 2026-09-29 from `pass-2-reconciliation.md`, the verify files and `round2.md` in `scratchpads/nate-herk-pass2/`, and `sources.tsv`. Only frameworks `[F]`, rules `[R]` and judgments `[J]`. Builds, scripts and tool profiles go to Layer 2.

**Reading an entry.** Type tag, one provenance marker (the highest grade the evidence allows), the claim, the source in parentheses, volatility.

- `[D]` a caption quote of 40 words or fewer, recorded in a verify file or Pass 2, in Nate's voice. Quotes keep caption spelling: "cloud" or "claw" is Claude, "naden" or "Nit" is n8n, "Soul" is Sol, "Churnney" is Cherny.
- `[D:guest:name]` a guest's words, listed apart in each section and never counted as Nate's position.
- `[G]` an outcome he states about his own build or business, with no caption quote on file.
- `[M]` Gemini's synthesis from a NotebookLM answer (q##), not checked line by line.
- Sources are transcript filenames in `knowledge/corpus/nate-herk/video/` (`.md` dropped) with the YouTube upload date from `sources.tsv`.
- **stable** is a method or principle. **version-bound** is a price, limit, model or feature true on that date.

All numbers are Pass 2's corrected values. Where Gemini's number differs, the entry says so once, so the lens can spot the wrong version.

**Who Nate is.** YouTube educator and former agency owner. He co-founded True Horizon AI and sold it, and runs a free Skool community (AI Automation Society) and a paid one (AIS Plus). On 2026-09-23: "the channel passed a million subscribers my book hit number one and we launched a certification i'm 24". Background: "University of Iowa I got a double major in business analytics and marketing so no formal coding education" (so-you-re-building-ai-agents-now-what, 2025-08-09). His viewers want to sell AI work to businesses, so most technical rules end in a pricing or sales rule.

---

## 1. Claude Code setup and context

### 1.1 claude.md

- `[F]` `[D]` claude.md is the onboarding file: "if Claude Code is an employee then claw.md is their onboarding document" (claude-code-source-code-just-leaked-8-things-you-must-do, 2026-04-01). "System Constitution" and "Master Router" are Gemini's labels. · stable
- `[R]` `[D]` Length cap, three spoken forms: "keep it under 150 lines" (generate-content-for-9-socials-on-autopilot-with-claude-code, 2026-03-17); "claude auto reads it at the start of every single chat as system context so keep it under 200 lines" (18-claude-code-token-hacks-in-18-minutes, 2026-04-02); "between 150 and 200 lines max" (32-tricks-to-level-up-claude-code-in-16-mins, 2026-04-27). · version-bound
- `[R]` `[D]` The 95% rule: "do not make any changes until you have 95% confidence in what you need to build ask me follow-up questions until you reach that confidence level" (18-claude-code-token-hacks-in-18-minutes, 2026-04-02). · stable
- `[R]` `[D]` Applied Learning section, same video: "when Nate has to reexplain or when a workaround is found for a platform tool or limitation add a oneline bullet here keep each bullet under 15 words no explanations". · stable
- `[R]` `[D]` His style lines: "I use bullet points and don't use m dashes and you know use the Oxford comma but then I go into a routing map" (build-sell-with-codex-5-hour-course, 2026-09-21). "TypeScript strict mode" is Anthropic's example, read in the source-leak video, not his rule. · stable
- `[F]` `[M]` Five parts: role line, core rules and style, the 95% rule, a routing map, Applied Learning (q01). The `context/MI.md` routing example is in no caption. · stable
- `[J]` `[M]` claude.md holds operating context and pointers; raw data, full SOPs, API docs and logs go elsewhere (q01, q02). Keep claude.md and agents.md identical so one repo runs in both harnesses (q16). · version-bound

**Not his:** "over 80% of the system prompt" is Anthropic trimming Claude Code's own prompt, asked about in an interview (i-deleted-all-my-claude-skills-and-claude-got-smarter, 2026-08-12).

### 1.2 Context and tokens

- `[R]` `[D]` The 200k-era rule: "compact at around 60% capacity autocompact triggers at like 95% by which point your context is already pretty degraded" (18-claude-code-token-hacks-in-18-minutes, 2026-04-02). Repeated as "Hack number six" on 2026-04-27. · version-bound
- `[R]` `[D]` He explains and replaces it: "when we only had 200,000 tokens in the context window I was basically always clearing and compacting when I got to about 60% which was about 120,000 tokens". On 1M Opus: "I never ever go above like 120k tokens or about 12%" (how-to-never-hit-your-claude-session-limit-again, 2026-04-20). · version-bound
- `[J]` `[D]` Same video: "i don't use /compact at all anymore". Past about 120k he asks for a full summary, runs /clear and pastes it back, later packaged as a session-handoff skill. · version-bound
- `[R]` `[D]` Latest threshold on file: "my best practice is basically if we get past 250,000 300,000 I'm going to do a session handoff" (claude-code-for-non-coders-6-hour-course, 2026-07-11). 1M Opus 4.7 "gets sloppy past you know about 50% capacity" (every-level-of-claude-explained-in-21-minutes, 2026-05-12). · version-bound
- `[J]` `[D]` "it's not a limits problem it's a context hygiene problem" (18-claude-code-token-hacks-in-18-minutes, 2026-04-02). · stable
- `[R]` `[D]` History cost: "message one could be 500 message 30 could be 15,500 which is 31 times more" (same video). · stable
- `[R]` `[D]` Cache: "if you're using Claude via API or sub agents then the TTL or the time to live is only 5 minutes ... for cloud code inside of your terminal ... that's an hour" (give-me-10-mins-and-i-ll-save-you-millions-of-claude-tokens, 2026-05-21). · version-bound
- `[R]` `[D]` MCP overhead: "one server alone might be something like 18,000 tokens per message" (18-claude-code-token-hacks-in-18-minutes, 2026-04-02). Stale that day, by his own dating: "enthropic shipped a feature in january called tool search that auto defers tool loading the moment your mcp overhead crosses 10% of your window so it cuts that overhead by 85%" (every-level-of-claude-explained-in-21-minutes, 2026-05-12). · version-bound
- `[R]` `[D]` Convert before pasting: "for HTML to markdown you're getting like 90% fewer tokens for PDF to markdown you're getting like 65 to 70% tokens reduction for DOCX files to markdown you're getting about 33%" (how-to-never-hit-your-claude-session-limit-again, 2026-04-20). · stable
- `[R]` `[D]` "during the peak hours which are 8 am to 2 p.m eastern time on weekdays" the 5-hour window drains faster (18-claude-code-token-hacks-in-18-minutes, 2026-04-02). That is 8:00 pm to 2:00 am in Manila during US daylight time. Limits doubled on 2026-05-07. · version-bound
- `[J]` `[D]` "boris Churnney the creator of Claude Code starts every single session in plan mode i do the same thing" (how-to-never-hit-your-claude-session-limit-again, 2026-04-20). · stable
- `[J]` `[M]` The other hacks: /clear between tasks, paste the function not the file, press Escape when it wanders, disconnect unused MCP servers, /btw for side questions (q06). · version-bound
- `[R]` `[D]` Other people's numbers, his words: "one developer actually tracked a 100 plus message chat and found that 98.5%" of tokens went to re-reading (18-claude-code-token-hacks-in-18-minutes); "a developer ran an analysis on GitHub of 18,000 thinking blocks across 7,000 sessions" (how-to-never-hit-your-claude-session-limit-again); "one X user" cut tokens 95% with a 383-file wiki (andrej-karpathy-just-10x-d-everyone-s-claude-code, 2026-04-05). None is `[G]`. · version-bound

### 1.3 Skills

- `[F]` `[D]` "the six-step skill building framework so number one is the name and the trigger ... number two is the goal so in one sentence what will this skill accomplish ... number five is the rules think about what could go wrong" (master-95-of-claude-code-skills-in-28-minutes, 2026-02-27). Steps 3, 4 and 6: process, reference files, a self-improvement loop. · stable
- `[F]` `[D]` Step 6 is the bike method: "your skill is never done" (how-to-build-codex-skills-better-than-99-of-people, 2026-09-19). Five files from 2026-04-23. Watch where it tilts, give feedback, have the agent edit its own skill.md, let go by degrees. · stable
- `[R]` `[D]` "keep the skill.md under 500 lines", a docs ceiling he cites, and "front matter is only going to be you know maybe roughly 100 tokens" (master-95-of-claude-code-skills-in-28-minutes, 2026-02-27). · version-bound
- `[J]` `[D]` References inside the skill folder, or "option B is that they're not directly nested right under that skill"; he teaches both (same video). · stable
- `[J]` `[D]` "it's so much easier to run the process get the output and say "Okay let's turn that into a skill."" (build-sell-with-codex-5-hour-course, 2026-09-21). · stable
- `[R]` `[D]` A description states job and trigger: "This skill creates LinkedIn carousels from a topic from a transcript or an outline Use this when the user asks for a carousel carousel slides or a LinkedIn document post." (anthropic-engineer-explains-what-to-build-instead-of-ai-agents, 2026-09-13). · stable
- `[J]` `[D]` "A mechanic might own hundreds of tools but he doesn't dump every single one onto the bench before he starts changing a tire" (same video). · stable
- `[J]` `[D]` "more skills and more system prompts are probably breaking your system", yet he did not sweep-delete, and warns "you can't just take advice you see from Boris Churnney or from some other YouTuber or from me ... and just blanket statement apply it to your work" (i-deleted-all-my-claude-skills-and-claude-got-smarter, 2026-08-12). · version-bound

**Relayed from Anthropic:** progressive disclosure, "something that Enthropic calls progressive disclosure" (Gemini said it came from UX design); a script saved in the skill "as in their own words a tool for its future self" (both anthropic-engineer-explains-what-to-build-instead-of-ai-agents, 2026-09-13); "a capability uplift skill which basically is a prompt" against encoded preference (claude-code-skills-just-got-even-better, 2026-03-05). Test-first skill writing is the Superpowers plugin's doc, read aloud (this-one-plugin-just-10x-d-claude-code, 2026-04-12).

### 1.4 Plan before building

- `[J]` `[M]` Order: plan mode, grill-me interview, PRD or plan.md, roast, then build with the main session as project manager (q07). · stable
- `[F]` `[D]` Six-seat roast council: "a contrarian whose only job is to find fatal flaws ... an expansionist ... a first principles thinker ... a deep researcher ... and then we have the buyer", and a judge who gives "green light reshape or kill and it also gives you the single cheapest test that you can run in the next 48 hours" (i-asked-claude-code-to-make-me-as-much-money-as-possible, 2026-06-25). · stable
- `[J]` `[D]` Why: models agree too easily. He cites ELEPHANT, where models "fail to push back on the way you frame something about 88% of the time and for humans it's around 60%" (same video; third-party). · stable
- `[J]` `[D]` "i want it to not agree with me but I want it to um criticize it i want it to roast it" (claude-code-for-non-coders-6-hour-course, 2026-07-11). · stable

**Relayed:** Matt Pocock's Grill Me, "Interview me relentlessly about every aspect of this plan until we reach a shared understanding" (the-skill-that-10x-d-my-claude-code-projects, 2026-06-04), in 14 files. Sabrina's "Ask me clarifying questions one at a time until you are 95% confident that you can complete the task successfully." (build-sell-with-claude-code-10-hour-course, 2026-03-12).

### 1.5 Integrations and permissions

- `[F]` `[D]` "cli first api endpoints second skills third and mcp only when nothing else fits" (every-level-of-claude-explained-in-21-minutes, 2026-05-12). Gemini dropped the skills tier. · stable
- `[R]` `[D]` Two sources behind it. An unnamed "real benchmark": "mcp used 35 times more tokens than the CLI on the same task and reliability drops from 100% with the CLI to 72% with MCP" (this-is-the-most-powerful-tool-to-give-to-claude-code, 2026-05-09). His reading of Anthropic's docs: "60 to 70% fewer tokens" (every-level-of-claude-explained-in-21-minutes). · version-bound
- `[J]` `[D]` "I created an account called Up AI and now I give my uppai API key to cloud code" (build-sell-claude-code-operating-systems-2-hour-course, 2026-05-01). · stable
- `[J]` `[D]` "give each agent only the credentials and the tools needed for its job" (hermes-agent-zero-to-personal-ai-assistant-1-hour-course, 2026-05-10). · stable
- `[J]` `[D]` "if my AI could touch data or could read data I have to assume that it will even if I never prompt it" (claude-code-for-non-coders-6-hour-course, 2026-07-11). Cole Medin says nearly the same. · stable
- `[J]` `[D]` From his own team's 150,000-email incident: "you can tell your agent never send emails only write drafts but if it still has a send email tool then it can still send", and "if the answer scares you then fix the access not the prompt" (5000-hours-of-building-ai-in-just-17-minutes, 2026-08-04). "Prompts are suggestions, tools are walls" is Gemini's line. · stable
- `[J]` `[D]` He kept bypass mode, fenced by a settings file: "I felt comfortable about it because it could never do anything that was actually risky" (claude-code-for-non-coders-6-hour-course, 2026-07-11). Gemini's "stopped using bypass" is wrong. · version-bound
- `[R]` `[D]` "over 900 servers that have been exposed with no password protection" running Clawdbot (100-hours-testing-clawdbot-vs-claude-code-honest-results, 2026-01-28). · version-bound
- `[R]` `[M]` Keys only in `.env`; never share the /remote-control QR; no unverified plugins or MCP servers; a human approves money, deletions and mass sends (q03, q19, q33). · stable

---

## 2. Agents and the harness

### 2.1 Workflows first

- `[F]` `[D]` "a framework called the wat framework which basically just stands for workflows agent and tools" (agentic-workflows-just-changed-ai-automation-forever-claude-code, 2026-01-25). It "separates concerns so that the probabistic AI handles reasoning while deterministic code actually handles the execution" (build-sell-with-claude-code-10-hour-course, 2026-03-12). 15 files to 2026-07-11. The chef analogy is `[M]` (q03). "Visual Agentic Workflow Framework" has zero caption hits. · stable
- `[R]` `[D]` "if each step is 90% accurate then you're down to 59% success after just five steps" (how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code, 2026-02-07). · stable
- `[J]` `[M]` The agent builds and repairs tools locally; production ships workflow and tools on Modal or Trigger.dev with no agent (q03). · stable
- `[J]` `[D]` "is the order of operations fixed is it predictable if yes you're going to go with an ai workflow" (ai-agents-are-overused-here-s-what-to-build-instead, 2025-12-19). · stable
- `[J]` `[D]` "workflows deterministic workflows beat AI agents nine times out of 10", "boring is beautiful" (build-sell-claude-code-operating-systems-2-hour-course, 2026-05-01); "predictable is beautiful boring is beautiful because you know exactly what's going to happen every single time" (build-sell-with-claude-code-10-hour-course, 2026-03-12). · stable
- `[F]` `[D]` Golden ratio: "60% traditional automation 30% AI assisted and then that last 10% being human touch or human approval" (you-re-doing-ai-automation-wrong-here-s-how-to-fix-it, 2025-10-15; 3 files to 2026-04-18). No "90/10" rule exists in captions. · stable
- `[F]` `[D]` "a vending machine is deterministic you put in a quarter you hit E4 you get a Coke same input same output" (claude-code-for-non-coders-6-hour-course, 2026-07-11; 7 files from 2026-02-27). The 3 M's turn the image negative, "treat AI as a mentor not a vending machine": one use is architecture, the other is prompting habit. · stable
- `[F]` `[D]` Era 1 "five-step AI agent playbook": "step one is the foundations don't run before you walk", "the second step is actually identifying high ROI opportunities", "the third step is process mapping", step four "never force an agent into a process that doesn't actually need it", step five "fail fast debug often". Mapping looks for trigger, decision point, criteria, data destination. Credited with "over $240,000 in the past 6 months" (my-proven-ai-agent-formula-explained, 2025-05-05). · stable
- `[J]` `[D]` "prompting needs to be done reactively i see way too many people doing this proactively" (your-ai-agent-prompts-are-wrong-here-s-the-fix, 2025-02-26; 5 files). Method, `[M]` (q08): empty prompt, one tool, test on real inputs, one sentence per observed mistake. He retired his own prompt generator: "I don't really use that thing anymore" (same video). · stable
- `[J]` `[D]` "I was taking all types of data no matter what it was and I was just chucking it into a vector database" (6-months-of-building-ai-agents-in-43-minutes-without-the-hype, 2025-03-05). Tables for structured data (`[M]`, q09). · stable
- `[J]` `[D]` For a chatty n8n parent: "you are an orchestrator agent your only job is to delegate the task to the correct tool no need to write emails or create summaries". Split tools across children, since with 25 tools "you wouldn't know where to start" debugging (multi-agent-systems-have-never-been-easier-to-build-n8n-no-code, 2025-06-10). · stable

### 2.2 Loops and verification

- `[F]` `[D]` A loop has "two most important pillars": "the goal" and "verification" (finally-agent-loops-clearly-explained, 2026-06-19). Reason-act-observe is how "some people" describe loops, not his framework. · stable
- `[F]` `[D]` /goal lets you "set kind of like an end condition and then you can have Claude keep working" (claude-code-clay-makes-lead-generation-actually-fun, 2026-07-12). · version-bound
- `[J]` `[D]` A working agent has only shown it "worked one time on one output" (5000-hours-of-building-ai-in-just-17-minutes, 2026-08-04). · stable
- `[J]` `[D]` Check the render: "i screenshotted every generated PDF and looked five layout defects found and fixed then reproven on a fresh generation a geometry fit check script now guards all 10 slides" (build-sell-ai-saas-products-2-hour-course, 2026-08-10). The worker never declares itself done (`[M]`, q19). · stable
- `[R]` `[D]` Agent teams: "if you have three sessions running that's basically going to be three times the cost ... I like to stay around maybe two to five agents max" (how-to-build-claude-agent-teams-better-than-99-of-people, 2026-03-23). Gemini's swarms of 40 to 200 and `max_turns=10` are invented. · version-bound
- `[J]` `[M]` Subagent when reads would flood the main chat, a cheaper model fits, tasks are independent, or tools must be restricted; not for one-file edits, dependent chains or debate (q05). · stable

### 2.3 The AI operating system

- `[F]` `[D]` "I call this my four C's of building an effective AI operating system So the four C's are context connections capabilities and cadence" (build-sell-grok-bots-2-hour-course, 2026-08-31). "you have to go in this order 1 2 3 4" (build-sell-claude-code-operating-systems-2-hour-course, 2026-05-01). Capabilities: "you have a bunch of SOPs". Cadence: "you can now turn off your laptop and things will still run". AIOS in 45 files from 2025-09-24; 4 C's in 9 from 2026-05-01. · stable
- `[F]` `[D]` Hermes's five pillars (memory, skills, soul, crons, self-improving loop): "my Hermes agent helped me think of" it (hermes-agent-zero-to-personal-ai-assistant-1-hour-course, 2026-05-10). In the same course: "Claude Code is still my daily driver that's where I do 90% of my knowledge work". · version-bound

### 2.4 Hosting

- `[R]` `[D]` Cloud Routines: "on pro you can have five runs a day on max you can have 15 runs a day and on team and enterprise you can have 25", "minimum scheduled interval which is one hour", "four vCPUs 16 gigs of RAM and 30 gigs of disk space" (how-to-build-24-7-claude-agents-easy, 2026-04-14). · version-bound
- `[R]` `[D]` /loop: "only last for 3 days" (32-tricks-to-level-up-claude-code-in-16-mins, 2026-04-27), then "like seven days" (i-tested-every-claude-code-feature-these-12-are-the-best, 2026-06-03). · version-bound
- `[R]` `[D]` Modal: "five free bucks to start with and if you put in a credit card you'll get an extra 25", about $30 once (claude-code-for-non-coders-6-hour-course). Trigger.dev: schedules every 2 minutes on the free plan, starts can drift "by up to an hour" (the-easiest-way-to-host-your-claude-code-agents, 2026-02-20; how-to-build-gpt-6-astra-automations-that-don-t-eat-your-usage-limit, 2026-09-16). Hostinger KVM 2 "six bucks a month n[ine] bucks", affiliate (100-hours-testing-clawdbot-vs-claude-code-honest-results, 2026-01-28). · version-bound
- `[J]` `[M]` /loop for short desk monitoring; desktop tasks when the laptop stays on; Cloud Routines for full loops with it off; Trigger.dev for frequent schedules and webhooks; Modal for plain Python; a VPS for always-on assistants (q11). · version-bound

### 2.5 n8n after Claude Code

- `[J]` `[D]` "if I have a use case and I could build it in 10 minutes or less in Nit I'm just going to do it there"; the two tools are "fundamentally different" (is-n8n-dead, 2026-02-01). · stable
- `[F]` `[D]` "learning to ride a bike i've got balance i know how to steer i know how to pedal but now we're going to be hopping on to like a motorcycle", and "naden wasn't a detour" (agentic-workflows-just-changed-ai-automation-forever-claude-code, 2026-01-25). · stable
- `[R]` `[D]` "About 90% of all workflows will rely on the same 15 or so core nodes" (how-i-d-learn-n8n-if-i-had-to-start-over-in-2026, 2025-12-10). · stable
- `[J]` `[M]` n8n for fixed flows, one-click hosting, visual run history; Claude Code for reasoning, apps, self-repair (q10, q12). The "30+ steps" break point is not in captions. · stable

**Borrowed, not his:** Karpathy's spec, verifier, environment, from a reel Nate edits as demo footage: "his method has three layers layer one is the spec" (gpt-6-astra-finally-solves-ai-video-editing-full-guide, 2026-09-08). Who voices it is open; Gemini credited Cole Medin, whose interview never mentions Karpathy. STORM's five perspectives are Stanford's (2026-06-29).

---

## 3. Models and tool choice

- `[J]` `[D]` "my number one goal is to never be loyal to a provider only be loyal to my harness and my assets and I will switch the brain interchangeably" (how-to-actually-choose-the-right-ai-agent, 2026-09-11). **Speaker open:** it sits in the cold-open teaser of the Mark Kashef interview. · stable
- `[F]` `[D]` "when I say walk it down I mean walking it down the model list", then effort levels, after setting quality on a top model (build-sell-with-codex-5-hour-course, 2026-09-21). · stable
- `[F]` `[D]` "take benchmarks with a grain of salt" (opus-4-8-just-dropped-here-s-how-to-actually-use-it, 2026-05-28). He runs 10 to 38-task tests with time and cost beside quality: "Fable took 23 minutes whereas Soul took almost 7 minutes" (i-tested-gpt-5-6-sol-vs-fable-5-what-you-need-to-know, 2026-07-10). · stable
- `[R]` `[D]` Stated prices per million tokens. Haiku "$1 ... input ... $5 ... output", Sonnet $3 and $15 (claude-code-for-non-coders-6-hour-course, 2026-07-11). Opus "$5 per million input and $25 per million output" (claude-just-told-us-to-stop-using-their-best-model, 2026-04-09). Fable "double opus", $10 and $50 (how-anthropic-engineers-actually-prompt-fable-5, 2026-07-01). Astra $10 and "50 bucks" (build-sell-with-codex-5-hour-course, 2026-09-21). No Sol, Terra or Luna price is spoken; Gemini's Sol at $2 and $10 is invented. · version-bound
- `[R]` `[D]` GLM 5.2: "$1.40 ... on the input and $4.40 on the output ... about five times cheaper"; "80% or more of your knowledge work" could run on it, not 80% of Opus (glm-5-2-in-claude-code-is-blowing-my-mind, 2026-06-19). · version-bound
- `[R]` `[D]` "the subscription of Codeex actually gets you about $14,000 of inference" (build-sell-with-codex-5-hour-course, 2026-09-21). · version-bound
- `[J]` `[D]` Early default: "use Sonic for 80% of work switch to Opus for complex architecture decisions or tricky bugs" (build-sell-with-claude-code-10-hour-course, 2026-03-12). After limits doubled: "if you were consistently delegating a lot of work to haiku or sonnet just because you were trying to really maximize your uh session limit then maybe you can start to ... give yourself" (claude-just-solved-session-limits, 2026-05-07). Later builds orchestrate on Opus or Fable (`[M]`, q05). · version-bound
- `[J]` `[D]` opusplan, "opus does the planning and sonnet does the execution", recommended 2026-04-09 and 2026-05-12, then retracted: "I do want to apologize ... each plan toggle is a model switch and starts a fresh cache" (give-me-10-mins-and-i-ll-save-you-millions-of-claude-tokens, 2026-05-21). · version-bound
- `[J]` `[D]` "it feels to me like Claude Code is like a wise old owl and then it feels like Codex is like the Rottweiler" (how-to-actually-choose-the-right-ai-agent, 2026-09-11; interview file, speaker untagged). In the SaaS course the owl is Fable; "surgeon" is nowhere. Working split, `[M]` (q14): plan, design, front end in Claude Code; strict execution, review, structured PDFs in Codex. · version-bound
- `[R]` `[D]` Per-task results, not rankings. Sol against Fable 5: "Soul won 24 to3 ... Soul costed 16 bucks while Fable costed 63 bucks" (i-tested-gpt-5-6-sol-vs-fable-5-what-you-need-to-know, 2026-07-10). "astra won 10 of them and Fable won five of them" (i-tested-gpt-6-astra-vs-fable-5-1-on-15-real-use-cases, 2026-09-06). Fugu: "36 of the 38 tasks end in a tie we had Fugu being 4.5 times slower overall and five times more expensive" (i-battle-tested-sakana-fugu-s-fable-killer, 2026-06-23). The "new AI design king" is Astra, not Fable 5.1. · version-bound
- `[J]` `[M]` Routers lose: going direct to Claude Code or Codex beat Fugu on speed and cost at equal quality (q19). · version-bound
- `[R]` `[D]` Opus 4.7's tokenizer: "the same input might actually cost you more just like 1 to 1.3". Same video relays an AMD director's analysis where thinking depth "collapsed 73%", third-party (claude-opus-4-7-just-dropped-or-did-it-really, 2026-04-16). · version-bound
- `[R]` `[D]` "using your cloud subscription inside of a third party tool like OpenClaw or Hermes isn't allowed unless Anthropic specifically approves you" (100-hours-testing-claude-code-vs-chatgpt-codex-honest-results, 2026-05-26). OpenAI allows a ChatGPT login in Hermes (`[M]`, q16). · version-bound
- `[J]` `[M]` Local models are free and private but fail at multi-tool calls and large context; use for cheap volume and as a fallback (q15). Jev is a hosted TypeSafe classifier, not a local option. · version-bound
- `[J]` `[D]` Pick the format the model can check by eye. Remotion edits his HeyGen pipeline on 2026-04-15; on 2026-04-18 Hyperframes is "kind of like a better version of Remotion". · stable
- `[R]` `[D]` "on a $200 a month plan for max that design system took about 6% of my session limit already" (claude-design-2-hour-course-beginner-to-pro, 2026-04-30). Rules there, `[M]` (q18): design system first, hex codes and references over adjectives, one structural change per prompt. · version-bound

**Open, B-C03, which harness spends fewer tokens.** "Codex wrote about 2 to 5x fewer output tokens than Claude" (2026-05-26). Typeform clone: Codex about 11.5M output against Claude's 2M (2026-08-14). Design test: Codex 100,000 tokens and $20, Claude about 500k and $65 (2026-08-26). Don't quote one side as his rule.

**Release dates by title:** Opus 4.7 2026-04-16, Opus 4.8 2026-05-28, Fable 5 2026-06-12, GPT-5.6 Sol 2026-07-09, Fable 5.1 2026-09-01, GPT-6 Astra 2026-09-03, Opus 5.5 2026-09-23. A rule naming one of these is no older than its date.

---

## 4. Pricing and offers

### 4.1 The AI Service Ladder

- `[F]` `[D]` "earn each rung by standing on the one below it" (how-to-build-a-one-person-ai-business-using-claude-code, 2026-08-11); "trust comes before retainers" (how-to-sign-your-first-ai-automation-client-in-7-days-with-proof, 2026-02-04). Order: "education or consulting then audit then project then retainer". Four rungs, 0 to 3. · stable

| Rung | 2026-05-22 (the-ai-offer-you-can-sell-tomorrow-morning) | 2026-08-11 (how-to-build-a-one-person-ai-business-using-claude-code) |
|---|---|---|
| 0 · hours, education | "$100 to $500 a session" | $100 to $500 an hour, "$200 is a great default" |
| 1 · audit | "$500 to 2500 bucks" | "500 bucks to maybe even 3,000 bucks" |
| 2 · project | $2,500 to $10,000 | $2,500 to $10,000 |
| 3 · retainer | "$3 to $10,000 a month ongoing" | $3,000 to $10,000 a month "for a solo operator" |

All cells `[D]`, version-bound. Both columns are his, 81 days apart. The Grok Bots course (2026-08-31) starts from free work and prices audits $1,000 to "upwards of 10,000". **Not on the ladder:** $20,000 a month (True Horizon's minimum), $15,000 to $35,000 (Devin Karns's blueprint), a "scaled $15k to $20k+" rung and a "$5,000 enterprise audit" (both Gemini's).

- `[J]` `[D]` Hourly is an on-ramp: "for your first two or three projects when you've got you know nothing to point at ... billing hourly is a safer ask" (18-months-of-pricing-ai-automations-in-21-mins, 2026-08-01). · stable
- `[J]` `[D]` "if you're really trying to get your first client and you can get that then i would say do it reps over cash" (the-3-step-system-behind-my-20k-month-ai-agency-retainers, 2026-08-25). · stable

### 4.2 Value pricing

- `[R]` `[D]` "they should roughly see 10 times the return on whatever they pay you within the first year" (how-to-price-ai-workflows-without-losing-clients, 2025-11-30). "The golden rule" in 9 files from 2025-05-05. · stable
- `[R]` `[D]` "pick somewhere between 10% and 20% of that number as my starting point", the number being first-year annualized value (18-months-of-pricing-ai-automations-in-21-mins, 2026-08-01). The PRICE video (2025-11-30) anchors at 10%. Gemini's "10 to 15%" is wrong. · stable
- `[F]` `[D]` PRICE: "the P is for prepare", "the R is for research", "the I which is for identify identify the ROI", "the C is for communicate", "the E is for expand" (how-to-price-ai-workflows-without-losing-clients, 2025-11-30). "Cost of Inaction" has zero caption hits; he says "annualized" and "ceiling". · stable
- `[R]` `[D]` "20 hours a week at $40 an hour is about $800 bucks a week and if you multiply that by 52 ... that's $41,600 annualized"; build "right around 13% ... 5,500 bucks"; "about a 7.5 multiple", lead growth covering the rest (18-months-of-pricing-ai-automations-in-21-mins, 2026-08-01). His example misses his 10x rule, and he says so. · stable
- `[R]` `[D]` **Open, R42-15.** The same $5,500 build on 2025-11-30: "$38,400 per year", "I priced the product at 15% of those annualized savings and that came out to $5,500", maintenance "$550 per month which is about 10% of the original project's fee" (how-to-price-ai-workflows-without-losing-clients). 15% of $38,400 is $5,760; the slip is his. One client or two, captions can't say. Treat 2026-08-01 as current.
- `[R]` `[D]` "an hour of that rep's time is about 50 bucks ... that equals about $12,000 to the business so 10% of that $12,000 is $1,200" (18-months-of-pricing-ai-automations-in-21-mins, 2026-08-01). $12,000 implies about 240 working days. The "$18,000 and $1,800" version is Gemini's. · stable
- `[R]` `[D]` Hard dollars beat hours: a build "only saved like 45 minutes a day but it helped them avoid around $12,000 a month in scheduling errors ... it's hard dollars" (same video). · stable
- `[F]` `[D]` "option one is 10% so $10,000 option two is 25% so 25,000 and option three is 50% 50 grand and I'm just kind of throwing out rough numbers here"; "the middle one is kind of the one that's designed to win because the bottom one looks thin the top one maybe makes them wse" (same video). Earlier real tiers: "our scale package is 25,000 ... most clients actually go with the growth package at 12K" (how-i-sold-these-4-ai-agents-for-23-000-as-a-beginner, 2025-08-31). No $5,000 starter. · stable
- `[R]` `[D]` "the top of that proposal is three short paragraphs and none of them are about you or your pricing they're about where the business is right now in their words with their numbers" (18-months-of-pricing-ai-automations-in-21-mins). · stable
- `[R]` `[D]` "client's account client's card every single time your fee is for design consulting building testing now the tokens are a utility bill" (same video). No test-token markup figure exists. · stable
- `[J]` `[D]` Hold the price, cut the build: "it sounds like 20 grand isn't in the budget right now why don't we just like reduce the scope a little bit and start with a smaller project" (same video). No "$7,000 MVP" line exists. · stable
- `[J]` `[D]` No early quote: "I really need to understand more in depth the complexity" (same video). · stable
- `[R]` `[D]` Pricing off a job post: "I've priced this assuming that there's about 200 of these a month and you know if that's off let's hop on a 15-minute call" (same video). "Assumption Frame" is Gemini's label. · stable
- `[R]` `[D]` Terms, dated: "$3,000 upfront and then maybe a $3,000 upon completion" on a live call (how-i-sold-a-6000-ai-workflow-to-a-business-live-sales-call, 2025-09-07); later a $9,000 project in "three payments" 30 days apart (18-months-of-pricing-ai-automations-in-21-mins, 2026-08-01). No 33/33/34. · stable
- `[R]` `[D]` Maintenance is flat: "a standard maintenance plan so this was 400 bucks a month", and "that $400 a month isn't for me to bolt on new features" (same video). A $200 to $1,500 per-system range is `[M]`. $20,000 is never maintenance. · version-bound
- `[R]` `[D]` "the general target margin for this type of work is 50 to 70% 50% is a good baseline", so $5,000 delivery cost prices at $10,000; "one $15,000 per month client than five $3,000 per month clients" (how-to-price-ai-workflows-without-losing-clients, 2025-11-30). · stable
- `[R]` `[D]` The client owns the build; "the real IP in the system is the prompts your data your workflows" (same video). · stable
- `[F]` `[D]` "the specific KPI is Xmetric the baseline today is X number and after 60 days we expect X target four blanks"; buckets are more customers, more per customer, lower costs (how-to-build-a-one-person-ai-business-using-claude-code, 2026-08-11). · stable
- `[F]` `[D]` "the three Ps pain promise person actually no I like to go pain person promise" (anthropic-s-ceo-how-to-build-a-1-person-business-with-claude, 2026-09-18; 9 files from 2026-02-04). · stable
- `[R]` `[D]` "$5,000 just for the AI business audit and then make another 20 to even $100,000 implementing"; SCAN's sizing: "$200,000 a year in labor and AI can cut it by 70% that's $140,000 savings opportunity" (how-i-d-make-money-with-ai-in-2026-if-i-had-to-start-over, 2025-10-03). · version-bound
- `[R]` `[D]` "$5,000 to get you and your team set up with Grockbot" (build-sell-grok-bots-2-hour-course, 2026-08-31). A "$15k+ retainer" follow-on is not spoken. · version-bound

### 4.3 SaaS

- `[F]` `[D]` "we have the pain we need to start building out the promise the product the plumbing and the packaging ... and then the last one is proof" (build-sell-ai-saas-products-2-hour-course, 2026-08-10). · stable
- `[R]` `[D]` Client Pack, same video: "39 bucks a month and 390 for the year", a watermarked free deck; a "29 to 49" band from "835 price sentences"; "4 cents ... 9 cents ... 13 cents for a full deck"; value "in one sitting in 5 minutes". · version-bound
- `[J]` `[D]` "the prompt that powers this on the back end is what matters because anyone could come in here and rebuild this entire thing in one day" (same video). · stable
- `[R]` `[D]` "at $499 bucks per month Agent Report Card would need 168 active customers monthly to pass $1 million in annual recurring revenue" (anthropic-s-ceo-how-to-build-a-1-person-business-with-claude, 2026-09-18). · stable

### 4.4 True Horizon, stated correctly

- `[R]` `[D]` "I scaled my agency to over $100,000 a month and then I sold it"; "the minimum to work with us was a $20,000 a month retainer", same words in 3 videos (18-months-of-pricing-ai-automations-in-21-mins, 2026-08-01). · version-bound
- `[R]` `[D]` "I've scaled my own agency True Horizon to $2.5 million this year" (you-re-doing-ai-automation-wrong-here-s-how-to-fix-it, 2025-10-15): 2025 revenue, not ARR. "past $100,000 a month in under a year and I ended up exiting it" (so-you-learned-claude-now-what, 2026-06-22). No transcript dates the exit. Co-founders "Milan our CEO and Tyler our CTO" (2025-08-31) describe the agency before the sale. · version-bound
- `[R]` `[D]` His build prices: $1,200 in 2 hours, "600 bucks an hour" (i-built-this-ai-agent-in-2-hours-and-got-paid-1200, 2025-08-17); $1,650, "pretty random", $4,000, $6,000 and $12,000, summing to $23,650 (how-i-sold-these-4-ai-agents-for-23-000-as-a-beginner, 2025-08-31); $2,600 (2025-12-17). Prices rose with value framing, not build hours. · stable

**Guest and relayed:**
- `[D:guest:Devin Karns]` A fixed-price workshop (no figure), a blueprint where "we charge around 15 to 35k for this right now", a fixed build, then "I'm going to take 15% of the topline revenue"; "mid-markets are so prime"; about 5x once past $5 to $10M (the-playbook-for-a-100m-ai-agency, 2026-05-25). Gemini's workshop and build prices are invented, and Nate never says avoid SMBs.
- `[D:guest:Jonathan Stark]`, relayed from AIS Live: hourly "pays you more to be slow"; "cost doesn't justify price price justifies cost", with the landscaper (18-months-of-pricing-ai-automations-in-21-mins, 2026-08-01). Nate's later "cost doesn't justify price value justifies price" (2026-08-25) is also his; they share the first half.

---

## 5. Sales

### 5.1 Discovery

- `[F]` `[D]` "I use a framework that I call the LRP which stands for listen repeat poke" (how-i-sold-a-6000-ai-workflow-to-a-business-live-sales-call, 2025-09-07); "I listen while they describe their week ... i repeat back the pattern to confirm alignment and then I poke to quantify it" (build-sell-with-claude-code-10-hour-course, 2026-03-12). 6 files to 2026-09-21. · stable
- `[F]` `[D]` "act as the doctor not the pharmacist i've used this analogy a lot on my channel a pharmacist just fills a prescription that someone else wrote" (build-sell-with-claude-code-10-hour-course; 8 files). · stable
- `[R]` `[D]` "listen for 70% of the time speak for 30% of the time focus conversation on business value not technical details" (how-i-sold-a-6000-ai-workflow-to-a-business-live-sales-call, 2025-09-07). · stable
- `[J]` `[D]` "there's just a lot of power in silence ... i stopped talking" (build-sell-with-codex-5-hour-course, 2026-09-21). · stable
- `[R]` `[D]` Openers: "what prompted you to book a call and what you're looking to do here" (2025-09-07); "where are you losing the most time in your business what processes do you wish could run themselves" (build-sell-with-claude-code-10-hour-course). · stable
- `[R]` `[D]` Pokes: "where are you paying people to copy and paste or chase info ... what interrupts you the most between 9 and noon ... where do mistakes cause rework refunds or churn" (stop-selling-ai-agents-sell-ai-solutions-instead, 2025-09-24). · stable
- `[R]` `[D]` "how many people touch it and what happens when it goes wrong these are all sizing questions they measure the ceiling not the build"; proxies, "how many locations do you have or how many of these come in on your busiest days" (18-months-of-pricing-ai-automations-in-21-mins, 2026-08-01). · stable
- `[R]` `[D]` Supply-constrained: "if you had 10x the business tomorrow what would break first you ask them that and then you just be quiet". Demand-constrained: ask what would 10x the business coming in (build-sell-with-codex-5-hour-course, 2026-09-21). · stable
- `[F]` `[D]` "you run three buckets of questions why this why now and why me", asking aloud "couldn't you vibe code this couldn't you hand it to an intern" (18-months-of-pricing-ai-automations-in-21-mins). **Open, R44-12:** he credits Stark for nearby lines and is silent on where this came from. · stable
- `[R]` `[D]` "Yeah he probably could get a version of this up and running. But what I'd want to know is who's going to watch it at 2 in the morning when the model updates" (same video; the builder is "my nephew"). · stable

### 5.2 The offer

- `[F]` `[D]` "you want your offer to be so good that people would feel stupid saying no ... I call the four Rs result road map risk reversal and review". Result: "I can automate 90% of your onboarding process if it currently takes you 5 hours I can bring that down to 30 minutes". Risk reversal: "a free build in exchange for testimonial or offer a money back" guarantee. Review: objections, "we call these hidden costs" (how-to-sign-your-first-ai-automation-client-without-starting-an-agency, 2025-11-17; one file). · stable
- `[J]` `[D]` "the framing that actually wins in 2026 is being an AI partner because builders sell features but partners sell real out[comes]" (how-to-build-a-one-person-ai-business-using-claude-code, 2026-08-11). · stable
- `[J]` `[D]` "stop selling AI agents and workflows and start selling AI solutions" (stop-selling-ai-agents-sell-ai-solutions-instead, 2025-09-24). "businesses really only care about three things: time money focus ... they don't care if you deliver it with AI or a VA or duct tape and chewing gum" (build-sell-with-claude-code-10-hour-course). · stable
- `[J]` `[D]` Clients think "they're actually just buying relief ... you're not trying to provide relief if you're trying to provide real business value so the whole idea is to reframe" (the-3-step-system-behind-my-20k-month-ai-agency-retainers, 2026-08-25). Devin Karns uses "buying relief" approvingly; Gemini swapped them. · stable
- `[J]` `[D]` "A portfolio says 'I built this thing.' But a receipt says 'Here's what this thing actually did for the business.'" (5000-hours-of-building-ai-in-just-17-minutes, 2026-08-04). · stable

### 5.3 Getting clients

- `[F]` `[D]` "step one is offer first so pick a niche pick a problem do some research create an offer around an outcome" (how-to-sign-ai-workflow-clients-with-0-followers, 2026-02-16). Step two, validate with volume toward five clients. "Sell before you build" is from another video (2026-08-10); Gemini's one-line slogan is a splice. · stable
- `[J]` `[D]` "your goal for day one would be to write down 20 people that you can reach out to", then a free small pilot for a case study (how-to-sign-your-first-ai-automation-client-in-7-days-with-proof, 2026-02-04). · stable
- `[J]` `[D]` Against "high volume tons of cold outreach with no soul and no positioning using tools or automations to scrape LinkedIn" (same video). Manual DMs at volume are fine: "aim for at least 100 a day" (how-to-sign-ai-workflow-clients-with-0-followers). · stable
- `[F]` `[D]` Trojan Horse: "instead of trying to build trust from scratch with cold prospects ... you borrow someone else's", then "I'll give you 20% of that project revenue" (build-sell-with-claude-code-10-hour-course, 2026-03-12). His "92% of B2B buyers trust referrals" and "46% faster" carry no source. · stable
- `[J]` `[D]` Upwork is the second channel after the warm network, not a rung: "this is where strangers go shopping for what you're selling so the intent is already there which is the whole game" (how-to-build-a-one-person-ai-business-using-claude-code, 2026-08-11). Keywords he names include "AI integration", "automation setup" and "custom workflow design". The bidding playbook is paywalled. · version-bound
- `[R]` `[D]` Clay sells warmed domains "and they're going to make sure that you're only sending 30 per day"; its waterfall lifts match rates "up to more like 80 to 90%" (claude-code-clay-makes-lead-generation-actually-fun, 2026-07-12). The "4.7 stars across 4,100 reviews" email there is Claude's output. · version-bound
- `[R]` `[D]` Third-party: Upwork found "demand for AI integration work specifically grew 178% year-over-year ai enabled freelancers on the platform earn about 40% more per hour" (how-to-build-a-one-person-ai-business-using-claude-code). · version-bound

**Guest, not Nate's:**
- `[D:guest:Sav]` (how-a-college-student-made-500k-with-cold-email-exact-framework, 2026-02-14). "anything above a 5% reply rate below a 10% reply rate I would say that's like the golden zone". Started on one domain, five inboxes, about 150 a day; now "40 to 50 inboxes". Funnel: 9,000 sends, about 450 replies, about 225 interested; Gemini's calls and deals are not spoken. Pipeline "over half a million dollars in sales opportunities in just 6 months", later "700K plus"; opportunities, not revenue. The salon owner reached $10k MRR, not Sav. "Sonam" came from the question text.
- `[D:guest?]` "I will get you 10 meetings on the calendar in 30 days and if not you don't have to pay me a dime" (same file); grep cannot tell Sav from Nate.
- `[D:guest:Christian, student]` The 450-a-day scrape failure is his, not Sav's. He closed $1,500 five days in, then "we're doing uh 2,000 now" (how-to-sign-your-first-ai-automation-client-in-7-days-with-proof, 2026-02-04). Gemini's "members frequently close in 5 to 7 days" rests on this one case.

---

## 6. Content, community and business numbers

- `[F]` `[D]` One video (how-i-d-make-money-with-ai-in-2026-if-i-had-to-start-over, 2025-10-03) names a framework per stage, each once. BUILD: "block byb block", understand the use case, "install and imitate" with a 60-second demo, "land the first client", "document and duplicate". SCAN: "study the business", "calculate the opportunity", "architect the solution", "narrate the results". SHARE: show, hook, attract, "The R stands for recommend", "the E stands for expand Keep producing videos and templates". GROW: "The G stands for get developers ... The R stands for retain authority ... The O is for onboard sales ... And the W is win with brand". · stable
- `[F]` `[M]` Funnel: YouTube, free Skool, AIS Plus, then certification, AIS Live and coaching; one call to action per video, a free resource in the free Skool (q27, q28). · version-bound
- `[J]` `[M]` Show the destination, not the car (q28, q40). A 2026-09-29 grep found "ai is the car the result is the actual destination" in how-to-sell-ai-workflows-without-starting-an-agency (2025-08-24); no verify file logs it yet. · stable
- `[J]` `[M]` Titles carry a dollar or time outcome ("I Built an AI Agent in 2 Hours and Got Paid $1,200"). Clients buy boring automations while swarms get the views (q28). · stable
- `[R]` `[D]` Free community: over 230,000 (2026-01-25); "over 375,000" (2026-05-22); "pushing way past 400,000" (2026-06-23); over 440,000 (2026-08-31); "almost half a million" (2026-09-09); 450,000 (2026-09-23). He rounds, so the last two run backwards. · version-bound
- `[R]` `[D]` AIS Plus: "$89 a month soon to increase" (2025-10-03). Sizes rise from 1,400 to "over 3.5,000" (3,500). Live calls went from "five live calls per week" (21 files, to 2025-06-18) to one a week (12 files, from 2025-10-29). "~$300k MRR" is Gemini's 3,500 × $89. · version-bound
- `[R]` `[D]` Revenue, dated: "over $240,000 in the past 6 months" from builds (2025-05-05); "over $6,000 a month from YouTube" (2025-06-24); "over $150,000 per month in pure profit from teaching AI automation No payroll no big expenses" (2025-10-03); $231,000 in a month, "the majority of that revenue came from my B TOC side" (2025-10-31); a "13 person team", "my only job is to learn AI make videos delegate the rest" (i-turned-claude-into-the-ultimate-second-brain, 2026-06-10); "just under $5 million of topline revenue" in 12 months across "education communities certifications events newsletters" (build-sell-grok-bots-2-hour-course, 2026-08-31); "an average of over $400,000 per month" across units (build-sell-with-codex-5-hour-course, 2026-09-21). · version-bound
- `[R]` `[D]` Channel: about 800k subscribers on 2026-06-10 (the "620,000" there is stale data he calls wrong); past 1M by 2026-09-09, where "September 19th of 2024" is his analytics filter start, not the milestone; "41 videos in 2024 261 videos in 2025" against 9 and 128 dated in sources.tsv, so his count likely includes shorts. · version-bound

**Guest:** `[D:guest:Cole Medin]` "I had um about 50,000 subscribers when Nate first reached out to me and he had like 10,000" (how-to-use-claude-code-better-than-98-of-people, 2026-06-18).

### How Nate teaches

From q40 (`[M]`), with caption counts run 2026-09-29, for recognising his material. Nothing here generates in his voice.

- **Format.** 10 to 25 minute breakdowns, 1 to 2 hour mini-courses, 6 to 10 hour courses. Open on the finished output, sketch the architecture (often Excalidraw), build live with errors left in, do the business math, point to a free resource. Long courses reuse earlier videos word for word.
- **Phrases.** "by the end of this video" opens 37 files. The closer "I appreciate you guys making it to the end of the video" is in 217 of 299. "boring is beautiful" 9 files, "AI slop" 18, doctor and pharmacist 8 or more. "let me quit yapping" appears once (2026-08-22), so Gemini's "default transition" overstates it.
- **The mindset aside.** Gemini's "Another one of Nate's healthy mindset shifts" has zero hits, but the move exists: "think of a failure as a good thing because it gave you more data about what not to ever do again another one of those super healthy Nate mindset shifts" (build-sell-claude-code-operating-systems-2-hour-course, 2026-05-01).
- **Tone.** "you guys", jokes at his own slips, leans on his non-coding degree. He names the people he borrows from (Pocock, Sabrina, Stark, Cherny); Gemini often drops the credit.

---

## 7. Mindset and predictions

- `[J]` `[D]` "The AI is the one thing that everyone has equal access to" (5000-hours-of-building-ai-in-just-17-minutes, 2026-08-04). "Context is king" is a separate video (claude-code-for-non-coders-6-hour-course, 2026-07-11) that verify-c located but did not quote; Gemini glued them into one line. · stable
- `[J]` `[D]` "the tool was never the valuable part It's what you've learned and how you think that's actually valuable"; "don't wait around for the perfect tool and don't stress when the one that you love gets replaced" (same 2026-08-04 video). · stable
- `[J]` `[D]` On Karpathy joining Anthropic: "the model is not the moat forever the moat is the application and the adoption" (what-karpathy-joining-anthropic-actually-means-for-claude, 2026-05-19). · stable
- `[J]` `[D]` "You cannot learn automation by just watching someone else click buttons"; rebuild it and break it (how-i-d-learn-n8n-if-i-had-to-start-over-in-2026, 2025-12-10). · stable
- `[F]` `[D]` "the default shift ... before you do any task just ask yourself how could AI do this or at least how could AI do 30% of it" (build-sell-claude-code-operating-systems-2-hour-course, 2026-05-01). Gemini's "30% to 50%" is wrong. · stable
- `[F]` `[D]` "the mindset the method and the machine"; "treat AI as a mentor not a vending machine" (same video; 4 files to 2026-09-23). · stable
- `[R]` `[D]` "whenever you make a change you typically are going to expect a 20% decrease in productivity" (same video). · stable
- `[J]` `[D]` "step two pick one real task not 10 just pick one" (how-claude-is-creating-a-new-generation-of-millionaires, 2026-07-03). · stable
- `[J]` `[M]` AI-native is what your brain reaches for first on a new task. Prediction: automation shifts from triggers to systems that watch inboxes and CRMs and flag problems first. He reads Amodei's one-person billion-dollar company as a $1M ARR solo business (q31). · stable
- `[J]` `[M]` On safety news (a September 8 Anthropic resignation, captioned "Jacob Coxin"; Evan Hubinger's tweet) he treats advanced AI as a present concern and answers with hard tool permissions (q34). · version-bound

**Guest and relayed:**
- `[D:guest:Devin Karns]` "the value of actually doing development is trending towards zero" (the-playbook-for-a-100m-ai-agency, 2026-05-25). Gemini made it Nate's and added a "40 to 60% of code" figure with no caption hit.
- `[D:guest:Nate B. Jones]` "going the last mile is how we deliver value as builders" (why-your-ai-offer-isn-t-selling-and-how-to-fix-that, 2026-07-20).
- `[D:guest:Mark Kashef, speaker open]` "Boris Churnney dropped a tweet saying you should delete all of your skills every six months" (how-to-actually-choose-the-right-ai-agent, 2026-09-11). The rule is Cherny's.

---

## 8. Eras and reversals

Dates from sources.tsv. Cut points are Pass 2's: the first "Claude Code" title and the AIOS course.

| Era | Window | Videos | Transcripts | Anchor |
|---|---|---|---|---|
| 1 · n8n | to 2026-01-13 | 140 dated + 28 undated | 116 | n8n titles 32 in 2025-Q2, 0 in 2026-Q2 |
| 2 · Claude Code | 2026-01-14 to 2026-04-30 | 73 | 73 | WAT first named 2026-01-21 |
| 3 · AIOS and fleets | 2026-05-01 on | 111 | 110 | AIOS course and 4 C's 2026-05-01 |

Output rose from about 30 videos a quarter in 2025 to 71 in 2026-Q2. The 52 videos with no transcript are all Era 1 (2024-10-06 to 2025-02-19, plus 27 undated).

**Reversals, with both dates:**

1. **n8n to Claude Code.** First Claude Code caption 2025-10-10. "For the longest time my main thing was nodn ... But these days my main tool is cla code" (2026-08-04). n8n kept for jobs under 10 minutes (2026-02-01) and for teaching. Last n8n title 2026-03-21.
2. **Agents to outcomes.** Agent-price titles 2025-08-17 to 2025-09-07; the turn is "Stop Selling AI Agents, Sell AI Solutions Instead" (2025-09-24). The $2,600 and $1,650 titles after it retell old builds. Peak: the Ladder (2026-05-22) and the pricing retrospective (2026-08-01).
3. **Context reset.** 60% (2026-03-12, 2026-04-02) → 120k and no /compact (2026-04-20) → 250k with Cole (2026-06-18) → 250k to 300k (2026-07-11). A list video repeats 60% on 2026-04-27. Treat the token threshold as current.
4. **Default model.** Sonnet for 80% (2026-03-12, 2026-04-02); limits doubled 2026-05-07; Fable 5 from 2026-06-12. opusplan recommended 2026-04-09 and 2026-05-12, retracted 2026-05-21.
5. **/loop.** 3 days (2026-04-27) → about 7 days (2026-06-03), likely a product change.
6. **Remotion to Hyperframes.** 2026-04-15 → 2026-04-18.
7. **OpenClaw to Hermes.** Clawdbot 2026-01-27; Hermes named 2026-04-17, course 2026-05-10. On 2026-09-28: "I actually did this experiment before using Open Claw".
8. **Grok Bot access.** Cursor Ultra required (2026-08-12) → "just 30 bucks a month So it used to be when it first came out it was just the 200 bucks a month" (2026-08-31).
9. **Upwork.** "pretty much going to be similar to cold outreach" (2026-02-04, 2026-03-12) → "so so so much easier than cold outreach because they posted a job" (2026-08-11).
10. **Terms, calls, payroll.** 50/50 (2025-09-07) → three monthly payments (2026-08-01). Five live calls a week (to 2025-06-18) → one (from 2025-10-29). "No payroll" (2025-10-03) → 13-person team (2026-06-10).

**Not reversals, though Gemini says so:** he did not adopt skill deletion (2026-08-12) and did not drop bypass mode (2026-07-11). The reactive-prompting video (2025-02-26) is itself the early source; the only earlier trace is his retired prompt generator. q48's ordering of ten reversals is Gemini's.

---

## 9. How the lens should use and distrust this corpus

**Use it for:** placing a proposed service on the ladder (4.1) and pricing it with the annualize, 10 to 20%, three-tier method (4.2); if year one gives the client less than 10x, name the multiple and the assumption covering the gap, as he does. Run the workflow-or-agent gate (2.1) before any agent build; his default is a workflow with AI on a few steps and a human on money, deletions and mass sends. Take the latest dated form of each Claude Code rule (section 1). Use 5.1 and 5.2 for call and offer structure.

**Distrust it because:**
- **Gemini errs often.** Of 526 rows checked, 125 were corrected and 41 unsupported, about 32%. About 143 Pass 1 signals were never checked. Every `[M]` line sits in that risk.
- **Guests talk, and captions have no speaker tags.** Interview files: Sav (2026-02-14), Christian the student (2026-02-04), Devin Karns (2026-05-25), Cole Medin (2026-06-18), Nate B. Jones (2026-07-20), an Anthropic staff member (2026-08-12), Mark Kashef (2026-09-11). Check the speaker before quoting any line from them as Nate's.
- **Courses repeat older videos.** The 10-hour (2026-03-12), non-coders (2026-07-11) and Codex (2026-09-21) courses embed earlier videos word for word. A course date can misdate a position, and a course plus its source video is one origin.
- **Other people's numbers:** SWE-bench 80.9% against 76.2%, 98.5% re-reading, 18,000 thinking blocks, the 383-file cut, 35x and 72%, ELEPHANT's 88%, Upwork's 178%, 92% referrals, "46% faster". None is his outcome.
- **Affiliate codes** (Hostinger "Nate Herk" 10%, Apify "30 Nate Herk" 30%, Firecrawl) sit beside S-tier verdicts.
- **Arithmetic slips:** $5,500 is 14.3% of $38,400; the $12,000 case implies 240 working days; 200 invoices × 13 minutes is 43.3 hours, not 45; the "$23,000" title sums to $23,650; he switches between 52 weeks and 4-week months.
- **Names absent from captions:** Visual Agentic Workflow Framework, Cost of Inaction, Assumption Frame, Two-Monitor Puzzle, System Constitution, Master Router, "prompts are suggestions, tools are walls". "10 Hours to 10 Seconds" and "Agent Zero" are courses, not frameworks.
- **Spellings:** Mark Kashef, Klouse (his chief-of-staff bot), Key AI (probably kie.ai) and "Jacob Coxin" are unsettled. Fable, Astra, Sol, Terra and Luna are real models.
- **Version-bound entries went stale inside the corpus.** Prices, plan limits, Routine counts, /loop expiry and MCP costs all changed between 2026-03 and 2026-09. Quote them with their date or not at all.

**Open contradictions, both sides kept:**

| # | Side A | Side B |
|---|---|---|
| A-C05 | q08's system-prompt sections | q09's; the real structure was on screen (2025-05-23) |
| B-C01, R42-15 | $41,600, 13%, $400 flat (2026-08-01) | $38,400, 15%, $550 at 10% of fee (2025-11-30) |
| B-C03 | Codex 2 to 5x fewer output tokens (2026-05-26) | Codex 11.5M against 2M (2026-08-14); design test flips (2026-08-26) |
| B-C13 | Max plan "virtually unlimited" (not in captions) | Claude Design used 6% of a session (2026-04-30) |
| X-12 | Hostinger VPS "$5 to $10" (Gemini) | only "six bucks ... n[ine] bucks" spoken (2026-01-28) |
| R44-12 | why this, why now, why me is Nate's | it is Jonathan Stark's why conversation |
| R49-19 | AIS Plus "over 200" (15 files) | a caption drop of 2,000 |
| B061, C-064 | discount email to "about 150,000" (2026-07-11, 2026-08-04) | "almost 200,000" (2026-08-24) |
| I-5 | Cherny and harness-loyalty lines are Nate's | they are Mark Kashef's |
| I-6 | the Karpathy reel is in Nate's voice | someone else voices it |

**Gaps:** no transcripts for the 52 oldest n8n videos; no churn, close-rate or cold-email numbers from his own agency (every volume and reply rate is Sav's); paid syllabi and the Upwork playbook are paywalled; on-screen text (prompt sections, `MI.md`, URLs) never reached captions. Full list in `pass-2-reconciliation.md` section 6.

---

## Cross-references

- Signals: `pass-1-extraction.md`
- Corrections ledger, framework clusters, contradictions, eras: `pass-2-reconciliation.md`
- Caption quotes behind every `[D]`: `scratchpads/nate-herk-pass2/verify-a.md`, `verify-b.md`, `verify-c.md`, `round2.md`
- Upload dates: `sources.tsv`
