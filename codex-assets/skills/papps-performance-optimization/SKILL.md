---
name: papps-performance-optimization
description: >-
  Canvas perf: cut OnStart, Concurrent parallel loads, delegate at source, minimize control count & nested galleries, ClearCollect caching, monitor profiling.
---

# papps-performance-optimization

Startup is the biggest lever. Shrink **App.OnStart**: move static/derived values to **named formulas** (lazy, no startup cost) and parallelize required loads with `Concurrent(ClearCollect(a,..), ClearCollect(b,..))` instead of sequential calls. Load data **delegably** so you fetch tens of rows, not thousands pulled and filtered locally. Reduce **control count** — every control adds to load and memory; flatten deep container/gallery nesting and avoid galleries inside galleries (N×M control explosion). Cache reference data with ClearCollect once, reuse everywhere; don't re-query the same lookup per gallery row. Set `DelayOutput=true` on search TextInputs so typing doesn't fire a query per keystroke; debounce filters. Defer non-critical screen loads to `Screen.OnVisible` with a guard flag so OnStart stays lean. Profile with **Monitor** (Studio) to see each network call, its duration, and delegation issues live; the **App Checker** flags formula/perf/accessibility problems. Pitfalls: 'load everything upfront so it's fast later' (slow launch, big memory); recomputing expensive formulas in a gallery template (each row recalculates — precompute into the Items table or a collection); image-heavy galleries without sizing.

**Tools:** Concurrent, named formulas, App.OnStart, Monitor, delegation, DelayOutput, ClearCollect
