---
name: sde-back-of-envelope-estimation
description: >-
  Compute QPS, storage, bandwidth, and memory budgets fast to size every component and justify design choices with numbers.
---

# sde-back-of-envelope-estimation

Estimation turns hand-waving into engineering. Anchor on round numbers: seconds/day approx 86400 approx 10^5; year approx 3x10^7 s. **QPS**: avg = total_requests/day / 10^5; peak = avg x 2-5. **Storage**: daily_writes x record_bytes x retention_days; multiply by replication factor (typically 3). **Memory for cache**: apply the 80/20 rule - cache the 20% of keys serving 80% of reads; cache_GB = hot_keys x value_bytes. **Bandwidth**: QPS x avg_response_bytes. Know the latency ladder: L1 approx 1ns, main memory approx 100ns, SSD read approx 16us, network round-trip within DC approx 0.5ms, cross-continent approx 150ms, disk seek approx 10ms. **Sizing a server**: a modern box handles roughly thousands of QPS for simple reads; divide target QPS to get machine count. **Pitfall**: false precision - round aggressively (use 10^x), the goal is the right order of magnitude to decide 'one box vs a fleet', not an exact figure. Always restate the assumption behind each number.

**Tools:** powers-of-ten, latency numbers, capacity math
