---
name: webask-lead-quality
description: "Analyses the quality of leads collected by a WebAsk survey: how many reached the contact question, which questions scare people off, and how leads differ by channel. Use when a survey works as a lead form and someone asks about the number or quality of leads."
---

# Lead quality, not lead count

When a survey works as a lead form, what matters is not the completion rate but how
many people left a usable contact and what can be done with them.

Reply to the person in the language they write in.

## Collect

`get_quiz_structure` — find the contact questions: `phone`, `email`, `fio`.

`get_quiz_summary` and `get_quiz_report` — how many submissions and how many carry
a filled contact.

`get_answer_extra_field_values` — source labels, if the link was distributed by
channel.

## Compute

1. **Share with a contact** out of everyone who started. That is the headline
   number, not completion.
2. **Where they are lost.** Compare answers on the question before the contact with
   the contact itself: the gap is people who got there and changed their mind.
3. **Contact usability.** Obviously fake numbers, `123@123.ru` addresses,
   one-character names. Count separately: a lead with a dead phone is not a lead.
4. **By channel**, if labels exist.

## What usually gets in the way

- **The contact is asked too early**, before the value is clear. Move it later.
- **Too much is asked.** Phone and email at once, plus city. Every extra field
  costs leads.
- **No reason given.** One line — "we will call to arrange a time" — lifts the
  share more than any design change.
- **A required contact in an otherwise optional survey** — people leave without
  even answering.

## How to present

Numbers first: started, reached the contact, left a usable contact, share of
starters. Then where they are lost and what to do, ordered by payoff.

With channels, a table plus a conclusion about where leads are better in substance,
not in count.

## What not to do

- **Do not count a submission without a contact as a lead.**
- **Do not dump contacts into chat** — they belong in an export or a CRM.
- **Do not advise removing every required field**: a lead without a contact is
  useless.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

