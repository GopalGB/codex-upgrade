---
name: xls-whatif-goalseek-solver
description: >-
  What-if analysis: Goal Seek, Solver for optimization with constraints, one/two-variable Data Tables, Scenario Manager
---

# xls-whatif-goalseek-solver

**Goal Seek** (Data > What-If > Goal Seek) back-solves ONE input to hit a target output: 'set NPV cell to 0 by changing discount-rate cell' — fast for break-even, IRR-style single-variable problems. **Solver** (add-in: File > Options > Add-ins) optimizes (max/min/value) one objective by changing many cells **subject to constraints** — use for portfolio allocation, production mix, scheduling. Pick the engine: **Simplex LP** for linear models (fast, global optimum), **GRG Nonlinear** for smooth nonlinear (local optimum — try multistart), **Evolutionary** for non-smooth/IF-heavy models (slow, no optimality guarantee). **Data Tables** (What-If > Data Table) stress one or two inputs across a grid in one shot — row input + column input cells; the whole grid recalcs together (it's an array — can't delete one cell). **Scenario Manager** saves named input sets (Best/Base/Worst) and produces a summary. Pitfalls: Goal Seek finds only one solution and needs a monotonic relationship; Data Tables are volatile and slow huge models (switch calc to Automatic-except-tables); Solver needs sensible starting values and bounded variables or it diverges.

**Tools:** Goal Seek, Solver, Data Table, Scenario Manager
