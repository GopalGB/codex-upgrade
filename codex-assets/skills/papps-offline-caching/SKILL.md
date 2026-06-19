---
name: papps-offline-caching
description: >-
  Offline canvas apps: SaveData/LoadData local cache, Connection.Connected detection, queue-and-sync writes, and the new offline-first capabilities/limits.
---

# papps-offline-caching

Classic offline pattern: cache data to the device with `SaveData(colData, "localData")` and restore on launch with `LoadData(colData, "localData", true)` (the true = ignore-if-missing). Detect state with `Connection.Connected` (and `Connection.Metered`): when online, ClearCollect from the source and SaveData; when offline, read the cached collection. Queue writes made offline into a separate collection (e.g. colPending), then on reconnect ForAll-Patch them to the source and clear the queue, handling conflicts/errors. SaveData has size limits and only runs on the mobile player (not web). The modern approach is the built-in **offline-first capability** (offline profiles) for canvas apps backed by Dataverse — it auto-syncs defined tables and handles conflict resolution declaratively, far more robust than manual SaveData; check current GA status and the supported-source/feature limits before committing. Pitfalls: assuming SaveData works in the browser (it doesn't — mobile only); not handling sync conflicts (last-write-wins can lose edits); caching huge collections (device limits, slow LoadData); trusting `Connection.Connected` as instantaneous (it can lag — also wrap writes in IfError); storing sensitive data unencrypted in local cache.

**Tools:** SaveData, LoadData, Clear, Connection.Connected, ClearCollect, Patch, offline profiles
