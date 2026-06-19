---
name: xls-date-time
description: >-
  Date/time math: serial numbers, EDATE/EOMONTH/WORKDAY/NETWORKDAYS, DATEDIF, time fractions, timezone/locale date-parse fixes
---

# xls-date-time

Excel stores dates as **serial numbers** (1 = 1900-01-01; times are the fractional part, 0.5 = noon) — that's why date math is just arithmetic. Build dates safely with **DATE(y,m,d)** (never type locale-ambiguous literals); DATE auto-rolls (`DATE(2026,13,1)`=Jan-2027), handy for month-ends. **EDATE(start,months)** shifts by months (keeps day), **EOMONTH(start,months)** returns the last day of a month offset — core for financial period ends. Working days: **WORKDAY.INTL** / **NETWORKDAYS.INTL** with a weekend code and a holidays list (the `.INTL` versions let you define non-Mon-Fri weekends). **DATEDIF(start,end,"y"/"m"/"d"/"ym"/"md")** computes age/tenure (undocumented but works; `"md"` has known bugs near month-ends — verify). Extract parts with YEAR/MONTH/DAY/WEEKDAY/WEEKNUM/ISOWEEKNUM. Pitfalls: dates imported as TEXT won't do math (the #1 issue — fix with DATEVALUE or Power Query type-change, or a `=A1+0` coercion); 1900 leap-year bug (Excel thinks 1900 was a leap year) skews very old date diffs; subtracting times across midnight goes negative — add the day. Format ≠ value: changing display doesn't change the underlying serial.

**Tools:** DATE, EDATE, EOMONTH, WORKDAY.INTL, NETWORKDAYS.INTL, DATEDIF
