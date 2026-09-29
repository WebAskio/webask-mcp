---
name: webask-prelaunch-check
description: "Checks a WebAsk survey before launch and finds what will break on live respondents. Use when someone is about to publish a survey, send out the link, or asks whether everything is ready."
---

# Checking a survey before launch

Survey mistakes surface after the link goes out, when part of the responses are
already collected through a broken questionnaire and cannot be compared with
anything.

Reply to the person in the language they write in.

## Order

Read `get_quiz_structure` (questions and logic), `get_quiz_texts` (labels) and
`get_quiz_list` (whether the survey is published and at what address), then walk
the list below. Fix nothing silently: show the findings first, then ask what to
repair.

## What to check

**Branching**

- Dead ends: a branch with no way forward and no way to finish.
- Unreachable questions: nothing routes to them.
- Conditions pointing at deleted or renamed questions.
- An operator that does not fit the question type — "greater than" on a text field.

**Questions**

- A choice question with no options.
- Required questions that do not need to be required: each one costs responses.
- Open text where a count is needed: a rating typed as text never reaches the
  summary.
- Excessive length: if there are more than fifteen questions, say so plainly.

**Texts**

- Empty headings, default button labels, missing thank-you text.
- Is there a `finish` screen at all? Without it the respondent hits a blank page.

**Where the answers will go**

- `get_quiz_integrations` — is anything enabled at all. A survey with no
  notifications collects responses in silence.
- `get_quiz_email_settings` — are recipients set and **are their addresses
  confirmed**. An unconfirmed address looks configured but receives nothing.
- If webhooks or messengers are set up, check the plan is not blocking them.

**Plan and access**

- Limits: number of surveys, responses, file storage.
- Is the survey published and reachable by link.

## What not to do

- **Do not fix silently.** List the findings and let the person decide.
- **Do not publish on your own initiative.**
- **Do not rewrite question wording** — that is separate work.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

## What to say at the end

Findings ordered by weight: what will break collection, what will degrade data
quality, what is merely worth improving. If everything is clean, say so — do not
invent remarks.