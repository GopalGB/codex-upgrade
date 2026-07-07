# Codex Upgrade — a portable, no-MCP power kit for OpenAI Codex CLI

Turn a plain Codex CLI into an expert **office + engineering agent — built for a
locked-down office** where you cannot attach MCP servers, install packages freely, or
run anything as admin. Clone (or copy) this repo, run one command, and Codex "absorbs"
a curated set of expert **skills** — Excel · PowerPoint · VBA · Power BI / Automate / Apps
· Copilot Studio · M365 + Graph · business analytics, plus software / ML / AI engineering,
agent-building, and an exhaustive code **audit** — as slash-command **prompts** and an
operating-law **AGENTS.md**. Curated for office work: personal packs (résumé/interview
prep) were pruned so what installs is what you actually use at work.

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
| `ml-engineer` | **Deep** end-to-end ML/AI eng (train→fine-tune→eval→quantize→serve) | sklearn etc (auto) |
| `py-pro` | Production Python discipline + 2026 toolchain | none |
| `expert-hire` | **Meta**: install an existing skill or create a new one per project | none |
| `swarm` | **Multi-agent**: fan a task across N expert lenses in parallel, then synthesize | **none — stdlib** |
| `ui-ux-engineer` | Distinctive, taste-driven UI — anti-AI-slop (shadcn/Base UI/Tailwind v4/Motion) | none |
| `research-expert` | Deep research **methodology** + best research-agent repos | none |
| `rag-engineer` | RAG done right — hybrid + rerank + eval (not cosine-and-pray) | none |
| `agent-builder` | Production agentic systems (LangGraph/MCP/A2A, eval+observe) | none |
| `data-engineer` | Idempotent ELT, no-OOM (dbt/SQLMesh/DuckDB/Polars/dlt) | none |
| `claude-review` | **Cross-review**: Claude Opus 4.8 reviews the git diff (the verify gate) | none |
| `security-auditor` | Secret scan + SAST + dep-audit (gitleaks/semgrep/osv/pip-audit) | none* |
| `production-audit` | **Exhaustive audit**: 24-lens converge-until-clean, every finding proven at file:line, + fix mode | none |
| `toolbelt` | Prefer fast CLI tools (rg/jq/pandoc/duckdb + ast-grep/fd/yq) over scripts | none* |
| `doc-forge` | DOCX + universal convert (pandoc) + OCR for scanned PDFs/patents | pandoc/ocrmypdf |
| `ponytail` | **Minimalism**: write less code — the YAGNI→reuse→stdlib→native→one-line decision ladder | none |

<sub>*orchestrates CLI tools; most are already on a typical dev box (the skill notes what to install).</sub>

### Skill library — 363 deep sub-skills (v3.6.1)
On top of the 20 core experts, a namespaced library covers your work in depth
(**383 skills total**). Codex auto-triggers them by description — no command needed.
Full index: [`docs/SKILL-LIBRARY.md`](docs/SKILL-LIBRARY.md).

