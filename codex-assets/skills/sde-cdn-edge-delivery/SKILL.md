---
name: sde-cdn-edge-delivery
description: >-
  Serve static and cacheable content from edge PoPs - cache headers, TTL, purge, origin shielding, and dynamic edge logic.
---

# sde-cdn-edge-delivery

A CDN caches content at edge points-of-presence near users, cutting latency and offloading origin. **Pull CDN** fetches from origin on first miss then caches (simple, good for large catalogs); **push CDN** you upload assets ahead of time (control over freshness, good for predictable hot files). Control behavior with HTTP headers: `Cache-Control: public, max-age=31536000, immutable` for hashed/fingerprinted assets; short max-age + `stale-while-revalidate` for semi-dynamic; `ETag`/`Last-Modified` for conditional revalidation (304s). **Invalidation**: prefer content-hashed filenames (`app.a1b2c3.js`) so a new deploy = new URL = no purge needed; explicit purge is slow and rate-limited. Use **origin shielding** (a designated mid-tier PoP) to collapse origin requests during cache fill. Edge functions (Cloudflare Workers, Lambda@Edge) run logic at the edge for A/B, auth, redirects. **Pitfall**: caching personalized/authenticated responses publicly - leaks one user's data to another; mark them `private`/`no-store` and vary on the right keys.

**Tools:** CloudFront/Cloudflare, Cache-Control, ETag, edge functions, push vs pull
