---
name: retail-market-basket
description: >-
  Run market-basket / affinity analysis with support, confidence, lift to find cross-sell pairs and bundle opportunities for basket analysis, association rules, attach rate
---

# retail-market-basket

Market-basket analysis mines transaction lines for **association rules** {A} -> {B}. Three metrics: **Support** = P(A and B) = baskets with both / all baskets (frequency — is it worth acting on?). **Confidence** = P(B|A) = baskets with both / baskets with A (how often B follows A). **Lift** = confidence / P(B) = how much more likely B is given A vs baseline; **lift >1 = real affinity**, =1 independent, <1 substitutes.

The expert move: confidence alone misleads — bread has high confidence after everything because bread is everywhere. **Lift corrects for popularity**, so sort rules by lift with a support floor (ignore rare flukes). Use high-lift, high-margin pairs to drive **bundles, adjacencies, 'frequently bought together', and targeted coupons** (offer the complement, not the thing already bought).

Pitfalls: chasing high-confidence/low-lift rules (trivially popular items), too-low support thresholds (spurious pairs from a handful of baskets), and acting on correlation without margin logic (bundling two loss leaders). Mind the **diaper-beer myth** — verify before merchandising. Apriori/FP-growth scale this; in Excel a SUMPRODUCT co-occurrence matrix works for a few hundred SKUs.

**Tools:** association rules, support/confidence/lift, Apriori, cross-sell bundles
