---
name: pptx-morph-transition
description: >-
  Use Morph for smooth object movement/zoom/transform between slides (the keynote-style effect) including name-matching tricks and text morphs
---

# pptx-morph-transition

Morph animates the difference between two slides — move, resize, recolor, or rotate the same object across slides and PowerPoint tweens it. Workflow: build slide A, duplicate it (so objects are identical instances), on slide B change position/size/color/rotation of objects, then apply Transitions > Morph to slide B. PowerPoint matches objects by identity (from the duplicate) — that's why duplicating beats rebuilding. Effect Options: Objects (default), Words, or Characters for text-level morphs. Power trick: force a match between two different shapes by naming both with the same `!!`-prefixed name in Selection Pane (e.g. `!!box`) — Morph then transforms one into the other. Great for: zoom-into-detail, building a diagram piece by piece across slides, animated number changes, agenda-item highlighting. Pitfall: if objects don't morph and instead fade, they weren't recognized as the same object — duplicate the slide rather than copy-pasting shapes, or use the `!!name` trick. Keep duration ~0.5-0.75s. Combine with Zoom (Insert > Zoom) for navigable, motion-rich decks. App-only feature — not scriptable via python-pptx.

**Tools:** Transitions > Morph; Effect Options (Objects/Words/Characters); !!name match; duplicate-slide workflow
