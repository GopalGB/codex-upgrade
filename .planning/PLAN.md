# PLAN — codex-upgrade v3.4.0 (ponytail + long-memory + curated experts)

**Goal:** Upgrade the no-MCP OpenAI Codex CLI power kit with (1) ponytail minimal-code
discipline as a skill AND operating law, (2) a real file-based long-term MEMORY system
(context-safe, no-MCP), (3) a curated set of genuinely-missing core coding experts —
without bloating the startup skill-metadata footprint (the "~2%" Codex context meter).

## Context facts (grounded this session)
- Codex loads ONLY each skill's `name`+`description` at startup (progressive disclosure);
  body loads on trigger; bundled scripts run WITHOUT entering context.
- Current footprint: 390 skills · name+desc ≈ 75,470 chars ≈ 18.9k tokens ≈ ~1.9% of a
  ~1M window ("the 2%"). It grows linearly per skill ⇒ keep new descriptions tight (~1 line).
- Bundled-tool convention in this repo: `skills/<name>/bin/<tool>.py`, stdlib-first,
  path-resolve snippet at top of SKILL.md. Validator: lib/validate_skill.py (name==folder,
  lowercase-hyphen ≤64, description ≤1024, SKILL.md only — no README/CHANGELOG in dir).

## Deliverables
- [ ] P1 `skills/ponytail/SKILL.md` — minimal-code ladder, Codex/no-MCP framing.        (me)
- [ ] P1 `AGENTS.md` §Q — MINIMAL-CODE LAW (default behavior; pairs with §D/§K).         (me)
- [ ] P2 `skills/memory-keeper/SKILL.md` + `bin/memory.py` + `references/`               (me)
        long-term recall over markdown cards in ~/.codex/memory/cards/, keyword×recency×
        importance scored, stdlib-only, top-k (context-safe), self-test/demo built in.
- [ ] P2 `AGENTS.md` §F upgrade — wire `memory.py recall/add` into the memory law.        (me)
- [ ] P2 `hooks/session-start.py` — surface memory-card count + recall hint (best-effort). (me)
- [ ] P3 `skills/tdd-engineer/SKILL.md`                                          (agent, parallel)
- [ ] P3 `skills/git-flow/SKILL.md`                                              (agent, parallel)
- [ ] P3 `skills/sql-pro/SKILL.md`                                               (agent, parallel)
- [ ] P4 Updates: VERSION→3.4.0 (law v2.9), README core table + memory section,
        docs/SKILL-LIBRARY.md (core 18→23, total 390→395), install.sh (cards dir seed).
- [ ] P5 VERIFY: validate_skill.py OK · memory.py selftest OK · install.sh --dry-run clean.

## Success criteria
- `python3 lib/validate_skill.py codex-assets/skills` → OK (395 valid).
- `python3 codex-assets/skills/memory-keeper/bin/memory.py selftest` → OK (add→recall→forget).
- `./install.sh --dry-run` runs clean, reports new skills + memory wiring.
- New descriptions tight (~500 chars each) ⇒ +~0.06% footprint, "2%" stays ~2%.
- AGENTS.md edits surgical (block markers preserved, law v2.8→v2.9).

## Out of scope (curation — kit philosophy is "experts, not a dump"; ponytail = don't speculate)
- Vector/embedding memory (needs a model/network ⇒ violates no-MCP/office). Keyword recall is
  the correct no-MCP long-memory design.
- A large skill batch. +5 core only, each a real coding-agent gap. Expand on explicit request.

STATUS: EXECUTING (additive + fully reversible via git — no approval gate needed).
