<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Check before launch</sub>

# Pre-launch check

**Finds what will break on real respondents while the link is still unsent**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-prelaunch-check` | 1.0.0 | 5 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-prelaunch-check-en.zip) |

## What it does

1. **Reads the whole survey first.** Structure, logic, wording and publication state — before judging anything the assistant looks at what is actually there.
2. **Walks every route to the end.** Dead ends, unreachable questions, conditions on deleted questions, a «greater than» operator on a text field — the things that surface on live respondents.
3. **Checks where the responses will land.** A survey with no recipients and no integrations collects in silence. An unconfirmed address looks configured but never receives mail.
4. **Hands over a list and waits.** Nothing is fixed quietly: findings come sorted by severity, and the decision to fix is yours.

## What you get

| Breaks collection | Hurts data | Minor | Clean |
|:-:|:-:|:-:|:-:|
| **2** | **3** | **4** | **3** |
| <sub>fix before sending</sub> | <sub></sub> | <sub></sub> | <sub>checked, nothing to report</sub> |

| | | |
|---|---|---|
| **The «never used the service» branch leads nowhere** | logic · question 6 | critical |
| **No email recipients and no integrations at all** | where responses land | critical |
| **Recipient address is not confirmed** | email · marketing@… | important |
| **Phone is required at question three of nine** | questions | important |
| **The finish screen has no text** | copy · finish | important |
| **Button labels are still the defaults** | copy | minor |

> **Not ready to publish yet**  
> Two findings will lose responses outright: the dead end in the logic and leads nobody receives. The rest can wait until after launch.

<sub>The findings above are an example. In your account the check runs against your survey.</sub>

## How to ask

> Check the survey before launch — is everything ready

> I am about to send the link, did I forget anything?

> Find logic and copy problems before I publish

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_email_settings` | Quiz email settings | read |
| `get_quiz_integrations` | Quiz integration state | read |
| `get_quiz_list` | Quiz list | read |
| `get_quiz_structure` | Quiz structure | read |
| `get_quiz_texts` | Quiz default texts | read |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
