---
name: vba-error-handling
description: >-
  Robust error handling: On Error GoTo label, Err.Number/Description/Source, Resume/Resume Next, centralized cleanup, re-raise with Err.Raise, avoiding On Error Resume Next abuse
---

# vba-error-handling

The disciplined pattern: at the top `On Error GoTo ErrHandler`, do the work, then `Exit Sub` before the handler so success doesn't fall through. The handler inspects `Err.Number` and `Err.Description`, logs/messages, then `Resume CleanExit` to run shared teardown. Put resource cleanup (close files, `Application.EnableEvents = True`, `ScreenUpdating = True`) at a `CleanExit:` label that both the success path and error path reach.

Expert moves: use `On Error Resume Next` **surgically** — wrap exactly one line that may legitimately fail (e.g., `Set ws = Sheets("X")` to test existence), check `If Err.Number <> 0` / `If ws Is Nothing`, then immediately `On Error GoTo 0` to restore normal trapping. Re-raise custom errors with `Err.Raise vbObjectError + 513, "MyModule", "Customer not found"` so callers can handle them. `Resume` retries the failing line (useful after fixing a condition); `Resume Next` skips to the line after. Always `Err.Clear` or let `On Error GoTo 0` reset.

Pitfalls: blanket `On Error Resume Next` at the top of a procedure hides every bug and is the #1 cause of silent data corruption — it's banned in good code except in tight, checked scopes. Leaving events/ScreenUpdating off after an error makes Excel appear frozen. Nested error handlers: an error inside a handler isn't caught by the same handler. Don't forget `Exit Sub` before the label — without it, the handler runs on success.

**Tools:** On Error GoTo, On Error Resume Next, Err object, Resume, Resume Next, Err.Raise, Err.Clear, vbObjectError
