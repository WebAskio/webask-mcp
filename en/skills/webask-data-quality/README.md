<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Check before launch</sub>

# Data quality check

**Answers whether this data can be trusted before anyone builds conclusions on it**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-data-quality` | 1.0.0 | 3 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-data-quality-en.zip) |

## What it does

1. **Checks by signal, not by feel.** Suspiciously fast completions, straight-lining, duplicate contacts, junk in text fields, contradictions, bursts in time — each signal is counted on its own.
2. **Shows the share, not just the count.** For every signal: how many completions and what part of the total. Without the share the number says nothing.
3. **Works out whether conclusions move.** The most useful part of the check: if the key figures are the same after cleaning, there is no reason to clean.
4. **Leaves low scores alone.** An unhappy respondent is not fraud. Harsh comments and one-star ratings are not treated as junk.

## What you get

| Questionable | Would remain | Average now | Average after |
|:-:|:-:|:-:|:-:|
| **54** | **358** | **4.1** | **4.2** |
| <sub>13% of the total</sub> | <sub></sub> | <sub></sub> | <sub>difference within noise</sub> |

| | | |
|---|---|---|
| **Under a minute for nine questions** | speed | 23 · 6% |
| **Same option everywhere** | straight-lining | 14 · 3% |
| **One phone number twice or more** | duplicate contacts | 9 · 2% |
| **«aaa», «123», random letters** | junk in text | 11 · 3% |
| **«Never used it» followed by a service rating** | contradiction · likely a logic error | 7 · 2% |

> **Cleaning would not change the conclusions**  
> The average moves by a tenth and the order of options stays the same. Tag the questionable completions if you like, but deleting them for these numbers is not worth it.

<sub>The numbers above are an example. The check runs on your collected responses.</sub>

## How to ask

> Can I trust these responses — check the data quality

> This survey looks gamed, take a look at the data

> Find suspicious completions and tell me if they change the conclusions

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_answers` | Quiz answers | read |
| `get_quiz_report` | Quiz report | read |
| `get_quiz_report_inputs` | Text answers of a question | read |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
