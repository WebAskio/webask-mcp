<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Understand the results</sub>

# What the survey showed

**Answers «so what did the survey say» with figures and a conclusion, not a raw export**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-results-digest` | 1.0.0 | 6 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-results-digest-en.zip) |

## What it does

1. **Takes the summary, not one response at a time.** Distributions are already calculated. Raw completions are needed only for a specific person or to look at wording.
2. **Checks whether the data is complete.** If many completions were abandoned, they are counted separately instead of being folded into one number with the finished ones.
3. **Slices when a condition is named.** «September only», «only from the mailing» — filtering by dates and source tags rather than counting by eye.
4. **Leads with the conclusion.** Not «question 3 has this distribution», but «two thirds are unhappy with turnaround» — followed by the base that percentage is taken from.

## What you get

| Completions | Finished | Average score | With a contact |
|:-:|:-:|:-:|:-:|
| **412** | **318** | **4.1** | **186** |
| <sub></sub> | <sub>77%</sub> | <sub>out of 5</sub> | <sub>45% of those who started</sub> |

| Item | | |
|---|---|--:|
| Very satisfied | `████░░░░░░` | 134 · 42% |
| Somewhat satisfied | `███░░░░░░░` | 92 · 29% |
| Neutral | `██░░░░░░░░` | 48 · 15% |
| Somewhat dissatisfied | `█░░░░░░░░░` | 29 · 9% |
| Very dissatisfied | `░░░░░░░░░░` | 15 · 5% |

> **The headline: turnaround, not price**  
> In the free-text answers 41 of 96 respondents name the waiting time, and 12 name the price. The percentages above are taken from 318 finished completions; abandoned ones are excluded.

<sub>The numbers above are an example. The digest is built from your real responses.</sub>

## How to ask

> What did the survey show — give me the short version

> Show results for September only, and only for people from the mailing

> Summarise the survey and tell me what deserves attention

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `export_answers_xlsx` | Export answers to Excel | read |
| `get_answer_extra_field_values` | Link label values | read |
| `get_quiz_answers` | Quiz answers | read |
| `get_quiz_report` | Quiz report | read |
| `get_quiz_report_inputs` | Text answers of a question | read |
| `get_quiz_summary` | Quiz summary | read |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
