---
name: webask-webhook-setup
description: "Sets up delivery of WebAsk survey responses to an external URL via webhook — address, method, which fields and their names, headers, whether to send unfinished completions. Use when someone asks to send responses to their own server or system, to Make or n8n, to change webhook fields, or to turn a webhook on or off."
---

# Webhook: responses to your own address

A webhook is the most direct way to get responses into your own system: every
response goes out as an HTTP request to the given address. Quick to set up, quiet
when it breaks — so order matters more than speed here.

Reply in the language the person writes in.

## 1. Check that webhooks are available

`get_workspace_tariff` — webhooks are not part of every plan. If they are not
available, say so right away and stop: collecting the address, method, field set
and headers only to hit a refusal at the last step wastes the conversation.

## 2. See what already exists

`get_quiz_webhooks` — the survey's webhooks and whether each is on. A second webhook
to the same address is almost always a mistake, not a wish: check before creating.

## 3. Find out four things

Nothing can be created without them:

| What | Why |
|---|---|
| **Address** | where to send; `https` only, the receiver must answer 2xx |
| **Method** | `post` almost always; `get`, `put`, `patch` if the receiver demands |
| **Which fields** | a phone and two or three key answers beat the whole questionnaire — easier for the receiver |
| **Field names** | if the system expects `phone` and our question is "Your phone", rename via `body_naming` |

Question names and identifiers come from `get_quiz_structure`.

## 4. Create

`create_quiz_webhook`: a title (for yourself, to tell them apart), address, method,
fields (`body`), renaming (`body_naming`), headers (`headers` — access keys for the
receiver go here).

**Unfinished completions** — `incomplete` and `hours`. By default only finished ones
are sent. If abandoned ones are wanted too, send them with a delay (1, 6, 12 or 24
hours): otherwise a person who comes back to finish arrives twice.

## 5. Verify delivery

Right after creating — `get_quiz_webhook_logs`: the receiver's response code and
body. `200` — working. `4xx` — the receiver rejected it: usually the address, method
or body format. `5xx` — an error on their side. An empty log means no responses yet;
that is not an error.

Do not resend with `resend_quiz_webhook_log` while the receiver answers with an
error: the same thing will happen again.

## Change, disable, delete

- Fix the address or fields — `update_quiz_webhook`. **An update overwrites the
  whole webhook**, headers included: header values come back masked with
  asterisks, so ask the person for them again before updating rather than
  writing them back empty.
- Disable while they fix their side — `toggle_quiz_webhook`, not delete.
- Delete — `delete_quiz_webhook`, only on a direct request: the settings cannot be
  recovered.

## What not to do

- **Do not create a second webhook to the same address** without asking.
- **Do not send every question** when there are many — the receiver needs the right fields.
- **Do not ask the person to dictate access keys into the chat** — ask them to put
  the keys into headers in the app, or insert only what they themselves sent.
- **Do not enable a webhook that was disabled on purpose.**
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
