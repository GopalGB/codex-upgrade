---
name: ba-spreadsheet-modelling-discipline
description: >-
  Build auditable financial/analytical spreadsheet models: inputs/calcs/outputs separation, one-formula-per-row consistency, named ranges, no hardcodes in formulas, error/trace checks; avoid fragile mega-formulas.
---

# ba-spreadsheet-modelling-discipline

A model is read and trusted by others, so structure for audit. Separate three zones (ideally three tab colors): inputs/assumptions (blue font, the ONLY hardcoded cells, each labeled with units and source), calculations, and outputs/summary. Golden rule: never bury a constant inside a formula — every number a user might change lives in a labeled input cell so sensitivity works and assumptions are visible. Keep formulas consistent across a row (one logic, copied) so you can audit by spot-check; a row where column F differs from G–Z is a bug magnet. Prefer many simple linked steps over one unreadable mega-formula; intermediate cells are free and debuggable. Use named ranges or structured Table[references] for key drivers. Add checks: balance-sheet balances row, a control total that must equal a known figure, and conditional formatting on any cell that goes negative/errors. Expert moves: build a 'check' panel of asserts (=IF(sum_of_parts=total,'OK','BREAK')); use Trace Precedents/Dependents and Evaluate Formula to audit; flag IFERROR wrappers — they hide real breaks, so log what they catch; version and date the file. Pitfalls: hardcoded numbers inside formulas; circular references (turn on iterative only deliberately); mixing inputs and calcs so a paste destroys logic; volatile functions (OFFSET, INDIRECT, NOW) bloating recalc; copy-paste-values that silently breaks links; no single-source assumption sheet so two tabs use different prices; merged cells breaking fill and references.

**Tools:** Excel, Google Sheets, FAST/SMART modeling standards
