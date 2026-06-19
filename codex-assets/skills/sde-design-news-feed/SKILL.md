---
name: sde-design-news-feed
description: >-
  Design a social feed - fan-out on write vs read, the celebrity hot-key problem, hybrid push/pull, ranking, and feed caching.
---

# sde-design-news-feed

The whole problem is **fan-out**: when a user posts, how do followers' feeds get it? **Fan-out on write (push)**: at post time, push the post ID into every follower's precomputed timeline (in Redis lists). Reads are O(1) and instant - great for the common case - but a write fans out to millions for big accounts (the **celebrity/hot-key problem**) and wastes work on inactive followers. **Fan-out on read (pull)**: build the feed at read time by merging recent posts from everyone the user follows. Cheap writes, but reads are expensive and slow for users following many people. **Hybrid (the production answer)**: push for normal users; for **celebrities, don't fan out** - their followers pull the celebrity's posts at read time and merge with their precomputed timeline. Cache the merged feed and paginate with a **cursor** (timestamp/post-ID), never OFFSET (OFFSET degrades on deep pages). **Ranking**: chronological is simplest; engagement ranking adds a scoring service. Store posts once (post store) and timelines as lists of post IDs (hydrate on read) to avoid duplicating post bodies. **Pitfall**: pure fan-out-on-write with no celebrity special-case (a single post melts the system), and OFFSET pagination on huge feeds.

**Tools:** fan-out on write/read, hybrid push-pull, timeline cache, ranking, pagination
