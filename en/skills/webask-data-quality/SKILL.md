---
name: webask-data-quality
description: "Checks the quality of collected WebAsk responses: too-fast submissions, flat-lined answers, duplicates and junk text. Use when someone doubts the data, suspects manipulation, or is preparing results to present."
---

# Can this data be trusted

Before building conclusions it is worth looking at what they are made of —
especially if the survey was distributed for a reward or through an open link.

Reply to the person in the language they write in.

## What to check

**Too fast.** Completed in less time than it takes to read the questionnaire. Rule
of thumb: at least five seconds per question; for ten questions, anything under a
minute is suspicious.

**Flat-lined.** The first option everywhere, one rating throughout, a whole matrix
column.

**Duplicates by contact.** The same phone or email several times. Sometimes honest
— a double submission by mistake — but in a rewarded survey it is manipulation.

**Junk text.** "Aaa", "123", random letters in a required open field.

**Contradictions.** "Never used the service" followed by a detailed rating of it.
Usually this means the display logic is wrong, not that the person lied.

**Time spikes.** Twenty submissions in a minute with an identical answer pattern.

## How to collect

`get_quiz_answers` with filters and `get_quiz_report` — one trait at a time. Texts
for the junk check come from `get_quiz_report_inputs`.

## How to present

Per trait: how many submissions match and what share of the total. Separately: how
many unique submissions remain if all of it is removed, and how the key numbers
change.

That last part matters most: if the conclusions hold after cleaning, there is no
need to clean.

## What to do with findings

Propose, do not act:

1. Tag them — the data stays, but the doubtful ones are marked.
2. Hide from reports — reversible.
3. Delete — only on explicit request and with confirmation.

Start with the first.

## What not to do

- **Do not call low ratings and harsh comments junk.** An unhappy respondent is not
  manipulation.
- **Do not delete anything yourself** off the back of this check.
- **Do not trim the sample** toward a desired result.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

