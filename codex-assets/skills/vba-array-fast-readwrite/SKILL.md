---
name: vba-array-fast-readwrite
description: >-
  Read a whole range into a Variant array, process in memory, write back in one shot — the order-of-magnitude speedup that avoids slow cell-by-cell loops; LBound/UBound, Transpose
---

# vba-array-fast-readwrite

The single biggest VBA performance win: **never loop cell-by-cell on a worksheet**. Each `.Value` read/write crosses the VBA↔Excel boundary (~milliseconds each); 100k touches = minutes. Instead read once: `Dim data As Variant: data = ws.Range("A2:D100000").Value` — this returns a 1-based 2-D array `data(row, col)`. Process entirely in memory, then write back in one shot: `ws.Range("A2:D100000").Value = data`. This is typically 100–1000× faster.

Expert moves: the array is **always 1-based** from a range, dimension 1 = rows, dimension 2 = columns. Loop with `For i = LBound(data,1) To UBound(data,1)`. A single column read still comes back 2-D — `data(i, 1)`. Build a results array of the same shape, fill it, write it. For a 1-D array into a column, use `Application.Transpose(arr)`; note Transpose has a ~65,536-element limit and chokes on errors/nulls — for big data, build a 2-D array directly. `ReDim Preserve` can only grow the **last** dimension.

Pitfalls: a single-cell range returns a scalar, not an array — `If IsArray(rng.Value)` guards it. Writing back changes the destination size to match the array, so sizes must align. Mixed-type cells come in as `Variant` subtypes; check `IsError(data(i,j))` for cells holding `#N/A`. Date cells return as `Date`, currency as `Double` — formatting is lost (it lives on the cell, not the value).

**Tools:** Variant array, Range.Value, LBound, UBound, Application.Transpose, ReDim Preserve
