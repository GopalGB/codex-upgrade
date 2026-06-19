---
name: pa-apply-to-each-loops
description: >-
  Apply to each, Do until, concurrency control, nested loops, and why loops destroy flow performance (batch instead)
---

# pa-apply-to-each-loops

**Apply to each** iterates an array; current element = `items('Apply_to_each')?['Field']`. **Do until** loops while false (set Count + Timeout under ... so it can't run forever - default caps ~60 iterations / 1 hour). Top performance lever: **Concurrency Control** (loop Settings) - Apply to each runs **sequentially** by default; enable it and set Degree of Parallelism up to **50** for independent items. BUT disable concurrency when iterations share state - appending to an array variable inside a **parallel** loop causes **race conditions / lost writes**; keep sequential or use **Select** instead. Pitfalls: loops are the #1 performance killer - a 5000-item loop with a per-item action is slow and burns API calls; prefer **Select** to transform arrays in one shot, **Filter array** to subset, and connector **batch** ops (Dataverse batch, SharePoint $batch) over per-item calls. Nested loops are fine but reference the inner `items()` explicitly. To loop a fixed count use `range(0,10)`. Watch the action-per-day quota - loops multiply it.

**Tools:** Apply to each, Do until, Concurrency Control (Degree of Parallelism 50), items(), Select, Filter array, range()
