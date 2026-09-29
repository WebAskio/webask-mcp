---
name: webask-quiz-logic
description: "Configures question display logic in a WebAsk survey — branching, skipping blocks, screening out unsuitable respondents and quotas. Use when someone wants different questions shown to different people, or reports that the survey routes respondents to the wrong place."
---

# Branching and routing

Logic is where surveys break silently: a condition references a question by
identifier, and a branch built blind leads the respondent into a dead end with no
way out.

Reply to the person in the language they write in.

## The order is strict

1. `get_quiz_structure` — read the current state and question identifiers.
2. Build the change against what actually exists.
3. `update_quiz_logic` — write.

The first step cannot be skipped. Identifiers cannot be guessed, and writing over
questions that do not exist produces a survey that will not open.

## What can be built

- **Branch on an answer.** "Rated below four — ask why."
- **Skip a block.** "Did not use the service — do not ask about its quality."
- **Screen out.** A respondent who does not fit belongs on a `screenout` screen,
  not driven to the end and cleaned up afterwards.
- **Quotas.** Once a group is full, stop admitting it.

## Rules people trip over

- **Every branch needs an exit** — to the next block or to the finish screen.
- **A condition on "Other"** matches the option, not the text typed into it.
- **The operator must fit the question type.** Greater/less than are for numbers
  and scales, not for text or choices.
- **Order matters**: the first matching condition wins.
- **A branch must not lead back** to an already answered question — the respondent
  ends up in a loop.

## After the edit

Walk the route by eye: from the first question along every branch to the finish. If
there are more than three or four branches, describe the map in words — who ends
up where.

## What not to do

- **Do not write logic without reading the structure.**
- **Do not change the question set in the same edit** — when something breaks it
  becomes unclear which change caused it.
- **Do not build branching where one question with options is enough.**
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

