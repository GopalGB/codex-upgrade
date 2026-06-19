---
name: papps-dataverse-tables-relationships
description: >-
  Dataverse data modeling: tables, columns/types, primary name, choice/lookup columns, 1:N/N:N relationships, and querying related rows in Power Fx.
---

# papps-dataverse-tables-relationships

Dataverse is the relational backbone: define **tables** (with a Primary Name column), typed **columns** (Text, Number, Choice = local option set, Choices = global, Lookup = FK to another table, Currency, Date). Model **relationships**: 1:N (one Account has many Contacts — adds a Lookup on the N side), N:N (many-to-many via an intersect table). In Power Fx, traverse relationships directly: `ThisItem.Customer.Name` (read parent across a lookup), `LookUp(Accounts, Name="Acme").'Contacts'` or `Filter(Contacts, Account.Name="Acme")` for children. Set a lookup by assigning the related record (see patch skill). Use **alternate keys** for upserts/dedupe by business key. `Relate()`/`Unrelate()` manage N:N links. Security rides on tables (security roles, row-level ownership) — a reason to choose Dataverse over SharePoint. Pitfalls: over-normalizing tiny lookups that hurt delegation; choice (local) vs choices (global) confusion when reusing option sets across tables; N:N when a real intersect table with extra columns was needed; expanding related records in a gallery causing many calls — shape the query or use views. Schema/logical names differ from display names — scripts/Patch use logical names.

**Tools:** Dataverse, lookup column, choice/choices, 1:N & N:N relationships, alternate keys, Relate/Unrelate
