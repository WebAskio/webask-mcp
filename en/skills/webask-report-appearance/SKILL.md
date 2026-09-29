---
name: webask-report-appearance
description: "Configures how a WebAsk survey and its reports look: theme, report palette, fonts and logo. Use when someone asks to match brand style, change colours, or prepare a report to show a client."
---

# Styling the survey and the reports

The survey and the report are what outsiders see: the respondent and the client.
These settings are cheap and change the impression a great deal.

Reply to the person in the language they write in.

## Survey theme

Report styling and branding live at account level, and almost every tool below
needs the account id — take it from `get_workspace_list`.

`get_theme_list` — what already exists in the account. **Look at existing themes
first**: usually a suitable one is already there.

`apply_quiz_theme` — apply to a survey. `create_theme` and `update_theme` for
custom colours. `manage_theme` for order and deletion.

Ask about brand colours concretely: the main button colour, the background, whether
there is a logo. More than two or three colours in a survey is too many.

## Report styling

`get_workspace_report_appearance` — current state.
`update_workspace_report_palette` — the palette charts are drawn with.

The palette is account-wide: changing it changes every report. Warn about this if
the person is editing it for a single report.

`create_report_appearance_preset` and `delete_report_appearance_preset` — saved
sets, useful when reports go to different clients.

## Logo and copyright

`update_workspace_branding`, `upload_workspace_logo`, `delete_workspace_logo`.

These are account-wide, not per survey. Hiding the copyright is not available on
every plan: if the plan does not allow it, say so plainly and do not push an
upgrade.

## Advice worth giving

- **Contrast beats beauty.** Light grey on white is unreadable on a phone, and
  most surveys are taken on phones.
- **Chart palettes must survive black-and-white printing** — reports get printed.
- **A logo on the survey is fine; on every question it is not.**

## What not to do

- **Do not change the account palette for one report** without warning.
- **Do not create a new theme** when a suitable one exists.
- **Do not suggest a plan upgrade** to hide the copyright.