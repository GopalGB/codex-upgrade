---
name: retail-supply-chain-leadtime
description: >-
  Manage lead time, order cycle and pipeline/in-transit inventory; compute lead-time demand and pipeline stock for supply chain, inbound logistics, on-time delivery
---

# retail-supply-chain-leadtime

Total **lead time = order processing + supplier production + transit + receiving/putaway**. Each adds days and variance. **Lead-time demand = avg daily demand x lead time** is what you must cover before the next order lands. **Pipeline (in-transit) inventory = avg demand x lead time** — capital tied up in goods you've paid for but can't sell yet; halving lead time halves pipeline stock and frees cash.

The expert move: attack **lead-time variability**, not just the average — variance drives safety stock (see safety-stock skill) more than the mean does. Track **OTIF (On-Time-In-Full)** per supplier; a supplier with a short but unreliable lead time forces more buffer than a longer but rock-steady one. Use it in vendor scorecards and to decide near-shore vs offshore (longer lead time = more pipeline + safety stock + markdown risk on fashion).

Pitfalls: planning to *quoted* lead time instead of *actual measured* (suppliers under-quote), ignoring customs/port variability on imports, and treating receiving/putaway as zero (a container sitting in the yard isn't sellable inventory). Map the end-to-end timeline, attack the longest and most variable leg first, and reflect real lead time in OTB commit dates.

**Tools:** lead-time demand, pipeline inventory, order cycle, OTIF, lead-time variability
