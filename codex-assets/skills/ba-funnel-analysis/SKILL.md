---
name: ba-funnel-analysis
description: >-
  Build conversion funnels, compute step + overall conversion and drop-off, choose strict-order vs any-order and the conversion window; avoid the off-funnel-path and denominator-shift traps.
---

# ba-funnel-analysis

Define the ordered steps (e.g. visit → signup → activate → pay), then compute step conversion (each step / prior step) AND overall conversion (last / first). The drop-off between steps is where you act — rank steps by absolute users lost, not just percentage, so you fix the leak that matters in volume. Decide three things up front: (1) strict order vs any-order completion (does step 3 only count if 1→2→3 in sequence?); (2) the conversion window (must steps happen within 24h? 7d? — a 'funnel' with no window silently counts users who converted months later); (3) unique users vs events as the unit. Segment the funnel by source/device/cohort — a flat overall rate often hides one broken segment. Expert moves: build a time-to-convert distribution per step (a long tail means your window is wrong); look at the off-funnel paths users actually take (Sankey) — they may reach the goal via a route you didn't model; pair funnel CR with downstream retention so you don't optimize a step that attracts churning users. Pitfalls: the denominator-shift error (each step's base must be the prior step's completers, not all entrants); counting backfills/re-entries; ignoring that a redesigned funnel changes step definitions so trends break; reporting % with no absolute counts.

**Tools:** SQL, Amplitude, Mixpanel, GA4, pandas
