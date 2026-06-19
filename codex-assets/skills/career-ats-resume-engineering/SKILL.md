---
name: career-ats-resume-engineering
description: >-
  Build an ATS-parseable, recruiter-skimmable engineer resume with quantified impact bullets — use when writing or rewriting a resume for online applications.
---

# career-ats-resume-engineering

ATS systems (Workday, Greenhouse, Lever, iCIMS) parse text, not graphics. **Single-column, standard fonts, no tables/columns/text-boxes/headers-footers, no icons.** Save as .docx or text-layer PDF; section headers must be literal (`Experience`, `Education`, `Skills`). The screen is two-stage: keyword match, then a 6–8 second human skim. Mirror the JD's exact noun phrases (`Kubernetes`, `distributed systems`, `PyTorch`) — ATS does fuzzy-but-imperfect synonym matching, so use the literal tokens from the posting.

Every bullet = **XYZ: Accomplished X, measured by Y, by doing Z.** Lead with a strong past-tense verb (Architected, Shipped, Cut, Scaled), then a metric. `Cut p99 API latency 380ms→90ms by adding Redis read-through cache, serving 2M req/day.` No metric = no bullet; estimate if needed (% faster, $ saved, users, QPS, dataset size).

**What top candidates do differently:** tailor per-role (3–5 reordered/reworded bullets), front-load the top third with the most relevant role, and quantify *outcome* not *activity*. **Common mistake:** a 'Responsibilities' list ('Responsible for backend services') — duties not results — plus skill bars and a 2-page resume for sub-8-years experience. Run Jobscan/Teal to hit 75%+ keyword match before submitting.

**Tools:** XYZ bullet formula, single-column layout, JD keyword mirroring, Jobscan/Teal
