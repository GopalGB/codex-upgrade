---
name: sde-design-url-shortener
description: >-
  Design TinyURL/bit.ly - short-key generation (base62, counter, hash), 301 vs 302 redirect, KV store, and read-heavy caching.
---

# sde-design-url-shortener

Classic read-heavy design. **Core API**: POST /shorten(longUrl)->shortUrl, GET /{key}->redirect. **Key generation** is the crux: (a) **base62 of a global counter** - use a distributed ID generator or hand out **ranges** to each app server (server grabs IDs 1M-2M, no per-request coordination) then base62-encode - 7 chars of base62 = 62^7 approx 3.5 trillion URLs, collision-free and short; (b) **hash (MD5/SHA) + take first N chars** - simple but needs collision handling (retry with salt). Prefer the counter+range approach to avoid collisions entirely. **Storage**: a key-value store (key -> longUrl, created_at, expiry) - billions of small records, simple lookups, so NoSQL/KV scales cleanly; this is read-heavy (clicks >> creates), so put a **cache (Redis, LRU)** in front - hot links serve from memory. **Redirect**: **301 (permanent)** lets browsers cache and cuts your traffic but loses click analytics; **302 (temporary)** routes every click through you for analytics - pick based on whether you need metrics. **Estimate** to justify: e.g., 100M writes/day approx 1.2K QPS write, 100x reads approx 120K QPS read -> cache + replicas mandatory. **Pitfall**: predictable sequential keys (enumeration/scraping) - if that matters, shuffle/encrypt the counter before encoding; and forgetting custom aliases + expiry in the data model.

**Tools:** base62, distributed counter/Snowflake, KV store, 301/302, cache, range allocation
