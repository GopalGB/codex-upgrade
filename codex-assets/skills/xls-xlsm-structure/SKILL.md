---
name: xls-xlsm-structure
description: >-
  What makes a macro-enabled .xlsm: OOXML/ZIP package, vbaProject.bin, content types, Trust Center/macro security, .xlsm vs .xlsb vs .xlsx
---

# xls-xlsm-structure

An .xlsx/.xlsm is a **ZIP package (OOXML)** — rename to .zip and you'll see `xl/worksheets/sheetN.xml`, `xl/sharedStrings.xml`, `xl/styles.xml`, `[Content_Types].xml`, and `_rels`. The ONLY structural difference for **.xlsm** is it carries an `xl/vbaProject.bin` (the compiled VBA) AND declares the macro-enabled content type — that's why saving a workbook-with-macros as plain .xlsx silently strips the code (Excel warns once). So: code-bearing workbooks MUST be .xlsm (or .xlsb, which also stores VBA in binary). **Macro security** lives in **Trust Center > Macro Settings**: default 'Disable with notification'; macros from the internet are blocked by Mark-of-the-Web unless the file is in a **Trusted Location** or you Unblock it (file Properties). Inspect/repair a corrupt file by unzipping it. Pitfalls: emailing .xlsm often gets quarantined — zip it or use a trusted location; .xlsb opens faster and stores macros but some tools can't parse its binary sheets; `.xltm` is the macro-enabled template; never trust an .xlsm from an unknown source (macro = arbitrary code). Digitally sign the VBA project for distribution so users get a publisher prompt, not a block.

**Tools:** OOXML ZIP, vbaProject.bin, Trust Center, [Content_Types].xml
