<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Understand the results</sub>

# Comparing with past results

**Compares the survey with its own past: one figure means nothing, a change does**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-benchmark` | 1.0.0 | 4 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-benchmark-en.zip) |

## What it does

1. **Checks comparability first.** If wording or answer options changed between waves, the numbers are not comparable — and that is said plainly instead of showing a «trend».
2. **Looks at the distribution, not just the average.** The average can stay flat while half the satisfied group moved to dissatisfied and the other half moved the other way.
3. **Separates the two kinds of comparison.** One survey across periods is reliable. Different surveys can only be compared on shared metrics such as completion rate.
4. **Says whether the difference is significant.** On small samples a tenth of a point means nothing, and the assistant names that instead of presenting it as growth.

## What you get

| Spring | Autumn | Change | Survey |
|:-:|:-:|:-:|:-:|
| **4.0** | **4.3** | **+0.3** | **unchanged** |
| <sub>286 responses</sub> | <sub>318 responses</sub> | <sub></sub> | <sub>no edits between waves</sub> |

| Item | | |
|---|---|--:|
| Very satisfied · spring | `███░░░░░░░` | 31% |
| Very satisfied · autumn | `████░░░░░░` | 42% |
| Very dissatisfied · spring | `█░░░░░░░░░` | 11% |
| Very dissatisfied · autumn | `░░░░░░░░░░` | 5% |

> **The gain is real, and it lives at the edges**  
> The average moved three tenths, but the interesting part is elsewhere: the very dissatisfied group halved and the very satisfied group grew noticeably. The middle barely moved.

<sub>The numbers above are an example. Your own periods and surveys are compared.</sub>

## How to ask

> Compare the autumn wave of the survey with the spring one

> Did things get better or worse since the last measurement

> Compare completion rates across two surveys in the account

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_list` | Quiz list | read |
| `get_quiz_report` | Quiz report | read |
| `get_quiz_summary` | Quiz summary | read |
| `get_quiz_versions` | Quiz publication history | read |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
