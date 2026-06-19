---
name: pa-outlook-teams-flows
description: >-
  Outlook (send/receive/shared mailbox) + Teams (post message, adaptive cards, wait for response) automation patterns
---

# pa-outlook-teams-flows

**Office 365 Outlook**: trigger **When a new email arrives (V3)** (filter Folder/From/Subject/**Has Attachment**/Importance to narrow before the run), actions **Send an email (V2)** (To/CC/BCC, HTML body, **Attachments** as {Name, ContentBytes}), **Reply to email (V3)**, **Get attachments**, **Move email**, **Send from a shared mailbox (V2)** (needs Send As/On Behalf). For approval-by-email use **"Send email with options"** (returns SelectedOption). **Microsoft Teams**: **Post message in a chat or channel** (as Flow bot or user), **Post adaptive card and wait for a response** (paste **Adaptive Card JSON** with `Input.Text`/`Input.ChoiceSet`/`Action.Submit`; read replies via `body('Post_adaptive_card')?['data']?['fieldId']`), **Post a feed notification**, **Create a Teams meeting**. Pitfalls: HTML email body must be valid HTML with **inline CSS** (clients strip `<style>`); large attachments hit size limits; new-email trigger fires per message and on shared mailboxes needs the right connection/permission; target Adaptive Card **1.4-1.5** and avoid bleeding-edge features; "post as user" needs delegated consent; channel posts can't be edited by the flow afterward; gate attachment work with `triggerOutputs()?['body/hasAttachments']`.

**Tools:** Office 365 Outlook, When a new email arrives (V3), Send an email (V2), shared mailbox, Send email with options, Teams Post adaptive card and wait for a response
