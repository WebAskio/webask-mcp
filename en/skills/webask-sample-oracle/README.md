<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Understand the results</sub>

# How many responses are needed

**Says whether what you have is enough and how much more you need before conclusions hold**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-sample-oracle` | 1.0.0 | 1 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-sample-oracle-en.zip) |

## What it does

1. **Asks about the decision, not the percentage.** Getting a feel for the mood and choosing between two options need different precision, and that sets the sample size.
2. **Counts by segment, not in total.** Splitting by city or segment multiplies the requirement: every group needs its own volume, and one overall figure is not enough.
3. **Gives honest rules of thumb.** 30–50 answers for the general mood, around 400 for five-percent precision. These are conversation benchmarks and are called that.
4. **Can say «that is enough».** When there is enough data the assistant says so, instead of advising you to keep collecting just in case.

## What you get

| Collected | For the big picture | Precision now | For ±5% |
|:-:|:-:|:-:|:-:|
| **318** | **enough** | **±6%** | **+80** |
| <sub>finished</sub> | <sub>~100 was needed</sub> | <sub></sub> | <sub>more responses</sub> |

| | | |
|---|---|---|
| **London** | 100+ per segment needed | 142 · enough |
| **Manchester** | 100+ needed | 96 · almost |
| **Leeds** | 100+ needed | 44 · thin |
| **Other cities** | combined | 36 · thin |

> **National conclusions hold, city ones do not**  
> The most common situation. The overall picture can be shown today; comparing Leeds with London on 44 answers cannot — the gap will swing with every dozen new responses.

<sub>The numbers above are an example. The estimate is made for your survey and your segments.</sub>

## How to ask

> Can we draw conclusions yet or should we keep collecting?

> How many responses do I need to compare two cities

> Is there enough data to make a decision from this survey

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_summary` | Quiz summary | read |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
