<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Understand the results</sub>

# Survey timeline

**Answers «why did responses stop» by lining up collection against the edit history**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-quiz-timeline` | 1.0.0 | 3 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-quiz-timeline-en.zip) |

## What it does

1. **Builds two lines.** Responses by day and publication snapshots. Separately each explains little; together they explain almost everything.
2. **Looks for date matches.** A drop right after a publish means something was broken by an edit. A drop with no edits means the outside world: the mailing ended, the banner came down, the event passed.
3. **Checks the obvious separately.** A sharp drop to zero is a reason to see whether the survey was unpublished — the link stops opening instantly, and it looks like people simply stopped answering.
4. **Does not pass coincidence off as cause.** If an edit could not have affected collection, the assistant says so. An invented link is worse than an honest «nothing found».

## What you get

| Item | | |
|---|---|--:|
| 4–10 August | `██████████` | 96 |
| 11–17 August | `█████████░` | 88 |
| 18–24 August · published on the 19th | `███░░░░░░░` | 31 |
| 25–31 August | `███░░░░░░░` | 27 |
| 1–7 September · logic fixed on the 1st | `███████░░░` | 74 |
| 8–14 September | `████████░░` | 81 |

> **The collapse starts on the publish date, 19 August**  
> That version introduced a condition that sent part of the audience into a branch with no exit. After the fix on 1 September collection returned to its earlier level — the link shows up from both sides.

<sub>The dates above are an example. The lines are built from your survey and its versions.</sub>

## How to ask

> Why did the survey stop collecting responses

> Show how responses came in and when we edited the survey

> There was a drop in late August — work out what it was tied to

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_integrations` | Quiz integration state | read |
| `get_quiz_report` | Quiz report | read |
| `get_quiz_versions` | Quiz publication history | read |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
