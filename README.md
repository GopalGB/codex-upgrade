# Codex Upgrade — a portable, no-MCP power kit for OpenAI Codex CLI

Turn a plain Codex CLI into an expert dev / ML / data agent **anywhere — including
a locked-down office** where you cannot attach MCP servers or install things
freely. Clone this repo, run one command, and Codex "absorbs" a curated set of
expert **skills**, slash-command **prompts**, and an operating-law **AGENTS.md**.

Everything here is **100% file-based**: skills + prompts + plain Python scripts.
**Zero MCP required.** Tools self-install their Python deps into an isolated venv,
and if the office blocks pip they print the exact manual command instead of
failing silently.

---

## What you get

**Expert skills** (in `codex-assets/skills/`, curated — experts only, not a dump):

| Skill | What it does | Needs pip? |
|---|---|---|
| `xlsx-wrangler` | Read/transform/export **big** `.xlsx` without OOM | openpyxl (auto) |
| `deck-smith` | Read **and generate** PowerPoint `.pptx` | python-pptx (auto) |
| `pdf-extract` | PDF → text / tables / LLM-ready markdown | pymupdf etc (auto) |
| `research-scout` | Paper/prior-art search (Semantic Scholar/arXiv/Crossref; OpenAlex opt) | **none — stdlib** |
| `patent-scout` | US patent search (USPTO ODP, free key) + manual-link fallback | **none — stdlib** |
| `ml-engineer` | Build models that generalize (leakage-safe, baseline-first) | sklearn (auto) |
| `py-pro` | Production Python discipline + 2026 toolchain | none |
| `expert-hire` | **Meta**: install an existing skill or create a new one per project | none |
| `swarm` | **Multi-agent**: fan a task across N expert lenses in parallel, then synthesize | **none — stdlib** |

`research-scout` is keyless out of the box (Semantic Scholar + arXiv + Crossref).
`patent-scout`'s USPTO source needs a free key (it prints exact signup steps and
falls back to manual links + academic prior-art when absent — never fakes results).

**Slash prompts** (in `codex-assets/prompts/`) — invoked as `/prompts:<name>` in
Codex: `/prompts:absorb`, `/prompts:oracle`, `/prompts:plan`, `/prompts:council`,
`/prompts:new-skill`, `/prompts:prd`, `/prompts:lesson`, `/prompts:verify`,
`/prompts:swarm`.

**Swarm (multi-agent):** `/prompts:swarm` or the `swarm` skill fans one task across
several expert lenses **in parallel** — each is an isolated `codex exec` worker
(read-only, `--ephemeral`) — then synthesizes their findings. Portable (no MCP), uses
plain `codex exec` rather than the flaky native `[agents]`. Keep lens lists tight —
each lens is a full Codex session.

**Default methodology — the GSD loop (on by default, no command):** for any real
work Codex runs **clarify what+why → (PRD for software) → your approval → phased plan
→ your approval → build one phase at a time → verify**. Trivial edits/questions skip
the ceremony. It reads `LESSONS.md` before non-trivial work and, on any "wtf is this"
/ correction, logs the mistake so it's never repeated. (No hooks on the office path,
so these gates are behavioral law the model follows — best-effort, not enforced.)

**Law layer** (`codex-assets/AGENTS.md`): the GSD loop + approval gates, autonomy
doctrine, self-healing loop, reuse-don't-regenerate, lessons/wtf-log, security floor +
layered-architecture defaults, prompt-injection defense, JARVIS reporting,
AI-engineering expertise — all written to NOT depend on MCP/hooks.

---

## Install (one time, per machine)

```bash
git clone https://github.com/GopalGB/codex-upgrade.git
cd codex-upgrade
bash install.sh                            # backs up, then ADDS to ~/.codex (never overwrites)
```
(Office box with no GitHub access? Copy the folder over by drive and run the same
`bash install.sh`.)

`install.sh` is idempotent and additive: it backs up your existing `~/.codex`
config, replaces only its own marked block in `~/.codex/AGENTS.md` (your other
content is preserved), validates every SKILL.md, and copies the skills + prompts +
shared lib in. Re-run it any time to pull updates. **Restart Codex afterward** —
skills and prompts are only re-scanned at session start.

Useful flags:
```bash
bash install.sh --dry-run     # show exactly what would change, do nothing
bash install.sh --link        # symlink instead of copy (for active development)
bash install.sh --with-config # also merge the safe "office" profile into config.toml
bash install.sh --with-hooks  # OPTIONAL: hard-enforce the lessons loop via Codex hooks
bash install.sh --user-agents-dir  # install skills to ~/.agents/skills (future-proof)
```

### Optional: hard-enforce the lessons loop (home machines)
By default the GSD gates + "wtf is this → log a lesson" loop are **behavioral law the
model follows** (no hooks needed — works in a locked-down office). On a machine where
you can edit `config.toml`, `--with-hooks` makes the lessons loop **deterministic**:
it enables Codex's experimental `codex_hooks`, drops a `UserPromptSubmit` hook that
detects frustration signals (and writes an audit log + injects a forcing reminder),
and a `SessionStart` ritual that reminds the model of the method every session.
Experimental + unstable schema — opt-in only; the office-safe default never needs it.
Verify the whole kit any time: `bash tests/smoke.sh` (16 checks, no network).

### Or let Codex absorb it for you
From inside the repo, start `codex` and paste:
> Install this Codex Upgrade kit: run `bash install.sh`, then read
> `~/.codex/AGENTS.md` and run `/skills` to confirm the new skills are loaded.

---

## Use it

- **In any project**, run `/prompts:absorb` — Codex detects the stack and ensures
  the right experts are present (installing or creating project-scoped skills as
  needed), and drops a tailored `AGENTS.md` in the repo. This is the "works in any
  project" part.
- Skills auto-trigger by description, or invoke a tool directly, e.g.:
  ```bash
  python3 ~/.codex/skills/xlsx-wrangler/bin/xlsx.py info big.xlsx
  python3 ~/.codex/skills/research-scout/bin/research.py search "RAG eval" --source arxiv
  ```

See `docs/OFFICE-SETUP.md` for the locked-down-office runbook (no MCP, no admin,
pip blocked) and `docs/SKILLS.md` for the full skill reference.

---

## Design principles
1. **No MCP, ever required.** Office-safe by construction.
2. **Graceful degradation.** Tools try to self-install; if blocked, they tell you
   the one command to run. Never a silent failure.
3. **Additive + reversible.** Nothing is overwritten; everything is backed up.
4. **Curated experts, not a kitchen sink.** Few high-quality skills + a meta-skill
   that hires/creates more on demand, per project.
5. **Honest by default.** Anti-fabrication and anti-hallucination law baked in.
