<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Build and share</sub>

# Branching and routing

**Builds branching so that no respondent ever hits a dead end**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-quiz-logic` | 1.0.0 | 2 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-quiz-logic-en.zip) |

## What it does

1. **Reads the structure first.** Question identifiers cannot be guessed. Writing logic over a question that does not exist produces a survey that simply will not open.
2. **Builds the right kind of jump.** A branch by answer, a skipped block, a screenout for people who do not qualify, a quota per group — chosen to fit, not one method for everything.
3. **Knows the usual traps.** «Other» fires on the option, not on the text typed into it. «Greater than» does not work on text. Order matters: the first matching condition wins.
4. **Walks the route after the edit.** From the first question along each branch to the finish. If there are more than three or four branches, the assistant describes the map in words.

## What you get

| Branches | Dead ends | Unreachable | Jumps backwards |
|:-:|:-:|:-:|:-:|
| **4** | **0** | **0** | **0** |
| <sub></sub> | <sub>each one walked</sub> | <sub></sub> | <sub>no respondent loops</sub> |

| | | |
|---|---|---|
| **Rating below 4 → «What went wrong?»** | branch by answer · question 2 | has an exit |
| **Rating 4 and above → skip question 3** | skipped block | has an exit |
| **«Never used the service» → screenout** | screenout · question 4 | finish |
| **200 responses in the group → stop letting them through** | quota | finish |

> **«Other» fires on the option, not on the text**  
> A common mistake: people expect the jump to trigger on the words typed into the «Other» field. It triggers on the option being chosen — the text plays no part in the condition.

<sub>The jumps above are an example. Logic is built from your questions and their identifiers.</sub>

## How to ask

> If someone rates below four, ask them why

> Set up a skip for people who never used the service

> Check the survey logic for dead ends

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_quiz_structure` | Quiz structure | read |
| `update_quiz_logic` | Quiz branching logic | write |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
