---
name: webask-source-dashboard
description: "Compares where WebAsk survey respondents came from and which channels perform best. Use when someone asks which mailing or campaign worked, or wants responses broken down by source."
---

# Where they came from and what it gave

A survey is usually distributed across several places at once. Responses can be
split by channel only if source labels were attached to the links.

Reply to the person in the language they write in.

## Check there is something to compare

`get_answer_extra_field_values` — which label values actually arrived.

If there are no labels, there is nothing to compare: **they cannot be added
retroactively**. Say so plainly and suggest adding labels to future links.

## Collect

For each label value, a slice via `get_quiz_report`. Per channel you need: how many
arrived, how many finished, and the target metric — contacts, average rating,
whatever matters here.

## How to present

A table by channel, sorted by what matters to the person: channel, responses,
completion share, target metric.

Below it, three conclusions:

- **Where the most responses came from.** Obvious, and the least useful.
- **Where completion is best.** A channel can bring few people but good ones.
- **Where responses are worse.** Sometimes it is not the channel but the promise
  in the ad: the wrong people arrived.

## Worth stating

- **Volume and quality are different things.** A thousand people at five percent
  completion is worse than a hundred at fifty.
- **Do not compare small channels head-on with large ones**: at twenty responses
  the share jumps around.
- **Responses with no label** deserve their own row, not "other": usually direct
  visits or a label lost in forwarding.

## What not to do

- **Do not infer the channel from arrival time** — no label means no answer.
- **Do not advise switching a channel off** after a single run.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

