<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Build and share</sub>

# Distributing the survey

**Gets the survey ready to hand out so you can still tell which channel each response came from**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-quiz-distribution` | 1.0.0 | 5 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-quiz-distribution-en.zip) |

## What it does

1. **Starts with source tags.** One link, several places. Without tags the responses merge into one pile and cannot be separated afterwards — so tags are agreed before the send, not after.
2. **Gives one link per channel.** Email, social, messenger, banner — each gets its own address with a readable tag, not utm1 and utm2 that nobody decodes a month later.
3. **Covers the offline route.** A QR code with a choice of format, size and logo — for a sticker, a slide or a flyer. Verified before the print run, not after.
4. **Closes access when needed.** Passwords in batches of up to fifty, different ones for different groups. Plus a print version in PDF or Word when the survey is signed off on paper.

## What you get

| Address | Tags | Passwords | Print |
|:-:|:-:|:-:|:-:|
| **custom** | **4** | **50** | **PDF** |
| <sub>short and readable</sub> | <sub>one per channel</sub> | <sub>if the survey is closed</sub> | <sub>also Word, HTML, text</sub> |

| | | |
|---|---|---|
| **Email to the base** | tag email-sep | link |
| **Telegram channel** | tag tg-channel | link |
| **Website banner** | tag site-banner | link |
| **Counter in the showroom** | tag offline-qr · QR 600 px, logo in the centre | QR code |

> **The address of an already-sent survey stays put**  
> Old links stop opening, and the mailing has gone out. If the address really has to change, the assistant warns you before touching it.

<sub>The tags above are an example. Names are chosen to match your channels.</sub>

## How to ask

> How do I send this survey across several channels and tell them apart later

> Make a QR code for the survey to put on the counter

> I need a closed survey with passwords for twenty people

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `export_quiz_print` | Quiz print version | read |
| `get_answer_extra_field_values` | Link label values | read |
| `manage_quiz_passwords` | Passwords for a closed quiz | destructive |
| `manage_quiz_qr_code` | Quiz QR code | write |
| `set_quiz_link` | Quiz link address | write |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
