#!/usr/bin/env bash
# review.sh — get a Claude Opus 4.8 code review of the current git diff (no MCP).
#
# Cross-review: Codex writes, Claude Opus 4.8 reviews. Pipes the diff to the `claude`
# CLI in print mode (read-only). Part of the §C VERIFY gate ("Opus always reviews").
#
# Usage:
#   review.sh                 # review staged+unstaged vs HEAD (default)
#   review.sh <git-range>     # e.g. review.sh main...HEAD   or   review.sh HEAD~3
#   review.sh --staged        # only staged changes
# Env: CLAUDE_REVIEW_MODEL (default claude-opus-4-8)
#
# NOTE: needs the `claude` CLI + network. If Codex runs sandboxed with network OFF,
# the call will fail — that's a NAMED BLOCKER, not a silent pass. Run with network
# (or outside the sandbox) for the review.
set -uo pipefail

MODEL="${CLAUDE_REVIEW_MODEL:-claude-opus-4-8}"

command -v claude >/dev/null 2>&1 || {
  echo "BLOCKED: \`claude\` CLI not found on PATH. Install Claude Code, then re-run." >&2
  exit 3
}
command -v git >/dev/null 2>&1 || { echo "BLOCKED: not a git context (no git)." >&2; exit 3; }

case "${1:-}" in
  --staged) DIFF="$(git diff --cached 2>/dev/null)"; SCOPE="staged" ;;
  "")       DIFF="$(git diff HEAD 2>/dev/null)"; SCOPE="vs HEAD"
            [ -z "$DIFF" ] && DIFF="$(git diff 2>/dev/null)" && SCOPE="working tree" ;;
  *)        DIFF="$(git diff "$1" 2>/dev/null)"; SCOPE="$1" ;;
esac

if [ -z "${DIFF//[$' \t\n']/}" ]; then
  echo "no diff to review ($SCOPE)." >&2
  exit 0
fi

BYTES=$(printf '%s' "$DIFF" | wc -c | tr -d ' ')
if [ "$BYTES" -gt 400000 ]; then
  echo "⚠ diff is ${BYTES} bytes — large; reviewing anyway, but consider a path/range for sharper review." >&2
fi

INSTR="You are a senior code reviewer (Claude Opus 4.8). Review this git diff ($SCOPE) for
correctness BUGS, security issues, and quality/maintainability. Be terse and concrete:
list ONLY real findings as bullets, each with file:line and a one-line fix, ranked
CRITICAL > HIGH > MEDIUM > LOW. No praise, no restating the diff. End with a single
verdict line: SHIP or FIX-FIRST. If you see no real issues, say 'No blocking issues.'"

printf '%s\n\n--- DIFF ---\n%s\n' "$INSTR" "$DIFF" \
  | claude -p --model "$MODEL" --permission-mode plan 2>&1
RC=$?
[ "$RC" -ne 0 ] && {
  echo "BLOCKED: claude review call failed (exit $RC). Common cause: no network in the" >&2
  echo "Codex sandbox, or \`claude\` not logged in. Re-run with network / outside sandbox." >&2
  exit 3
}
