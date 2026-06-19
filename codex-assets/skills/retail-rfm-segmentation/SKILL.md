---
name: retail-rfm-segmentation
description: >-
  Segment customers with RFM (recency, frequency, monetary) scoring and quintile tiers to target champions, at-risk, lapsed for customer segmentation, loyalty targeting, CRM
---

# retail-rfm-segmentation

RFM scores each customer on **Recency** (days since last purchase — lower is better), **Frequency** (# orders in window), and **Monetary** (total/avg spend). Bin each into **quintiles 1-5** (NTILE(5) in SQL, PERCENTILE bins in Excel), 5 = best; recency is reverse-ranked (most recent = 5). Concatenate to an RFM code (e.g. 555 = best).

Map codes to named segments: **Champions** (555, 554), **Loyal** (high F), **Big Spenders** (high M), **At-Risk** (was high F/M, recency now low), **Can't-Lose** (top M, lapsed), **Hibernating/Lost** (111). The expert move: tailor action to segment — Champions get early access/referral asks (don't discount, they'd buy anyway), At-Risk get win-back offers (this is where discount $ earns its keep), Lost get one cheap reactivation then suppress. R is the strongest churn predictor — weight it heavily.

Pitfalls: treating all customers the same (blanket discounts erode Champion margin), using raw thresholds instead of quintiles (drift as base grows), and ignoring purchase-cycle length (a 60-day-recency furniture buyer is fine; a coffee buyer is churning). Refresh monthly; RFM is a snapshot, segments migrate.

**Tools:** RFM scoring, quintile bins, champions/at-risk/hibernating segments, NTILE
