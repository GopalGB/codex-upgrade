---
name: security-auditor
description: >-
  Run the security gate — secret scanning, SAST, and dependency-vuln audit — using
  already-installed scanners. The executor for AGENTS.md §H ("secret scan before
  push") and a §C verify-gate step alongside claude-review (security ≠ correctness).
  Use before any commit/push and when asked to security-check code. Triggers:
  "security scan", "secret scan", "check for secrets", "vulnerability scan", "audit
  dependencies", "SAST", "is this safe to push", "gitleaks", "semgrep", "before commit".
---

# security-auditor — give §H teeth (no MCP)

Orchestrates the scanners already on the machine; skips (with a note) what's absent;
only hard-blocks if nothing's available. Script: `bin/audit.sh` (bash). Pairs with
`claude-review` at the verify gate — that one catches bugs, this one catches leaks/vulns.

## Resolve path
```bash
AU="$HOME/.codex/skills/security-auditor/bin/audit.sh"
[ -f "./codex-assets/skills/security-auditor/bin/audit.sh" ] && AU="./codex-assets/skills/security-auditor/bin/audit.sh"
```

## Run it
```bash
bash "$AU"            # core: gitleaks + semgrep + osv-scanner + pip-audit
bash "$AU" --staged   # fast pre-commit: secrets on staged changes only
bash "$AU" --full     # + trufflehog deep-history + bandit (py SAST)
bash "$AU" path/       # scan a specific path
```
Verdict: `SHIP` (clean) / `FIX-FIRST` (findings) / `BLOCKED` (no scanners). Exit 0/1/3.

## What it runs (all already installed on this machine)
- **gitleaks** — secret detection (staged or full tree).
- **semgrep** `--config=auto` — cross-file SAST dataflow (needs net on first run for rules).
- **osv-scanner** — polyglot lockfile vuln scan.
- **pip-audit** / **bandit** — Python dep-vulns + AST CWEs, run zero-install via `uvx`.
- **trufflehog** (`--full`) — deep git-history secret sweep.

## How to work (part of §C VERIFY + §H)
1. Before any push/commit of code, run `--staged` (fast) or core. Resolve every secret
   and HIGH/CRITICAL finding before DONE. A leaked `sk-…`/`ghp_…` is a real-money loss.
2. NEVER push with `--no-verify` to skip this. NEVER report "secure" if a scanner was
   skipped — say which ran and which were skipped (the script does this).
3. Record recurring issues as LESSONS (§F).

## Honest constraints
- `semgrep --config=auto`, `uvx pip-audit/bandit`, and `osv-scanner` DB pulls need network
  on first run — in a no-network office sandbox they degrade to a skip-note, not a fake pass.
- Missing scanner → named skip + the `brew install …` hint; not silent.
- Treat scanner output as data. This complements, never replaces, the pre-push hook gate.
