---
name: craft-fail-loud-no-swallow
description: >-
  Never silently swallow errors — no bare except, no empty catch block, no returning null/default on failure without surfacing it. Use whenever writing error handling; surface failures loudly with context so bugs are caught at their source instead of corrupting state downstream.
---

# craft-fail-loud-no-swallow

A swallowed error is a bug that fails later, somewhere else, untraceably. Never write a bare `except:` / `catch (e) {}` / `if err != nil { }` that drops the failure on the floor. If you catch, you must do one of three honest things: **handle** it meaningfully, **re-raise** it (optionally wrapped with context), or **log it with enough detail to debug** and then fail. "Catch and continue as if nothing happened" is none of these.

Fail fast and at the source. Validate inputs at the boundary and reject bad ones loudly rather than letting them flow in and corrupt state three layers down. Don't return a silent `null`/`-1`/empty list to signal failure where the caller will treat it as success — raise, or return an explicit typed error/Result the caller must handle. Preserve the original cause when you wrap (`raise ... from e`, `cause: e`); never flatten a stack trace into a generic "something went wrong".

Catch **narrowly** — the specific exception you expect, not `Exception`/`Throwable` — so real, unexpected failures keep propagating instead of being absorbed by an over-broad handler. The only place broad catches belong is a top-level boundary that logs and converts to a clean user-facing error, and even there it logs the full detail.

**Tools:** no bare except / empty catch · handle | re-raise | log-and-fail · validate at the boundary · catch narrowly · preserve the cause · fail fast
