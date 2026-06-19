---
name: pbi-row-level-security
description: >-
  Implement RLS with DAX filter roles, dynamic USERPRINCIPALNAME security, and propagation across the star schema
---

# pbi-row-level-security

Row-level security restricts which rows a user sees. In Power BI Desktop: Modeling > Manage roles > create a role > add a DAX filter on a dimension table, e.g. on Geography: `[Region] = "West"`. Static roles hardcode values; dynamic RLS scales to thousands of users with one role: filter a Users/security table by `[Email] = USERPRINCIPALNAME()`, and let the relationship propagate the filter down to the fact. For a security mapping table use `[UserEmail] = USERPRINCIPALNAME()` then ensure a relationship from the security dimension flows to facts (may need bi-directional or a bridge). Test with Modeling > View as > pick role/other user. Assign members to roles in the Service (semantic model > Security). Pitfall #1: RLS filters a dimension but won't reach the fact unless cross-filtering propagates — verify the relationship direction; a one-way relationship from a security table to a dimension that doesn't reach the fact leaves data unfiltered. Pitfall #2: USERPRINCIPALNAME in Desktop returns your own UPN — always test via 'View as'. Pitfall #3: measures that use ALL/REMOVEFILTERS can bypass RLS visually for totals — RLS still secures rows, but design totals carefully. Pitfall #4: RLS roles do nothing until users are assigned in the Service; admins/members with workspace edit access bypass RLS.

**Tools:** USERPRINCIPALNAME, USERNAME, LOOKUPVALUE, RLS roles, Manage roles
