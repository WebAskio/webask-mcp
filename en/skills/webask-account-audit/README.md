<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Keep the account tidy</sub>

# Account audit

**Shows in one report where the account is losing responses, storage and money**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-account-audit` | 1.0.0 | 10 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-account-audit-en.zip) |

## What it does

1. **Finds surveys collecting into silence.** Published, fresh responses, but no email recipients and no integrations. The most valuable finding of the audit: data piles up and nobody knows.
2. **Separates ghosts from drafts.** Published with no responses and created-then-abandoned are different stories. The second kind also eats into the survey limit.
3. **Counts storage and limits.** How much is used, by what, and whether files have started being hidden above the quota — hidden files are invisible to respondents in their own responses.
4. **Reviews access.** Unaccepted invitations and members with more rights than they need. A quiet problem, usually noticed later than it should be.

## What you get

| Surveys | Drafts | Storage | Findings |
|:-:|:-:|:-:|:-:|
| **34** | **11** | **82%** | **6** |
| <sub>of 50 on the plan</sub> | <sub>abandoned over six months ago</sub> | <sub>files will start being hidden</sub> | <sub></sub> |

| | | |
|---|---|---|
| **«Delivery feedback» collects into silence** | 47 responses this month · no recipients, no integrations | losing data |
| **Two surveys published, no responses since April** | the link is no longer shared, or it is broken | check |
| **11 drafts take up the limit** | last edited in February or earlier | tidy up |
| **Storage is 82% full** | 3.4 GB · mostly files uploaded by respondents | watch |
| **One invitation is still unaccepted** | sent in July | resend |

> **Start with one item**  
> «Delivery feedback» is the only finding that is losing data right now: 47 leads arrived and were never read. The rest can be dealt with calmly.

<sub>The findings above are an example. The report is built from your account, and the audit changes nothing.</sub>

## How to ask

> Audit the account: what is abandoned, where is storage running out

> Are there surveys collecting responses that nobody reads?

> Run an account audit and tell me where to start cleaning up

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `get_folder_list` | Folder list | read |
| `get_quiz_email_settings` | Quiz email settings | read |
| `get_quiz_integrations` | Quiz integration state | read |
| `get_quiz_list` | Quiz list | read |
| `get_workspace_details` | Workspace details | read |
| `get_workspace_hidden_files` | Files hidden over quota | read |
| `get_workspace_member_access` | Member access | read |
| `get_workspace_members` | Workspace members | read |
| `get_workspace_storage_usage` | Storage usage | read |
| `get_workspace_tariff` | Workspace plan | read |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
