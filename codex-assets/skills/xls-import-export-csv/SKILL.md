---
name: xls-import-export-csv
description: >-
  CSV/text import and export: encoding (UTF-8 BOM), delimiter and locale traps, leading zeros, date misparse, Power Query vs legacy import
---

# xls-import-export-csv

**Never double-click a CSV** for important data — Excel auto-converts: leading zeros vanish (`007`→`7`), long IDs become scientific notation (`1.23E+15`), `MAR-1` becomes a date, and locale decides comma-vs-dot decimals. Instead use **Power Query (Get Data > From Text/CSV)**: set file origin/encoding (**UTF-8** — use UTF-8-BOM when exporting for Excel to read accents correctly), choose the delimiter, and set each column's type explicitly (keep ID columns as **Text** to preserve zeros). For exports, write a Table to CSV via Save As, but be aware Excel exports the system locale's list separator (semicolon in some regions) — Power Query Output or a script gives control. To force display formats use **TEXT(value,"0000")** before export, or store as text. Pitfalls: the legacy Text Import Wizard is hidden (enable in Options > Data); fixed-width files need column breaks; round-tripping CSV loses formulas and types; for repeatable imports, build a PQ query and just **Refresh** when the file updates. Tab/pipe-delimited avoids comma-in-field quoting headaches.

**Tools:** Power Query, Text Import, Get Data, CSV, UTF-8, TEXT
