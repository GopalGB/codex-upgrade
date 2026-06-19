---
name: research-confidence-intervals-effect-sizes
description: >-
  Report and interpret CIs and effect sizes (Cohen's d, r, odds ratio, eta-squared) — the magnitude/uncertainty layer p-values omit — use whenever reporting any quantitative result
---

# research-confidence-intervals-effect-sizes

A p-value tells you IF; the effect size tells you HOW MUCH and the CI tells you HOW PRECISELY. Report all three. Pick the effect size to match the test: **Cohen's d** (or Hedges' g for small n) for mean differences (~0.2 small, 0.5 medium, 0.8 large — but field benchmarks beat Cohen's rules of thumb); **Pearson r** / r-squared for correlation/variance explained; **odds ratio** or **risk ratio** for binary outcomes; **eta-squared** / partial eta-squared for ANOVA.

A **95% CI** is the range of plausible parameter values; interpret its WIDTH (precision) and whether it crosses the null (0 for differences, 1 for ratios). The correct reading: "95% of such intervals from repeated samples contain the true value" — NOT "95% probability the true value is in THIS interval." For non-normal stats or small samples, use a **bootstrap CI** (resample with replacement, take 2.5/97.5 percentiles).

Pitfall: reporting only p with no effect size — reviewers and meta-analyses need the magnitude. Second pitfall: declaring two groups "different" because one CI excludes a value and the other doesn't — compare the CI of the DIFFERENCE, or test directly; overlapping CIs don't imply non-significance.

**Tools:** Cohen's d, Hedges' g, Pearson r, odds/risk ratio, eta-squared, 95% CI, bootstrap CI
