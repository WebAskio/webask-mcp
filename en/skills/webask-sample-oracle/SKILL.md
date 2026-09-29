---
name: webask-sample-oracle
description: "Estimates how many responses a WebAsk survey needs and whether conclusions can already be drawn. Use when someone asks whether there is enough data, how much longer to wait, or whether collection can be stopped."
---

# How many responses are needed

Two questions come up constantly: "can we draw conclusions yet?" and "how much
longer?". Both are settled in one conversation.

Reply to the person in the language they write in.

## What to ask

1. **How large the audience is** the conclusion is about: a hundred customers or a
   hundred thousand. A small audience needs a small sample.
2. **What decision the results serve.** "Get a feel for the mood" and "choose
   between two options" need different precision.
3. **Whether conclusions are needed per group.** Breaking down by city or segment
   multiplies the requirement.

## Estimate

`get_quiz_summary` — how much is collected, including within the needed breakdowns.

Practical anchors for the conversation:

| Goal | Order of responses needed |
|---|---|
| Get a general sense | 30–50 |
| State shares to about 10% | ~100 |
| Precision around 5% | ~400 |
| Compare two groups | 100+ in each |
| Break down by five segments | 100 per segment, so 500+ |

These are conversation anchors, not a formal calculation. If a formal estimate is
needed, say the numbers are approximate and what they depend on.

## How to answer

- **Enough collected** — say it plainly: collection can stop.
- **Not enough** — say how much more is needed and warn that conclusions may
  reverse.
- **Enough overall but not per breakdown** — the most common case. State which
  conclusions are already sound and which are not.

## What not to do

- **Do not demand representativeness** where a quick internal decision is being
  made.
- **Do not stay silent about a small sample** when plans are being built on it.
- **Do not count abandoned submissions** toward the collected volume.