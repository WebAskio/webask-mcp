<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Understand the results</sub>

# Report and survey styling

**Tidies up what people see from outside: the survey theme, the report palette and the logo**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-report-appearance` | 1.0.0 | 13 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-report-appearance-en.zip) |

## What it does

1. **Looks at existing themes first.** Most of the time a suitable theme already exists in the account. Creating another one just adds something nobody maintains.
2. **Asks concrete questions.** Not «what is your brand style», but the main button colour, the background and whether there is a logo. Two or three colours are plenty.
3. **Warns about account-wide settings.** The report palette and branding apply to the whole account. Change them for one report and they change everywhere.
4. **Advises on substance.** Contrast beats beauty: light grey on white is unreadable on a phone, and most surveys are taken on phones.

## What you get

| | | |
|---|---|---|
| **Survey theme** | an existing account theme, no new one created | per survey |
| **Chart palette** | distinguishable in black-and-white print | per account |
| **Saved preset for a client** | report appearance preset | per account |
| **Logo and copyright** | hiding the copyright is not on every plan | per account |

> **The palette is shared — you get warned first**  
> Change it for one report and the charts repaint in all the others. When reports go to different clients, saved presets are the right tool.

<sub>The list above is an example. Settings apply to your account and your survey.</sub>

## How to ask

> Give the survey a theme in our brand colours

> Change the chart palette in reports

> Put the company logo on the survey and the reports

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `apply_quiz_theme` | Apply theme to quiz | write |
| `create_report_appearance_preset` | Create report appearance preset | write |
| `create_theme` | Create theme | write |
| `delete_report_appearance_preset` | Delete report appearance preset | destructive |
| `delete_workspace_logo` | Delete workspace logo | destructive |
| `get_theme_list` | Theme list | read |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_report_appearance` | Workspace report appearance | read |
| `manage_theme` | Manage themes | destructive |
| `update_theme` | Update theme | write |
| `update_workspace_branding` | Workspace logo and copyright | write |
| `update_workspace_report_palette` | Workspace report palette | write |
| `upload_workspace_logo` | Upload workspace logo | write |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
