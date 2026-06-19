---
name: toolbelt
description: >-
  Reach for FAST CLI tools first instead of writing slow Python/grep one-offs. The
  reach-for-it layer: structural code search/refactor, file find, JSON/YAML/CSV/Parquet
  wrangling, doc conversion, readable diffs. Use whenever a task tempts you to write an
  os.walk/pandas/sed script for something a one-liner already does. Triggers: "search
  the code", "find files", "refactor across files", "rename everywhere", "parse this
  json/yaml/csv", "convert this file", "grep", "which tool for".
---

# toolbelt — prefer the sharp tool, don't hand-roll (no MCP)

The expert reflex: a maintained CLI tool beats a 40-line script for search, refactor,
data wrangling, and conversion. This skill is the decision table + usage one-liners.
Most are ALREADY installed — the highest-value win is just *preferring* them.

## Decision table (reach for the RIGHT one)
| Need | Use | Note |
|------|-----|------|
| search code text | **`rg`** (ripgrep) | installed · faster than grep, gitignore-aware |
| find files | **`fd`** | `brew install fd` · faster/simpler than `find` |
| **structural** search/refactor (cross-line, AST) | **`ast-grep`** (`sg`) | `brew install ast-grep` · safe rewrites `sed`/`comby` can't do |
| JSON | **`jq`** | installed |
| YAML / TOML / XML | **`yq`** | `brew install yq` · jq syntax; edit `config.toml` + skill frontmatter |
| tabular: SQL over CSV/Parquet/JSON | **`duckdb`** | installed · `duckdb -c "SELECT … FROM 'f.parquet'"` |
| tabular: streaming reshape/stats | **`mlr`** (miller) | installed · constant-memory CSV/TSV/JSON |
| convert docs (md↔docx↔pdf↔html…) | **`pandoc`** | installed · (see `doc-forge` for OCR/docx-gen) |
| readable git diff | **`delta`** | optional · `brew install git-delta` |
| view a file (syntax+lines) | **`bat`** | optional · `brew install bat` |

(Optional, list-don't-force: `qsv` for heavy CSV ops beyond mlr; `difftastic`/`difft`
for structural diffs when delta isn't enough. duckdb+mlr+delta cover ~90%.)

## Usage one-liners
```bash
rg -n "TODO|FIXME" --type py                       # search
fd -e ts -x wc -l                                  # find + act
sg -p 'console.log($A)' -r 'logger.debug($A)' -l ts  # AST-safe refactor
jq '.results[].name' data.json                     # JSON
yq '.profiles.office.sandbox_mode' ~/.codex/config.toml   # TOML/YAML
duckdb -c "SELECT col, count(*) FROM 'big.csv' GROUP BY 1 ORDER BY 2 DESC LIMIT 10"
mlr --csv stats1 -a mean,p50,max -f price big.csv  # streaming stats
pandoc report.md -o report.docx                    # convert
```

## How to work
1. Before writing a script to search/refactor/parse/convert, check this table — a tool
   almost always wins (faster, safer, less code = the kit's reuse + minimal-code law).
2. **`ast-grep` for any structural change** (rename a call pattern, wrap an API across
   files) — never `sed` a multi-line code construct; never `comby` (not AST-aware).
3. Big data → `duckdb`/`mlr` stream it; never `pandas.read_csv(huge)` (see `data-engineer`).
4. If a tool is missing, the table shows the one-line install; degrade to the stdlib/Python
   path only when install is blocked — and say so.
