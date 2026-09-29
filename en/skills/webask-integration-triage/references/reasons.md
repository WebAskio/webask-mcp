# Integration failure reasons

Reference for the `webask-integration-triage` skill.

## Status codes from `get_quiz_integrations`

| Code | Meaning | Who fixes it |
|---|---|---|
| `blocked_by_tariff` | not included in the current plan | the account owner |
| `not_connected` | no connection: the account is not linked | the person, in the web app |
| `disabled` | connected, sending switched off | can be enabled from chat, with consent |
| empty | settings are fine, look in the log | — |

## Common Telegram and MAX failures

| In the log | What happened | What to do |
|---|---|---|
| bot blocked, kicked, not a member | the bot was removed from the group | return the bot, then resend |
| chat not found | the chat was deleted or changed id | connect the chat again |
| topic closed | the group topic is closed | reopen it or pick another chat |
| unauthorized, token | the token was revoked | reissue and reconnect |
| too many requests | temporary rate limit | nothing: these retry automatically |

The last case matters: it is **not** a failure. The message will be retried on its
own and needs no intervention.

## CRM

CRM has no log of its own. The only reliable check is `manage_quiz_crm` with the
`check` action, which reaches out to the portal.

If the connection is dead, the cause is almost always revoked access on the CRM
side — the administrator changed, or the integration token expired. It is restored
in the web app by reconnecting.

## Google Sheets

Silence almost always means revoked access to the Google account. Second most
common: the spreadsheet was deleted or the sheet renamed.

## Webhooks

Here the cause shows in the receiver's response code:

| Code | Meaning |
|---|---|
| 401, 403 | the receiver rejected authorisation: the header key changed |
| 404 | the address no longer exists |
| 5xx | a failure on the receiving side, worth resending later |
| no response | the address is unreachable or too slow |