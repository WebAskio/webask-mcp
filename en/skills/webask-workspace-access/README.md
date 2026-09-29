<sub><a href="../../README.md">WebAsk MCP</a> › <a href="../README.md">Skills</a> › Keep the account tidy</sub>

# Members and access

**Works out why a member cannot see the surveys, and grants exactly the rights they need**

| Skill | Version | Tools | Download |
|---|---|---|---|
| `webask-workspace-access` | 1.0.0 | 13 | [ZIP](https://github.com/WebAskio/webask-mcp/releases/download/skills-latest/webask-workspace-access-en.zip) |

## What it does

1. **Shows the current picture first.** Who is in the account, with which role, and what they actually see. «Give Peter access» without that usually ends with Peter holding too much.
2. **Knows the two reasons for «he cannot see it».** The invitation was never accepted — the person is listed but has no access. Or the role is there but no folders are open, so the survey list is empty.
3. **Asks about the job, not the role.** Viewing results, building surveys, configuring integrations are different sets of rights. Full access belongs only to people who administer the account.
4. **Never revokes on its own initiative.** Removing a member cannot be undone — only a new invitation brings them back. So it happens only when you ask.

## What you get

| Members | Not accepted | No folders | Too much access |
|:-:|:-:|:-:|:-:|
| **6** | **1** | **1** | **1** |
| <sub></sub> | <sub>listed but cannot see</sub> | <sub>has a role, sees nothing</sub> | <sub></sub> |

| | | |
|---|---|---|
| **Anna** | administrator · all folders | working |
| **Peter** | invited on 4 September, never accepted | no access |
| **Maria** | «Analyst» role, no folders open | empty list |
| **Igor** | full access, only needs to view | over-permissioned |
| **Olga** | view results · 2 folders | working |

> **Both «I added him and he sees nothing» cases come from here**  
> Peter has an unaccepted invitation and needs it resent. Maria has a role but no folders, so she signs in to an empty list. Neither looks like a fault in the system.

<sub>The members above are an example. The review is built from your account.</sub>

## How to ask

> Add a colleague with access to results only

> Why can this member not see the surveys

> Show who has which rights in the account

## Tools it calls

| Tool | What it does | Kind |
|---|---|---|
| `delete_workspace_role` | Delete member role | destructive |
| `get_folder_list` | Folder list | read |
| `get_workspace_list` | Workspace list | read |
| `get_workspace_member_access` | Member access | read |
| `get_workspace_members` | Workspace members | read |
| `get_workspace_roles` | Member roles | read |
| `invite_workspace_member` | Invite member | write |
| `manage_folder_access` | Folder access | destructive |
| `remove_workspace_member` | Remove member | destructive |
| `resend_workspace_member_invite` | Resend member invite | write |
| `save_workspace_role` | Member role | write |
| `set_workspace_member_folders` | Folders available to a member | write |
| `set_workspace_member_role` | Change member role | write |

## Files

- [`SKILL.md`](SKILL.md) — the skill itself: instructions for the assistant
- [`agents/openai.yaml`](agents/openai.yaml) — MCP tools the skill depends on
