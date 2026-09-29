---
name: webask-integration-triage
description: "Finds why responses to a WebAsk survey do not reach an external system, and fixes it. Use when someone reports that leads are not arriving in their CRM, notifications are missing in Telegram or MAX, rows are not added to a Google Sheet, or a webhook does not fire."
---

# Why responses are not leaving the survey

A silent integration has four different causes, each with a different fix. Work
strictly in order: every next step costs more than the previous one.

Reply to the person in the language they write in.

## 1. Get the survey id

Nothing can be done without it. If the survey was named in words, find it with
`get_quiz_list` and confirm it is the right one before changing anything.

## 2. Read the state: `get_quiz_integrations`

Returns every integration with a ready-made reason. This covers most requests and
costs nothing.

| Reason | Meaning | What to do |
|---|---|---|
| `blocked_by_tariff` | not included in the plan | state it plainly and stop, see the prohibition below |
| `not_connected` | no connection at all | connecting happens in the web app: give the steps, do not attempt it |
| `disabled` | connected, sending switched off | ask whether that was deliberate; enable only with consent |
| empty | settings are fine | go to step 3 |

Webhooks are not in this response — they have their own setup, see step 5.

## 3. Find the refusal

Behaviour differs by system, because not everything has a log.

**Telegram and MAX** — `get_integration_logs`. The messenger's refusal text is
there: bot removed from the group, chat deleted, topic closed, token revoked. The
unsent counter shows how much is waiting.

**Bitrix24** — no log of its own; use `manage_quiz_crm` with the
`check` action. It reaches the portal and reports whether access is alive. Tokens
are revoked on the CRM side, and from the survey this looks exactly like a working
integration — so this step is mandatory even if step 2 was clean.

**Google Sheets** — `manage_quiz_google_sheets` with the `show` action. The usual
cause of silence is revoked access to the Google account.

## 4. Resend only after the cause is fixed

`resend_integration_logs` for messengers: one entry, or all failures in a period.

Resending while the cause is alive is pointless — the same refusal repeats and the
log fills with noise. The person fixes their side first: returns the bot to the
group, reissues the token, restores access.

## 5. Webhooks separately

`get_quiz_webhooks` — the list and whether each is enabled. `get_quiz_webhook_logs`
— the delivery log with the receiver's response code. `resend_quiz_webhook_log` —
resending.

Header values in responses are masked: they hold access keys to someone else's
system. Do not ask the person to read them out, and do not offer to overwrite a
header "to test" — editing a webhook rewrites it in full.

## What not to do

- **Do not suggest a plan upgrade and do not link to checkout.** When the plan
  blocks an integration, name the reason and stop.
- **Do not enable sending yourself** — a disabled integration is often disabled on
  purpose.
- **Do not resend "just in case"** — see step 4.

## What to say at the end

Three things: which integration is silent, for what exact reason, and what the
person needs to do. If the cause was fixed and the backlog resent — how many went
out.