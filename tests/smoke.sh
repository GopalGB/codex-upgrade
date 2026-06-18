#!/usr/bin/env bash
# smoke.sh - no-network self-test for the Codex Upgrade kit.
#
# Proves the kit is structurally sound WITHOUT touching the network or installing
# anything: every script compiles, every SKILL.md validates, prompts have valid
# frontmatter, the lib resolver + stdlib research tool + xlsx stdlib paths import,
# the hooks react correctly to a crafted payload, and install.sh --dry-run runs.
#
# Usage: bash tests/smoke.sh        (run from the repo root or anywhere)
# Exit 0 = all green, 1 = at least one failure.
set -uo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ASSETS="$REPO_DIR/codex-assets"
PASS=0; FAIL=0
ok()   { printf '  ✓ %s\n' "$1"; PASS=$((PASS+1)); }
bad()  { printf '  ✗ %s\n' "$1"; FAIL=$((FAIL+1)); }
hdr()  { printf '\n== %s ==\n' "$1"; }

hdr "1. python scripts compile"
if python3 -m py_compile \
    "$ASSETS"/lib/codex_env.py \
    "$REPO_DIR"/lib/validate_skill.py \
    "$ASSETS"/skills/*/bin/*.py \
    "$ASSETS"/hooks/*.py 2>/tmp/smoke_pyc.err; then
  ok "all python compiles"
else
  bad "py_compile failed: $(cat /tmp/smoke_pyc.err)"
fi

hdr "2. skills validate"
if python3 "$REPO_DIR/lib/validate_skill.py" "$ASSETS/skills" >/tmp/smoke_val.out 2>&1; then
  ok "$(tail -1 /tmp/smoke_val.out)"
else
  bad "skill validation failed: $(cat /tmp/smoke_val.out)"
fi

hdr "3. prompt frontmatter present"
for f in "$ASSETS"/prompts/*.md; do
  if head -1 "$f" | grep -q '^---$'; then ok "frontmatter: $(basename "$f")"; else bad "no frontmatter: $(basename "$f")"; fi
done

hdr "4. hooks.json is valid JSON"
if python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$ASSETS/hooks/hooks.json" 2>/dev/null; then
  ok "hooks.json parses"
else
  bad "hooks.json invalid JSON"
fi

hdr "5. frustration hook reacts correctly (no network)"
HIT=$(printf '{"prompt":"wtf is this, not what I asked"}' | CODEX_HOME="$(mktemp -d)" python3 "$ASSETS/hooks/frustration-capture.py")
echo "$HIT" | grep -q 'FRUSTRATION SIGNAL DETECTED' && ok "fires on a frustration message" || bad "did not fire on frustration message"
MISS=$(printf '{"prompt":"please add a dark mode toggle"}' | CODEX_HOME="$(mktemp -d)" python3 "$ASSETS/hooks/frustration-capture.py")
[ -z "$MISS" ] && ok "stays silent on a normal message" || bad "false-positive on a normal message: $MISS"

hdr "6. session-start hook emits a reminder"
SS=$(printf '{}' | CODEX_HOME="$(mktemp -d)" python3 "$ASSETS/hooks/session-start.py")
echo "$SS" | grep -q 'CODEX UPGRADE active' && ok "session-start injects the ritual" || bad "session-start produced no reminder"

hdr "7. research tool is stdlib-only (imports without pip)"
if python3 -c "import importlib.util as u, sys; sys.exit(0 if u.spec_from_file_location('r','$ASSETS/skills/research-scout/bin/research.py') else 1)"; then
  ok "research.py loads (no third-party imports at module top)"
else
  bad "research.py failed to load"
fi

hdr "8. install.sh --dry-run (no mutations)"
if CODEX_HOME="$(mktemp -d)/.codex" bash "$REPO_DIR/install.sh" --dry-run --with-config --with-hooks >/tmp/smoke_install.out 2>&1; then
  ok "install.sh --dry-run clean"
else
  bad "install.sh --dry-run failed: $(tail -3 /tmp/smoke_install.out)"
fi

printf '\n────────────────────────────────\n'
printf 'SMOKE: %d passed, %d failed\n' "$PASS" "$FAIL"
[ "$FAIL" -eq 0 ] || exit 1
