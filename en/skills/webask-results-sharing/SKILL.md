---
name: webask-results-sharing
description: "Prepares WebAsk survey results for handing to someone else — a public link to the report, summary or responses, a PDF or Word file, or an AI report with conclusions. Use when someone asks to send results to a client, share a report with a colleague, export the outcome, or build a report with findings."
---

# Handing over results

Survey results are read by more people than those who built the survey. A client, a
manager or a colleague does not need access to the account — they need a finished
thing: a link or a file.

Reply in the language the person writes in.

## Ask what exactly is needed first

Three different things, and mixing them up is expensive:

| What they ask for | What to hand over | Tool |
|---|---|---|
| "Show me the results", figures per question | the summary | `share_summary_link`, `export_summary_pdf` |
| A report with breakdowns, by period or filter | the report | `share_report_link`, `export_filtered_report_pdf`, `export_filtered_report_word` |
| Individual completions, who answered what | the responses | `share_answers_link`, `export_answers_xlsx` |
| Text with conclusions rather than tables | the AI report | `generate_ai_report`, `get_ai_report`, `share_ai_report` |

If the request does not make it clear — ask one question. If the survey is named in
words, find it with `get_quiz_list`.

## Link or file

**A link** lives until revoked and always shows fresh data — right when results are
still coming in and the client will come back more than once.

**A file** freezes the state at export time — right for a report "as of a date" or
when the recipient must not see what arrives later. Download links live for an
hour: say so.

## Check before handing anything outside

1. **Are there contacts in the survey?** `get_quiz_structure` — if there is a phone,
   email or name, a public link to *responses* gives them to anyone who has the
   link. Offer the summary or the report instead; if responses are really needed,
   ask whether they should go outside at all.
2. **Period and scope.** Report and responses accept a date range and completion
   status (`is_complete`). Ask whether abandoned completions are wanted: for a
   client, usually not.
3. **Saved filter.** If the report already has a configured slice
   (`get_quiz_report_filters`), hand that over instead of building a new one.

## The AI report

`generate_ai_report` builds a written analysis: quantitative, comparative and
free-text — all three or one `section`. It is not instant; fetch the finished one
with `get_ai_report`, hand it out with `share_ai_report` as a link or PDF.

Do not build an AI report on a dozen answers: the conclusions will sound confident
and rest on nothing. Say the data is thin.

## What to say at the end

What exactly was handed over (summary, report, responses), for which period, with
which filters, and whether the link is permanent or lives an hour. If responses with
contacts were shared — remind that the link is public.

## What not to do

- **Do not share responses with contacts via a public link** without asking directly.
- **Do not export a file when a link was asked for**, or the other way round — they are different things.
- **Do not build an AI report silently** — it takes a while, warn first.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.
