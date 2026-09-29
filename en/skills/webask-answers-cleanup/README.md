<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Keep the account tidy</sub>

# Cleaning up responses

**Removes test completions and duplicates — but shows you the list before anything goes**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-answers-cleanup` | 1.0.0 | 10 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-answers-cleanup-en.zip) |

## What it does

1. **Shows first, deletes second.** The list to be cleaned comes with counts, the period and the rule it was selected by. Deletion happens only after you have seen it.
2. **Builds groups by signal.** Test runs before the send date, too-fast completions, straight-lining, duplicate contacts — separate groups with numbers, not one pile.
3. **Moves from reversible to final.** Hide from reports first — that can be undone. Then the bin. Permanent deletion only when you ask for it directly.
4. **Offers a tag instead of deletion.** A tagged response stays in the statistics but is visible. «Call back», «complaint», «duplicate» are easier to work with than a spreadsheet export.

## What you get

| Selected | Hide | Bin | For good |
|:-:|:-:|:-:|:-:|
| **64** | **undoable** | **restorable** | **on request** |
| <sub></sub> | <sub>stays in the database</sub> | <sub>if you change your mind</sub> | <sub>only when you ask</sub> |

| | | |
|---|---|---|
| **Test runs: before the send date, 3–6 September** | your own runs while building the survey | 18 |
| **Faster than a minute** | a nine-question survey | 23 |
| **Same option in every question** | straight-lining | 14 |
| **Duplicate phone numbers** | one number twice or more | 9 |

> **The assistant has deleted nothing**  
> This is a list for approval. Hiding from reports is the suggested start: the figures correct themselves immediately and the responses stay in place if the call has to be reversed.

<sub>The groups above are an example. The selection rules are chosen for your survey.</sub>

## How to ask

> Remove the test completions from the survey statistics

> Find duplicate phone numbers and show them before deleting

> Tag everyone who left a phone number and a complaint as «call back»

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `create_answer_tag` | Create answer tag | write |
| `delete_answer_tag` | Delete answer tag | destructive |
| `delete_quiz_answers` | Delete answers | destructive |
| `get_answer_tags` | Account answer tags | read |
| `get_quiz_answers` | Quiz answers | read |
| `get_workspace_list` | Workspace list | read |
| `set_answer_note` | Answer note | write |
| `set_answers_order_mode` | Question order in an answer | write |
| `tag_answer` | Tags on an answer | write |
| `toggle_answer_visibility` | Hide an answer from reports | write |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
