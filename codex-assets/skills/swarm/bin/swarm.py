#!/usr/bin/env python3
"""swarm.py — fan ONE task across multiple expert lenses in parallel (no MCP).

Each lens runs as its own isolated `codex exec` worker (--ephemeral, read-only
sandbox), in parallel, with a bounded concurrency cap. The script collects every
worker's final message; the CALLING agent then synthesizes them (per SKILL.md).
This is the portable swarm: it uses plain `codex exec` subprocesses, NOT the flaky
experimental native [agents] feature.

Stdlib only — nothing to pip-install.

Usage:
  swarm.py "<task>" --lenses security,performance,correctness [--max 4]
  swarm.py "<task>"                 # default review panel if --lenses omitted
  swarm.py "<task>" --lenses a,b,c --sandbox workspace-write --model gpt-5.1-codex
  swarm.py "<task>" --synthesize    # add a final worker that merges the findings

Flags: --max N (concurrency, default 4) · --timeout S (per worker, default 600) ·
       --cd DIR · --model M · --sandbox read-only|workspace-write · --json (raw)

COST: each lens = a full Codex session (real model calls). Keep --lenses focused —
"experts only, not everything." Default cap is 4 concurrent.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import shutil
import subprocess
import sys
import tempfile

DEFAULT_LENSES = ["correctness", "security", "performance", "simplicity"]

WORKER_TMPL = (
    "You are the {lens} expert reviewing this task. Focus ONLY on the {lens} "
    "dimension — do not try to cover everything.\n\nTASK:\n{task}\n\n"
    "You may READ files to ground your analysis (read-only). Return concise, "
    "concrete findings as short bullets, each actionable. If the {lens} dimension "
    "is not relevant here, say so in one line. No preamble."
)


def _named_blocker(msg: str) -> int:
    print(f"BLOCKED: {msg}", file=sys.stderr)
    return 3


def run_worker(lens: str, task: str, args) -> dict:
    """Run one lens as an isolated codex exec worker; return its final message."""
    out_fd, out_path = tempfile.mkstemp(prefix=f"swarm-{lens}-", suffix=".txt")
    os.close(out_fd)
    cmd = [
        "codex",
        "exec",
        "--skip-git-repo-check",
        "--ephemeral",
        "--color",
        "never",
        "-s",
        args.sandbox,
        "-o",
        out_path,
    ]
    if args.model:
        cmd += ["-m", args.model]
    if args.cd:
        cmd += ["-C", args.cd]
    cmd.append(WORKER_TMPL.format(lens=lens, task=task))
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=args.timeout)
        msg = ""
        if os.path.exists(out_path):
            with open(out_path, encoding="utf-8") as fh:
                msg = fh.read().strip()
        ok = proc.returncode == 0 and bool(msg)
        return {
            "lens": lens,
            "ok": ok,
            "findings": msg,
            "error": ""
            if ok
            else (proc.stderr.strip()[:400] or f"exit {proc.returncode}, empty output"),
        }
    except subprocess.TimeoutExpired:
        return {
            "lens": lens,
            "ok": False,
            "findings": "",
            "error": f"timed out after {args.timeout}s",
        }
    except Exception as exc:  # noqa: BLE001
        return {"lens": lens, "ok": False, "findings": "", "error": str(exc)[:400]}
    finally:
        try:
            os.unlink(out_path)
        except OSError:
            pass


def synthesize(task: str, results: list[dict], args) -> str:
    """Optional: one extra worker merges the lens findings into a verdict."""
    bundle = "\n\n".join(
        f"### {r['lens']}\n{r['findings'] or '(no findings)'}"
        for r in results
        if r["ok"]
    )
    prompt = (
        "Synthesize these independent expert reviews into ONE verdict for the task. "
        "De-duplicate, resolve conflicts, rank the top 3 actions.\n\n"
        f"TASK:\n{task}\n\nREVIEWS:\n{bundle}"
    )
    out_fd, out_path = tempfile.mkstemp(prefix="swarm-synth-", suffix=".txt")
    os.close(out_fd)
    cmd = [
        "codex",
        "exec",
        "--skip-git-repo-check",
        "--ephemeral",
        "--color",
        "never",
        "-s",
        "read-only",
        "-o",
        out_path,
    ]
    if args.model:
        cmd += ["-m", args.model]
    if args.cd:
        cmd += ["-C", args.cd]
    cmd.append(prompt)
    try:
        subprocess.run(cmd, capture_output=True, text=True, timeout=args.timeout)
        with open(out_path, encoding="utf-8") as fh:
            return fh.read().strip()
    except Exception as exc:  # noqa: BLE001
        return f"(synthesis worker failed: {exc})"
    finally:
        try:
            os.unlink(out_path)
        except OSError:
            pass


def main() -> int:
    p = argparse.ArgumentParser(
        description="parallel codex-exec swarm over expert lenses"
    )
    p.add_argument("task", help="the task/question to fan out")
    p.add_argument(
        "--lenses", help="comma-separated expert angles (default: a review panel)"
    )
    p.add_argument(
        "--max", type=int, default=4, help="max concurrent workers (default 4)"
    )
    p.add_argument(
        "--timeout", type=int, default=600, help="per-worker timeout seconds"
    )
    p.add_argument("--cd", help="working dir for workers (-C)")
    p.add_argument("--model", help="model for workers (-m)")
    p.add_argument(
        "--sandbox",
        default="read-only",
        choices=["read-only", "workspace-write"],
        help="worker sandbox (default read-only)",
    )
    p.add_argument("--synthesize", action="store_true", help="add a final merge worker")
    p.add_argument("--json", action="store_true", help="emit raw JSON results")
    a = p.parse_args()

    if not shutil.which("codex"):
        return _named_blocker(
            "`codex` CLI not found on PATH. Install Codex, then re-run "
            "(this skill orchestrates parallel `codex exec` workers)."
        )
    if not os.path.exists(os.path.expanduser("~/.codex/auth.json")):
        return _named_blocker(
            "Codex not authenticated (~/.codex/auth.json missing). "
            "Run `codex login` first."
        )

    lenses = [
        s.strip()
        for s in (a.lenses.split(",") if a.lenses else DEFAULT_LENSES)
        if s.strip()
    ]
    if not lenses:
        return _named_blocker("no lenses to run")
    cap = max(1, min(a.max, 8))  # hard ceiling 8 (rate-limit safety)
    print(
        f"swarm: {len(lenses)} lenses [{', '.join(lenses)}] · concurrency {cap} · "
        f"each = a full codex session",
        file=sys.stderr,
    )

    results: list[dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=cap) as ex:
        futs = {ex.submit(run_worker, lens, a.task, a): lens for lens in lenses}
        for fut in concurrent.futures.as_completed(futs):
            r = fut.result()
            results.append(r)
            print(f"  {'✓' if r['ok'] else '✗'} {r['lens']}", file=sys.stderr)
    results.sort(key=lambda r: lenses.index(r["lens"]))

    if a.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0

    print(f"\n# Swarm results — {a.task}\n")
    for r in results:
        print(f"## {r['lens']}")
        print(r["findings"] if r["ok"] else f"_(failed: {r['error']})_")
        print()
    failed = [r["lens"] for r in results if not r["ok"]]
    if failed:
        print(
            f"> ⚠ {len(failed)} lens(es) failed: {', '.join(failed)}", file=sys.stderr
        )
    if a.synthesize:
        print("## synthesis\n" + synthesize(a.task, results, a))
    else:
        print(
            "> Now SYNTHESIZE the lenses above into one verdict (dedupe, resolve "
            "conflicts, rank the top 3 actions). — calling agent"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
