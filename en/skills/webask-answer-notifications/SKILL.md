---
name: webask-answer-notifications
description: "Sets up and repairs notifications about new responses to a WebAsk survey — emails to recipients, messages in Telegram and MAX. Use when someone wants responses delivered to their inbox, wants to add a recipient, or asks why notifications stopped arriving."
---

# Where new responses are announced

The most common setting in WebAsk and the most common cause of "responses are
coming in and nobody knows".

Reply to the person in the language they write in.

## 1. See what is already set

`get_quiz_email_settings` — are survey emails on, who receives them, which
questions go into the message.

`get_quiz_integrations` — are Telegram and MAX connected and allowed by the plan.

## 2. Email

- Add a recipient — `add_quiz_email_recipient`.
- **The address must be confirmed**: a code is sent to it, and until it is
  confirmed nothing is delivered. The setting still looks complete — this is the
  single most common cause of "we set it up and get nothing". Confirm with
  `confirm_quiz_email_recipient`.
- Turn delivery on and off — `toggle_quiz_email` for all, or
  `toggle_quiz_email_recipient` for one person.
- What goes into the message: `set_quiz_email_questions` and
  `save_quiz_email_template`.

Do not put every question into the email when there are many: the contact and two
or three key answers are more useful than the whole questionnaire.

## 3. Messengers

`manage_quiz_messenger` — state, activation, question selection, and a `test`
action. A test send is the best way to verify the setup without waiting for a live
respondent.

Connecting the bot to a chat happens in the web app, where a messenger login is
required. If the bot is not connected, say so and give the steps rather than
attempting it.

## If it stopped working

1. `get_quiz_integrations` — switched off, or blocked by the plan.
2. For messengers, `get_integration_logs` — the refusal text is there: bot removed
   from the group, chat deleted, token revoked.
3. For email, check address confirmation and whether the recipient is disabled.
4. Once the cause is fixed, `resend_integration_logs` delivers the backlog.
   Resending earlier is pointless: the same refusal repeats.

## What not to do

- **Do not enable notifications the person switched off deliberately** — ask.
- **Do not resend before the cause is fixed.**
- **Do not add your own or a guessed address** — only the one given.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

