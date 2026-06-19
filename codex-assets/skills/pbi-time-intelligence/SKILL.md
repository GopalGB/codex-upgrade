---
name: pbi-time-intelligence
description: >-
  YTD/QTD/MTD, prior-period and YoY comparisons with TOTALYTD, SAMEPERIODLASTYEAR, DATEADD — requires a marked date table
---

# pbi-time-intelligence

Every time-intelligence function needs a dedicated, contiguous Date table marked as a date table (Model view > Mark as date table) with one row per day and no gaps. Without it, functions silently misbehave or return blanks. Core patterns: `Sales YTD = TOTALYTD([Total Sales], 'Date'[Date])`; non-calendar fiscal year add a year-end string: `TOTALYTD([Total Sales], 'Date'[Date], "06-30")`. Prior year: `Sales PY = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))`. YoY %: `YoY % = DIVIDE([Total Sales] - [Sales PY], [Sales PY])`. Flexible shifts use DATEADD: `Sales PM = CALCULATE([Total Sales], DATEADD('Date'[Date], -1, MONTH))`. Pitfall #1: DATEADD requires a complete, dense date column — partial/filtered date tables break it; use it on the Date table column, never on the fact's date. Pitfall #2: SAMEPERIODLASTYEAR only shifts exactly one year; for arbitrary offsets use DATEADD. Pitfall #3: applying these over a relationship where the fact date isn't related to the Date table yields blanks — verify the active relationship. Pitfall #4: a date table built with `CALENDARAUTO()` can include unwanted years; prefer explicit `CALENDAR(MIN, MAX)`.

**Tools:** TOTALYTD, SAMEPERIODLASTYEAR, DATEADD, DATESYTD, PARALLELPERIOD, CALCULATE
