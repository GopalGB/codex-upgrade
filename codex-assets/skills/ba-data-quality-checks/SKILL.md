---
name: ba-data-quality-checks
description: >-
  Validate dataset quality before analysis across the 6 dimensions (completeness/accuracy/consistency/validity/uniqueness/timeliness): null/dup/range/referential profiling, outlier detection; avoid analyzing dirty data silently.
---

# ba-data-quality-checks

Profile before you analyze — the fastest way to a wrong conclusion is trusting dirty data. Check the six dimensions: completeness (null/blank counts per column, missing rows vs expected volume), validity (values conform to type/format/domain — emails, dates parseable, enums in allowed set, ranges sane), accuracy (matches a source of truth / reasonable bounds), consistency (same fact agrees across tables; units and timezones uniform), uniqueness (primary-key dedup, fuzzy duplicates), timeliness (freshness vs SLA, no stale partitions). Concrete moves: row-count reconciliation vs source; COUNT vs COUNT(DISTINCT pk) to catch dup grain; GROUP BY on categoricals to spot typo variants ('US'/'USA'/'U.S.'); min/max/percentiles to catch impossible values (negative age, future dates, 999 sentinels); referential-integrity anti-joins for orphan FKs; distribution shifts vs last load. Automate with Great Expectations or dbt tests (not_null, unique, accepted_values, relationships) in the pipeline so checks run every refresh. Expert moves: quantify and DOCUMENT what you excluded and why — silently dropping 12% of rows changes the answer; distinguish missing-at-random from systematic gaps (a whole region absent biases everything); flag, don't auto-impute, without saying so. Pitfalls: averaging over nulls treated as zero; sentinel codes (−1, 9999, 1900-01-01) skewing stats; aggregating before checking grain (double counts); assuming the export equals the source; presenting results without a data-caveats note.

**Tools:** SQL, pandas-profiling, Great Expectations, dbt tests
