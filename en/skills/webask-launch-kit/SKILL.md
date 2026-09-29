---
name: webask-launch-kit
description: "Prepares launch material for a WebAsk survey: announcement copy for email and social media, links with source labels, a QR code. Use when someone is about to send out a survey and asks how to present it or what to write."
---

# Launch material

The survey is ready but still has to reach people. That is usually done by hand in
three different places. Prepare it all at once.

Reply to the person in the language they write in. Write the announcement copy in
the language of the survey's audience.

## 1. Establish the channels

Ask where it goes: an email list, social media, a messenger, a banner, offline.
Each channel gets its own labelled link — otherwise there is no way to tell what
worked.

## 2. Links with labels

`set_quiz_link` — the address itself, plus a source label per channel.

Name labels readably: `email-sep`, `vk`, `tg-channel`, not `utm1` and `utm2` —
nobody will remember what those meant in a month.

Check the survey is published: an unpublished one will not open and the mailing
goes nowhere.

## 3. Announcement copy

One per channel, all following one rule: **why it matters to the reader, how long
it takes, what happens next**.

- **Email.** A subject line that does not start with the word "survey" — "Three
  questions about your visit". Two or three lines and a button in the body.
- **Social and messengers.** One sentence and the link. Reader benefit first.
- **Site banner.** Five words at most.

Do not promise a reward that does not exist, and do not understate the time: "takes
a minute" for a fifteen-question form buys abandonment and irritation.

## 4. Offline

`manage_quiz_qr_code` — a code carrying the offline channel label. Verify it points
where it should before printing a run.

## 5. Last thing to say

Where the responses will land: are notifications configured. If not, offer to set
them up before the send-out, not after (`get_quiz_email_settings`,
`get_quiz_integrations`).

## What not to do

- **Do not send anything yourself** — this prepares material; the person launches.
- **Do not publish the survey unasked.**
- **Do not invent figures** for the announcement.
- **Do not suggest a plan upgrade or lead to payment.** If a limit is hit, state
  the fact and stop.

