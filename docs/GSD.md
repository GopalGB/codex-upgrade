# GSD (Get Shit Done) — in the Codex kit

The `gsd-*` skills adapt the Claude Code **GSD** methodology suite
(`~/.claude/skills/gsd-*`) for Codex — file-based, no Claude-Code-agent tooling, using
`.planning/` for state, `swarm` for parallel phases, and `claude-review` + `security-auditor`
at the gates.

**Lifecycle:** `gsd-new-project` → `gsd-spec` → `gsd-discuss` → `gsd-plan-phase` →
`gsd-execute-phase` → `gsd-verify` → `gsd-code-review` → `gsd-ship` → `gsd-extract-learnings`.
Plus `gsd-map-codebase` (join a repo), `gsd-debug` (persistent-state debugging),
`gsd-progress` (where am I / what next).

**Strict (AGENTS.md ⛔ gates):** GSD is the DEFAULT for all non-trivial work — not opt-in —
and **Claude Opus 4.8 must review the code** (`claude-review`) before anything is DONE.

Origin: the GSD suite is a Claude Code skill set; these are Codex-adapted ports of the same
plan→execute→verify discipline. Run `gsd-progress` anytime you're unsure of the next step.
