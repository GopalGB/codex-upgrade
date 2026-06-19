---
name: pa-error-handling-runafter
description: >-
  Configure run after (failed/skipped/timed out), Scope try/catch/finally pattern, result() for error details, Terminate with status
---

# pa-error-handling-runafter

Power Automate has no try/catch keyword - build it with **Configure run after** + **Scopes**. Actions run only after the predecessor **is successful** by default; open ... > **Configure run after** and check **has failed**, **is skipped**, **has timed out** to make an action a catch handler. The pattern: wrap main logic in a **Scope "Try"**; add a **Scope "Catch"** set to run after Try **has failed / timed out / skipped**; add a **Scope "Finally"** set to run after Catch with **all four** boxes checked so it always runs (cleanup/logging). Inside Catch, get the real error with **`result('Try')`** - an array of failed actions with `status`, `error.code`, `error.message`; filter status='Failed' to log the cause. End explicitly with **Terminate**: status **Failed** (custom code/message surfaces in run history) or **Cancelled**, so a handled error still marks the run red for monitoring. Pitfalls: without a Catch run-after, one failed action aborts the run silently; a Scope fails if any child fails; `result()` only works on a completed Scope; ensure Finally runs after Catch with success+failed+skipped+timedout all checked or it's skipped when Try succeeds.

**Tools:** Configure run after, Scope (Try/Catch/Finally), result(), Terminate action, has failed / is skipped / has timed out
