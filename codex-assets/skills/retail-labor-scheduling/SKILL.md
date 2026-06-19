---
name: retail-labor-scheduling
description: >-
  Build store labor schedules from traffic-driven demand, sales-per-labor-hour and coverage to match staffing to footfall for workforce management, scheduling, SPLH
---

# retail-labor-scheduling

Store labor is the largest controllable expense after COGS. Schedule to **demand, not equal shifts**: build an hourly **traffic/transaction curve** (from door counters / POS), then staff to a target **coverage ratio** (customers or transactions per associate) so service holds at peak without idle payroll at open.

Key metrics: **Sales per Labor Hour (SPLH) = net sales / labor hours** (productivity), **labor as % of sales** (cost control, often budgeted 8-15% depending on format), and **conversion** (did adding staff at peak actually convert more traffic?). The expert move: optimize the **trade-off curve** — understaffing peak loses sales (low conversion when lines form); overstaffing troughs burns margin. Find the point where the marginal associate's incremental sales x conversion still beats their cost.

Pitfalls: scheduling to last week's *sales* instead of *traffic* (sales are censored by how staffed you were — a stockout/queue suppressed them), ignoring task labor (receiving, replenishment, BOPIS picking) that competes with selling labor, and violating **predictive-scheduling / fair-workweek laws** (advance notice, clopening rules) that carry penalties. Schedule selling staff to traffic, task staff to off-peak; track plan-vs-actual hours daily.

**Tools:** sales per labor hour, traffic-to-staff ratio, demand-based scheduling, labor as % of sales
