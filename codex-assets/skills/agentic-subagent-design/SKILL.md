---
name: agentic-subagent-design
description: >-
  Design focused sub-agents with a single responsibility, an explicit input/output contract, and an isolated context that returns only distilled results to the caller. Use when splitting work across multiple agents so each one is debuggable, reusable, and doesn't pollute the parent's context window.
---

# agentic-subagent-design

A good sub-agent is a **function, not a colleague**: one clear responsibility, a defined input, a defined output, and no hidden side effects. Scope it to a single job ("find every call site of X and return file:line + a one-line description", "review this diff for security issues only") rather than a broad persona. Narrow scope is what makes a sub-agent reliable, testable, and reusable across orchestrations.

The decisive design choice is **context isolation**. Each sub-agent runs in its own window, so it can read, explore, and reason at length without spending the parent's context — and it must return a *compact, structured* result (the answer, not the journey). The parent should never inherit a sub-agent's raw transcript; it gets the distilled output and moves on. This is the whole efficiency argument for sub-agents: parallel depth without context bloat. So specify the **output contract** explicitly (shape, fields, max size) and have the sub-agent honor it.

Give each sub-agent exactly the inputs it needs and the least tool access required for its job (a read-only researcher shouldn't have write tools). Make boundaries explicit ("only this directory", "don't modify files") so workers don't collide or overreach. Prefer many small single-purpose sub-agents over one configurable mega-agent — the former compose and debug cleanly; the latter accretes flags and special cases. When a sub-agent's result is unusable, the fix is almost always a sharper objective or a tighter output contract, not a smarter model.

**Tools:** single responsibility · explicit input + output contract · isolated context, return distilled results · least-privilege tools · clear boundaries · many small over one configurable · debuggable + reusable
