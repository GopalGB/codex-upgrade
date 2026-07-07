---
name: agentic-state-durability
description: >-
  Make long-running agents and workflows durable — checkpoint state to external storage, design idempotent resumable steps, and survive crashes, restarts, and context resets without redoing or double-executing work. Use for multi-step, long-horizon, or human-in-the-loop runs that can't fit or finish in a single context window.
---

# agentic-state-durability

An agent that holds all its state in the context window dies when the window resets, the process crashes, or it pauses for a human. **Durable execution** fixes this: persist the run's state to external storage (a file, DB, or workflow engine) so it can be reconstructed and resumed exactly where it left off. Treat the context as cache and the durable store as truth — the agent rebuilds working memory from the store on resume, not from a remembered transcript.

Design steps to be **idempotent and checkpointed**. After each meaningful step, write a checkpoint: what's done, the outputs, the next step. On resume, read the checkpoint and continue — never re-run a completed side-effecting step. Make side effects safe to retry with idempotency keys / dedup so an at-least-once retry doesn't double-charge, double-send, or double-write. Separate *decisions* (re-derivable) from *effects* (must not repeat) and guard the effects.

This is what lets agents run for hours or across sessions, pause for approval and pick back up, and recover from transient failures with retry/backoff instead of restarting from zero. Workflow engines (Temporal, Inngest, etc.) provide durable state, retries, and replay out of the box; or roll a simple checkpoint file for lighter cases. Keep the checkpoint compact and versioned, and make "where am I?" answerable from storage alone — the same `.planning/`-style state note that lets a fresh context resume the task. Test the resume path explicitly: kill the run mid-way and confirm it continues correctly without duplicating effects.

**Tools:** durable store = truth, context = cache · checkpoint after each step · idempotent resumable steps · idempotency keys for side effects · separate decisions from effects · retry/backoff not restart · test the kill-and-resume path
