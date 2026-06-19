---
name: pbi-deployment-pipelines
description: >-
  Promote content across Dev/Test/Prod workspaces with deployment pipelines, parameter rules, and workspace governance
---

# pbi-deployment-pipelines

Deployment pipelines give a Dev > Test > Prod promotion flow for Power BI/Fabric content. Assign a workspace to each of the three stages, then deploy forward stage-to-stage; the pipeline compares content and shows what changed. Critical: use deployment rules so promoting doesn't carry Dev connections into Prod — set data source rules (swap a Dev SQL server for the Prod server) and parameter rules (change a Power Query parameter value per stage) on the dataset in each target stage. This keeps one artifact moving while each environment points at its own data. Pair with branch-based dev: developers build in feature workspaces or Git-integrated workspaces (Fabric Git integration syncs PBIP/TMDL to a repo) and merge before promotion. Pitfall #1: forgetting data source/parameter rules means Prod ends up querying Dev data after a deploy — set rules once per stage. Pitfall #2: pipelines require Premium/PPU/Fabric capacity on the workspaces. Pitfall #3: deploying a report without its dataset (or vice versa) breaks the binding — deploy together or ensure the dataset exists in the target. Pitfall #4: incremental refresh policies and RLS role memberships don't always travel — re-verify RLS assignments in Prod. Pitfall #5: manual changes made directly in Prod create drift the pipeline will flag/overwrite; treat Prod as deploy-only.

**Tools:** Deployment pipelines, workspaces, dataset rules, parameter rules, Premium/Fabric capacity
