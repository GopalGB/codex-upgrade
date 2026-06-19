---
name: pbi-gateways-refresh
description: >-
  Configure on-prem data gateways, scheduled and incremental refresh, and diagnose refresh failures and timeouts
---

# pbi-gateways-refresh

The on-premises data gateway bridges cloud Power BI to on-prem/VNet data sources for both scheduled refresh and DirectQuery. Install the standard (enterprise) gateway, register data sources in the Service (Settings > Manage connections and gateways) with stored credentials, and bind each dataset to a gateway connection whose source paths exactly match those in Power Query (a mismatched server/database name leaves the dataset unable to map). Set scheduled refresh (up to 8/day Pro, 48/day Premium) in dataset Settings. For large tables use incremental refresh: define `RangeStart`/`RangeEnd` datetime parameters in Power Query, filter the source on them (folding to SQL), then in the model set the incremental policy (archive N years, refresh last M days) — only recent partitions reload, dramatically faster, and it enables larger datasets. Pitfall #1: gateway source definition must character-match the M source (case/whitespace/server alias) or you get 'unable to find gateway' / cannot bind. Pitfall #2: incremental refresh requires query folding on the RangeStart/RangeEnd filter — if folding breaks, every refresh pulls everything. Pitfall #3: RangeStart/RangeEnd must be Date/Time type and used as a filter, not edited to literal values. Pitfall #4: a single gateway node is a SPOF — cluster gateways for HA. Pitfall #5: refresh timeouts (2h Pro / 5h Premium) and credential expiry are top failure causes — monitor refresh history and rotate creds.

**Tools:** On-premises data gateway, scheduled refresh, incremental refresh, RangeStart/RangeEnd
