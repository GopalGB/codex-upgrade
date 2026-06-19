---
name: pptx-tables-pro
description: >-
  Build readable slide tables — banded rows, merged header cells, right-aligned numbers, autofit control — and generate them from data without the default ugly grid
---

# pptx-tables-pro

Default PowerPoint tables are heavy (thick borders, centered everything). Fix: Table Design > pick a light banded style or strip borders entirely and use subtle row banding for scanability. Left-align text, right-align numbers (so digits line up by place value), bold the header row, set a single accent underline beneath the header instead of full gridlines. Merge cells for grouped headers (select > Merge Cells). Control width manually — autofit-to-window often overflows the slide. In python-pptx: `shapes.add_table(rows, cols, x,y,cx,cy).table`, then `tbl.cell(r,c).text`, `tbl.cell(r,c).merge(tbl.cell(r,c2))` for spans, set `tbl.columns[i].width = Emu(...)`, and per-paragraph alignment via `cell.text_frame.paragraphs[0].alignment = PP_ALIGN.RIGHT`. Style fills with `cell.fill.solid(); cell.fill.fore_color.rgb`. Pitfall: large tables belong in an appendix or a linked Excel — a slide table over ~6 columns x 10 rows is unreadable from the back of a room; summarize and link the detail. Set `tbl.first_row = True` to enable header styling from the table style.

**Tools:** Insert > Table; Table Design tab; python-pptx add_table, cell.merge, cell.text_frame, _Cell.fill
