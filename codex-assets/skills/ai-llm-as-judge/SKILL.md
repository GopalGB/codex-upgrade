---
name: ai-llm-as-judge
description: >-
  Use an LLM to grade outputs reliably: rubric design, pairwise vs pointwise, bias mitigation (position/verbosity/self-preference), and judge calibration — use to scale eval beyond humans.
---

# ai-llm-as-judge

LLM-as-judge scales evaluation but has known biases you MUST mitigate: position bias (favors first/last option — always swap order and average, or call twice), verbosity bias (favors longer answers), and self-preference (a model rates its own outputs higher — use a different, strong model as judge). Prefer PAIRWISE ('which is better, A or B, and why') over absolute 1-10 scoring; pairwise is far more consistent. Give the judge an explicit rubric with concrete criteria and, where possible, a reference answer (reference-guided grading sharply improves agreement). Force the judge to reason THEN emit a structured verdict (so you can parse it and audit reasoning). Calibrate: build a small human-labeled set, measure judge-vs-human agreement (Cohen's kappa); if low, fix the rubric before trusting the judge at scale. Use a strong model (frontier-tier) as judge even if production runs a cheap model. Common mistake: trusting raw judge scores without checking position bias or human agreement, then optimizing your system toward the judge's quirks (Goodhart). Re-validate the judge whenever you change the rubric.

**Tools:** pairwise comparison, rubric/criteria scoring, position-swap, reference-guided grading, judge calibration vs humans
