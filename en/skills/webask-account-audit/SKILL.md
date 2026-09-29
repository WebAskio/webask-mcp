---
name: webask-account-audit
description: "Reviews the state of a WebAsk account in one report: abandoned surveys, missing notifications, approaching limits and storage. Use when someone asks to tidy things up, understand what is going on in the account, or find out why something stopped working."
---

# The account in one report

Accounts silt up: surveys collecting responses nobody reads, year-old drafts,
storage running out. The job is to show it all at once.

Reply to the person in the language they write in.

## What to gather

| What | Tool |
|---|---|
| Surveys and folders | `get_quiz_list`, `get_folder_list` |
| Account and permissions | `get_workspace_details`, `get_workspace_member_access` |
| Plan and limits | `get_workspace_tariff` |
| Storage and files | `get_workspace_storage_usage`, `get_workspace_hidden_files` |
| Members | `get_workspace_members` |
| Where responses go, for key surveys | `get_quiz_integrations`, `get_quiz_email_settings` |

There may be many surveys: check integrations for the ones with recent responses,
not for all of them.

## What to look for

**Responses piling up unseen.** A published survey with recent responses but no
email recipients and no enabled integrations. The most valuable finding of an audit.

**Ghost surveys.** Published, but no responses for a long time.

**Drafts.** Created and abandoned. They still count against the survey limit.

**Storage.** How much is used, by what, and whether files have started to be hidden
over quota. Hidden files are not visible to respondents in their answers.

**Plan limits.** What is already hit or close: surveys, responses, emails.

**Access.** Members whose invitation was never accepted. Members with wider access
than needed.

## How to present

In sections, by weight: first what is losing data or money right now, then what is
merely worth tidying.

For each finding: how many objects and what specifically to do. No vague "clean it
up".

## What not to do

- **Delete and change nothing during the audit.** It is a report, not a cleanup.
- **Do not suggest a plan upgrade** when limits are hit: state the fact.
- **Do not call a survey abandoned** when it is simply seasonal — ask.