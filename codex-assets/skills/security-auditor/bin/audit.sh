#!/usr/bin/env bash
# audit.sh — run the security gate using already-installed scanners (no MCP).
#
# Orchestrates whatever is present; SKIPS (with a named note) what's absent; only
# hard-blocks if NOTHING is available. Gives AGENTS.md §H ("secret scan before push")
# a real executor. Runs at the §C verify gate alongside claude-review.
#
# Usage:
#   audit.sh            # core scan of the repo (gitleaks + semgrep + osv + pip-audit)
#   audit.sh --staged   # secrets on staged changes only (fast pre-commit)
#   audit.sh --full     # core + trufflehog deep-history + bandit
#   audit.sh <path>     # scan a specific path
# Exit: 0 clean, 1 findings, 3 no scanners available.
set -uo pipefail

MODE="core"; SCOPE="."
for a in "$@"; do
  case "$a" in
    --staged) MODE="staged" ;;
    --full)   MODE="full" ;;
    -*)       echo "unknown flag: $a" >&2; exit 2 ;;
    *)        SCOPE="$a" ;;
  esac
done

FINDINGS=0; RAN=0; SKIP=()
hdr(){ printf '\n## %s\n' "$1"; }
have(){ command -v "$1" >/dev/null 2>&1; }
# run a scanner: $1=label, rest=command; nonzero exit => flag for review
scan(){ local label="$1"; shift; hdr "$label"; RAN=$((RAN + 1))
  if "$@" 2>&1; then echo "  ✓ clean"; else echo "  ⚠ findings above — review"; FINDINGS=$((FINDINGS + 1)); fi; }

finish(){
  hdr "verdict"
  [ "${#SKIP[@]}" -gt 0 ] && printf '  skipped (not installed): %s\n' "$(IFS='; '; echo "${SKIP[*]}")"
  if [ "$RAN" -eq 0 ]; then
    echo "  BLOCKED: no security scanners available — install at least gitleaks + semgrep."; exit 3
  fi
  if [ "$FINDINGS" -gt 0 ]; then echo "  FIX-FIRST — $FINDINGS scanner(s) flagged issues above (ran $RAN)."; exit 1; fi
  echo "  SHIP — $RAN scanner(s) clean."; exit 0
}

echo "# security-auditor — mode=$MODE scope=$SCOPE ($(date '+%Y-%m-%d %H:%M'))"

# --- secrets: gitleaks ---
if have gitleaks; then
  if [ "$MODE" = "staged" ]; then scan "gitleaks (staged secrets)" gitleaks protect --staged --no-banner --redact
  else scan "gitleaks (secrets)" gitleaks detect --no-banner --redact -s "$SCOPE"; fi
else SKIP+=("gitleaks — brew install gitleaks"); fi

# staged mode = fast secrets-only path
[ "$MODE" = "staged" ] && finish

# --- SAST: semgrep (needs net for --config=auto first run) ---
if have semgrep; then scan "semgrep (SAST)" semgrep --config=auto --error --quiet "$SCOPE"
else SKIP+=("semgrep — brew install semgrep"); fi

# --- deps: osv-scanner ---
if have osv-scanner; then scan "osv-scanner (deps)" osv-scanner scan --recursive "$SCOPE"
else SKIP+=("osv-scanner — brew install osv-scanner"); fi

# --- python deps: pip-audit (zero-install via uvx if uv present) ---
if have uv; then scan "pip-audit (py deps)" uvx pip-audit --progress-spinner off
elif have pip-audit; then scan "pip-audit (py deps)" pip-audit
else SKIP+=("pip-audit — uvx pip-audit (needs uv) or pip install pip-audit"); fi

# --- full: deep-history secrets + python SAST ---
if [ "$MODE" = "full" ]; then
  if have trufflehog; then scan "trufflehog (deep history)" trufflehog filesystem "$SCOPE" --no-verification --no-update
  else SKIP+=("trufflehog — brew install trufflehog"); fi
  if have uv; then scan "bandit (py SAST)" uvx bandit -r "$SCOPE" -ll -q
  elif have bandit; then scan "bandit (py SAST)" bandit -r "$SCOPE" -ll -q
  else SKIP+=("bandit — uvx bandit (needs uv)"); fi
fi

finish
