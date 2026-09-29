---
name: webask-ab-significance
description: "Compares A/B variants of a WebAsk survey and checks whether the difference is real or within noise. Use when someone asks which variant performs better or is about to make a decision based on a test."
---

# Comparing A/B variants

The main A/B mistake is deciding on random noise. On fifty responses a ten percent
difference appears by itself, for no reason at all.

Reply to the person in the language they write in.

## Collect

`get_quiz_summary` and `get_quiz_report` filtered by variant. For each variant you
need: how many saw it, how many finished, and the target metric.

Ask first what counts as success: completion share, share leaving a contact,
average rating. Without that there is nothing to compare.

## Compute

1. The metric per variant with its base: "42 of 180" beats "23%".
2. The difference in percentage points, not percent of a percent.
3. Whether there is enough data. Rule of thumb: a five point difference needs
   hundreds per group, a twenty point one needs dozens. Below a hundred per group
   a difference can rarely be called proven.
4. That the groups are comparable: same period, same traffic source.

## How to answer

Three possible conclusions — pick one honestly:

- **There is a difference.** State its size and what it means in practice.
- **There is no difference.** The variants perform the same, which is also a
  result: choose either on other grounds.
- **Not enough data.** Say how much more is needed and give no recommendation.

The third is the most common and the least popular — and giving it honestly matters
more than guessing.

## What not to do

- **Do not declare a winner on a couple of points** on a small sample.
- **Do not compare variants from different periods** — seasonality breaks it.
- **Do not peek and stop the test** the moment the preferred variant pulls ahead.
- **Do not call a difference significant because it is badly wanted.**
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

