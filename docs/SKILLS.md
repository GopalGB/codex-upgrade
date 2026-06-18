# Skill reference

Curated expert skills (experts only — not a kitchen sink). Each is a folder under
`codex-assets/skills/<name>/` with a `SKILL.md` (name + description) and, where it
needs to *do* something, a `bin/` script that self-bootstraps its deps via
`~/.codex/lib/codex_env.py` (venv + pip-or-graceful-degrade). Read each `SKILL.md`
for the full command list.

| Skill | Use it for | Backing script | Deps |
|---|---|---|---|
| **xlsx-wrangler** | Big `.xlsx` read/stats/grep/CSV-export/build | `bin/xlsx.py` | openpyxl, xlsxwriter (auto) |
| **deck-smith** | Read + generate PowerPoint | `bin/deck.py` | python-pptx (auto) |
| **pdf-extract** | PDF → text/tables/markdown (permissive libs) | `bin/pdf.py` | pypdf, pdfplumber (auto) |
| **research-scout** | Papers / prior art / DOIs (keyless) | `bin/research.py` | stdlib only |
| **patent-scout** | US patents (USPTO ODP, free key) + manual links | `bin/patents.py` | stdlib only |
| **ml-engineer** | Build models that generalize | — (playbook) | sklearn etc (when used) |
| **py-pro** | Production Python discipline | — (playbook) | none |
| **expert-hire** | Find/install/create a skill on demand | — (meta) | none |

## How invocation works (Codex v0.121)
- **Skills auto-trigger** from their `description` (the sole always-in-context
  signal). You can also drive a tool directly:
  `python3 ~/.codex/skills/<skill>/bin/<script>.py ...`.
- **Prompts** are explicit: `/prompts:absorb`, `/prompts:oracle`, `/prompts:plan`,
  `/prompts:council`, `/prompts:new-skill`, `/prompts:prd`, `/prompts:lesson`.
- After installing or editing skills/prompts, **restart Codex** (re-scan happens at
  session start only).

## Default methodology (the GSD loop — AGENTS.md §C/§F)
On by default, no command needed. Trivial work → just done. Real work → **clarify
what+why → (PRD for software) → your approval → phased plan → your approval → build
one phase at a time → verify**. Codex reads `LESSONS.md` before non-trivial work and,
on any "wtf is this" / correction, logs the mistake so it isn't repeated.
**Honesty:** the §C clarity/PRD gates and the §F lessons loop are behavioral law the
model follows — there are **no hooks on the office-safe path**, so they are
best-effort, not harness-enforced. `/prompts:prd` and `/prompts:lesson` are the manual
levers. (The kit's GSD law is its own §C; unrelated to any host `gsd:*` skill suite.)

## Authoring rules (so new skills load on v0.121)
- Folder name == `name`, lowercase/digits/hyphens, ≤64 chars.
- Frontmatter has ONLY `name` + `description` (+ optional `metadata.short-description`).
  Codex silently drops `allowed-tools`/`model`/`license` — put tool/policy metadata
  in a sibling `agents/openai.yaml` if you need it.
- Pour all "when to use this" language into `description`.
- No `README.md`/`CHANGELOG.md` inside a skill folder (skill-creator discourages it).
- Validate before shipping: `python3 lib/validate_skill.py codex-assets/skills`.

## Adding your own
Use the `expert-hire` skill or `/prompts:new-skill <capability>`. Project-specific
skills belong in the repo's `.agents/skills/`; globally-reusable ones in
`~/.codex/skills/` (or `~/.agents/skills/`).
