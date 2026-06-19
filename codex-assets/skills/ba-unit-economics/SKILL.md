---
name: ba-unit-economics
description: >-
  Model unit economics: contribution margin, CAC, LTV (and LTV:CAC), payback period, cohort-based LTV; avoid revenue-not-margin LTV and blended-CAC vanity errors.
---

# ba-unit-economics

Work at the per-unit/per-customer level. Contribution margin = price − variable cost per unit; this, not gross revenue, is what funds CAC and fixed costs. CAC = fully-loaded S&M spend (salaries, ads, tooling) / new customers acquired in the SAME period — use paid/new CAC for decisions, never blended CAC that hides organic in the denominator. LTV = (average margin per period × gross margin %) ÷ churn rate for a simple steady-state, or better, sum discounted contribution margin over a retention curve from real cohorts. The two decision metrics: LTV:CAC (healthy SaaS ≈ 3:1 — below 1 you lose money per customer, far above 3 you're under-investing in growth) and CAC payback (months of contribution margin to recover CAC; <12mo strong for SMB SaaS, <18-24 for enterprise). Expert moves: build LTV bottom-up from cohort retention + expansion (NRR) rather than a single churn assumption; segment unit economics by channel/segment — blended healthy numbers often hide one unprofitable channel; gate growth spend on payback, not LTV (cash timing kills startups). Pitfalls: LTV using revenue instead of gross margin (inflates 2-5×); ignoring that early-cohort churn overstates lifetime; counting CAC and customers from different periods; treating LTV:CAC as static when both move; forgetting cost-to-serve and support in margin.

**Tools:** Excel, cohort SQL, SaaS metrics
