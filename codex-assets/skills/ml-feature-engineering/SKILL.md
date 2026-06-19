---
name: ml-feature-engineering
description: >-
  Craft, encode, and transform raw columns into model-ready features — the highest-leverage step in tabular ML
---

# ml-feature-engineering

Feature engineering usually beats model choice for tabular wins. **Categoricals:** one-hot for low cardinality; target/mean encoding for high cardinality (but compute it inside CV folds — leaky otherwise — or use CatBoost's ordered encoding); frequency encoding; never label-encode nominal categories for linear/distance models (imposes false order). **Numeric:** log/Box-Cox for skewed/heavy-tailed; binning to capture non-linearity for linear models; standardize for distance/linear/NN models (trees don't need it). **Datetime:** extract day-of-week, month, is_holiday; encode cyclical features as sin/cos pairs so December is near January. **Interactions/ratios:** products and domain ratios (e.g., debt/income) often add the most signal. **Text:** TF-IDF, char n-grams, embeddings. **The cardinal pitfall — data leakage:** any feature that encodes the target or uses future/test information (target encoding without folds, scaler fit on full data, aggregates computed across train+test) inflates CV and collapses in production. Fit every transformer on train only, inside a Pipeline. Handle missingness deliberately (add is_missing flags; median/iterative impute) rather than dropping rows.

**Tools:** target/one-hot encoding, binning, interactions, scaling, datetime/cyclical, log transforms
