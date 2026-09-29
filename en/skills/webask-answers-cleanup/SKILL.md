---
name: webask-answers-cleanup
description: "Puts collected WebAsk responses in order: removes test and junk submissions, adds notes and tags, restores accidentally deleted ones. Use when someone asks to clean up responses, mark some of them, or complains about junk in the results."
---

# Cleaning up responses

Test runs, random clicks and duplicates distort the statistics. Cleaning restores
meaning to reports — but it is irreversible, and that is the main thing to keep in
mind.

Reply to the person in the language they write in.

## Look first, delete second

`get_quiz_answers` with filters — show exactly what would be affected: how many
submissions, over what period, selected by what trait. Delete only after consent.

## What does what

| Task | Tool |
|---|---|
| Hide a response from reports without deleting | `toggle_answer_visibility` |
| A note on a response | `set_answer_note` |
| Tags on a response | `tag_answer` |
| Account tag dictionary | `get_answer_tags`, `create_answer_tag`, `delete_answer_tag` |
| Move to trash, restore, delete permanently | `delete_quiz_answers` |
| Question order inside a response card | `set_answers_order_mode` |

## Three levels of removal

1. **Hide** — the response stays but leaves the reports. Reversible. Right choice
   when unsure.
2. **Trash** — removed but recoverable.
3. **Permanent** — nothing to recover from. Requires confirmation, and that
   confirmation must come from the person in words.

Start at level one. Offer level three only when permanent deletion is explicitly
requested.

## What people usually look for

- **Test submissions** — your own, made while building. Usually the earliest ones,
  before the send-out date.
- **Too fast** — completed quicker than the questionnaire can be read.
- **Flat-lined** — the first option everywhere, or one rating throughout.
- **Duplicates by contact** — the same phone or email several times.

Show them as separate groups with counts, not one long list.

## Tags and notes

The tag list belongs to the account, not to the survey, so the tag tools need the
account id — take it from `get_workspace_list`.

Tags beat deletion: the response stays in the statistics but is marked. "Call
back", "complaint", "needs work" are easier to work with than an exported sheet.

Create a new tag only if nothing suitable exists in the account dictionary —
otherwise you end up with three spellings of the same thing.

## What not to do

- **Do not delete permanently without explicit consent** for the specific volume.
- **Do not clean "outliers" by answer value** — low ratings are not junk.
- **Do not delete responses to improve the numbers.**
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

