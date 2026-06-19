---
name: research-meta-analysis
description: >-
  Pool effects across studies: extract effect sizes, fixed vs random effects, heterogeneity (I-squared), forest/funnel plots, publication-bias tests, moderators — use to synthesize quantitative evidence
---

# research-meta-analysis

Convert every study to a common effect size (d, OR, r, or risk difference) with its variance, then weight by **inverse variance** so precise studies count more. Choose the model from the heterogeneity assumption: **fixed-effect** assumes one true effect (rarely justified across labs/populations); **random-effects** assumes a distribution of true effects and is the safe default for real-world syntheses — it estimates between-study variance **tau-squared**.

Quantify heterogeneity with **I-squared** (% of variance from real between-study differences, not chance: ~25/50/75% = low/moderate/high). High I-squared means don't just report one pooled number — run **subgroup analysis or meta-regression** on moderators (dose, population, year). Visualize with a **forest plot** (each study CI + pooled diamond).

Probe **publication bias**: funnel plot asymmetry, **Egger's regression test**, and trim-and-fill to estimate corrected effect. Search grey literature and registries to prevent it upstream.

Pitfall: pooling apples and oranges — combining incomparable designs/outcomes produces a meaningless average; heterogeneity must be defensible. Second pitfall: double-counting (multiple effect sizes from one sample treated as independent) — use multilevel/robust variance estimation.

**Tools:** fixed/random-effects, I-squared/tau-squared, forest plot, funnel plot, Egger's test, trim-and-fill, metafor/meta R, RevMan
