---
name: webask-quiz-timeline
description: "Shows the history of a WebAsk survey over time: when it was published, when responses came in, where the spikes and drops are. Use when someone asks why responses stopped, what changed, or how collection went over a period."
---

# Survey timeline

"Why did responses stop" is answered by lining up two things: how responses came in
and what was done to the survey.

Reply to the person in the language they write in.

## Two lines

**Responses over time** — `get_quiz_report` filtered by date, by week or by day
depending on how long collection ran.

**Edit history** — `get_quiz_versions`: every publication leaves a snapshot, so it
is visible when the survey changed and which version was live at each moment.

## Line them up

Find matches by date:

- **A drop right after a publication** — something was broken by an edit: a logic
  branch, a required field, the link address.
- **A drop with no edits** — an outside cause: the mailing or campaign ended, the
  banner came down, the event finished.
- **A spike** — also useful: understand what worked and repeat it.
- **A steady decline** — normal decay: the audience the link reached ran out.

## Check separately

If the drop is sharp and to zero, check `get_quiz_integrations` and whether the
survey was unpublished. An unpublished survey stops opening immediately, which from
the outside looks exactly like people no longer answering.

## How to present

Briefly and by date: period, what happened, what it lines up with. Not a forty-row
table but a few anchor points.

One sentence of conclusion: "responses stopped on this date, apparently because of
that". If no link is found, say so rather than inventing one.

## What not to do

- **Do not pass a date coincidence off as a cause** when the edit could not have
  affected it.
- **Do not compare weekdays with weekends** without noting it: most surveys have a
  weekly rhythm.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

