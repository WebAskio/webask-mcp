<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Build and share</sub>

# Launch kit

**Puts the whole launch together at once: tagged links, announcement copy and a QR code**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-launch-kit` | 1.0.0 | 4 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-launch-kit-en.zip) |

## What it does

1. **Starts from the channels.** Email, social, messenger, banner, offline — each gets its own tagged link, otherwise there is no way to tell later what worked.
2. **Writes copy per channel.** Email: a subject line without the word «survey» and two lines in the body. Social: one sentence. Banner: five words. One rule: why it matters and how long it takes.
3. **Does not oversell.** No «takes a minute» for a fifteen-question survey and no invented figures like «10,000 customers already chose us».
4. **Checks where responses land.** Before the send, not after: if notifications are not configured, the assistant offers to set them up while the link is still unsent.

## What you get

| | | |
|---|---|---|
| **«Three questions about your visit»** | email to the base · subject, two lines and a button | email-sep |
| **«Been in this week? Tell us how it went — 2 minutes»** | telegram channel · one line and a link | tg-channel |
| **«How was our service?»** | website banner · five words | site-banner |
| **QR code with a logo** | counter sticker · 600 px | offline-qr |

> **Before you send: responses currently go nowhere**  
> The survey has no email recipients and no active integrations. Worth setting up now — after the send the first leads will pile up in silence.

<sub>The copy and tags above are an example. Announcements are written for your audience and channels.</sub>

## How to ask

> Prepare everything for the launch: links, copy, QR

> Write the survey announcement for email and for Telegram

> We are launching across three channels — make the tagged links

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_email_settings` | Quiz email settings | read |
| `get_quiz_integrations` | Quiz integration state | read |
| `manage_quiz_qr_code` | Quiz QR code | write |
| `set_quiz_link` | Quiz link address | write |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
