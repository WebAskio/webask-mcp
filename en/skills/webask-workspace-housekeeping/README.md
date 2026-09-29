<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Keep the account tidy</sub>

# Tidying up the account

**Sorts, archives, copies and cleans — and knows which of those cannot be undone**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-workspace-housekeeping` | 1.0.0 | 16 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-workspace-housekeeping-en.zip) |

## What it does

1. **List first, actions second.** On "tidy up" the assistant does not start deleting: it shows what it proposes for each survey and waits for agreement.
2. **Tells archive, bin and permanent apart.** A finished survey with responses goes to the archive — the responses are useful for comparison. Drafts go to the bin. Permanent is only for files, and only with confirmation.
3. **Makes a new wave as a copy.** Last time's survey is not edited — it is copied under a new name. The previous wave stays comparable. A recurring survey becomes a template.
4. **Does not archive live surveys.** Checks for recent responses before archiving: an archived survey stops opening by link.

## What you get

| Archive | Bin | Template | Permanent |
|:-:|:-:|:-:|:-:|
| **6** | **12** | **1** | **0** |
| <sub>reversible</sub> | <sub>restorable</sub> | <sub></sub> | <sub>not confirmed yet</sub> |

| | | |
|---|---|---|
| **"Delivery feedback — spring" and 5 more** | no responses since April, responses are kept | archive |
| **11 drafts without a single question** | last edited in February | to the bin |
| **"Survey (copy) (copy)"** | duplicate of a live survey, no responses | to the bin |
| **"Service quality"** | runs every quarter | template |
| **3.4 GB of respondent files from archived surveys** | frees space, cannot be undone | ask |

> **Nothing has been done yet — this is a plan for approval**  
> Archive and bin are reversible, so they can start right after a "yes". Respondent files are deleted for good — they need a separate answer.

<sub>The list above is an example. The plan is built from your account.</sub>

## How to ask

> Tidy up the account: sort surveys into folders, old ones to the archive

> Copy the survey for the autumn wave into the "2026" folder

> Make a template from the quality survey, we run it every quarter

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `archive_quiz` | Archive quiz | write |
| `create_folder` | Create folder | write |
| `delete_quiz` | Delete quiz | destructive |
| `duplicate_quiz` | Duplicate quiz | write |
| `get_folder_list` | Folder list | read |
| `get_quiz_list` | Quiz list | read |
| `get_quiz_summary` | Quiz summary | read |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_templates` | Workspace templates | read |
| `make_quiz_template` | Make quiz a template | write |
| `manage_workspace_files` | Workspace files | destructive |
| `manage_workspace_folder` | Manage folder | destructive |
| `move_quiz` | Move quiz to a folder | write |
| `rename_quiz` | Rename quiz | write |
| `restore_quiz` | Restore quiz from trash | write |
| `update_quiz_note` | Quiz note | write |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
