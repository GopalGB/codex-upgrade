---
name: craft-read-before-edit
description: >-
  Read the file and its neighbors before changing them — understand the existing conventions, naming, imports, error-handling style, and test layout, then write code that reads like the surrounding code. Use before any edit to avoid imposing a foreign style or breaking patterns you didn't notice.
---

# craft-read-before-edit

Before you edit, **read** — the target file end to end, plus a couple of sibling files and the nearest tests. You're looking for the local conventions: how things are named, how errors are handled, how modules import each other, how state is managed, where tests live and how they're written. Code that ignores these reads as a foreign graft and creates churn for whoever maintains it.

Match what you find. Use the project's naming style, its logging and error idioms, its existing utilities (don't re-implement a helper that's already three files over), its formatting. If the codebase uses Result types, don't throw; if it uses a logger, don't `print`. The goal is that a reviewer can't tell which lines you wrote from style alone — your change should be indistinguishable from the surrounding hand.

This also prevents whole classes of bugs: you discover the function you were about to duplicate, the invariant you were about to violate, the config that already exists. Reading first is faster than editing twice. When a codebase is large, read the module you're in and the interfaces you cross — not the whole repo, but enough to act in-context, not from assumption.

**Tools:** read target + neighbors + tests first · match naming/imports/error-style · reuse existing helpers · write indistinguishable-from-surrounding code
