---
name: craft-comment-why-not-what
description: >-
  Comment the why — intent, tradeoffs, non-obvious constraints, and gotchas — never narrate the what the code already states, and match the file's existing comment density. Use when adding comments or docstrings so they earn their keep instead of restating the obvious or rotting into lies.
---

# craft-comment-why-not-what

Good comments explain **why**, not **what**. The code already says what it does; a comment that restates it (`i++ // increment i`, `// loop over users`) is noise that rots the moment the code changes. Spend comments on what the code *can't* say: the reason behind a non-obvious choice, the tradeoff you made, the constraint that forces this shape, the bug this guards against, the link to the spec/ticket that explains it.

The litmus test: if deleting the comment loses no information a competent reader couldn't get from the code in five seconds, delete it. Reserve comments for the surprising — `// ponytail: in-memory until ~10k rows`, `// must run before auth middleware or the session is empty`, `// API returns cents, not dollars`, `// O(n²) is fine here, n < 50 by schema`. Those save the next reader (or you) a debugging session.

Match the file's existing comment density and style — don't drop a verbose block into a terse codebase or vice versa. Prefer making the code self-explanatory (a well-named function over a comment explaining a cryptic one) before reaching for a comment. Keep comments next to what they describe and update them in the same edit as the code — a stale comment is worse than none because it actively misleads.

**Tools:** comment the why not the what · delete comments that restate code · reserve for the surprising/constraints/tradeoffs · match existing density · prefer self-explanatory code · keep comments in sync
