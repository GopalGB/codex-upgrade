---
name: gsd-map-codebase
description: >-
  Map an unfamiliar codebase before changing it — parallel reader passes (swarm) into .planning/codebase/ docs: architecture, key modules, conventions, risks. Use when joining a repo.
---

# gsd-map-codebase

Before editing an unfamiliar repo, build a map. Fan out parallel reads with the `swarm` skill across dimensions — architecture/entry-points, key modules + data flow, conventions/patterns, tests, and risk areas — and write each to `.planning/codebase/<dimension>.md`. Use the `toolbelt` (rg for search, ast-grep for structure, `code-review-graph` MCP if present) instead of slow manual reads. The map makes every later GSD phase faster and prevents reinventing what exists (§D reuse ladder). Adapted from `gsd-map-codebase`. Pitfall: changing code you haven't mapped = breaking hidden contracts; an hour mapping saves days debugging. Keep the maps short + current. Next: `gsd-spec` the change.

**Tools:** swarm, rg/ast-grep (toolbelt), .planning/codebase/
