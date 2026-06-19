---
name: retail-clv
description: >-
  Estimate customer lifetime value (CLV/LTV) via margin x frequency x lifespan and retention/discount models to cap CAC and prioritize segments for LTV, unit economics, CAC payback
---

# retail-clv

Simple **historic CLV = avg order value x purchase frequency x gross margin% x customer lifespan (years)**. Lifespan from churn: **lifespan = 1 / churn rate** (5% annual churn -> 20-yr horizon, cap it realistically). A cleaner predictive form for contractual/retention businesses: **CLV = (avg margin per period x retention rate) / (1 + discount rate - retention rate)**, which discounts future cash and weights by survival.

The expert move: CLV exists to govern acquisition — the rule of thumb is **LTV:CAC >= 3:1** and **CAC payback < 12 months**. Compute CLV **per RFM/acquisition-channel segment**, not blended — a blended LTV hides that paid-social buyers churn fast while referral buyers are gold, and you'll overspend on the wrong channel.

Pitfalls: using *revenue* not *gross margin* (inflates LTV, justifies overspend), assuming flat retention (early cohorts churn fastest — use a survival/retention curve), and ignoring the discount rate on multi-year value. For non-contractual retail use **BG/NBD + Gamma-Gamma** (probabilistic) rather than naive frequency, since customers silently lapse. Validate CLV predictions against realized cohort revenue.

**Tools:** CLV formula, retention rate, churn, LTV:CAC ratio, discounted CLV
