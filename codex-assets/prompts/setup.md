---
description: Add or refresh this Codex Upgrade kit in ~/.codex and wire it up — USER-LEVEL only, no admin/sudo, office-safe. Runs install.sh, loads the law (AGENTS.md), and verifies the skills + prompts loaded. Use to install the kit or pull updates from inside the repo.
argument-hint: "[optional install flags: --with-config | --with-hooks | --link]"
---
# /prompts:setup — install & wire up the Codex Upgrade kit (no admin, office-safe)

Add this repo's kit to Codex and confirm it's live. **USER-LEVEL ONLY — never `sudo`,
never a system path, no MCP.** Everything lands under `~/.codex`. Works on a locked-down
office box; if pip/network is blocked, surface the one manual command — never fail silently.

Extra flags (optional): $ARGUMENTS

Do this:
1. **Locate the repo** — the current folder (or wherever this kit lives). Confirm
   `codex-assets/` and `install.sh` are present; `cd` to the repo root.
2. **Install** — run `bash install.sh $ARGUMENTS`. It backs up `~/.codex` first, validates
   every `SKILL.md`, then copies the skills + prompts + shared lib **under `~/.codex` only**
   (never `/usr`, `/etc`, `/opt`, and never a privileged installer). Re-running it just pulls
   updates. Add `--with-config` to also merge the read-only/no-network office profile.
3. **Load the law** — read `~/.codex/AGENTS.md` so you pick up the operating law + GSD gates.
4. **Verify** — run `/skills` and `/prompts`; confirm the kit loaded (e.g. `production-audit`,
   `ponytail`, the `craft-*` and `agentic-*` packs, `/prompts:audit`). If they don't appear,
   tell me to **restart the session** (skills/prompts are re-scanned only at startup), then re-check.
5. **Never escalate** — if any step needs admin, network, or a system path, **STOP and print
   the exact command** for me to run; do not `sudo`, do not work around the sandbox.

End with the §J completion block: what installed, the skills/prompts counts from `/skills`
+ `/prompts`, and any NAMED BLOCKER (missing dep/network) with its exact fix command.
