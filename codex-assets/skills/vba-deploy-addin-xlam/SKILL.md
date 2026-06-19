---
name: vba-deploy-addin-xlam
description: >-
  Package and deploy macros as an Excel add-in (.xlam) — SaveAs xlOpenXMLAddIn, IsAddin, install via Add-ins dialog, AddIns.Add, ribbon integration, update/versioning, vs .xla legacy
---

# vba-deploy-addin-xlam

An add-in (`.xlam`) is a hidden, always-available macro library — the right way to ship reusable tools across many workbooks. Create one by setting `ThisWorkbook.IsAddin = True` (hides the sheets) and SaveAs type **xlOpenXMLAddIn** (`.xlam`); or programmatically `wb.SaveAs path, xlOpenXMLAddIn`. Users install via File > Options > Add-ins > Go > Browse, or programmatically `AddIns.Add(path).Installed = True`. Installed add-ins load on every Excel start.

Expert moves: surface the add-in's commands through a **custom Ribbon tab** (customUI XML inside the .xlam) so users get buttons, not a hidden macro list — the professional deployment pattern. UDFs in an installed add-in are available to all workbooks (reference them plainly, or fully-qualified `'MyAddin.xlam'!MyFunc` to disambiguate). For **updates**, deploy a new .xlam to the same path and have Excel pick it up on restart; bump a version constant and expose it. Keep the add-in in a **Trusted Location** so macros run without prompts. Default install folder: `%AppData%\Microsoft\AddIns`.

Pitfalls: an add-in's worksheets are hidden and `ActiveSheet`/`ThisWorkbook` refer to the add-in, not the user's data — always pass or grab the target workbook explicitly (`ActiveWorkbook`). Forgetting to set `IsAddin = True` ships a normal workbook. Copying an installed add-in's file while Excel holds it locked fails — close Excel to update. `.xla` is the legacy binary format (pre-2007); prefer `.xlam`. Path-based installs break if the file moves — pin to a stable network/local path.

**Tools:** SaveAs xlOpenXMLAddIn, ThisWorkbook.IsAddin, AddIns.Add, AddIns(...).Installed, .xlam, Application.AddIns2, customUI
