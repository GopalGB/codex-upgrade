---
name: ba-scenario-sensitivity-analysis
description: >-
  Run scenario (base/bull/bear), sensitivity (one-way + tornado), and Monte Carlo analysis on models; use Excel Data Tables / Goal Seek / Scenario Manager; avoid changing many inputs at once.
---

# ba-scenario-sensitivity-analysis

Three distinct techniques, often confused. Sensitivity = flex ONE input at a time, hold others, see output swing — use Excel one-variable/two-variable Data Tables (DATA → What-If → Data Table), then rank drivers in a tornado chart (widest bar = the input your result is most exposed to; that's where to focus diligence). Scenario = change a coherent SET of inputs to tell a story — base / bull / bear with internally consistent assumptions (recession lowers volume AND price AND raises churn together); use Scenario Manager or a switch cell + CHOOSE/INDEX. Goal Seek / Solver inverts the model: 'what discount rate makes NPV = 0' or 'what volume hits breakeven'. Monte Carlo replaces point inputs with distributions and simulates thousands of draws to get a probability distribution of outcomes, not a single number. Expert moves: tornado first to find the 2-3 inputs that actually matter, then build scenarios around only those; always show the breakeven/threshold value, not just the swing. Pitfalls: changing many inputs at once so you can't attribute the result; double-counting correlated drivers; presenting a single 'forecast' with false precision when the realistic answer is a range; sensitivity ranges pulled from thin air — anchor them to historical volatility; circular references breaking Data Tables.

**Tools:** Excel Data Tables, Goal Seek, Scenario Manager, @RISK, Monte Carlo
