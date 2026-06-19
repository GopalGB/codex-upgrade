---
name: xls-text-functions-split
description: >-
  TEXTSPLIT/TEXTJOIN/TEXTBEFORE/TEXTAFTER, LEFT/MID/RIGHT, SUBSTITUTE/TRIM/CLEAN, parsing and concatenating text
---

# xls-text-functions-split

Modern parsing beats nested LEFT/MID/FIND. **TEXTSPLIT** spills text into columns/rows by delimiter: `=TEXTSPLIT(A1,",")` (cols), add row-delimiter as 2nd arg, `[ignore_empty]=TRUE` to collapse repeats, `[pad_with]` to fill ragged rows. **TEXTBEFORE/TEXTAFTER** grab a token by delimiter and instance: `=TEXTBEFORE(email,"@")`, `=TEXTAFTER(path,"\\",-1)` (negative = count from end). **TEXTJOIN(delim, ignore_empty, range)** concatenates with a separator and skips blanks — far better than CONCATENATE/`&`. Cleanup: **TRIM** removes extra spaces (not non-breaking `CHAR(160)` — strip those with `SUBSTITUTE(x,CHAR(160)," ")`), **CLEAN** removes non-printables. **SUBSTITUTE(text,old,new,[n])** replaces the nth occurrence; **REPLACE** works by position. For padding/format use **TEXT(value,"0000")**. Pitfall: LEFT/RIGHT return TEXT — wrap in VALUE for math. For pattern extraction, prefer REGEXEXTRACT (see regex skill) over deep TEXTBEFORE chains.

**Tools:** TEXTSPLIT, TEXTJOIN, TEXTBEFORE, TEXTAFTER, SUBSTITUTE, TRIM, CONCAT
