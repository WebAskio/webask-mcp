---
name: webask-response-funnel
description: "Works out where respondents abandon a WebAsk survey and explains why. Use when someone complains about few responses, low conversion, many incomplete submissions, or asks why the survey is not finished."
---

# Where the survey is abandoned

"Few responses" rarely means few people arrived. Usually one specific question is
where people close the tab.

Reply to the person in the language they write in.

## Build the picture

1. `get_quiz_summary` — total submissions and how many completed.
2. `get_quiz_report` filtered to incomplete ones — where they stopped.
3. `get_quiz_structure` — question order and types, to tie a position to content.

Compute the completion share and the number of answers per question: the last
answered question is where the drop happens.

**If the report has no incomplete submissions.** Showing them is not part of
every plan: `get_workspace_tariff` tells whether it is available. When it is not,
say so plainly — there is nothing to compute the drop-off point from. What is
left is the completion share from `get_quiz_summary` and a reading of the form
itself: length, order, required questions. That is weaker, and the person should
be told, not handed a guess dressed up as a measurement.

## Reading it

- **A steady few percent decline** from question to question is normal.
- **A cliff at one question** — that is the problem. Look at it closely.
- **A cliff on the first screen** — not the question but the promise: people did
  not understand what it is for, or saw that it is long.
- **A cliff at the last step** — almost always contacts: asked before the person
  understood why they should give them.

## Common causes by type

| Question | Why people leave |
|---|---|
| Open text | typing is effort, especially on a phone |
| Required contact | unclear why, and not trusted |
| A ten-row matrix | looks like work |
| A long option list | nobody wants to read it |
| File upload | awkward on a phone |
| A personal question with no explanation | feels intrusive |

## What to propose

Not "shorten the survey" but specifics: make this one optional, move that one
later, split this matrix, add one line explaining why you ask.

Ask for contacts at the end, after the person has already invested effort.

## What not to do

- **Do not compute conversion over all submissions** if some are your own test
  runs — cut them off by date first.
- **Do not draw conclusions from twenty submissions.**
- **Do not edit the survey yourself** — present the findings and propose.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

