---
name: craft-vertical-slice-delivery
description: >-
  Build in thin end-to-end slices — one feature path working through every layer — instead of big-bang horizontal layers, keeping the build green and the app runnable at each slice. Use when implementing a feature or breaking down work, so progress is demonstrable and integration risk is paid down continuously.
---

# craft-vertical-slice-delivery

Deliver **vertical slices**, not horizontal layers. A slice is one narrow path that works all the way through — UI → API → logic → storage → back — for a single small case. Build that thinnest end-to-end thread first; it proves the layers actually connect, surfaces integration problems immediately, and gives something runnable and demonstrable. Then widen: add the next case, the next field, the next branch, each on top of a working whole.

The anti-pattern is building all of one layer before any of the next — the entire data model, then the entire service layer, then the UI — so nothing runs until the very end, integration bugs all hit at once, and "90% done" hides the riskiest 10%. Horizontal layering defers integration risk to the worst possible moment. Vertical slicing pays it down continuously.

Keep the build green and `main` deployable at every slice boundary — each slice is a complete, shippable increment even if the feature is only partially covered. Hide the unfinished parts behind a flag or a narrow entry point rather than leaving the tree broken. Decompose tasks the same way: "make one happy-path request return real data end-to-end" is a better first step than "build the database schema".

**Tools:** thinnest end-to-end thread first · widen case-by-case · green build at every slice · integrate continuously not big-bang · slice tasks vertically · flag the unfinished edges
