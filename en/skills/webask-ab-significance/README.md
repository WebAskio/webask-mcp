<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Understand the results</sub>

# A/B variant analysis

**Tells you whether the difference between variants is real or just noise**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-ab-significance` | 1.0.0 | 2 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-ab-significance-en.zip) |

## What it does

1. **Counts from the base, not in percentages.** Not «23% against 19%», but «42 of 180 against 34 of 179» — numbers like that show what the conclusion rests on.
2. **Checks there is enough data.** On fifty responses a ten-point gap appears on its own. The skill says when it is too early to call it.
3. **Verifies the comparison is fair.** Different periods and different traffic sources break the comparison, and that is checked before a winner is named.
4. **Is willing to say «no difference».** That is a result too: it means the variant can be chosen on other grounds.

## What you get

| Variant A | Variant B | Difference | Data |
|:-:|:-:|:-:|:-:|
| **23.3%** | **19.0%** | **4.3 pp** | **thin** |
| <sub>42 of 180 left a contact</sub> | <sub>34 of 179</sub> | <sub>in favour of A</sub> | <sub>400+ per group needed</sub> |

| Item | | |
|---|---|--:|
| Variant A — «Three questions about your visit» | `██░░░░░░░░` | 23.3% |
| Variant B — «Service quality survey» | `██░░░░░░░░` | 19.0% |

> **Too early to declare a winner**  
> A 4.3-point gap on samples of 180 sits inside the margin of error. To claim A is better you need around 400 completions in each group.

<sub>The numbers above are an example. The skill works from your real variants and picks whichever of the three verdicts is honest.</sub>

## How to ask

> Compare the A/B variants of this survey — which one is better

> Can we pick a winner yet or is the data too thin?

> Check whether the difference between the two first screens is significant

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_report` | Quiz report | read |
| `get_quiz_summary` | Quiz summary | read |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
