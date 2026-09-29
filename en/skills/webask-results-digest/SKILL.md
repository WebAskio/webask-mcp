---
name: webask-results-digest
description: "Explains what a WebAsk survey showed: pulls the summary, slices and exports and turns them into conclusions. Use when someone asks about survey results, wants to compare periods, or needs figures for a report."
---

# What the survey showed

The answer is not a dump of raw responses — it is a few numbers with an
explanation of what they mean.

Reply to the person in the language they write in.

## Which tool for what

This is where the wrong tool gets picked most often:

| What you need | Tool | What it returns |
|---|---|---|
| Overall picture | `get_quiz_summary` | distributions, ready percentages |
| A filtered slice | `get_quiz_report` | the same, over selected responses |
| Individual submissions | `get_quiz_answers` | raw responses one by one |
| Free text of one question | `get_quiz_report_inputs` | all text answers |
| A file for a human | `export_answers_xlsx` and other `export_*` | a download link |

**Start with the summary, not with raw answers.** Raw answers are for a specific
submission or for quoting examples.

## Order

1. `get_quiz_summary` — how many submissions, what the distributions are.
2. Check whether the data is complete: how many finished, how many were abandoned.
   If many were abandoned, say so and treat them separately.
3. If a condition was named — "September only", "only from the mailing" — build a
   slice with `get_quiz_report`. Values for filtering by link labels come from
   `get_answer_extra_field_values`.
4. Export a file only if a file was asked for. The link lives for one hour.

## How to answer

- **Conclusion first, numbers second.** Not "question 3 has this distribution" but
  "two thirds are unhappy with turnaround times — here is the breakdown".
- **Always name the base** for a percentage: all submissions or completed ones.
- **Do not present conclusions from ten responses as fact.**
- **Do not retell free text one by one** — group it into themes with a couple of
  representative quotes.

## What not to do

- **Do not export a file unasked** — chat needs numbers, not an XLSX link.
- **Do not recompute by hand** what the summary already provides.
- **Do not mix completed and abandoned** in one figure without saying so.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

