---
type: corpus
aliases: ["Outbound Playbooks — Nicolas Gromer"]
corpus: nicolas-gromer
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Outbound Playbooks — Nicolas Gromer

**Corpus:** nicolas-gromer
**Generated:** 2026-03-26

---

## Services Company Playbook (Warm Outbound)

**Source:** Signal 8

The most directly actionable framework from the interview. Designed for services companies (not SaaS), making it the closest match to the client's model.

### Steps
1. **Build large lead list** (10K prospects). Too big for individual outbound.
2. **Run top-of-funnel ads** on the list for 1-2 weeks. Impression goal, not conversion. Just brand familiarity.
3. **Clay segmentation** after ad exposure. Pull the top 200 leads showing intent or matching ICP tightly.
4. **Warm outbound** on those 200. Reply rates increase because prospects have seen the brand.

### Why it works
The ad exposure turns cold prospects lukewarm. The Clay segmentation ensures outbound effort goes to highest-probability targets. The result is warm outbound at cold outbound prices (impression-based LinkedIn ads are cheap).

### ColdIQ parallel
Michel Lieben's inbound-led outbound follows the same warm > cold principle but uses organic LinkedIn engagement as the warming mechanism rather than paid ads. The two approaches are complementary: paid ads warm a larger audience faster, organic content warms a smaller audience deeper.

---

## Multi-Channel Behavior-Based Sequences

**Source:** Signal 5

### Sequence Structure
1. LinkedIn profile visit
2. Connection request
3. **Branch:** Accepted → LinkedIn message | Not accepted → email
4. **Branch on email:** Clicked link → different follow-up | No click → standard follow-up

### Principle
Every touchpoint branches based on the prospect's actual behavior. No static drip. The sequence adapts.

### Old vs. New
- **Old:** 4-5 emails, two days apart, same for everyone
- **New:** Multi-channel, behavior-branching, tailored per response pattern

---

## Smart CTA Framework

**Source:** Signal 6

### Rule
The CTA must state what the prospect gets, not what you want from them.

### Examples
| Fails | Works |
|-------|-------|
| "Do you mind taking 15 minutes for a demo?" | "Do you mind taking 15 minutes to learn how to launch outbound campaigns to get your first customer?" |
| Vague/mysterious emails (high reply rate, terrible close rate) | Clear value proposition (fewer replies, better pipeline) |

### For one client
| Generic | Specific |
|---------|----------|
| "Book a call to discuss our M&A lead service" | "15 minutes to see how [industry] firms are finding acquisition targets right now" |

---

## AI in Outbound (Segmentation, Not Copy)

**Source:** Signals 3, 4

### The Mistake
Using AI to write the email copy. Produces noise, easy to spot, not really relevant.

### The Correct Use
1. Enrich leads with data from LinkedIn and other sources
2. Create segmented lists based on product-relevant variables (e.g., sales team size)
3. Generate unique per-lead message variables from enriched data
4. Keep the email structure and offer human-directed

### Worked Example
100 leads → split by sales team size (under 20 vs. over 30) → different sequences per segment → within each segment, AI generates unique first lines ("I saw you manage 5 SDRs and 2 AEs" vs. "I saw you manage 12 SDRs and 1 AE") → deliverability improves because messages are unique.
