---
name: vba-file-io
description: >-
  File and folder I/O: FileSystemObject (CreateTextFile/OpenTextFile/ReadAll), native Open/Print/Input, Dir loop over files, read/write CSV and text, check file exists, append mode
---

# vba-file-io

Two stacks: **FileSystemObject** (FSO) for object-oriented file work, and the **native `Open`** statement for classic sequential/random I/O. FSO: `Set fso = CreateObject("Scripting.FileSystemObject")`, then `fso.FileExists(path)`, `fso.OpenTextFile(path, ForReading)`, `.ReadAll` (whole file as string) or `.ReadLine` in a loop, and `fso.CreateTextFile(path, True)` then `.WriteLine`. FSO supports UTF via the `Tristate`/format arg in `CreateTextFile`/`OpenTextFile`.

Expert moves: native I/O is fastest for big text — `Dim f As Integer: f = FreeFile: Open path For Output As #f` (overwrite) or `For Append` (add), then `Print #f, line` (Print adds formatting/newline) vs `Write #f, ...` (adds quotes/commas for re-readable data). Read with `Open path For Input As #f` and `Line Input #f, lineVar` until `EOF(f)`. **Always `Close #f`** (or `Close` for all) in cleanup. Loop a folder: `fname = Dir(folder & "\*.csv")` then `Do While fname <> "": ... fname = Dir(): Loop` (call `Dir()` with no args to continue).

Pitfalls: `FreeFile` gives the next free handle — capture it; don't hardcode `#1`. Forgetting `Close` locks the file. CSV parsing via `Split(line, ",")` breaks on quoted commas — use a real parser or `Workbooks.Open` for messy CSVs. `Dir` is stateful and not reentrant — don't nest two `Dir` loops. FSO needs the Scripting Runtime (present on Windows; absent/limited on Mac Excel).

**Tools:** FileSystemObject, CreateObject Scripting.FileSystemObject, OpenTextFile, ReadAll, Open For Output/Append/Input, Print #, Line Input, Dir, FreeFile