| Pack | # | Covers |
|---|---|---|
| `gsd-*` | 12 | **GSD methodology**: new-project→spec→plan→execute→verify→ship + debug/map/progress ([docs/GSD.md](docs/GSD.md)) |
| `craft-*` | 16 | **Agent discipline** (ponytail-style): TDD red-green, surgical diffs, verify-before-done, no-hallucinated-APIs, read-before-edit, fail-loud, git-safety, domain-modeling, self-review |
| `pbi-*` | 23 | Power BI: DAX/CALCULATE, time-intelligence, Power Query M, modeling, RLS, performance |
| `pa-*` | 20 | Power Automate: flows, triggers, expressions, error handling, RPA/desktop flows, ALM |
| `copilot-*` | 15 | Copilot Studio: topics, entities, actions, generative answers, M365 declarative agents |
| `papps-*` | 15 | Power Apps: Power Fx, galleries/forms, delegation, Dataverse, model-driven |
| `m365-*` | 17 | M365 + Microsoft Graph: auth/scopes, SharePoint, Teams, Outlook, Office Scripts |
| `ml-*` | 25 | regression, trees, boosting, SVM, clustering, PCA, CV, tuning, metrics, time-series, SHAP |
| `ai-*` | 24 | prompting, CoT, structured output, RAG patterns, fine-tune, evals, guardrails, multimodal, cost |
| `agentic-*` | 18 | **Building agentic software**: agent-vs-workflow, prompt-chaining/routing/parallelization, orchestrator-workers, evaluator-optimizer, sub-agent + tool + skill design, context engineering, state durability, MCP, eval/tracing, least-privilege, app architecture |
| `sde-*` | 29 | system design, scalability, caching, sharding, queues, SOLID, patterns, concurrency, CI/CD, interviews |
| `pptx-*` | 20 | slide masters, themes, charts, SmartArt, morph, accessibility, export, PPT-VBA |
| `xls-*` | 26 | XLOOKUP/dynamic arrays/LAMBDA, pivots, Power Query, Power Pivot/DAX, dashboards, xlsm |
| `vba-*` | 20 | UDFs, UserForms, events, fast array I/O, class modules, ADO/SQL, add-in deploy, signing |
| `retail-*` | 25 | OTB, assortment, demand forecasting, markdown/pricing, GMROI, RFM/CLV, basket analysis |
| `research-*` | 22 | systematic review/PRISMA, survey design, stats, regression, A/B + power, meta-analysis |
| `ba-*` | 16 | dashboards, chart selection, SQL, cohort/funnel, forecasting, financial analysis, storytelling |
| `prod-*` | 20 | GTD, Eisenhower, time-blocking, deep work, OKRs, prioritization, habits, inbox-zero |

Each carries real expert how-to (median ~1.4k chars: actual functions, formulas, methods,
pitfalls), generated from verified catalogs. **Don't want a pack?** `rm -rf ~/.codex/skills/<prefix>-*`.

> ### ⚠ Skill budget — install a focused subset (important)
> Codex shows its skill list within a **~2% context budget (~8,000 chars)**. With all 383
> skills installed it shortens descriptions and **omits most of them from the auto-trigger
> list** (they still run when invoked by path, but won't fire on their own) — this is the
> "only ~2% of skills get used" effect. **Install only what you need** so your skills
> reliably trigger (~20–25 fit the budget):
> ```bash
> bash install.sh --only=xls,pptx,pbi,production-audit,ponytail   # comma-sep pack prefixes or exact names
> bash install.sh --exclude=ml,ai,sde,agentic,retail,research     # everything except these
> ```
> Or prune after installing: `rm -rf ~/.codex/skills/<prefix>-*`. Per-project, `/prompts:absorb`
> scopes the right experts into that repo's `./.agents/skills/` instead of the global set.

Skills marked **deep** are *repo-grounded*: each one's `SKILL.md` carries a verified
"absorb these repos" list (current best-in-class, with maintained/stale flags) + the
expert-vs-generic gaps — not generic advice.

`research-scout` is keyless out of the box (Semantic Scholar + arXiv + Crossref).
`patent-scout`'s USPTO source needs a free key (it prints exact signup steps and
falls back to manual links + academic prior-art when absent — never fakes results).

**Slash prompts** (in `codex-assets/prompts/`) — invoked as `/prompts:<name>` in
Codex: `/prompts:absorb`, `/prompts:oracle`, `/prompts:plan`, `/prompts:council`,
`/prompts:new-skill`, `/prompts:prd`, `/prompts:lesson`, `/prompts:verify`,
`/prompts:swarm`, `/prompts:audit`, `/prompts:setup`.

