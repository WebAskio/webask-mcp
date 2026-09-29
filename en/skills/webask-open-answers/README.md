<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Understand the results</sub>

# Analysing free-text answers

**Turns a hundred lines of free text into a handful of themes with numbers and quotes**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-open-answers` | 1.0.0 | 2 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-open-answers-en.zip) |

## What it does

1. **Groups by meaning, not by words.** «Waited too long», «waited forty minutes» and «the queue» are one theme. Matching words are not required.
2. **Counts the shares.** For each theme: how many answers and what share of everyone who wrote something. A theme without a number decides nothing.
3. **Sets aside the empty ones.** «No», «all fine», «-» go into their own group: not themed, but not hidden either — their size says something too.
4. **Quotes verbatim.** One or two characteristic quotes per theme, typos and all, with no polishing. Personal details are stripped out of the quote.

## What you get

| Item | | |
|---|---|--:|
| Long wait | `████░░░░░░` | 41 · 43% |
| Unclear what the price includes | `██░░░░░░░░` | 18 · 19% |
| Nobody called back | `█░░░░░░░░░` | 12 · 13% |
| Praise for the technician | `█░░░░░░░░░` | 9 · 9% |
| No content | `██░░░░░░░░` | 16 · 17% |

> **«waited almost an hour even though I booked for 10:00»**  
> The waiting theme is both the largest and the most consistent: people name a specific time rather than complaining in general. That is something you can measure and fix.

<sub>The themes and quote above are an example. The analysis runs on your own text answers.</sub>

## How to ask

> Group the free-text answers into themes and show what comes up most

> What are people writing in the «what could be better» question

> Pull themes out of the open answers with quotes

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_report` | Quiz report | read |
| `get_quiz_report_inputs` | Text answers of a question | read |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
