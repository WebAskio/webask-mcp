<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Understand the results</sub>

# Results for the client

**Turns results into something you can send: a link, a file or a report with conclusions**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-results-sharing` | 1.0.0 | 13 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-results-sharing-en.zip) |

## What it does

1. **Works out what is needed first.** Summary, report with breakdowns, individual responses or text with conclusions — four different things. One clarifying question instead of a guess.
2. **Picks link or file for the job.** A link is permanent and shows fresh data. A file freezes the state on a date. Download links live an hour — said up front.
3. **Checks what goes outside.** If the survey has phones or emails, a public link to responses gives them to anyone. The assistant warns and offers the summary instead.
4. **Can build an AI report.** Quantitative, comparative and free-text analysis as prose with conclusions. And says honestly when the data is too thin.

## What you get

| Responses | Period | Format | Contacts |
|:-:|:-:|:-:|:-:|
| **318** | **Sept** | **link** | **hidden** |
| <sub>finished</sub> | <sub></sub> | <sub>plus dated PDF</sub> | <sub>not in the report</sub> |

| | | |
|---|---|---|
| **Public report link** | September · finished only · permanent | ready |
| **Summary as PDF** | snapshot as of 10 September · download link lives an hour | ready |
| **AI report** | three sections · building, a couple of minutes | in progress |
| **Link to responses** | the survey has a phone field — needs confirmation | waiting |

> **Responses with phone numbers did not go outside**  
> The survey has a phone field. A public link to responses would show it to anyone holding the link — so the client got the report and the summary, and the responses wait for explicit confirmation.

<sub>The layout above is an example. The assistant assembles what is asked for from your survey.</sub>

## How to ask

> Send the client the survey results for September

> Make a report link I can show my manager

> Build a report with conclusions and hand it over as a link

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `export_answers_xlsx` | Export answers to Excel | read |
| `export_filtered_report_pdf` | Export report to PDF | read |
| `export_filtered_report_word` | Export report to Word | read |
| `export_summary_pdf` | Export summary to PDF | read |
| `generate_ai_report` | AI report | write |
| `get_ai_report` | Ready AI report | read |
| `get_quiz_list` | Quiz list | read |
| `get_quiz_report_filters` | Saved report filters | read |
| `get_quiz_structure` | Quiz structure | read |
| `share_ai_report` | Public link to an AI report | write |
| `share_answers_link` | Public link to answers | write |
| `share_report_link` | Public link to a report | write |
| `share_summary_link` | Public link to a summary | write |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
