<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Deliver the leads</sub>

# Why responses are not delivered

**Finds why leads never reach your CRM, Telegram or spreadsheet — and what to do about it**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-integration-triage` | 1.0.0 | 9 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-integration-triage-en.zip) |

## What it does

1. **Goes from cheap to expensive.** It reads integration state first: that covers most cases and costs nothing. Anything further only if the reason is still unknown.
2. **Pulls the actual rejection text.** The bot was removed from the group, the chat is gone, the token was revoked, Google access was withdrawn — the delivery log names the reason in words.
3. **Checks CRMs separately.** Bitrix24 keeps no log: a token revoked on the portal side looks like a healthy integration. So access is verified by a live request.
4. **Resends only after the fix.** A retry against a live failure repeats the same rejection and doubles the noise in the log. Cause first, resend second.

## What you get

| Waiting to retry | Causes | Fixed in the app | Will resend |
|:-:|:-:|:-:|:-:|
| **148** | **3** | **2** | **148** |
| <sub>piled up over 6 days</sub> | <sub></sub> | <sub>requires signing in</sub> | <sub>once the cause is gone</sub> |

| | | |
|---|---|---|
| **Telegram** | bot removed from the «Leads» group on 3 September | failing |
| **Bitrix24** | portal access verified, responding | healthy |
| **Google Sheets** | Google account access revoked | failing |
| **Website webhook** | receiving side answers 500 | failing |
| **Email notifications** | recipient confirmed, delivery running | healthy |

> **The main cause: the bot was kicked out of the group**  
> Put the bot back in the «Leads» chat and the 148 queued messages go out in one retry. Resending while it is outside the group just repeats the same rejection.

<sub>The states above are an example. In your account your own integrations are checked.</sub>

## How to ask

> Leads are not reaching Bitrix — find out why

> Telegram notifications stopped arriving, what happened?

> Check every integration on this survey and resend what piled up

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_integration_logs` | Messenger delivery log | read |
| `get_quiz_integrations` | Quiz integration state | read |
| `get_quiz_list` | Quiz list | read |
| `get_quiz_webhook_logs` | Webhook delivery log | read |
| `get_quiz_webhooks` | Quiz webhooks | read |
| `manage_quiz_crm` | Sending answers to CRM | write |
| `manage_quiz_google_sheets` | Google Sheets export | destructive |
| `resend_integration_logs` | Resend to messenger | write |
| `resend_quiz_webhook_log` | Resend webhook | write |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`references/reasons.md`](references/reasons.md) — reference the skill loads on demand
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
