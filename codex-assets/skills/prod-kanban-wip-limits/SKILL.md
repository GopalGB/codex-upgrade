---
name: prod-kanban-wip-limits
description: >-
  Run a personal/team Kanban board with explicit WIP limits to visualize flow, expose bottlenecks, and finish work faster by limiting work-in-progress
---

# prod-kanban-wip-limits

Kanban visualizes work as cards flowing left-to-right across columns (e.g., Backlog -> To Do -> Doing -> Review -> Done) and improves throughput by **limiting work-in-progress**. The core move: set an explicit WIP limit on in-progress columns (personal Kanban: often 2-3 in 'Doing'). When a column is at its limit you may NOT pull a new card-you must first finish or unblock an existing one. This is counterintuitive but decisive: starting fewer things finishes more, because **Little's Law** (cycle time = WIP / throughput) means more concurrent work directly lengthens how long each item takes to complete. WIP limits surface bottlenecks visibly: if cards pile up before 'Review', that stage is the constraint-attend to it (Theory of Constraints). Use a **pull system** (downstream pulls when it has capacity) not push. Track **cycle time** (start-to-done) as your key metric, not how busy people look. The dominant failure mode is no WIP limit-then Kanban is just a prettier to-do list and everything is perpetually 'in progress' with nothing shipping. Start the limit low; raise only if flow stays smooth and starves.

**Tools:** Kanban, WIP limits, Little's Law, pull system, cycle time, cumulative flow
