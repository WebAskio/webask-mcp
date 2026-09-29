<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Build and share</sub>

# Rewriting survey copy

**Rewrites questions so people finish — starting from the data, not from taste**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-quiz-copy` | 1.0.0 | 5 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-quiz-copy-en.zip) |

## What it does

1. **Looks at where people quit.** The questions people abandon get fixed first, not the ones that look wrong. If there are no responses yet, that is said out loud.
2. **Fixes the known ailments.** Officialese, double-barrelled questions, double negatives, internal jargon, leading questions, questions with no boundaries — each with a before-and-after.
3. **Puts most work into the first screen.** That is where most people are lost. It needs three things: what is being asked, how long it takes and why it matters to the reader. The last one is usually missing.
4. **Writes only with your consent.** The list of edits comes first, the writing second. Survey copy is often signed off by a client or a legal team.

## What you get

| | | |
|---|---|---|
| **How happy are you with the work?** | was: Please rate your degree of satisfaction with the services rendered | officialese |
| **Was it on time? · Was the price fair?** | was: Were you happy with the timing and the price? | double question |
| **Rate the staff in the showroom** | was: Rate the performance of the front office | internal term |
| **How was our service?** | was: How much did you enjoy our excellent service? | leading |
| **Weekly · monthly · less often** | was: How often do you visit us? — as open text | no boundaries |

> **The first screen gets rewritten in full**  
> «Service quality survey» → «Three questions about how your visit went. Your answers help us cut the queues». Same meaning, but now the reader knows what it is for.

<sub>The wording above is an example. Edits are proposed for your copy and your audience.</sub>

## How to ask

> Rewrite the survey questions in plain language

> People quit at question three — look at the wording

> Make the first screen of the survey decent

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_report` | Quiz report | read |
| `get_quiz_structure` | Quiz structure | read |
| `get_quiz_texts` | Quiz default texts | read |
| `update_quiz_texts` | Edit default texts | write |
| `update_quiz_widgets` | Quiz questions and structure | write |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
