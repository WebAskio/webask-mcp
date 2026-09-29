<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Deliver the leads</sub>

# Lead quality

**Counts usable contacts, not completion rate**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-lead-quality` | 1.0.0 | 4 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-lead-quality-en.zip) |

## What it does

1. **Makes the right number the headline.** Share of people who left a contact, out of everyone who started. Completion can be high while leads are almost absent.
2. **Finds where they changed their mind.** It compares the question before the contact field with the field itself: the gap shows how many got there and still closed the tab.
3. **Filters out the unusable.** Obviously fake numbers, 123@123.ru addresses, one-letter names — a lead with a dead phone number is not a lead and does not count.
4. **Splits by channel.** If the link carried source tags, you can see where there are more leads and where they are better. Those are different channels more often than not.

## What you get

| Started | Reached the contact | Left a contact | Usable |
|:-:|:-:|:-:|:-:|
| **512** | **243** | **186** | **164** |
| <sub></sub> | <sub>47%</sub> | <sub></sub> | <sub>32% of those who started</sub> |

| Item | | |
|---|---|--:|
| Email to the base | `████░░░░░░` | 38% usable |
| Telegram channel | `███░░░░░░░` | 31% |
| Website banner | `██░░░░░░░░` | 19% |
| No tag | `██░░░░░░░░` | 24% |

> **The loss is not in the survey, it is at the moment you ask**  
> 57 people reached the phone field and left it empty. One line explaining why the number is needed usually lifts that share more than any styling change.

<sub>The numbers above are an example. The count runs on your responses and your tags.</sub>

## How to ask

> How many usable leads did this survey collect

> Break down lead quality and tell me where we lose them

> Which channel brings better leads

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_answer_extra_field_values` | Link label values | read |
| `get_quiz_report` | Quiz report | read |
| `get_quiz_structure` | Quiz structure | read |
| `get_quiz_summary` | Quiz summary | read |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
