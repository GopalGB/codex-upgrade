---
name: research-logistic-regression
description: >-
  Fit and interpret logistic regression for binary outcomes: log-odds, odds ratios, marginal effects, model fit (AUC, pseudo-R2), separation — use when the outcome is yes/no
---

# research-logistic-regression

Logistic regression models the log-odds of the outcome as linear in predictors. Coefficients are in log-odds (uninterpretable directly) — **exponentiate to odds ratios**: OR > 1 raises odds, OR < 1 lowers, and OR is multiplicative per one-unit X. For a more intuitive story, report **average marginal effects** (change in predicted probability), since the probability effect is nonlinear and depends on baseline.

Assess fit differently than OLS: there's no real R-squared — use **McFadden pseudo-R-squared**, the **Hosmer-Lemeshow** goodness-of-fit test (calibration), and **ROC AUC** for discrimination (0.5 = chance, > 0.8 = strong). Pick a classification threshold from the cost of errors, not the default 0.5, especially with class imbalance.

Watch for **complete/quasi separation** (a predictor perfectly splits the outcome -> coefficients blow up to infinity) — use penalized (Firth) logistic regression. Need >= ~10 events per predictor (EPV rule) or estimates are unstable.

Pitfall: interpreting odds ratios as risk ratios — for common outcomes they diverge sharply; report risk ratios or marginal effects if probability is the message. Second pitfall: evaluating an imbalanced classifier by accuracy alone (95% accuracy is trivial when 95% are negatives) — use AUC, precision/recall.

**Tools:** logit, odds ratio, log-odds, ROC/AUC, McFadden pseudo-R2, Hosmer-Lemeshow, marginal effects, statsmodels/sklearn
