<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Understand the results</sub>

# Comparing traffic sources

**Shows which channel brought people and which only brought numbers**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-source-dashboard` | 1.0.0 | 2 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-source-dashboard-en.zip) |

## What it does

1. **Checks the tags exist first.** Without them a channel breakdown is impossible and cannot be added retroactively. The assistant says so instead of inventing a split.
2. **Counts three things per channel.** How many arrived, how many finished, and the metric that matters — contacts or average score, depending on the goal.
3. **Separates volume from quality.** A thousand people at five percent completion is worse than a hundred with half finishing. The table shows it; a single total does not.
4. **Does not hide untagged responses.** They get their own row rather than a «other» bucket: usually direct visits, or a tag lost when the link was forwarded.

## What you get

| Item | | |
|---|---|--:|
| Email to the base — 168 people | `███████░░░` | 71% finished |
| Telegram channel — 94 | `██████░░░░` | 64% |
| No tag — 82 | `██████░░░░` | 58% |
| Website banner — 68 | `██░░░░░░░░` | 22% |

| | | |
|---|---|---|
| **Email to the base** | 168 arrived · 119 finished | 62 contacts |
| **Telegram channel** | 94 · 60 | 38 |
| **No tag** | 82 · 48 | 27 |
| **Website banner** | 68 · 15 | 9 |

> **The banner brings people, just not the right ones**  
> It delivers decent traffic and one in five finishes. Usually the channel is not at fault — the promise on the banner is. One run is not enough to switch it off.

<sub>The channels above are an example. The split is built from your own source tags.</sub>

## How to ask

> Where did respondents come from and which channel worked best

> Compare the mailing and Telegram by response quality

> Split the responses by source tag

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_answer_extra_field_values` | Link label values | read |
| `get_quiz_report` | Quiz report | read |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
