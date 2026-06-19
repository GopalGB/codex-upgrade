---
name: research-reproducibility-preregistration
description: >-
  Make a study reproducible and preregister it: protocol/analysis plan, OSF/AsPredicted, registered reports, computational repro (seeds, envs, data/code sharing), confirmatory vs exploratory — use before data collection
---

# research-reproducibility-preregistration

**Preregister** the hypotheses, design, sample size + stopping rule, exclusion criteria, and the EXACT analysis (which test, which covariates, how outliers handled) BEFORE seeing data — timestamp it on OSF or AsPredicted. This converts p-values from p-hacked to confirmatory. Anything not preregistered must be labeled **exploratory** when you write up; the line between the two is the integrity line. For the strongest form, submit a **registered report** (peer-reviewed and accepted on the protocol, before results exist — kills publication bias).

For **computational reproducibility**, ship more than results: version-control code with Git, pin the environment (conda `environment.yml` / Docker / `renv`), set and record RNG **seeds**, and share data + a **data dictionary** under FAIR principles (Findable, Accessible, Interoperable, Reusable) with a license. A stranger should reproduce your numbers from your repo and a README of run steps.

Pitfall: HARKing — Hypothesizing After Results are Known, then presenting it as a priori. Preregistration is what prevents it. Second pitfall: "available on request" data that never materializes — deposit it in a repository (Zenodo/OSF/Dryad) with a DOI now.

**Tools:** OSF, AsPredicted, registered reports, Git, Docker/conda envs, RNG seeds, README/data dictionary, FAIR data
