#!/usr/bin/env python3
"""pdf.py - extract text, tables, and markdown from PDFs (no MCP).

LICENSING (important for office/commercial use): the DEFAULT backends are
permissively licensed - pypdf (BSD) for text, pdfplumber (MIT) for tables. The
much-loved PyMuPDF / pymupdf4llm are AGPL-3.0, which can create source-disclosure
obligations in a commercial setting, so they are ONLY used when you pass
`--allow-agpl` (or set CODEX_ALLOW_AGPL=1). They are never the default.

Subcommands:
  info  FILE.pdf                       page count, metadata, encryption, text-layer?
  text  FILE.pdf [--pages 1-5] [-o]    plain text (pypdf; PyMuPDF if --allow-agpl)
  md    FILE.pdf [-o out.md]           markdown-ish (page headers + text/tables)
  tables FILE.pdf [--pages 1-5]        tables as CSV blocks (pdfplumber)
  search FILE.pdf PATTERN              pages + lines matching a regex

Examples:
  python pdf.py info report.pdf
  python pdf.py md report.pdf -o report.md
  python pdf.py tables statement.pdf --pages 2-4
"""

from __future__ import annotations

import argparse
import os
import re
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


def _allow_agpl(a) -> bool:
    return getattr(a, "allow_agpl", False) or os.environ.get("CODEX_ALLOW_AGPL") == "1"


def _parse_pages(spec: str | None, total: int) -> list[int]:
    if not spec:
        return list(range(total))
    out: set[int] = set()
    for part in spec.split(","):
        if "-" in part:
            lo, hi = part.split("-")
            out.update(range(int(lo) - 1, int(hi)))
        else:
            out.add(int(part) - 1)
    return sorted(p for p in out if 0 <= p < total)


# ---- permissive backend: pypdf (BSD) ----------------------------------------
def _pypdf_reader(path: str):
    codex_env.ensure("pypdf")
    from pypdf import PdfReader

    return PdfReader(path)


def cmd_info(a):
    r = _pypdf_reader(a.file)
    n = len(r.pages)
    sample = (r.pages[0].extract_text() or "") if n else ""
    print(f"file: {a.file}")
    print(f"pages: {n}")
    print(f"encrypted: {r.is_encrypted}")
    print(
        f"text_layer: {'yes' if sample.strip() else 'NO (looks scanned - needs OCR, e.g. ocrmypdf/tesseract)'}"
    )
    meta = r.metadata or {}
    for k in ("/Title", "/Author", "/Subject", "/CreationDate"):
        if meta.get(k):
            print(f"{k.strip('/').lower()}: {meta[k]}")


def cmd_text(a):
    if _allow_agpl(a):
        codex_env.ensure("pymupdf", import_names={"pymupdf": "fitz"})
        import fitz

        doc = fitz.open(a.file)
        pages = _parse_pages(a.pages, doc.page_count)
        _emit("\n\n".join(doc[p].get_text() for p in pages), a.output)
        return
    r = _pypdf_reader(a.file)
    pages = _parse_pages(a.pages, len(r.pages))
    _emit("\n\n".join((r.pages[p].extract_text() or "") for p in pages), a.output)


def cmd_md(a):
    """Markdown-ish: per-page header + text, with detected tables as CSV fences.

    Permissive by default (pypdf text + pdfplumber tables). With --allow-agpl,
    use pymupdf4llm for higher-fidelity markdown.
    """
    if _allow_agpl(a):
        try:
            codex_env.ensure("pymupdf4llm")
            import pymupdf4llm

            _emit(pymupdf4llm.to_markdown(a.file), a.output)
            return
        except codex_env.DependencyBlocked as exc:
            print(
                f"(pymupdf4llm unavailable: {exc.args[0].splitlines()[0]} - "
                f"falling back to permissive path)",
                file=sys.stderr,
            )
    r = _pypdf_reader(a.file)
    codex_env.ensure("pdfplumber")
    import csv
    import io
    import pdfplumber

    parts: list[str] = []
    with pdfplumber.open(a.file) as pdf:
        for i, page in enumerate(pdf.pages):
            parts.append(f"\n## Page {i + 1}\n")
            txt = (r.pages[i].extract_text() or "").strip() if i < len(r.pages) else ""
            if txt:
                parts.append(txt)
            for j, t in enumerate(page.extract_tables(), start=1):
                buf = io.StringIO()
                csv.writer(buf).writerows(
                    [["" if c is None else c for c in row] for row in t]
                )
                parts.append(f"\n```csv\n# table {j}\n{buf.getvalue().rstrip()}\n```")
    _emit("\n".join(parts), a.output)


def cmd_tables(a):
    codex_env.ensure("pdfplumber")
    import csv
    import io
    import pdfplumber

    with pdfplumber.open(a.file) as pdf:
        pages = _parse_pages(a.pages, len(pdf.pages))
        n = 0
        for p in pages:
            for t in pdf.pages[p].extract_tables():
                n += 1
                print(f"\n### Table {n} (page {p + 1})")
                buf = io.StringIO()
                csv.writer(buf).writerows(
                    [["" if c is None else c for c in row] for row in t]
                )
                print(buf.getvalue().rstrip())
        if n == 0:
            print("no tables detected", file=sys.stderr)


def cmd_search(a):
    r = _pypdf_reader(a.file)
    rx = re.compile(a.pattern, re.IGNORECASE)
    hits = 0
    for i, page in enumerate(r.pages, start=1):
        for line in (page.extract_text() or "").splitlines():
            if rx.search(line):
                print(f"p{i}: {line.strip()}")
                hits += 1
    print(f"{hits} match(es)", file=sys.stderr)


def _emit(text: str, output: str | None):
    if output:
        with open(output, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {len(text)} chars -> {output}", file=sys.stderr)
    else:
        sys.stdout.write(text)


def main():
    p = argparse.ArgumentParser(
        description="PDF text/table/markdown extractor (permissive by default)"
    )
    p.add_argument(
        "--allow-agpl",
        action="store_true",
        help="permit AGPL PyMuPDF/pymupdf4llm for higher-fidelity extraction",
    )
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("info")
    s.add_argument("file")
    s.set_defaults(fn=cmd_info)
    s = sub.add_parser("text")
    s.add_argument("file")
    s.add_argument("--pages")
    s.add_argument("-o", "--output")
    s.set_defaults(fn=cmd_text)
    s = sub.add_parser("md")
    s.add_argument("file")
    s.add_argument("-o", "--output")
    s.set_defaults(fn=cmd_md)
    s = sub.add_parser("tables")
    s.add_argument("file")
    s.add_argument("--pages")
    s.set_defaults(fn=cmd_tables)
    s = sub.add_parser("search")
    s.add_argument("file")
    s.add_argument("pattern")
    s.set_defaults(fn=cmd_search)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
