---
name: xls-auditing-trace
description: >-
  Formula auditing: trace precedents/dependents, evaluate formula, show formulas, error checking, range finder, find broken links and circular refs
---

# xls-auditing-trace

When a number looks wrong, audit don't guess. **Trace Precedents/Dependents** (Formulas tab, or Alt+T U P) draws arrows to inputs/outputs — double-click an arrow to jump. **Evaluate Formula** (Alt+T U F) steps through a formula one calculation at a time to see exactly where it goes wrong — the single best debugging tool for nested formulas. **Show Formulas** (Ctrl+`) reveals all formulas at once to spot hardcoded numbers hiding among formulas (the classic broken-model cause). Select a formula and press **F2** to see the colored **range finder** highlighting referenced cells. **Error Checking** (Formulas > Error Checking) walks every error; the green-triangle flags catch inconsistent-formula and number-as-text issues. **Watch Window** monitors key cells while you edit elsewhere. Find **circular references** via Formulas > Error Checking dropdown (shows the cell); find **external links** via Data > Edit Links (broken links throw `#REF!`/prompts on open). Pitfalls: inconsistent formula in a row (one cell breaks the copy-across pattern) is the most common silent bug — Show Formulas + the inconsistency flag catch it; tracer arrows clear on edit.

**Tools:** Trace Precedents/Dependents, Evaluate Formula, Ctrl+`, Watch Window
