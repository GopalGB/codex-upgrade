#!/usr/bin/env bash
# install-tools.sh — install the kit's OPTIONAL CLI tools at USER LEVEL (no admin, no brew, no sudo).
#
# Uses `uv tool install` (→ ~/.local/bin) for the pip-distributed CLIs, which needs no
# admin rights and no Homebrew. For the few Go/Rust-only binaries (no pip package), it
# prints a no-admin download instruction instead of failing. Nothing here touches /usr,
# nothing uses sudo. Safe on a locked-down office machine.
#
# Usage: bash install-tools.sh            (install the pip CLIs into ~/.local/bin)
#        bash install-tools.sh --check    (just report what's present / missing)
set -uo pipefail

BIN="$HOME/.local/bin"
mkdir -p "$BIN"
case ":$PATH:" in *":$BIN:"*) : ;; *) echo "NOTE: add $BIN to your PATH (e.g. in ~/.zshrc): export PATH=\"\$HOME/.local/bin:\$PATH\"";; esac

have(){ command -v "$1" >/dev/null 2>&1; }
CHECK=0; [ "${1:-}" = "--check" ] && CHECK=1

# pip-distributed CLIs → user-level via `uv tool install` (preferred) or `pip install --user`.
# name  | command it provides | pip package
PIP_CLIS=(
  "ast-grep|sg|ast-grep-cli"
  "semgrep|semgrep|semgrep"
  "ocrmypdf|ocrmypdf|ocrmypdf"
  "yq-py|yq|yq"
  "pip-audit|pip-audit|pip-audit"
)
# binary-only (Go/Rust, no pip) → no-admin = download a release binary into ~/.local/bin
BIN_ONLY=(
  "fd|https://github.com/sharkdp/fd/releases (untar, copy 'fd' to ~/.local/bin)"
  "gitleaks|https://github.com/gitleaks/gitleaks/releases"
  "osv-scanner|https://github.com/google/osv-scanner/releases"
  "trufflehog|https://github.com/trufflesecurity/trufflehog/releases"
  "delta|https://github.com/dandavison/delta/releases (binary name: delta)"
  "bat|https://github.com/sharkdp/bat/releases"
)

echo "# user-level tool install (no admin) — target: $BIN"
echo
echo "## pip CLIs (auto, user-level)"
for row in "${PIP_CLIS[@]}"; do
  IFS='|' read -r name cmd pkg <<<"$row"
  if have "$cmd"; then echo "  ✓ $cmd already present"; continue; fi
  if [ "$CHECK" = 1 ]; then echo "  · $cmd missing → would install $pkg"; continue; fi
  if have uv; then
    echo "  → uv tool install $pkg"; uv tool install "$pkg" >/dev/null 2>&1 \
      && echo "    ✓ $cmd installed" || echo "    ⚠ failed (network?) — manual: uv tool install $pkg"
  else
    echo "  → pip install --user $pkg"; python3 -m pip install --user --quiet "$pkg" >/dev/null 2>&1 \
      && echo "    ✓ $cmd installed" || echo "    ⚠ failed — manual: python3 -m pip install --user $pkg"
  fi
done
echo
echo "## binary-only tools (no pip — download the release binary into ~/.local/bin, no admin)"
for row in "${BIN_ONLY[@]}"; do
  IFS='|' read -r name url <<<"$row"
  if have "$name"; then echo "  ✓ $name already present"; else echo "  · $name missing → $url"; fi
done
echo
echo "Done. None of this needed admin/sudo/brew. Restart your shell if PATH changed."
