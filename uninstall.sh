#!/usr/bin/env bash
# uninstall.sh - remove the Codex Upgrade kit from ~/.codex. Backups are kept.
# Removes only THIS kit's files: its skills, its prompts, the shared lib, and the
# marked AGENTS.md block. Your other Codex config is left untouched.
set -euo pipefail

CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASSETS="$REPO_DIR/codex-assets"
DRY=0; [ "${1:-}" = "--dry-run" ] && DRY=1
run() { if [ "$DRY" = 1 ]; then echo "  [dry-run] $*"; else eval "$*"; fi; }

echo "Uninstalling Codex Upgrade from $CODEX_HOME $( [ "$DRY" = 1 ] && echo '(dry run)')"

# skills shipped by this kit (by folder name)
if [ -d "$ASSETS/skills" ]; then
  for d in "$ASSETS"/skills/*/; do
    name="$(basename "$d")"
    [ -e "$CODEX_HOME/skills/$name" ] && run "rm -rf '$CODEX_HOME/skills/$name'" && echo "  - skill $name"
  done
fi
# prompts shipped by this kit
if [ -d "$ASSETS/prompts" ]; then
  for f in "$ASSETS"/prompts/*.md; do
    base="$(basename "$f")"
    [ -e "$CODEX_HOME/prompts/$base" ] && run "rm -f '$CODEX_HOME/prompts/$base'" && echo "  - prompt $base"
  done
fi
# shared lib
[ -e "$CODEX_HOME/lib/codex_env.py" ] && run "rm -f '$CODEX_HOME/lib/codex_env.py'" && echo "  - lib codex_env.py"

# strip the marked AGENTS.md block (keep everything else)
TARGET="$CODEX_HOME/AGENTS.md"
if [ -f "$TARGET" ] && grep -q 'CODEX-UPGRADE:BEGIN' "$TARGET"; then
  if [ "$DRY" = 1 ]; then echo "  [dry-run] strip CODEX-UPGRADE block from AGENTS.md";
  else
    tmp="$(mktemp)"
    awk 'BEGIN{skip=0} /CODEX-UPGRADE:BEGIN/{skip=1} skip==0{print} /CODEX-UPGRADE:END/{skip=0}' "$TARGET" > "$tmp"
    mv "$tmp" "$TARGET"; echo "  - AGENTS.md block removed"
  fi
fi

echo "Done. The tools venv (~/.codex/tools-venv) and your backups (~/.codex/backups) were left in place."
echo "Note: config.toml office profiles (if added) were NOT auto-removed — edit it by hand if desired."
