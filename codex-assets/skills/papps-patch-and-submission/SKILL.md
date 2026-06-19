---
name: papps-patch-and-submission
description: >-
  Writing data with Patch: create vs update, Defaults(), patching relationships/lookups & choices, ForAll+Patch bulk writes, error handling on writes.
---

# papps-patch-and-submission

`Patch(Source, baseRecord, changes)` is the write primitive. **Create**: `Patch(Orders, Defaults(Orders), {Title:"X", Amount:10})` — Defaults() seeds a new blank record. **Update**: `Patch(Orders, LookUp(Orders, ID=123), {Status:"Done"})` — pass the existing record as the base. Capture the result (`Set(gblNew, Patch(...))`) to get the server-assigned ID/autonumber. **Dataverse lookups/relationships**: set a related record, not a string — `Patch(Orders, Defaults(Orders), {Customer: LookUp(Accounts, Name="Acme")})`; for choices set the option set value. **Bulk**: `Patch(Source, ForAll(colEdits, {...}))` (table form) is far faster than `ForAll(colEdits, Patch(...))` which fires one network call per row. Always wrap writes: `IfError(Patch(...), Notify("Save failed",Error))` and check `Errors(Source, record)`. Forms: prefer `SubmitForm` for single-record edits (free validation/required/concurrency). Pitfalls: ForAll-with-inner-Patch on 500 rows = 500 round-trips and timeouts; patching a lookup with a text value (silently fails or errors); forgetting Defaults() so an 'update' accidentally creates; not handling the offline/save-conflict error path.

**Tools:** Patch, Defaults, ForAll, SubmitForm, LookUp, AsType, Notify, IfError
