#!/usr/bin/env bash
# install.sh - absorb the Codex Upgrade kit into ~/.codex (idempotent, additive).
#
# Backs up first. Never overwrites your config blindly. Re-run any time to update.
# Works with NO MCP, NO admin, NO network. Pure file operations.
#
# Flags:
#   --dry-run      show what would change, do nothing
#   --link         symlink skills/prompts instead of copying (for development)
#   --with-config  also merge the safe "office" profile into ~/.codex/config.toml
#   --help
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASSETS="$REPO_DIR/codex-assets"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
TS="$(date +%Y%m%d-%H%M%S)"
BACKUP="$CODEX_HOME/backups/$TS"

DRY=0; LINK=0; WITH_CONFIG=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY=1 ;;
    --link) LINK=1 ;;
    --with-config) WITH_CONFIG=1 ;;
    --help|-h)
      sed -n '2,15p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown flag: $arg (try --help)"; exit 2 ;;
  esac
done

say()  { printf '%s\n' "$*"; }
run()  { if [ "$DRY" = 1 ]; then say "  [dry-run] $*"; else eval "$*"; fi; }
line() { printf '%s\n' "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"; }

line
say " CODEX UPGRADE — install $( [ "$DRY" = 1 ] && echo '(DRY RUN)' )"
line
say "repo:        $REPO_DIR"
say "codex home:  $CODEX_HOME"
say "mode:        $( [ "$LINK" = 1 ] && echo symlink || echo copy )"
say "config:      $( [ "$WITH_CONFIG" = 1 ] && echo 'merge office profile' || echo 'skip (use --with-config)')"
say ""

[ -d "$ASSETS" ] || { echo "ERROR: $ASSETS not found - run from the repo root."; exit 1; }

# --- 0. dirs + backup ---------------------------------------------------------
run "mkdir -p '$CODEX_HOME/skills' '$CODEX_HOME/prompts' '$CODEX_HOME/memory' '$BACKUP'"
if [ -f "$CODEX_HOME/AGENTS.md" ]; then run "cp '$CODEX_HOME/AGENTS.md' '$BACKUP/AGENTS.md'"; fi
if [ -f "$CODEX_HOME/config.toml" ]; then run "cp '$CODEX_HOME/config.toml' '$BACKUP/config.toml'"; fi
say "✓ backup -> $BACKUP"

# --- 0b. validate skills BEFORE installing (fail loud on a bad SKILL.md) -------
if [ -f "$REPO_DIR/lib/validate_skill.py" ]; then
  if [ "$DRY" = 1 ]; then
    python3 "$REPO_DIR/lib/validate_skill.py" "$ASSETS/skills" || { echo "ERROR: invalid skill(s) - fix before install"; exit 1; }
  else
    python3 "$REPO_DIR/lib/validate_skill.py" "$ASSETS/skills" || { echo "ERROR: invalid skill(s) - aborting"; exit 1; }
  fi
  say ""
fi

# --- 1. shared lib (codex_env.py) -> ~/.codex/lib (NOT a skills root) ----------
install_dir() { # $1 = src dir, $2 = dest dir
  local src="$1" dest="$2"
  if [ -e "$dest" ] && [ "$LINK" != 1 ]; then run "rm -rf '$BACKUP/$(basename "$dest").bak'; mv '$dest' '$BACKUP/$(basename "$dest").bak' 2>/dev/null || true"; fi
  if [ "$LINK" = 1 ]; then run "ln -sfn '$src' '$dest'"; else run "cp -R '$src' '$dest'"; fi
}

install_dir "$ASSETS/lib" "$CODEX_HOME/lib"
say "✓ shared lib (codex_env.py) -> $CODEX_HOME/lib"

