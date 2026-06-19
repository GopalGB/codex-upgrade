---
name: retail-replenishment-autoreorder
description: >-
  Design min/max and reorder-point auto-replenishment, EOQ order quantities and review cycles to automate restocking for replenishment, auto-reorder, par levels, basic stock
---

# retail-replenishment-autoreorder

Replenishment keeps **basic/never-out** SKUs in stock automatically. Two control systems: **continuous review (s,Q)** — when on-hand+on-order hits reorder point s, order fixed quantity Q; and **periodic review (R,S)** — every R days, order up to max level S. Continuous reacts faster; periodic batches orders for shipping/labor efficiency.

**Reorder point = demand-during-lead-time + safety stock**. **Order-up-to S = demand over (review period + lead time) + safety stock**. Size Q with **EOQ = sqrt(2 x annual demand x order cost / annual holding cost per unit)** — the quantity that balances ordering cost vs carrying cost.

The expert move: round order quantities to **case/pallet packs** and respect supplier MOQs; raw EOQ ignores them and creates fractional, un-orderable quantities. Auto-reorder is for stable A/B basics — never auto-replenish fashion/seasonal (you'll re-buy a dying trend). Gate auto-orders with **demand-anomaly checks** so a one-off spike (a promo, a bulk B2B order) doesn't trigger a giant phantom reorder.

Pitfalls: feeding shipment data instead of POS (bullwhip), ignoring **phantom/negative on-hand** from shrink (system thinks stock exists, never reorders — reconcile to physical), and static safety stock through seasonality. Suppress auto-reorder on items flagged for discontinuation.

**Tools:** min/max, reorder point, EOQ, periodic vs continuous review, par levels
