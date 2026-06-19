---
name: research-sampling-methods
description: >-
  Choose and execute a sampling strategy: probability (SRS, stratified, cluster, systematic) vs non-probability (quota, purposive, snowball) + sample-size logic — use when deciding who to study
---

# research-sampling-methods

First decide probability vs non-probability by your goal: generalizable population estimates REQUIRE probability sampling (every unit has a known nonzero selection probability); theory-building or hard-to-reach groups justify purposive/snowball. State the **sampling frame** explicitly and name its coverage gaps (the frame error).

Probability options: **Simple random** (baseline); **stratified** (sample within strata — gains precision when strata differ, lets you oversample small subgroups, then weight back); **cluster** (sample groups then units — cheaper for dispersed populations but raises variance via the **design effect**, deff = 1 + (m-1)*ICC); **systematic** (every kth — fast but deadly if the list has periodicity matching k).

Size from precision, not gut: for a proportion, n = z^2 p(1-p)/e^2, then apply the finite-population correction for small populations and multiply by the design effect for clusters. For comparisons, size from a power analysis (see research-ab-testing-power).

Pitfall: convenience sampling reported as if representative — this is the #1 generalizability killer. Second pitfall: ignoring nonresponse bias; a 60% response rate from a probability frame can be more biased than a smaller balanced sample.

**Tools:** Stratified/cluster/systematic sampling, sampling frame, design effect, finite population correction, power-based n
