---
name: expert-hire
description: >-
  Meta-skill: when a task needs expertise the current skills do not cover, FIND
  an existing skill and install it, or CREATE a new project-scoped expert skill -
  then use it. Also the dispatcher: pick the few RIGHT experts for a task, not
  everything. Use at the start of any non-trivial, domain-specific task.
  Triggers: "I need an expert in", "is there a skill for", "create a skill",
  "set up tooling for this project", "you don't have a tool for this".
---

# expert-hire — get the right expert, or build one (no MCP)

The doctrine G asked for: **"if a skill exists, get it; if not, create your own —
project by project, by the actual requirement. Experts only, top tier, not
everything."** This skill operationalizes that.

## Step 0 — Dispatch, don't dump (the "two should be two" rule)
For the task in front of you, name the 1-3 experts that ACTUALLY apply and use
only those. Do not fan out every skill. Quality and focus over breadth.
- big Excel / spreadsheets → `xlsx-wrangler`
- PowerPoint → `deck-smith`   · PDFs → `pdf-extract`
- papers / prior art / DOIs → `research-scout`
- modeling → `ml-engineer`    · Python craft → `py-pro`
- patents → `patent-scout`
If one of those fits, just use it. Only proceed below when NONE fits.

## Step 1 — Check what's already installed
```bash
ls ~/.codex/skills/ 2>/dev/null
[ -d .agents/skills ] && ls .agents/skills/   # project-scoped skills
```
Read the candidate `SKILL.md` before deciding it doesn't fit.

## Step 2 — Try to INSTALL an existing skill
Codex ships a system skill for this. Prefer reusing a vetted skill over writing one:
```
Invoke the system skill:  skill-installer
```
Give it the capability you need (e.g. "PDF form filling", "DOCX generation",
"SQL schema diffing"). It locates and installs a skill. Vet the source before
trusting it (stars, last update, license, no obvious supply-chain risk) — an
unvetted skill that hooks every tool call is a YELLOW, never an auto-GREEN.

## Step 3 — If none exists, CREATE one (project-scoped by default)
Use the Codex system skill `skill-creator`. Author the new skill where it belongs:
- **Project-specific need** → `<repo>/.agents/skills/<name>/SKILL.md`
  (travels with the repo; the right default for client/work projects).
- **Reusable everywhere** → `~/.codex/skills/<name>/SKILL.md`.

A good new skill has:
- YAML frontmatter: `name` + a `description` packed with trigger phrases so Codex
  auto-surfaces it.
- A crisp "How to work" section and guardrails.
- A `bin/` script if it needs to DO something — make scripts self-bootstrap deps
  via `~/.codex/skills/_lib/codex_env.py` (venv + pip-or-graceful-degrade), so the
  new tool also survives a locked-down, no-MCP office.

Then immediately use the skill you just made and report what you created.

## Step 4 — Record it
Append one line to `~/.codex/memory/MEMORY.md`:
`[date] created/installed skill <name> for <why>` so future sessions reuse it.

## Guardrails
- Never install a skill that wants broad outbound network + sensitive-file read in
  one loop (two-loop prohibition). Split or refuse.
- Keep the global skill set lean; push niche/project skills into `.agents/skills/`.
- Prefer keyless, dependency-light tools (office constraint).
