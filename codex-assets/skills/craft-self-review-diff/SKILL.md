---
name: craft-self-review-diff
description: >-
  Before declaring work done, read your own diff line by line as a hostile reviewer — hunt for leftover debug prints, commented-out code, TODOs, secrets, off-by-ones, and untested branches. Use as the final gate on every change; the cheapest bug to fix is the one you catch in your own diff.
---

# craft-self-review-diff

Before you say "done", **review your own diff** the way a skeptical reviewer would — `git diff` (and `--staged`), top to bottom, every hunk. The goal is to catch the obvious-in-hindsight problems while they're free to fix, not after they're shipped. Read it as if someone else wrote it and you're looking for reasons to reject.

Run the checklist: leftover `print`/`console.log`/debugger statements; commented-out code you meant to delete; `TODO`/`FIXME`/`XXX` you're leaving without a note; hardcoded secrets, tokens, or local paths; off-by-one and boundary cases (empty input, null, the last element); error paths you added but never exercised; a function you changed whose other callers you didn't check; stray files or formatting churn that shouldn't be in this diff; the test you said you'd write but didn't.

Also re-read against the *task*: does this diff actually do what was asked, fully, and nothing it shouldn't? Did you leave the change half-done with a "will finish later"? Self-review is not optional polish — it's the last gate before you make a claim about your work, and it routinely catches what running the tests doesn't (dead code, leaked secrets, scope creep). Fix what you find, then re-verify.

**Tools:** read every hunk as a hostile reviewer · catch debug prints / commented code / TODOs / secrets · check boundaries + error paths + other callers · no stray churn · re-check against the task · then re-verify
