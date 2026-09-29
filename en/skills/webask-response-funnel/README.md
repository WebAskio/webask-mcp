<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Understand the results</sub>

# Completion funnel

**Shows which question makes people close the tab — and why**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-response-funnel` | 1.0.0 | 4 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-response-funnel-en.zip) |

## What it does

1. **Finds the drop-off.** Counts how many people answered each question. Where the count falls, that is where the problem is.
2. **Explains the reason.** Open text, a required contact field, a ten-row matrix — each question type is abandoned for its own reasons.
3. **Separates normal from broken.** A couple of percent lost at every step is always there. A cliff at one question is not.
4. **Suggests specific edits.** Not «make the survey shorter», but which question to make optional and which one to move closer to the end.

## What you get

| Opened | Started | Finished | Drop-off |
|:-:|:-:|:-:|:-:|
| **1,284** | **912** | **318** | **question 5** |
| <sub></sub> | <sub>71% of those who opened</sub> | <sub>35% of those who started</sub> | <sub>minus 41% in one step</sub> |

| Item | | |
|---|---|--:|
| 1. Welcome | `██████████` | 912 · 100% |
| 2. How happy are you? | `██████████` | 874 · 96% |
| 3. Was it finished on time? | `█████████░` | 831 · 91% |
| 4. What could be better? (open text) | `███████░░░` | 602 · 66% |
| 5. Your phone number (required) | `████░░░░░░` | 355 · 39% |
| 6. Thank you | `████░░░░░░` | 318 · 35% |

> **The main loss is the required phone number at step five**  
> More than half of the people who got there walk away. Move the contact field after the thank-you screen and explain in one line why it is needed.

<sub>The numbers above are an example. In your account the funnel is built from real completions.</sub>

## How to ask

> Why does this survey get so few responses — find where people quit

> How many people finish the survey and where do they drop off?

> Break down the completion funnel and suggest what to fix

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_report` | Quiz report | read |
| `get_quiz_structure` | Quiz structure | read |
| `get_quiz_summary` | Quiz summary | read |
| `get_workspace_tariff` | Workspace plan | read |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
