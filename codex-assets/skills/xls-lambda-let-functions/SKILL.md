---
name: xls-lambda-let-functions
description: >-
  LET for naming intermediate calcs, LAMBDA custom functions, recursion, and BYROW/BYCOL/MAP/REDUCE/SCAN helper functions
---

# xls-lambda-let-functions

**LET** names sub-expressions so you compute once and read clearly: `=LET(x,FILTER(...), avg,AVERAGE(x), IF(avg>0,avg,0))` — faster (no recomputation) and self-documenting. Pairs are name,value,name,value,…,final_expression. **LAMBDA** defines reusable functions: write `=LAMBDA(rate,nper,pv, pv*rate/(1-(1+rate)^-nper))` then save it via Name Manager (e.g. `PMT2`) to call `=PMT2(...)` anywhere. **Recursion**: a named LAMBDA can call itself (base case + recursive case) — used for parsing/splitting. **Iteration helpers** avoid recursion: `BYROW(rng,LAMBDA(r,SUM(r)))` collapses each row to one value; `MAP(a,b,LAMBDA(x,y,x*y))` is element-wise; `REDUCE(0,rng,LAMBDA(acc,v,acc+v))` folds to a scalar; `SCAN` returns running totals. Pitfall: BYROW/BYCOL's LAMBDA must return a single value (not an array) or you get `#CALC!`. Use **MAKEARRAY(r,c,LAMBDA(i,j,...))** to build a grid from row/col indices. Define LAMBDAs in Name Manager for workbook-wide reuse, or use Excel Labs' Advanced Formula Environment for editing.

**Tools:** LET, LAMBDA, BYROW, BYCOL, MAP, REDUCE, SCAN, MAKEARRAY
