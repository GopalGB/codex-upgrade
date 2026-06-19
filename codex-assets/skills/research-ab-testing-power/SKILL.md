---
name: research-ab-testing-power
description: >-
  Plan and read online A/B tests + power/sample-size analysis: MDE, power, alpha, sample size, peeking, novelty effects, SRM — use for product experiments and any two-arm comparison
---

# research-ab-testing-power

Compute sample size BEFORE launch from four levers: **alpha** (.05), **power** (1-beta, target 0.80+), the **minimum detectable effect** (the smallest lift worth shipping), and baseline variance/rate. Smaller MDE -> quadratically more traffic. Use G*Power or statsmodels' `tt_ind_solve_power` / proportion power. Fix the duration to >= one full business cycle (a week) to absorb day-of-week effects, and pre-commit to it.

Do NOT peek and stop at first significance — repeated looks inflate false positives massively (the #1 A/B sin). If you must monitor, use **sequential testing** (alpha spending, mSPRT) or Bayesian methods designed for continuous evaluation. Run a **Sample Ratio Mismatch** check (chi-square on actual vs intended split) — a failing SRM means the experiment is broken; discard it.

Guard against **novelty/primacy effects** (early adopters react to change, not value) by reading a stable later window. Reduce variance (more power for free) with **CUPED** using pre-period covariates. Correct alpha across multiple metrics/variants.

Pitfall: declaring a winner on an underpowered test (false null) or on a peeked one (false positive). Second pitfall: ignoring practical significance — a statistically significant 0.1% lift may not pay for itself.

**Tools:** power analysis (power, alpha, MDE), G*Power/statsmodels, sequential testing, SRM chi-square, CUPED, Bonferroni
