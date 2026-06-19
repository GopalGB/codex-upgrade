---
name: research-data-cleaning
description: >-
  Clean and prepare data for analysis: missing-data mechanisms (MCAR/MAR/MNAR) + imputation, outliers, type coercion, dedup, tidy/long format, validation — use before any modeling
---

# research-data-cleaning

Profile first (`df.info()`, `df.describe()`, value counts, missingness map) so you fix real problems, not imagined ones. Diagnose **missingness mechanism** because it dictates the fix: **MCAR** (missing at random of everything) -> listwise deletion is unbiased but wasteful; **MAR** (missingness depends on observed vars) -> **multiple imputation (MICE)** or model-based methods; **MNAR** (depends on the unseen value itself, e.g., high earners hiding income) -> needs modeling assumptions and sensitivity analysis. Never default to mean imputation — it shrinks variance and distorts correlations.

Reshape to **tidy/long format** (one variable per column, one observation per row) — most analysis and plotting tools assume it. Coerce types deliberately (dates, categoricals), standardize categories ("NY"/"New York"), de-duplicate on a defined key, and trap outliers with IQR/z-score (investigate, don't auto-delete). Encode an explicit missing indicator if missingness itself is informative.

The expert move: write **assertion/validation checks** (ranges, uniqueness, referential integrity) that fail loudly, so a re-run catches new dirty data. Keep cleaning as scripted, version-controlled steps — never hand-edit the raw file.

Pitfall: silent coercion turning IDs into floats or dropping leading zeros. Second pitfall: imputing then reporting standard errors as if data were complete — use multiple imputation pooling (Rubin's rules).

**Tools:** pandas/dplyr/tidyr, MCAR/MAR/MNAR, multiple imputation (MICE), IQR/z-score, tidy data, pandas-profiling, assert checks
