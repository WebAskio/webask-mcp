---
name: webask-benchmark
description: "Compares WebAsk survey results against each other: one questionnaire across periods, or different surveys in the account. Use when someone asks whether things improved, how ratings changed, or which survey performs better."
---

# Comparing with your past self

A single number means almost nothing: is 4.2 good or bad? Meaning appears only
against a previous measurement.

Reply to the person in the language they write in.

## Two kinds of comparison

**One survey across periods** — waves. The most reliable: same questionnaire, same
audience, only time differs.

**Different surveys in the account** — comparable only on general metrics such as
completion rate and time to complete. Substantive answers cannot be compared when
the questions differ.

## How to collect

For waves: `get_quiz_report` filtered by date, once per period.

For different surveys: `get_quiz_list`, then `get_quiz_summary` for each.

**Check `get_quiz_versions` before comparing.** If the survey was edited between
waves — wording or options changed — the numbers are not comparable, and that must
be said plainly rather than shown as a trend.

## What to compare

| Metric | What a change means |
|---|---|
| Average rating | a shift in audience sentiment |
| Distribution across options | more precise than the average: shows where the shift came from |
| Completion share | a change in the questionnaire or in audience quality |
| Number of responses | distribution activity, not product quality |

Look at the distribution, not only the average: the average can hold steady while
half the satisfied move to dissatisfied and the other half the other way.

## How to answer

- **State direction and size.** "The average rose from 4.0 to 4.3" — and how many
  responses each is based on.
- **Say whether it is meaningful.** On small samples, tenths mean nothing.
- **Do not explain a cause that is not in the data.** A guess can be offered, but
  labelled as a guess.

## What not to do

- **Do not compare periods of different length** without normalising.
- **Do not compare waves with an edited questionnaire** in between without saying so.
- **Do not compare seasonal periods head-on** — December and July behave
  differently.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

