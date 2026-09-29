<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Deliver the leads</sub>

# New response notifications

**Sets up where new responses are announced, and fixes it when they stop arriving**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-answer-notifications` | 1.0.0 | 11 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-answer-notifications-en.zip) |

## What it does

1. **Looks at what is already set.** Whether email is on, who the recipients are, whether Telegram and MAX are connected and whether the plan blocks them. Before edits, not instead of them.
2. **Remembers address confirmation.** The most common cause of «we set it up and nothing arrives»: the address is added but not confirmed. The setup looks complete either way.
3. **Does not stuff the email.** A contact and two or three key answers beat the full questionnaire: nobody reads a twenty-question email.
4. **Verifies with a test send.** A messenger can be checked immediately instead of waiting for a live respondent. If the bot is not in the chat, the assistant gives the steps rather than doing it for you.

## What you get

| In the email | Recipients | Channels | Check |
|:-:|:-:|:-:|:-:|
| **3** | **2** | **2** | **test send** |
| <sub>questions out of nine</sub> | <sub>one actually works</sub> | <sub></sub> | <sub>no waiting for a respondent</sub> |

| | | |
|---|---|---|
| **sales@example.com** | email · address confirmed | on |
| **marketing@example.com** | email · code sent, not confirmed | not sending |
| **Telegram, «Leads» group** | test message delivered | on |
| **MAX** | not included in the plan | unavailable |

> **The second address looks configured but receives nothing**  
> Until the address is confirmed with the code from the email, delivery to it never starts. This is the single most common reason for «notifications are not arriving».

<sub>The setup above is an example. The assistant reports the state of your own survey.</sub>

## How to ask

> Set up email notifications for new responses

> Send leads to our Telegram group

> Notifications stopped arriving — why?

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `add_quiz_email_recipient` | Add answer copy recipient | write |
| `confirm_quiz_email_recipient` | Confirm recipient address | write |
| `get_integration_logs` | Messenger delivery log | read |
| `get_quiz_email_settings` | Quiz email settings | read |
| `get_quiz_integrations` | Quiz integration state | read |
| `manage_quiz_messenger` | Telegram and MAX notifications | destructive |
| `resend_integration_logs` | Resend to messenger | write |
| `save_quiz_email_template` | Quiz email template | write |
| `set_quiz_email_questions` | Questions included in the email | write |
| `toggle_quiz_email` | Quiz emails on and off | write |
| `toggle_quiz_email_recipient` | Recipient on and off | write |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
