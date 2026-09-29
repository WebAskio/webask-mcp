---
name: webask-open-answers
description: "Analyses free-text answers from a WebAsk survey: finds themes, counts frequency and picks representative quotes. Use when someone asks to read the comments, understand what respondents write about, or summarise open answers."
---

# Analysing free-text answers

Open questions give the most valuable and the least convenient material: a hundred
lines of text that appear in the report as a plain list. The job is to turn them
into a few themes with numbers.

Reply to the person in the language they write in.

## Collect

`get_quiz_report_inputs` — all text answers for one question. If several questions
have text, take them one at a time: mixing answers to different questions produces
mush.

To filter first, use `get_quiz_report`, then pull texts for the selected responses.

## Analyse

1. **Extract themes** by meaning, not by wording: "waited long", "waited forty
   minutes" and "the queue" are one theme.
2. **Count.** How many answers per theme and what share of those who answered.
3. **Separate the empty ones.** "No", "all fine", "-" form a "no content" group:
   do not theme them, but do not hide them either — the size says something.
4. **Pick quotes.** One or two per theme, verbatim, the most characteristic.
5. **Note sentiment** where it is distinguishable: one theme can carry different
   attitudes.

## How to present

Themes by descending frequency. For each: a theme name in your own words, the
count, the share, one quote.

At the end: the two or three themes that recur most, which is what is worth acting
on.

## Honesty rules

- **Do not invent themes.** If the answers do not group, say so.
- **Do not bend results to expectations.** If they expected price complaints and
  people write about deadlines, report deadlines.
- **Quote verbatim**, typos included: a tidied quote stops being evidence.
- **Do not conclude from five answers.** Say the data is thin.

## What not to do

- **Do not mix answers to different questions** in one analysis.
- **Do not surface quotes containing personal data** — strip phone numbers and
  names out of the quote.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

