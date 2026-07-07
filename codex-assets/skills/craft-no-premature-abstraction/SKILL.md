---
name: craft-no-premature-abstraction
description: >-
  Resist abstracting too early — inline duplication until a pattern actually repeats (rule of three), and don't build frameworks, generic helpers, or config for a single caller. Use when tempted to extract a shared abstraction; a wrong abstraction costs more than the duplication it removes.
---

# craft-no-premature-abstraction

Duplication is cheaper than the **wrong** abstraction. The first time you write something, write it concretely. The second time something similar appears, note it but still resist — two cases rarely reveal the real axis of variation. By the **third** occurrence (rule of three) you can see what actually varies versus what's incidental, and only then extract — fitted to the evidence, not to a guess.

A premature abstraction hurts twice: it adds indirection and parameters nobody needed yet, and it *locks in the wrong seams* — when the third case doesn't fit, people bolt on flags and special-cases until the "shared" helper is a tangle serving no case well. Inlining the duplication would have been trivially deletable; un-abstracting is a refactor. Don't build a generic engine, a plugin system, or a configurable pipeline for one or two callers.

This is YAGNI applied to structure. Don't add a layer "so it's easy to swap later" before there's a second thing to swap in. Don't parameterize for hypothetical futures. Let the code stay concrete and a little repetitive until the repetition is real and stable — then abstract with confidence. Prefer a small duplicated function over a large parameterized one that every caller has to decode.

**Tools:** rule-of-three before extracting · inline duplication early · no framework/config for one caller · wrong-abstraction > duplication · YAGNI for structure · concrete until the pattern is stable
