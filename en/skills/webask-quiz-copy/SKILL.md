---
name: webask-quiz-copy
description: "Rewrites the copy of a WebAsk survey so that people finish it: question wording, button labels, welcome and thank-you screens. Use when someone asks to improve a survey, make it clearer, or complains that it is not completed."
---

# Rewriting so people finish

Surveys are abandoned not because they are long but because at some question the
person stops seeing what is in it for them. Fixing the copy often beats cutting
questions.

Reply to the person in the language they write in. Write the survey copy in the
language of its audience.

## Start from data, not taste

`get_quiz_report` over incomplete submissions — which questions people quit on. Fix
those first, not the ones that merely look wrong.

If there are no responses yet, say so honestly: we edit by general rules now and
look at behaviour later.

Copy comes from `get_quiz_texts` and `get_quiz_structure`; writing goes through
`update_quiz_texts` and `update_quiz_widgets`.

## What to fix

| Problem | How it looks | Better |
|---|---|---|
| Officialese | "Rate the degree of satisfaction with services rendered" | "How happy are you with the work?" |
| Double question | "Were the price and the deadline good?" | two separate questions |
| Double negative | "Do you not think it should not…" | a direct question |
| Internal jargon | "Rate the front office" | "Rate the staff in the showroom" |
| Leading question | "How much did you enjoy our excellent service?" | "How was our service?" |
| Question without bounds | "How often do you visit?" | options: weekly, monthly, less often |

## The first screen

This is where most people are lost. It needs three things: **what is being asked**,
**how long it takes**, and **why the person should care**. The last one is usually
missing, and it is the one that decides.

"Customer satisfaction survey" is weak. "Three questions about your visit. Your
answers help us cut the queues" is not.

## Buttons and thank-you

Default labels work, but a human label on the last step lifts completion. The
thank-you screen is the place to say what happens next.

## Order of work

1. Show the proposed edits: before and after, question by question.
2. Wait for agreement.
3. Write.

Do not rewrite everything silently: copy is often agreed with a client or a legal
team.

## What not to do

- **Do not change the meaning of a question** for the sake of nicer wording:
  comparability with earlier responses breaks.
- **Do not edit copy of a survey already collecting responses** without warning —
  answers before and after stop being comparable.
- **Do not add or remove questions** — that is other work.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

