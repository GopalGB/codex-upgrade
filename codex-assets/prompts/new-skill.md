---
description: Find + install an existing expert skill, or create a new project-scoped one, then use it
argument-hint: "[capability needed]"
---
# /new-skill — create or install an expert skill on demand

Need: $ARGUMENTS

Follow the `expert-hire` skill exactly:
1. **Check** `~/.codex/skills/` and `./.agents/skills/` — does one already fit?
   Read its `SKILL.md` before deciding it doesn't.
2. **Install** an existing vetted skill via the system `skill-installer` if one
   covers the need. Vet the source (stars, recency, license, no broad-network +
   sensitive-read combo) before trusting it.
3. **Create** otherwise via the system `skill-creator`:
   - Project-specific → `./.agents/skills/<name>/SKILL.md` (travels with the repo).
   - Reusable everywhere → `~/.codex/skills/<name>/SKILL.md`.
   - Frontmatter: `name` + a `description` full of trigger phrases.
   - If it needs a script, put it in `bin/` and have it self-bootstrap deps via
     `~/.codex/skills/_lib/codex_env.py` (venv + pip-or-graceful-degrade) so it
     survives a no-MCP, pip-blocked office.
4. **Use** the skill immediately to do the task, and record it in
   `~/.codex/memory/MEMORY.md`.

Keep the GLOBAL skill set lean; default niche skills to the project's `.agents/skills/`.
