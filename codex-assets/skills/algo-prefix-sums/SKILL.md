---
name: algo-prefix-sums
description: >-
  Prefix-sum / difference arrays for O(1) range queries and O(1) range updates — subarray-sum-equals-K, 2D submatrix sums, interval bumps.
---

# algo-prefix-sums

Precompute `pre[i] = a[0]+…+a[i-1]` so any range sum is `pre[j+1]-pre[i]` in O(1) after O(n) build. The high-leverage combo is **prefix-sum + hashmap**: for 'count subarrays summing to K', store counts of seen prefix sums and at each index add `seen[pre - K]` — O(n) instead of O(n²). Works for subarray-divisible-by-K (key on `pre % K`) and longest-subarray-sum-zero. 

**2D**: an integral image gives any submatrix sum in O(1) via inclusion-exclusion (`S[d]-S[b]-S[c]+S[a]`). **Difference array** is the dual: to add v over [l,r] many times, do `diff[l]+=v; diff[r+1]-=v` then one prefix pass — O(1) per update. For online point-update + range-query, graduate to a **Fenwick/BIT** (O(log n) each). 

Pitfalls: (1) off-by-one in the half-open `pre[j+1]-pre[i]` convention — always seed `pre[0]=0`. (2) For mod problems, normalize negatives: `((pre % K) + K) % K`. (3) Forgetting to pre-seed `seen[0]=1` so a prefix that itself equals K counts.

**Tools:** 1D prefix, prefix+hashmap, 2D integral image, difference array, Fenwick
