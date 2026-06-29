---
name: craft-small-surgical-diffs
description: >-
  Make the smallest change that fully solves the task — touch only the lines the task requires, with no drive-by reformatting, renaming, or unrelated refactors mixed in. Use on every edit to keep diffs reviewable and bisectable, and to avoid hiding a real change inside a wall of noise.
---

# craft-small-surgical-diffs

A good diff is **minimal and on-topic**. Change only what the task needs. Resist the urge to reformat the file, re-order imports, rename a variable you happened to read, or "tidy while you're in there" — every unrelated edit you bundle in makes the diff harder to review, harder to revert, and harder to bisect when something breaks later.

If you genuinely should refactor or reformat, do it as a **separate commit** with its own message, before or after the behavioral change — never interleaved. Reviewers should be able to see the real change in a handful of lines, not hunt for it among 300 lines of whitespace churn. Match the file's existing formatting exactly so your edit produces no incidental diff; don't let an auto-formatter rewrite lines you didn't touch.

Prefer the surgical edit over the rewrite: change the three lines that are wrong rather than replacing the whole function. When a change feels like it's sprawling across many files, stop — that's usually a sign the task wasn't decomposed, or you're solving more than was asked. Keep each diff a single, reviewable idea.

**Tools:** smallest-correct-change · no drive-by reformatting/renames · refactor in a separate commit · match existing formatting · one idea per diff
