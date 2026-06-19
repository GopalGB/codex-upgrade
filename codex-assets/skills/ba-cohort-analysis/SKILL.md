---
name: ba-cohort-analysis
description: >-
  Build retention/revenue cohort tables and triangle heatmaps by signup period, read retention curves (flattening = PMF), compute N-day and rolling retention; avoid survivorship and mixed-window bias.
---

# ba-cohort-analysis

Group users by acquisition period (cohort = signup week/month), then measure a behavior at periods 0,1,2... since acquisition, producing a triangle table where rows = cohort, columns = age. Pick the retention definition deliberately: N-day (active exactly on day N — strict, for daily-use apps), unbounded/rolling (active on day N or later — for less-frequent products), or bracket (active within a window). The signal you want: does the retention curve flatten to a non-zero asymptote? A flat tail = a sticky core = product-market fit; a curve decaying to zero = leaky bucket, fix before spending on acquisition. Read it two ways: down a column = is retention improving for newer cohorts (product getting better?); across a row = lifecycle decay of one cohort. Build in SQL with date_trunc for the cohort key and datediff for age, then pivot. Expert moves: overlay cohort curves on one line chart to compare vintages; build revenue/dollar-retention cohorts (NRR) not just logo; annotate releases on the cohort axis to attribute lifts. Pitfalls: survivorship bias (don't drop churned users — the denominator is the original cohort size, fixed); comparing a 30-day-old cohort's 'day 60' (impossible — it's still maturing) — only compare equal ages; mixing weekly and monthly windows; tiny cohorts that are pure noise.

**Tools:** SQL, pandas, Excel pivot, Amplitude, Mixpanel
