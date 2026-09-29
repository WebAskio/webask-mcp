<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Deliver the leads</sub>

# Webhook setup

**Sets up delivery of responses to your address and checks right away that the receiver accepted them**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-webhook-setup` | 1.0.0 | 9 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-webhook-setup-en.zip) |

## What it does

1. **Looks at what is already set up.** A second webhook to the same address is almost always a mistake. The assistant checks the list before creating, not after.
2. **Asks the four things nothing works without.** Address, method, which fields to send and what to call them. Field names to match your system — via renaming, not by chance.
3. **Careful with unfinished completions.** If abandoned completions are wanted, send them with a delay — otherwise a person who returns to finish arrives twice.
4. **Verifies delivery immediately.** Reads the log: 200 works, 4xx the receiver rejected, 5xx their error. Does not resend while the receiver keeps failing.

## What you get

| Fields | Unfinished | Deliveries | Errors |
|:-:|:-:|:-:|:-:|
| **3** | **no** | **47** | **0** |
| <sub>of nine questions</sub> | <sub></sub> | <sub>this week</sub> | <sub></sub> |

| | | |
|---|---|---|
| **https://crm.example.com/hooks/webask** | method post · finished only | enabled |
| **phone ← "Your phone"** | field renamed | required |
| **rating ← "How happy are you?"** | field renamed | — |
| **Authorization: ******** | header · value masked | set |
| **Last delivery** | 10 September 14:02 · receiver answered 200 | delivered |

> **The receiver accepted the first response — code 200**  
> The webhook works. If the receiver starts answering 4xx, the assistant will not resend blindly: cause first, retry second.

<sub>The address and fields above are an example. The setup is built for your system.</sub>

## How to ask

> Set up a webhook to send responses to our server

> Send the phone from the survey to our CRM as a field called phone

> Check whether responses are arriving via the webhook

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `create_quiz_webhook` | Create webhook | write |
| `delete_quiz_webhook` | Delete webhook | destructive |
| `get_quiz_structure` | Quiz structure | read |
| `get_quiz_webhook_logs` | Webhook delivery log | read |
| `get_quiz_webhooks` | Quiz webhooks | read |
| `get_workspace_tariff` | Workspace plan | read |
| `resend_quiz_webhook_log` | Resend webhook | write |
| `toggle_quiz_webhook` | Webhook on and off | write |
| `update_quiz_webhook` | Update webhook | write |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
