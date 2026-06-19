---
name: pa-approvals
description: >-
  Approvals connector: Start and wait, approval types (first-to-respond/everyone/custom), parallel approvers, reminders, escalation
---

# pa-approvals

The **Approvals** connector orchestrates sign-off. Use **"Start and wait for an approval"** (synchronous - flow pauses) for simple cases; use **"Create an approval"** + **"Wait for an approval"** separately to do work between (e.g. post a Teams card). **Approval type**: *First to respond* (any one decides), *Everyone must approve* (unanimous), *Custom Responses - one/all* (your own buttons like "Send back"/"Escalate"). Assign approvers as **semicolon-separated** UPNs; add Details (markdown), Item link, attachments. After completion branch on the top-level **Outcome** ("Approve"/"Reject") or iterate `outputs('Start_and_wait_for_an_approval')?['responses']` (Responder, Comments, ApprovalDate) in a Condition/Switch. Approvers act in Teams (adaptive card), Outlook (actionable message), or the Approvals app. Pitfalls: approvers need a Power Automate license in the same tenant; a waiting approval counts against the 30-day run limit - long waits risk expiry, so add a Do until + Delay reminder or timeout handling; you can't programmatically reassign a sent approval - build escalation by elapsed-time check + a new approval; sequential multi-stage = chain Start-and-wait blocks, branching to stop early on Reject.

**Tools:** Approvals connector, Start and wait for an approval, Create/Wait for an approval, First to respond / Everyone, Custom Responses, responses/Outcome
