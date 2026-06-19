---
name: xls-regex-functions
description: >-
  Native REGEXTEST/REGEXEXTRACT/REGEXREPLACE in Excel 365, capture groups, validation, extraction, cleaning with regular expressions
---

# xls-regex-functions

Excel 365 has native regex (rolled out 2024-25, GA 2026) using the PCRE-style ICU engine. **REGEXTEST(text,pattern,[case])** returns TRUE/FALSE — perfect for Data Validation (e.g. validate email/phone). **REGEXEXTRACT(text,pattern,[return_mode],[case])**: return_mode 0=first match, 1=all matches (spills), 2=capture groups. Extract a phone area code with a capture group: `=REGEXEXTRACT(A1,"\((\d{3})\)",2)`. **REGEXREPLACE(text,pattern,replacement,[occurrence],[case])** is a far stronger SUBSTITUTE — use `$1`,`$2` for backreferences, e.g. reformat dates: `=REGEXREPLACE(A1,"(\d{4})-(\d{2})-(\d{2})","$3/$2/$1")`. Common patterns: `\d` digit, `\w` word char, `\s` space, `+`/`*`/`?` quantifiers, `^`/`$` anchors, `[A-Z]` class, `|` alternation. Pitfall: Excel uses ICU regex, NOT .NET/JS — lookbehind support and some constructs differ; backslashes in formulas don't need doubling but watch quotes. For multi-step cleaning on large data, Power Query's Text.RegexReplace (M, 2024+) or replace steps are better than volatile sheet formulas.

**Tools:** REGEXTEST, REGEXEXTRACT, REGEXREPLACE
