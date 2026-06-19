---
name: vba-ado-sql
description: >-
  Query databases from VBA with ADO — Connection/Recordset, SQL SELECT/INSERT, parameterized commands to stop SQL injection, CopyFromRecordset to dump to a sheet, connection strings
---

# vba-ado-sql

ADO connects VBA to SQL Server, Access, Oracle, MySQL, even Excel files. `Set cn = CreateObject("ADODB.Connection")`, `cn.Open connString`, then `Set rs = cn.Execute(sql)` or use a `Recordset` for cursor control. Dump results to a sheet in one shot: `ws.Range("A2").CopyFromRecordset rs` (write headers separately from `rs.Fields(i).Name`). Connection strings come from connectionstrings.com — SQL Server e.g. `Provider=MSOLEDBSQL;Server=...;Database=...;Trusted_Connection=yes;`.

Expert moves: **always parameterize** to prevent SQL injection and type issues — use `ADODB.Command` with `.CreateParameter` and `cmd.Parameters.Append`, never string-concatenate user input into SQL. Set `rs.CursorLocation = adUseClient` for disconnected recordsets and accurate `RecordCount`. Open once, run many queries, then close. For writes, `cn.Execute "INSERT ...", , adExecuteNoRecords` skips building a recordset (faster). Wrap multi-statement writes in `cn.BeginTrans` / `cn.CommitTrans` / `cn.RollbackTrans`.

Pitfalls: forgetting `rs.Close` / `cn.Close` and `Set ... = Nothing` leaks connections and exhausts the pool. `CopyFromRecordset` writes data only — it ignores the field names, so add headers yourself. `RecordCount` returns -1 with a forward-only/server cursor. Driver mismatch (32- vs 64-bit Office) is the classic 'provider not registered' error — match the ACE/OLEDB bitness to Office. Date/locale formatting in literal SQL bites; use parameters.

**Tools:** ADODB.Connection, ADODB.Recordset, ADODB.Command, CopyFromRecordset, parameterized query, connection string, Microsoft ActiveX Data Objects