**Swarm (multi-agent):** `/prompts:swarm` or the `swarm` skill fans one task across
several expert lenses **in parallel** — each is an isolated `codex exec` worker
(read-only, `--ephemeral`) — then synthesizes their findings. Portable (no MCP), uses
plain `codex exec` rather than the flaky native `[agents]`. Keep lens lists tight —
each lens is a full Codex session.

**On-demand deep audit:** `/prompts:audit` (or the `production-audit` skill) sweeps the
codebase through **24 lenses to convergence** (stop only after two clean passes), proves
every finding against `file:line`, and — in `fix` mode — repairs in severity waves then
re-verifies. For when you want *everything* that's wrong, not a reassuring one-pass summary.

**⛔ Strict non-negotiable gates (v3.2):** GSD is **mandatory** on non-trivial work (not
opt-in) and **Claude Opus 4.8 must review your code** (`claude-review`) before anything is
DONE — hard gates, never silently skipped. (Codex law also folds in the cross-applicable
Fable-5 practices: skills-first, no-confabulation, file-vs-inline, source hygiene.)

**Global defaults (apply in EVERY project + new folder automatically — they live in
`~/.codex`):** GSD on every task · **Claude Opus 4.8 reviews the code** at the verify
gate (`claude-review`) · **reasoning effort high/xhigh only, never medium**
(`model_reasoning_effort=high`, plan-mode `xhigh`) · context discipline (compact / JIT /
`.planning/` scratchpad / respect context-rot). No per-project setup — `cd` into any
repo and they're active.

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
Verify the whole kit any time: `bash tests/smoke.sh` (19 checks, no network).

### Or let Codex wire it up for you (no admin — office-safe)
**User-level only: no `sudo`, no system paths, no MCP.** Everything installs under your
home (`~/.codex`). On a locked-down office box this just works — and if pip/network is
blocked the tools print the one manual command instead of failing.

From inside the repo, start `codex` and paste this prompt:

> Add this Codex Upgrade kit to my Codex and wire it up — **user-level only, no admin/sudo,
> office-safe**:
> 1. Run `bash install.sh` from the repo root. It backs up my existing `~/.codex` first,
>    validates every SKILL.md, then copies the skills + prompts + shared lib **under
>    `~/.codex` only** (never `/usr`, `/etc`, `/opt`, and never a privileged installer).
> 2. Read `~/.codex/AGENTS.md` so you pick up the operating law + GSD gates.
> 3. Run `/skills` and `/prompts` and confirm the kit loaded — e.g. `production-audit`,
>    `ponytail`, the `craft-*` and `agentic-*` packs, and `/prompts:audit`.
> 4. If they don't show, restart the session (skills/prompts are re-scanned at startup),
>    then re-check.
> Constraint: if any step needs admin, network, or a system path, **STOP and tell me the
> exact command** — never escalate, never run `sudo`.

No GitHub on the office machine? Copy the repo folder over by drive/USB and paste the same
prompt — nothing here phones home. To also merge the safe office `config.toml` profile
(read-only/no-network defaults), tell it to run `bash install.sh --with-config`. Once the kit
is installed, **`/prompts:setup`** re-runs this from inside Codex any time (to pull updates).

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
0. **User-level / no-admin, always.** No `sudo`, no system paths — everything installs
   under `~/.codex`, `~/.codex/tools-venv`, and `~/.local/bin` (via `uv tool` / `pip
   --user`). `brew` is optional, never required. Runs inside the Codex sandbox; never
   escalates. No-admin optional-tool installer: `bash lib/install-tools.sh`.
1. **No MCP, ever required.** Office-safe by construction.
2. **Graceful degradation.** Tools try to self-install; if blocked, they tell you
   the one command to run. Never a silent failure.
3. **Additive + reversible.** Nothing is overwritten; everything is backed up.
4. **Curated experts, not a kitchen sink.** Few high-quality skills + a meta-skill
   that hires/creates more on demand, per project.
5. **Honest by default.** Anti-fabrication and anti-hallucination law baked in.
