---
name: sde-debugging-method
description: >-
  Debug systematically - reproduce, isolate via bisection/binary search, form and test hypotheses, fix root cause not symptom.
---

# sde-debugging-method

Debugging is the scientific method, not random poking. (1) **Reproduce reliably** - a bug you can't trigger on demand you can't confirm fixed; reduce to a **minimal repro** by stripping inputs/config until it's the smallest case that still fails. (2) **Observe** the actual vs expected - read the full stack trace and error, don't skim; add targeted logging at the suspected boundaries. (3) **Hypothesize** one specific cause, then **test it** - change one variable at a time. (4) **Isolate by bisection**: binary-search the space - comment out half the code, bisect the input, or `git bisect` across commits to pin the introducing change in O(log n) steps instead of reading everything. (5) **Fix the root cause**, not the symptom - a null check that hides why it was null just moves the bug. Then add a **regression test** that fails before and passes after. **Heuristics**: 'it worked yesterday' -> diff what changed (deploy, data, dependency, config); rubber-duck it (explaining out loud surfaces wrong assumptions); check your assumptions first - the bug is usually in the code you're sure is correct. **Pitfall**: shotgun debugging (changing many things at once) so you never learn what actually fixed it.

**Tools:** scientific method, git bisect, binary search, logging, rubber-duck, minimal repro
