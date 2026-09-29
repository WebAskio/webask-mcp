---
name: webask-quiz-distribution
description: "Prepares a WebAsk survey for distribution: link address, QR code, passwords for restricted access, source labels and a printable version. Use when someone asks how to send out a survey, where to get the link, or how to tell which channel the responses came from."
---

# Distributing the survey

The survey is ready; the question now is how people receive it and how you later
tell where they came from.

Reply to the person in the language they write in.

## The link

`set_quiz_link` — the address the survey opens at. A short, meaningful address is
easier to remember and less alarming in a message.

**Source labels matter most here.** If the survey goes to several places — a
mailing, social media, a banner — labels attached to the link let you separate the
responses later. Without them everything merges and there is no way to tell what
worked. Values collected in responses come from `get_answer_extra_field_values`.

Suggest labels up front, not after the mailing has gone out: they cannot be added
retroactively.

## QR code

`manage_quiz_qr_code` — for offline: a table sticker, a conference slide, a flyer.
Format, size and colour can be set, and a logo placed in the centre.

Verify the code points at the right address **before** printing a run.

## Restricted survey

`manage_quiz_passwords` — passwords when the survey is not for everyone. They are
created in batches, and different groups can get different ones.

Up to fifty per call: for more, make several passes.

## Printable version

`export_quiz_print` — the survey as PDF, Word, HTML or plain text. Needed when the
questionnaire is filled on paper or the wording is approved with a client before
launch.

## Order when asked "how do I send this out"

1. Check the survey is published: an unpublished one will not open.
2. Agree on source labels for the channels named.
3. Hand over one labelled link per channel.
4. Add a QR code if there is an offline channel.
5. Mention that results can be compared by channel in the report.

## What not to do

- **Do not publish the survey unasked**, even if it is clearly ready.
- **Do not change the address of a survey already sent out** — existing links stop
  working. If asked to, warn about it.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

