---
name: research-hypothesis-testing-pvalues
description: >-
  Run and interpret NHST correctly: null/alt, choosing the test, one vs two-tailed, what p actually means, Type I/II errors, multiple comparisons — use when testing a hypothesis
---

# research-hypothesis-testing-pvalues

State H0 and H1 and alpha (usually .05) BEFORE looking at the data. Pick the test by data type and design: two independent means -> independent t-test (or **Mann-Whitney U** if non-normal/ordinal); paired -> paired t-test (or Wilcoxon); 3+ means -> ANOVA (then post-hoc Tukey); two categoricals -> chi-square (Fisher's exact if expected cell counts < 5). Check assumptions: normality of residuals (Shapiro-Wilk / QQ plot), homogeneity of variance (Levene), independence.

Interpret p precisely: it is P(data this extreme or more | H0 true), NOT the probability H0 is true and NOT effect size. p = .04 with n = 100,000 can be a trivial effect. Default to two-tailed; only go one-tailed if a directional prediction was preregistered.

Correct for **multiple comparisons**: Bonferroni (conservative) or Benjamini-Hochberg FDR (better-powered) when running many tests — 20 tests at alpha .05 expect ~1 false positive by chance.

Pitfall: p-hacking — trying tests/subgroups until p < .05. Preregister or report all tests run. Second pitfall: treating p > .05 as "proof of no effect" — absence of evidence != evidence of absence; report the CI and power.

**Tools:** t-test, chi-square, ANOVA, Mann-Whitney, alpha, Bonferroni/FDR, assumption checks (Shapiro, Levene)
