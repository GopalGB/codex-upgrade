---
name: agentic-human-in-the-loop
description: >-
  Put a human at the right checkpoints in an agent workflow — approval gates before consequential or irreversible actions, escalation when confidence is low, and clean decision surfaces that don't drown the human in context. Use when an agent can take real-world actions (spend, send, delete, deploy) or operates where mistakes are costly.
---

# agentic-human-in-the-loop

Autonomy is a dial, not a switch. The skill is placing the human at the **few checkpoints that matter** — before consequential or irreversible actions (spend money, send to customers, delete data, deploy, merge), at low-confidence forks, and at the boundaries where a wrong step is expensive — while letting the agent run unattended everywhere else. Too many gates and the human is a rubber stamp who stops reading; too few and the agent does damage. Gate by *blast radius*: reversible and cheap → proceed; irreversible or high-cost → confirm.

Design the **decision surface** for the human, not the machine. Surface a tight, sufficient summary: what the agent intends to do, why, the inputs it used, and the specific reversible/irreversible consequence — plus a clear approve/edit/reject. Don't dump the whole transcript; the goal is a 10-second confident decision. Offer a dry-run/preview for actions whose effect is hard to picture. Make rejection actionable feedback the agent can incorporate, not a dead end.

Pair this with **durable state** so the agent can pause for an approval that arrives minutes or hours later and resume cleanly. Calibrate the agent to *escalate on uncertainty* rather than guess confidently on ambiguous or high-stakes calls — an honest "I need a decision on X" beats a confident wrong action. Log every approval/override for audit and to learn where the gates are mis-placed. The target is an agent that's trusted because it asks at exactly the right moments — no more, no less.

**Tools:** gate by blast radius (confirm irreversible/costly) · few checkpoints that matter, autonomous elsewhere · tight decision surface (intent + consequence + approve/edit/reject) · dry-run previews · escalate on uncertainty · durable pause/resume · audit-log approvals
