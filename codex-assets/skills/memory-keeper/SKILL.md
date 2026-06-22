---
name: memory-keeper
description: >-
  Durable long-term memory for Codex across sessions WITHOUT a vector DB, server, or MCP
  — store facts/decisions/preferences as on-disk markdown cards and recall the top-k by
  keyword×recency×importance, so memory never floods context. Pure stdlib, works in a
  locked-down office. Use to remember a decision/fact/preference, or to recall what was
  decided/learned/configured before. Triggers: "remember that", "recall", "what did we
  decide", "save this for later", "what do you know about", "store this", "long-term memory".
---

# memory-keeper — file-based long-term memory (stdlib only, no MCP)

Script: `bin/memory.py`. Pure standard library — nothing to install, no network, no
server. Durable recall across sessions on a locked-down box.

## Resolve path
```bash
MEM="$HOME/.codex/skills/memory-keeper/bin/memory.py"
[ -f "./codex-assets/skills/memory-keeper/bin/memory.py" ] && MEM="./codex-assets/skills/memory-keeper/bin/memory.py"
```

## Commands
```bash
python3 "$MEM" add "GCB backend = FastAPI + httpx + pydantic v2" --tags gcb,stack --importance 4
python3 "$MEM" recall "what backend does gcb use" --k 5          # top-k only (context-safe)
python3 "$MEM" recall "office pip blocked" --scope global --json # machine-readable
python3 "$MEM" list  --tag gcb                                   # browse
python3 "$MEM" forget 20260622... [--decay]                     # delete (or just lower importance)
python3 "$MEM" gc    --ttl-days 120 --max 500 [--dry-run]       # bound growth
python3 "$MEM" stats                                            # count / scopes / top tags
python3 "$MEM" selftest                                        # round-trip self-check
```

## Why this and not the flat logs
The kit already has two flat files; this adds the third, queryable tier:
- `LESSONS.md` — **mistakes** never to repeat (§F wtf-log).
- `MEMORY.md` — append-only **task log** (one line per non-trivial task).
- **memory cards** (here) — **queryable facts/decisions/preferences** retrieved by relevance,
  not read top-to-bottom. This is the "semantic recall" tier from the `ai-agent-memory` skill.

## Context-safety (the whole point)
Cards live on disk in `~/.codex/memory/cards/` and are **never auto-loaded**. `recall`
returns only the top-k scored cards, so even 1000 memories cost ~0 context until you ask
the right question (§N context discipline; mirrors Codex progressive disclosure). Each
`recall` bumps the matched cards' `hits`/`last_used` so useful memories float up over time.

## Scoring
`score = TF-IDF(query, card) × importance/3 × recency`. Tags weigh 3× (deliberate index
terms). `importance` 1–5 (default 3). `recency` gently favors recently-used cards
(~1.3× fresh → 1.0× old) without letting recency beat a strong keyword match.

## What to STORE (be selective — durable facts only, not every token)
- A decision + its WHY ("chose keyset pagination over OFFSET because the table is 40M rows").
- A stable fact about the project/stack/env ("the office box blocks pip; use tools-venv").
- A user preference/correction worth keeping ("G wants prose over bullets in reports").
- A non-obvious config/credential LOCATION (never the secret itself — §G/§H).
Use `--scope project:<name>` for repo-specific memory, `global` (default) for cross-project.

## What NOT to store
Secrets/tokens/PII (§H — store a pointer, never the value) · transient state · anything
re-derivable in seconds · raw tool dumps (distill first). Run `gc` periodically to prune
stale, never-hit, low-importance cards so recall stays fast (unbounded growth is the
classic memory failure mode).

## Wired into the law (§F)
Before non-trivial work, `recall` what's relevant; after, `add` the one durable fact a
future session would pay 5+ min to re-learn. Best-effort model discipline — the
`session-start` hook surfaces the card count as a reminder when hooks are enabled.

## Self-check
`python3 "$MEM" selftest` round-trips add → dedup → recall-rank → forget in a temp dir and
asserts the ranking — run it after any edit to the tool.
