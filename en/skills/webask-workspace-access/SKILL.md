---
name: webask-workspace-access
description: "Manages WebAsk account members and their permissions: invitations, roles, folder access. Use when someone wants to give a colleague access, restrict it, or work out why a member cannot see the surveys they need."
---

# People and access

Permission mistakes are quiet: a member simply does not see part of the surveys and
assumes they do not exist — or sees things not meant for them.

Reply to the person in the language they write in.

## See the current picture first

Start with `get_workspace_list` to get the account id: every tool below asks for
it. Folders, if needed, come from `get_folder_list`.

`get_workspace_members` — who is in the account and with what role.
`get_workspace_member_access` — what a specific member can see and do.
`get_workspace_roles` — which roles exist and what they include.

Start here. "Give Peter access" without the current picture usually gives Peter more
than intended.

## Invite and configure

| Task | Tool |
|---|---|
| Invite | `invite_workspace_member` |
| Resend the invitation | `resend_workspace_member_invite` |
| Change role | `set_workspace_member_role` |
| Open folders | `set_workspace_member_folders` |
| Access to one folder | `manage_folder_access` |
| Remove | `remove_workspace_member` |
| Account roles | `save_workspace_role`, `delete_workspace_role` |

## About invitations

An invitation has to be **accepted**. Until then the person appears in the list but
has no access. This is the second most common cause of "I added them and they see
nothing".

The first is folders: the role is granted but no folders are opened, so the survey
list is empty.

## Choosing permissions

Ask what the person needs to do, not which role to give:

- View results only — a role without editing, plus the relevant folders.
- Build surveys — add editing, not necessarily deletion.
- Configure integrations — a separate permission: without it they cannot even see
  where responses are sent.
- Full access — only for people who actually administer the account.

"Own surveys only" limits a member to what they created themselves.

## What not to do

- **Do not remove a member without an explicit request** — access comes back only
  through a new invitation.
- **Do not grant full access "to be safe"** — the most common way to over-share.
- **Do not delete a role in use**: check who is on it first.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

