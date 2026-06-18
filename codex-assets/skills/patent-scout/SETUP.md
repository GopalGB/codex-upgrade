# patent-scout / research free-key setup (priority order)

All optional — the academic path (research-scout) is keyless. These unlock more
power when your environment allows signup. Set each as an env var.

| # | Source | Unlocks | Signup | Wait | Env var |
|---|--------|---------|--------|------|---------|
| 1 | **USPTO ODP** | US patent search (primary) | https://data.uspto.gov → Getting Started | ~minutes (USPTO.gov sign-in req. from 2026-06-18) | `USPTO_ODP_API_KEY` |
| 2 | Semantic Scholar key | off the shared anon pool (higher limits) | https://www.semanticscholar.org/product/api (request form) | ~1 day | `S2_API_KEY` |
| 3 | EPO OPS | EP/worldwide patents + legal status | https://developers.epo.org (OAuth app → token) | ~minutes | (OAuth — see EPO docs) |
| 4 | Lens.org token | combined scholarly + patent landscape | https://www.lens.org (service request, academic) | manual approval | (bearer token) |
| 5 | OpenAlex key | non-demo OpenAlex ($1/day free tier) | https://openalex.org | ~minutes | `OPENALEX_API_KEY` |
| — | (etiquette) | Crossref/OpenAlex polite pool (~10x faster) | just your email | instant | `CODEX_RESEARCH_MAILTO` |

## Verified facts (June 2026 — do not trust older guides)
- **PatentsView `search.patentsview.org` is DEAD** (retired 2026-03-20). Old keys
  do not work on ODP. Build against `https://api.uspto.gov` only.
- **OpenAlex is key-gated since 2026-02-13**; keyless calls are demo-only.
- **Google Patents has no official API**; only unofficial XHR (ToS risk) — not used
  as a primary source here.
- **Semantic Scholar, Crossref, arXiv remain keyless** (with rate limits).
