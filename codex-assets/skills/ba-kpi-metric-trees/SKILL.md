---
name: ba-kpi-metric-trees
description: >-
  Design KPIs and decompose them into metric trees / driver trees (North Star → inputs), separate leading vs lagging, set SMART targets, and avoid vanity metrics and Goodhart gaming.
---

# ba-kpi-metric-trees

Define one North Star metric that captures delivered customer value (e.g. weekly active teams, GMV, hours-streamed), then decompose it into a driver tree where each node is multiplied/added from its children: Revenue = Users × Conversion × ARPU; ARPU = price × units. Every leaf must be something a team can actually move. Classify each metric as leading (predicts, actionable now — trial signups, pipeline) vs lagging (confirms, slow — revenue, churn); dashboards over-index on lagging, so add the leading driver beside each. Make targets SMART with a baseline + comparison: 'reduce p95 latency from 800ms to 400ms by Q3', not 'improve speed'. Expert move: pair every efficiency metric with a counter-metric to prevent gaming (Goodhart: 'when a measure becomes a target it ceases to be a good measure') — e.g. tickets-closed paired with reopen-rate, sales-velocity paired with churn. Pitfalls: vanity metrics (cumulative totals, raw pageviews — always go up, never inform a decision); ratios without numerator+denominator shown; metrics with no owner; mixing rates and counts in one tree so the multiplication breaks. Limit a scorecard to 5-7 metrics; more dilutes focus.

**Tools:** metric trees, OKR, North Star framework, spreadsheets
