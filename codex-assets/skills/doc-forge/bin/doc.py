#!/usr/bin/env python3
"""doc.py - Word/DOCX + universal convert + OCR for scanned PDFs (no MCP).

Fills the office-doc gaps around xlsx-wrangler (Excel) / deck-smith (pptx) /
pdf-extract (PDF text). Permissive by default: MarkItDown (MIT) for office->markdown,
pandoc (system) for convert, ocrmypdf (system, MPL-2.0) for OCR, python-docx for
.docx generation. No AGPL.

Subcommands:
  to-md   FILE [-o out.md]            any office/pdf -> markdown (MarkItDown; for LLM reading)
  convert IN OUT                      universal convert via pandoc (md<->docx<->html<->…)
  ocr     IN.pdf [-o OUT.pdf]         add a text layer to a SCANNED pdf (ocrmypdf) -> then pdf-extract
  docx-new OUT.docx --from-md IN.md   generate a .docx from markdown (pandoc)

Examples:
  python doc.py to-md patent.pdf
  python doc.py ocr scanned-patent.pdf -o searchable.pdf
  python doc.py convert notes.md notes.docx
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
for _c in (
    os.path.join(_HERE, "..", "..", "..", "lib"),
    os.path.expanduser("~/.codex/lib"),
    os.path.expanduser("~/.agents/lib"),
):
    if os.path.isfile(os.path.join(_c, "codex_env.py")):
        sys.path.insert(0, os.path.abspath(_c))
        break
import codex_env  # noqa: E402


def _need(binname: str, hint: str):
    if not shutil.which(binname):
        sys.exit(f"BLOCKED: `{binname}` not found. Install it: {hint}")


def cmd_to_md(a):
    codex_env.bootstrap(
        "markitdown[pdf,docx,pptx,xlsx]",
        import_names={"markitdown[pdf,docx,pptx,xlsx]": "markitdown"},
    )
    from markitdown import MarkItDown

    md = MarkItDown().convert(a.file).text_content
    if a.output:
        with open(a.output, "w", encoding="utf-8") as fh:
            fh.write(md)
        print(f"wrote {len(md)} chars -> {a.output}", file=sys.stderr)
    else:
        sys.stdout.write(md)


def cmd_convert(a):
    _need("pandoc", "brew install pandoc (already installed on this machine)")
    # PDF output needs a LaTeX engine; warn but let pandoc speak.
    if a.out.lower().endswith(".pdf"):
        print(
            "note: pandoc->PDF needs a LaTeX engine (e.g. `brew install basictex`).",
            file=sys.stderr,
        )
    r = subprocess.run(["pandoc", a.inp, "-o", a.out])
    if r.returncode == 0:
        print(f"wrote {a.out}")
    else:
        sys.exit(f"pandoc failed (exit {r.returncode})")


def cmd_ocr(a):
    _need("ocrmypdf", "brew install ocrmypdf  (wraps tesseract, already installed)")
    out = a.output or (os.path.splitext(a.file)[0] + ".ocr.pdf")
    # --skip-text: don't re-OCR pages that already have text; safe + idempotent
    r = subprocess.run(["ocrmypdf", "--skip-text", a.file, out])
    if r.returncode == 0:
        print(f"OCR'd -> {out}  (now readable via pdf-extract)")
    else:
        sys.exit(
            f"ocrmypdf failed (exit {r.returncode}). For image-only PDFs try without --skip-text."
        )


def cmd_docx_new(a):
    _need("pandoc", "brew install pandoc")
    r = subprocess.run(["pandoc", a.from_md, "-o", a.output])
    if r.returncode == 0:
        print(f"wrote {a.output}")
    else:
        # fallback: python-docx for a minimal doc if pandoc unavailable mid-run
        sys.exit(f"pandoc failed (exit {r.returncode})")


def main():
    p = argparse.ArgumentParser(description="DOCX + convert + OCR (permissive, no MCP)")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("to-md")
    s.add_argument("file")
    s.add_argument("-o", "--output")
    s.set_defaults(fn=cmd_to_md)
    s = sub.add_parser("convert")
    s.add_argument("inp")
    s.add_argument("out")
    s.set_defaults(fn=cmd_convert)
    s = sub.add_parser("ocr")
    s.add_argument("file")
    s.add_argument("-o", "--output")
    s.set_defaults(fn=cmd_ocr)
    s = sub.add_parser("docx-new")
    s.add_argument("output")
    s.add_argument("--from-md", dest="from_md", required=True)
    s.set_defaults(fn=cmd_docx_new)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
