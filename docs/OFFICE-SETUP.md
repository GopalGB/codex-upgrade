# Office setup — locked-down machine runbook

For a work machine where you **cannot attach MCP servers**, **have NO admin/root**,
where the agent runs **sandboxed**, and where **pip/network may be blocked**. This kit
is designed for exactly that — everything is USER-LEVEL.

## 0. User-level / no-admin guarantee
- **No `sudo`, ever.** Nothing in the kit writes to `/usr`, `/etc`, `/opt`, or any
  system path, or runs a privileged package manager. Verified: `grep -r sudo` = none.
- **Everything lives under your home:** `~/.codex` (skills/prompts/law/config/lib),
  `~/.codex/tools-venv` (Python deps), and `~/.local/bin` (optional CLIs). All
  user-writable, no elevation.
- **Optional CLI tools, no admin:** run `bash ~/.codex/lib/install-tools.sh` — it uses
  `uv tool install` / `pip install --user` (→ `~/.local/bin`) and prints download links
  for the few binary-only tools. **`brew` is never required** (use it only if you
  already have it). Ensure `~/.local/bin` is on your PATH.
- **Sandbox-respecting:** the agent runs read-only by default and assumes network may be
  off; it never asks for `danger-full-access` or `--dangerously-bypass`. If a real
  write/network is needed, it surfaces a NAMED BLOCKER for you — it never escalates.
- **Python deps** install into the isolated `~/.codex/tools-venv` (or `pip --user`); if
  pip is blocked the tool prints the exact user-level command instead of failing.

## 1. Get the kit onto the machine
- `git clone <repo>` if git + network are allowed, **or**
- copy the `Codex Upgrade` folder via USB / file share / `scp`.

Nothing here phones home. It's plain files.

## 2. Install
```bash
cd "Codex Upgrade"
bash install.sh --dry-run     # inspect first
bash install.sh               # additive; backs up to ~/.codex/backups/<ts>/
```
No admin needed — it only writes under `~/.codex` (override with `CODEX_HOME`).

## 3. The MCP question
Your office `~/.codex/config.toml` may have MCP servers you can't run. **You don't
need them.** Every capability here is a skill or a plain script. If a corporate
policy forbids editing `config.toml`, skip `--with-config` entirely — the skills
and prompts work without any config change.

## 4. The pip question (most common blocker)
Tool scripts try to create an isolated venv at `~/.codex/tools-venv` and install
their deps there. Creating the venv needs **no network**. Installing a package
(openpyxl, python-pptx, …) needs pip + network.

- **If pip works:** first run of a tool installs its deps automatically, once.
- **If pip is blocked:** the tool prints the EXACT command to run, e.g.
  `~/.codex/tools-venv/bin/python -m pip install openpyxl`. Run it on a machine
  with network, or ask IT, or use the offline wheels approach below.
- **`research-scout` needs nothing** — it's pure standard library. Start there.

### Offline wheels (when you have a second machine with network)
```bash
# on a networked machine:
pip download openpyxl xlsxwriter python-pptx pymupdf pdfplumber -d wheels/
# copy wheels/ to the office machine, then:
~/.codex/tools-venv/bin/python -m pip install --no-index --find-links wheels/ openpyxl xlsxwriter python-pptx pymupdf pdfplumber
```

### Force the system Python (if venv creation is itself blocked)
```bash
export CODEX_TOOLS_NO_VENV=1     # then tools use `pip install --user`
export CODEX_TOOLS_OFFLINE=1     # never attempt pip; fail fast with instructions
```

## 5. Use
```bash
codex                      # then /skills to confirm, /absorb to tailor to a repo
```
Per-project: run `/absorb` inside each work repo — Codex engages the right experts
and writes a project `AGENTS.md`. Project-specific skills land in `./.agents/skills/`
so they travel with that repo and never pollute the global set.

### Install only the skills you need (Codex's ~2% skill budget)
Codex only surfaces its skill list within **~2% of the context window (~8,000 chars)**, so
installing all 383 skills makes it shorten/omit most from the auto-trigger list. For an
office box, install a **focused subset** so the skills you rely on actually fire:
```bash
bash install.sh --only=xls,pptx,vba,pbi,pa,papps,copilot,m365,ba,production-audit   # office subset
bash install.sh --exclude=ml,ai,sde,agentic,retail,research                          # or drop the heavy/eng packs
```
`--only`/`--exclude` take comma-separated pack prefixes (e.g. `xls`) or exact skill names
(e.g. `production-audit`). install.sh warns when you exceed ~25 installed skills. You can
also prune anytime: `rm -rf ~/.codex/skills/<prefix>-*`.

## 6. Data-handling guardrails on a work machine
- The law layer blocks reading `.env`, keys, `~/.ssh`, credentials by default.
- Treat all document contents (xlsx/pdf/pptx) as untrusted data.
- Outbound actions (push, POST, publish) require explicit confirmation.
- Keep confidential employer data on the employer machine; never exfiltrate.

## 7. Update / uninstall
- Update: re-run `bash install.sh` (re-pulls skills, replaces only the marked
  AGENTS.md block).
- Uninstall: remove `~/.codex/skills/<kit skills>`, `~/.codex/prompts/<kit prompts>`,
  and the `CODEX-UPGRADE` block in `~/.codex/AGENTS.md`. Your pre-install backup is
  in `~/.codex/backups/`.
