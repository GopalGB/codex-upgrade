---
name: m365-office-scripts-automate
description: >-
  Write Office Scripts (TypeScript) for Excel on the web and trigger them from Power Automate — when automating in-workbook logic with a no-Graph option
---

# m365-office-scripts-automate

Office Scripts run inside Excel on the web (Automate tab > New Script) in TypeScript with the `ExcelScript` API. Entry point is `function main(workbook: ExcelScript.Workbook)`. Example: `const sheet = workbook.getActiveWorksheet(); const rng = sheet.getRange('A1:B2'); rng.setValues([[1,2],[3,4]]);`. Return a value from `main` to pass data back to a flow; accept parameters by adding typed args to `main(workbook, threshold: number)`.

Trigger from Power Automate with the **Excel Online (Business) > Run script** action — pick the location, the script, and map flow inputs to the script parameters; the script's return value becomes a dynamic content output.

Pitfall: Office Scripts is **not** Office.js/VBA — no UI dialogs, no `Application` object, synchronous API only, and it only runs on Excel for the web/desktop with a qualifying license, not perpetual Office. Pitfall 2: scripts have a 1-minute execution limit when called from Power Automate and can't make external HTTP calls — do network work in the flow, computation in the script. Pitfall 3: `getValues()` on a huge range can time out; bound the range with `getUsedRange()`.

**Tools:** Office Scripts, ExcelScript.Workbook, getActiveWorksheet, Run script (Power Automate)
