"""codex_env.py - zero-config dependency bootstrap for Codex tool scripts.

Design goal: every Codex tool script "just works" even inside a locked-down
office where you may NOT be allowed to install packages globally and where
network access may be blocked. There is no MCP and no magic here - only the
Python standard library plus an isolated, self-healing virtualenv.

Strategy, in order:
  1. Run inside an isolated venv at ~/.codex/tools-venv (created on first use,
     no network needed for the venv itself).
  2. ensure(...) pip-installs missing packages INTO that venv. If pip works,
     the tool runs. If a package is already importable, nothing happens.
  3. If network/pip is blocked, raise DependencyBlocked with the EXACT command
     the human must run - never a silent crash, never a misleading traceback.

Usage in a tool script (top of file) - resolve this lib from repo OR install dir:

    import os, sys
    _HERE = os.path.dirname(os.path.abspath(__file__))
    for _c in (os.path.join(_HERE, "..", "..", "..", "lib"),
               os.path.expanduser("~/.codex/lib"),
               os.path.expanduser("~/.agents/lib")):
        if os.path.isfile(os.path.join(_c, "codex_env.py")):
            sys.path.insert(0, os.path.abspath(_c)); break
    import codex_env
    codex_env.bootstrap("openpyxl")        # re-exec into venv + ensure deps
    import openpyxl                          # now guaranteed importable

Environment overrides:
  CODEX_TOOLS_VENV   - path to the venv (default ~/.codex/tools-venv)
  CODEX_TOOLS_NO_VENV=1 - skip the venv, install with `pip install --user`
  CODEX_TOOLS_OFFLINE=1 - never attempt pip; fail fast with manual instructions
"""

from __future__ import annotations

import importlib
import os
import subprocess
import sys
import venv
from pathlib import Path

__all__ = ["bootstrap", "ensure", "DependencyBlocked", "venv_dir"]

_PIP_TIMEOUT_SEC = 240
_REEXEC_FLAG = "CODEX_TOOLS_ACTIVE"


class DependencyBlocked(RuntimeError):
    """Raised when a dependency is missing and cannot be installed.

    The message always contains a copy-pasteable command for the human.
    """


def venv_dir() -> Path:
    return Path(
        os.environ.get("CODEX_TOOLS_VENV", str(Path.home() / ".codex" / "tools-venv"))
    ).expanduser()


def _venv_python(d: Path) -> Path:
    if os.name == "nt":
        return d / "Scripts" / "python.exe"
    return d / "bin" / "python"


def _use_venv() -> bool:
    return os.environ.get("CODEX_TOOLS_NO_VENV") != "1"


def _inside_target_venv() -> bool:
    if os.environ.get(_REEXEC_FLAG) == "1":
        return True
    try:
        return Path(sys.prefix).resolve() == venv_dir().resolve()
    except OSError:
        return False


def _create_venv(d: Path) -> Path:
    py = _venv_python(d)
    if not py.exists():
        # with_pip=True works offline; it bootstraps from the bundled ensurepip.
        venv.EnvBuilder(with_pip=True, clear=False, symlinks=os.name != "nt").create(d)
    if not py.exists():  # pragma: no cover - extremely unusual
        raise DependencyBlocked(
            f"Could not create a Python venv at {d}. "
            f"Run tools with CODEX_TOOLS_NO_VENV=1 to use the system Python instead."
        )
    return py


def bootstrap(*packages: str, import_names: dict | None = None) -> None:
    """Re-exec the current script inside the tools venv, then ensure packages.

    Call this ONCE at the top of a tool script, before importing the deps.
    No-ops cleanly if already inside the venv or if CODEX_TOOLS_NO_VENV=1.
    """
    if _use_venv() and not _inside_target_venv():
        py = _create_venv(venv_dir())
        env = dict(os.environ, **{_REEXEC_FLAG: "1"})
        os.execve(str(py), [str(py), *sys.argv], env)  # replaces this process
    if packages:
        ensure(*packages, import_names=import_names)


def _is_importable(module: str) -> bool:
    try:
        importlib.import_module(module)
        return True
    except ImportError:
        return False


def ensure(*packages: str, import_names: dict | None = None) -> None:
    """Ensure each package is importable; pip-install the ones that are missing.

    `packages` are pip names (may include version pins, e.g. "openpyxl>=3.1").
    `import_names` maps a pip name to its import name when they differ
    (e.g. {"python-pptx": "pptx", "pymupdf": "fitz"}).
    """
    import_names = import_names or {}
    missing = []
    for pkg in packages:
        base = pkg.split("==")[0].split(">=")[0].split("<")[0].split("~=")[0].strip()
        mod = import_names.get(pkg) or import_names.get(base) or base.replace("-", "_")
        if not _is_importable(mod):
            missing.append(pkg)
    if not missing:
        return

    if os.environ.get("CODEX_TOOLS_OFFLINE") == "1":
        raise _blocked(missing, reason="CODEX_TOOLS_OFFLINE=1 is set")

    pip_cmd = [
        sys.executable,
        "-m",
        "pip",
        "install",
        "--quiet",
        "--disable-pip-version-check",
        "--no-input",
    ]
    if not _use_venv():
        pip_cmd.append("--user")
    pip_cmd += list(missing)

    try:
        subprocess.run(
            pip_cmd, check=True, timeout=_PIP_TIMEOUT_SEC, stdout=subprocess.DEVNULL
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError) as exc:
        raise _blocked(missing, reason=str(exc)) from exc

    # Verify the install actually made them importable.
    still_missing = []
    for pkg in missing:
        base = pkg.split("==")[0].split(">=")[0].split("<")[0].split("~=")[0].strip()
        mod = import_names.get(pkg) or import_names.get(base) or base.replace("-", "_")
        importlib.invalidate_caches()
        if not _is_importable(mod):
            still_missing.append(pkg)
    if still_missing:
        raise _blocked(still_missing, reason="installed but still not importable")


def _blocked(missing: list[str], reason: str) -> DependencyBlocked:
    target = venv_dir()
    py = _venv_python(target)
    if _use_venv():
        manual = f'"{py}" -m pip install ' + " ".join(missing)
        hint = (
            f"(the venv lives at {target}; if it is missing run any tool "
            f"once to create it, or `python3 -m venv {target}`)"
        )
    else:
        manual = "python3 -m pip install --user " + " ".join(missing)
        hint = "(CODEX_TOOLS_NO_VENV=1 is set, so this targets the system Python)"
    return DependencyBlocked(
        "\n".join(
            [
                f"Missing Python package(s): {', '.join(missing)}",
                f"Auto-install failed: {reason}",
                "",
                "This usually means the office network blocks pip. Ask IT / run on a",
                "machine with network, or run this exact command yourself:",
                f"  {manual}",
                hint,
            ]
        )
    )


if __name__ == "__main__":
    # `python codex_env.py <pkg> [pkg...]` - prewarm the venv with deps.
    bootstrap(*sys.argv[1:])
    print(
        f"OK: tools venv ready at {venv_dir()} "
        f"({'system python' if not _use_venv() else sys.executable})"
    )
