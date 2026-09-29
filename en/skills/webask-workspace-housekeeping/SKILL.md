---
name: webask-workspace-housekeeping
description: "Tidies up a WebAsk account — sorts surveys into folders, archives the finished ones, restores from the bin, duplicates for a new wave, turns a good survey into a template, cleans up files. Use when someone asks to tidy up, sort surveys, remove old ones, copy a survey or save it as a template."
---

# Tidying up the account

Accounts get overgrown: a hundred surveys in one folder, finished ones next to live
ones, year-old drafts. Tidying is irreversible only in places — but those places
have to be known.

Reply in the language the person writes in.

## Picture first, actions second

`get_workspace_list` — the account id, almost every tool below needs it.
`get_folder_list` and `get_quiz_list` — what is where. If the person asks to "tidy
up" in general, first show the list of what is proposed and get agreement. A health
check (what is abandoned, where storage is running out) is a separate skill; this
one is the hands.

## What does what

| Task | Tool | Reversible? |
|---|---|---|
| New folder | `create_folder` | yes |
| Rename, delete a folder, folder order | `manage_workspace_folder` | delete — no |
| Move a survey to a folder | `move_quiz` | yes |
| Rename a survey | `rename_quiz` | yes |
| Note on a survey | `update_quiz_note` | yes |
| Archive and back | `archive_quiz` | yes |
| Copy a survey | `duplicate_quiz` | yes |
| Make a template | `make_quiz_template` | yes |
| Own templates | `get_workspace_templates` | — |
| To the bin | `delete_quiz` | can be restored |
| Restore from the bin | `restore_quiz` | — |
| Account files: overview, list, delete | `manage_workspace_files` | delete — no |

## Three levels of "remove"

1. **Archive** — the survey stops opening by link and leaves the main list, but
   everything is kept. For finished surveys this is the right answer.
2. **Bin** — the survey is removed, `restore_quiz` brings it back. For drafts and duplicates.
3. **Permanent** — only deleting files and folders with contents; requires a
   separate confirmation flag. Offer last.

A finished survey with responses goes to the archive, not the bin: the responses
will be useful for comparing with the next wave.

## A new wave of a survey

Do not edit last time's survey — copy it: `duplicate_quiz` into the right folder
with a new name. Then the previous wave's responses stay untouched and comparable.
If the survey runs regularly — `make_quiz_template` and build the next one from the
template.

## Files

`manage_workspace_files` with `overview` — how much is used and by what; `list` —
what exactly, filtered by survey and type. Delete (`delete`) only on a direct
request and only what was shown to the person as a list: respondents' files from
responses cannot be recovered.

## What not to do

- **Do not delete permanently without explicit agreement** on a specific list.
- **Do not archive a survey that is still collecting responses** — it will stop
  opening. Check recent responses in `get_quiz_summary`.
- **Do not rename or move other people's surveys** in a shared account without
  asking: colleagues look for them by the old names.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