# --- 2. skills ----------------------------------------------------------------
SKILLS=0
for d in "$ASSETS"/skills/*/; do
  name="$(basename "$d")"
  [ "$name" = "_lib" ] && continue
  install_dir "$d" "$CODEX_HOME/skills/$name"
  SKILLS=$((SKILLS+1))
done
say "✓ skills installed: $SKILLS"

# --- 3. prompts ---------------------------------------------------------------
PROMPTS=0
if [ -d "$ASSETS/prompts" ]; then
  for f in "$ASSETS"/prompts/*.md; do
    [ -e "$f" ] || continue
    base="$(basename "$f")"
    [ -f "$CODEX_HOME/prompts/$base" ] && run "cp '$CODEX_HOME/prompts/$base' '$BACKUP/$base'"
    if [ "$LINK" = 1 ]; then run "ln -sfn '$f' '$CODEX_HOME/prompts/$base'"; else run "cp '$f' '$CODEX_HOME/prompts/$base'"; fi
    PROMPTS=$((PROMPTS+1))
  done
fi
say "✓ prompts installed: $PROMPTS"

# --- 4. AGENTS.md (replace our marked block, preserve everything else) --------
NEW_BLOCK="$ASSETS/AGENTS.md"
TARGET="$CODEX_HOME/AGENTS.md"
if [ ! -f "$TARGET" ]; then
  run "cp '$NEW_BLOCK' '$TARGET'"
  say "✓ AGENTS.md created"
else
  if [ "$DRY" = 1 ]; then
    if grep -q 'CODEX-UPGRADE:BEGIN' "$TARGET"; then say "  [dry-run] AGENTS.md: replace existing CODEX-UPGRADE block"; else say "  [dry-run] AGENTS.md: append CODEX-UPGRADE block"; fi
  else
    tmp="$(mktemp)"
    awk 'BEGIN{skip=0}
         /CODEX-UPGRADE:BEGIN/{skip=1}
         skip==0{print}
         /CODEX-UPGRADE:END/{skip=0}' "$TARGET" > "$tmp"
    # drop a trailing blank-only tail, then append fresh block
    printf '\n' >> "$tmp"
    cat "$NEW_BLOCK" >> "$tmp"
    mv "$tmp" "$TARGET"
    say "✓ AGENTS.md updated (block replaced; your other content preserved)"
  fi
fi

# --- 5. memory ----------------------------------------------------------------
if [ ! -f "$CODEX_HOME/memory/MEMORY.md" ]; then
  if [ "$DRY" = 1 ]; then say "  [dry-run] create memory/MEMORY.md";
  else
    cat > "$CODEX_HOME/memory/MEMORY.md" <<'EOF'
# Codex Cross-Session Memory
> One line per non-trivial task:
> [YYYY-MM-DD HH:MM] task="…" outcome="DONE|BLOCKED|PARTIAL" learning="…"
EOF
    say "✓ memory/MEMORY.md created"
  fi
else
  say "✓ memory/MEMORY.md exists (untouched)"
fi

# --- 6. optional config merge -------------------------------------------------
if [ "$WITH_CONFIG" = 1 ]; then
  if [ -f "$ASSETS/config.office.toml" ]; then
    if [ -f "$CODEX_HOME/config.toml" ] && grep -q 'CODEX-UPGRADE office profile' "$CODEX_HOME/config.toml"; then
      say "✓ config.toml already has the office profile (skipped)"
    else
      run "printf '\n' >> '$CODEX_HOME/config.toml'"
      run "cat '$ASSETS/config.office.toml' >> '$CODEX_HOME/config.toml'"
      say "✓ config.toml: appended office profile (review it: $CODEX_HOME/config.toml)"
    fi
  else
    say "! config.office.toml not present in this build - skipping"
  fi
fi

# --- done ---------------------------------------------------------------------
say ""
line
say " DONE${DRY:+}$( [ "$DRY" = 1 ] && echo ' (dry run — nothing changed)')"
line
say "⚠ RESTART Codex now — skills + prompts are only re-scanned at session start."
say "Verify:    codex  →  /skills     (lists xlsx-wrangler, deck-smith, pdf-extract, …)"
say "Prompts:   /prompts:absorb  (tailor experts to a repo) · /prompts:oracle · /prompts:council"
say "Smoke test: python3 '$CODEX_HOME/skills/research-scout/bin/research.py' search 'rag eval' --source arxiv --n 3"
say "Rollback:  your previous config is in $BACKUP"
