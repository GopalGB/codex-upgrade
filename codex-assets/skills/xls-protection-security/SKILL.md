---
name: xls-protection-security
description: >-
  Workbook/sheet/cell protection, locked vs unlocked cells, hide formulas, workbook structure lock, password limits, sensitivity labels
---

# xls-protection-security

Protection is layered. **Cell lock**: every cell is 'Locked' by default but it only takes effect AFTER you **Protect Sheet** (Review > Protect Sheet). So the workflow is: unlock the input cells (Format Cells > Protection > clear Locked), then Protect Sheet — now users edit only inputs. Tick **Hidden** on formula cells before protecting to hide formulas from the formula bar. On Protect Sheet, choose what's still allowed (select locked cells, use slicers/AutoFilter, format). **Protect Workbook (Structure)** stops adding/deleting/renaming/hiding sheets. **Allow Edit Ranges** grants specific ranges to specific people. **Encrypt with Password** (File > Info > Protect Workbook > Encrypt) is the only real security — it encrypts the file (AES-256). Pitfalls: sheet/workbook-structure passwords are trivially removable (NOT security — just guard rails against accidents); a forgotten encryption password is unrecoverable; protection doesn't stop a determined user; macros can be password-locked in the VBE but that lock is weak. For genuine confidentiality use file encryption + sensitivity labels (Information Protection), not sheet protection.

**Tools:** Protect Sheet, Protect Workbook, Format Cells lock, Allow Edit Ranges
