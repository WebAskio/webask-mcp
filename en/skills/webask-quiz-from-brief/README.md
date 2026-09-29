<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Build and share</sub>

# Build a survey from a brief

**Describe the job in plain words and get a working survey, not a list of questions**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-quiz-from-brief` | 1.0.0 | 12 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-quiz-from-brief-en.zip) |

## What it does

1. **Picks the right question types.** A rating becomes a scale, not a text box; phone and email become validated fields. Whether the results can be summarised later depends on this.
2. **Wires up the branching.** Unhappy respondents get asked why; people who never used the service skip that block. Every route is walked to the end, with no dead ends.
3. **Styles it and closes it properly.** A theme that already exists in the account, real button labels and a thank-you screen instead of a blank page.
4. **Publishes only when you say so.** Until then the survey is visible to you alone, so there is time to read the draft and change it.

## What you get

| Questions | Required | Branches | Length |
|:-:|:-:|:-:|:-:|
| **7** | **2** | **2** | **~2 min** |
| <sub>plus intro and finish</sub> | <sub>contact details only</sub> | <sub>by rating and service</sub> | <sub>to complete</sub> |

| | | |
|---|---|---|
| **How happy are you with the work?** | rating · 5 stars | — |
| **What could have gone better?** | input · shown when the rating is below 4 | branch |
| **Was it finished on time?** | yesno | — |
| **Rate reception, work and price** | matrix · 3 rows | — |
| **How can we reach you?** | phone · format checked | required |

> **Ready to launch, but not published**  
> The assistant hands over a draft and a preview link. Publishing is a separate step and happens only on your word.

<sub>The layout above is an example of how the phrase «rate the work and collect contacts for a repeat booking» is read.</sub>

## How to ask

> Build a survey for car service customers: rate the work and collect contacts for a repeat booking

> I need a short satisfaction survey after delivery, three questions and a phone number

> Create a consultation request form: name, phone, preferred time and the customer question

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `apply_quiz_theme` | Apply theme to quiz | write |
| `create_quiz` | Create quiz | write |
| `create_quiz_from_template` | Create quiz from template | write |
| `generate_ai_quiz` | Build quiz from description | write |
| `get_folder_list` | Folder list | read |
| `get_quiz_structure` | Quiz structure | read |
| `get_theme_list` | Theme list | read |
| `publish_quiz` | Publish quiz | write |
| `search_quiz_templates` | Search ready-made quizzes | read |
| `update_quiz_logic` | Quiz branching logic | write |
| `update_quiz_texts` | Edit default texts | write |
| `update_quiz_widgets` | Quiz questions and structure | write |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`references/widget-types.md`](references/widget-types.md) — reference the skill loads on demand
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
