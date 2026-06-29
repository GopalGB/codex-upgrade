# Codex Upgrade — Skill Library Index (382 skills)

> Codex auto-triggers by description; no command needed. Disable a pack: `rm -rf ~/.codex/skills/<prefix>-*`.


## Core experts (core-*) — 19

- **agent-builder** — Build PRODUCTION agentic systems — design for the failure path, eval + observe from
- **claude-review** — Get an independent Claude Opus 4.8 code review of the current git diff — the
- **data-engineer** — Modern data engineering — idempotent ELT, no-OOM big-data, schema contracts, lineage,
- **deck-smith** — Read and GENERATE PowerPoint (.pptx) decks without MCP, via python-pptx. Use
- **doc-forge** — Word/DOCX, universal document conversion, and OCR for SCANNED PDFs (patents,
- **expert-hire** — Meta-skill: when a task needs expertise the current skills do not cover, FIND
- **ml-engineer** — Deep, end-to-end ML / AI engineering — data → train/fine-tune → eval → quantize →
- **patent-scout** — Search US patents and do prior-art sweeps without MCP. Primary source is the
- **pdf-extract** — Extract text, tables, and LLM-ready markdown from PDF files without MCP. Use
- **ponytail** — Minimalism / "the best code is the code you never wrote": the YAGNI→reuse→stdlib→native→existing-dep→one-line decision ladder — ship the shortest correct diff, no speculative abstractions. Use on every build/edit.
- **py-pro** — Expert Python engineering discipline for production-grade code - structure,
- **rag-engineer** — Retrieval-Augmented Generation done RIGHT — hybrid search + reranking + real eval,
- **research-expert** — Deep research METHODOLOGY (decompose → multi-source → triangulate → adversarially
- **research-scout** — Literature and prior-art research from FREE, keyless APIs (arXiv, OpenAlex,
- **security-auditor** — Run the security gate — secret scanning, SAST, and dependency-vuln audit — using
- **swarm** — Fan ONE task across multiple expert lenses IN PARALLEL — a swarm of isolated
- **toolbelt** — Reach for FAST CLI tools first instead of writing slow Python/grep one-offs. The
- **ui-ux-engineer** — Distinctive, production-grade, taste-driven UI/UX engineering — the OPPOSITE of
- **xlsx-wrangler** — Read, inspect, transform, and export large Excel (.xlsx) files WITHOUT loading

## GSD methodology (gsd-*) (gsd-*) — 12

- **gsd-code-review** — Review the source changed during a phase for bugs, security, and quality — runs claude-review (Opus 4.8) + security-auditor, resolves blockers. Use at the verify gate.
- **gsd-debug** — Systematic debugging with persistent state across context resets — hypothesis-driven, one change at a time, logged to .planning/debug/. Use for any non-trivial bug.
- **gsd-discuss** — Gather phase context through adaptive questioning before planning — surface assumptions, constraints, and unknowns. Use between spec and plan.
- **gsd-execute-phase** — Execute a phase plan ONE step at a time with checkpoints — change, run the exact tests, self-heal on red, mark done. Parallelize independent steps via swarm. Use after plan approval.
- **gsd-extract-learnings** — After a phase, extract decisions, lessons, patterns, and surprises into LESSONS.md / .planning so the next phase compounds. Use after ship.
- **gsd-map-codebase** — Map an unfamiliar codebase before changing it — parallel reader passes (swarm) into .planning/codebase/ docs: architecture, key modules, conventions, risks. Use when joining a repo.
- **gsd-new-project** — Initialize a project the GSD way — deep context gathering into .planning/PROJECT.md (goal, users, constraints, stack, success criteria) before any build.
- **gsd-plan-phase** — Create a detailed, verifiable phase plan in .planning/PLAN.md — 3-7 phased steps, each with a success criterion, files affected, out-of-scope, security step. Use before executing.
- **gsd-progress** — The situational GSD command — 'where am I, what's next?' Reads .planning/ state and advises the next GSD step (or dispatches a freeform intent to the right phase). Use anytime you're unsure.
- **gsd-ship** — Ship after verification — branch, commit (Conventional Commits), run the security/secret gate, open a PR, prep for merge. Use only after verify + review pass.
- **gsd-spec** — Clarify WHAT a phase delivers, with ambiguity scoring, into .planning/SPEC.md — the contract before planning. Use before plan-phase on non-trivial work.
- **gsd-verify** — Goal-backward verification + conversational UAT — re-read the SPEC criteria, run the FULL suite, confirm each criterion actually passes, get Claude Opus review. Use before ship.

## Agent discipline (craft-*) — 16

- **craft-tdd-red-green** — Drive code test-first with RED→GREEN→REFACTOR — failing test first, watch it fail for the right reason, minimum code to pass, refactor under green; tests written after the fact are grounds to redo.
- **craft-small-surgical-diffs** — Make the smallest on-topic change — no drive-by reformatting, renames, or unrelated refactors; keep diffs reviewable and bisectable, refactors in their own commit.
- **craft-verify-before-done** — Never claim done or 'should work' without running it — build, test, exercise the real path end-to-end, read the output; name whatever is left unverified.
- **craft-no-hallucinated-apis** — Never invent functions, flags, config keys, or packages — verify every symbol exists in the installed version before using it; the #1 LLM coding failure.
- **craft-read-before-edit** — Read the file and its neighbors before editing — match existing naming, imports, error style, and tests so the change is indistinguishable from the surrounding code.
- **craft-fail-loud-no-swallow** — Never swallow errors — no bare except / empty catch; handle, re-raise, or log-and-fail; validate at the boundary, catch narrowly, preserve the cause.
- **craft-git-safety-guardrails** — Safe git hygiene — no force-push to shared branches, no committed secrets, branch off main, review the diff before staging, atomic Conventional Commits.
- **craft-handoff-context-notes** — Leave a precise handoff note before stopping — Done / Next / Broken / how-to-run / decisions — so the next session resumes without archaeology.
- **craft-domain-modeling-types** — Model the domain in types so illegal states are unrepresentable — parse don't validate, enums/sum-types over stringly-typed, domain newtypes over primitives.
- **craft-pushback-not-sycophancy** — Disagree when the user is wrong or ambiguous — propose the better path with reasons, no flattery; separate the goal (theirs) from the means (your judgment).
- **craft-research-before-implement** — Read the real docs/source for the installed version before coding against an unfamiliar API — don't pattern-match from stale memory; understand then implement.
- **craft-no-premature-abstraction** — Inline duplication until the rule of three — no framework, generic helper, or config for one caller; a wrong abstraction costs more than the duplication it removes.
- **craft-self-review-diff** — Read your own diff as a hostile reviewer before declaring done — catch debug prints, commented code, TODOs, secrets, off-by-ones, untested branches; then re-verify.
- **craft-vertical-slice-delivery** — Build thin end-to-end slices over big-bang horizontal layers — keep the build green and main runnable at each slice; integrate continuously, slice tasks vertically.
- **craft-comment-why-not-what** — Comment the why (intent, tradeoffs, gotchas), never narrate the what the code already states; match the file's comment density and keep comments in sync.
- **craft-delete-dead-code** — Delete dead code as you go — unreachable branches, unused imports/deps, commented-out blocks — and trust git history instead of 'just in case'; net-negative diffs win.

## Machine learning (ml-*) — 25

- **ml-anomaly-detection** — Detect outliers/novelties/fraud with Isolation Forest, LOF, one-class SVM, and statistical methods under extreme imbalance
- **ml-calibration** — Calibrate predicted probabilities (Platt/isotonic) so outputs match true frequencies for thresholding, ranking, and decisions
- **ml-classification-metrics** — Choose and interpret classification metrics (ROC-AUC, PR-AUC, F1, precision/recall) for the actual business cost
- **ml-cross-validation** — Design leakage-free validation (k-fold, stratified, grouped, time-series) to estimate generalization honestly
- **ml-decision-trees** — Build interpretable single decision trees for non-linear tabular splits and as the base learner for ensembles
- **ml-density-hierarchical-clustering** — DBSCAN/HDBSCAN and hierarchical/agglomerative clustering for arbitrary-shape clusters, outlier detection, and unknown k
- **ml-ensemble-methods** — Combine models via bagging, boosting, stacking, and voting to cut variance/bias and squeeze out final accuracy
- **ml-feature-engineering** — Craft, encode, and transform raw columns into model-ready features — the highest-leverage step in tabular ML
- **ml-feature-selection** — Reduce feature count via filter/wrapper/embedded methods to cut overfitting, speed inference, and improve interpretability
- **ml-gradient-boosting** — Sequential boosted-tree ensembles (XGBoost/LightGBM/CatBoost) — the top performer for structured/tabular data
- **ml-hyperparameter-tuning** — Search hyperparameter spaces efficiently with grid/random/Bayesian/Optuna + early stopping and pruning
- **ml-imbalanced-data** — Handle skewed class distributions (fraud/churn/rare-event) so the minority class is actually learned, not ignored
- **ml-kmeans-clustering** — Partition data into k clusters via k-means for customer segmentation, vector quantization, and unsupervised grouping
- **ml-knn** — k-Nearest Neighbors instance-based classification/regression for local non-parametric patterns and quick baselines
- **ml-linear-regression** — Fit and diagnose linear/OLS regression for continuous targets when relationships are roughly additive and interpretability matters
- **ml-logistic-regression** — Binary/multiclass classification with calibrated probabilities and interpretable log-odds when you need a transparent linear classifier
- **ml-model-interpretability** — Explain model predictions with SHAP, LIME, permutation importance, and PDP/ICE for trust, debugging, and compliance
- **ml-naive-bayes** — Naive Bayes probabilistic classifiers — fast baselines for text/spam and high-dimensional sparse features
- **ml-pca-dimensionality-reduction** — PCA and friends (t-SNE/UMAP) to compress features, remove multicollinearity, denoise, and visualize high-dimensional data
- **ml-random-forest** — Bagged decision-tree ensemble for robust low-tuning tabular classification/regression with built-in variance reduction
- **ml-recommender-systems** — Build recommendations via collaborative filtering, matrix factorization, content-based, and hybrid models with implicit/explicit feedback
- **ml-regression-metrics** — Select and read regression error metrics (RMSE, MAE, MAPE, R²) matched to scale, outliers, and business meaning
- **ml-regularization** — Apply L1/L2/ElasticNet penalties to control overfitting, induce sparsity, and stabilize coefficients in linear and other models
- **ml-svm** — Support Vector Machines for max-margin classification/regression, strong in high-dimensional or small-sample problems with kernel non-linearity
- **ml-time-series-forecasting** — Forecast temporal data with ARIMA/SARIMA, Prophet, ETS, and ML approaches — handling trend, seasonality, and stationarity

## AI / LLM engineering (ai-*) — 24

- **ai-agent-memory** — Give agents memory across turns and sessions: working vs episodic vs semantic memory, summarization buffers, vector recall, and write/forget policies — use when an agent must remember beyond one context window.
- **ai-chain-of-thought** — Elicit step-by-step reasoning for math, logic, and multi-hop tasks via CoT, self-consistency voting, and reasoning-model controls — use when the model rushes to a wrong final answer.
- **ai-chunking-strategies** — Split documents for retrieval without destroying meaning: size/overlap tuning, semantic and structure-aware chunking, and contextual retrieval — use when retrieved chunks are fragmented or context-less.
- **ai-context-window-management** — Fit work into the context window and fight 'lost in the middle' / context rot: budgeting, summarization, retrieval over stuffing, and prompt/cache structuring — use on long docs, chats, or agent loops.
- **ai-cost-latency-optimization** — Cut LLM cost and latency without wrecking quality: model right-sizing, prompt caching, batching, max-token caps, streaming, and distillation — use when bills or p95 latency are too high.
- **ai-embeddings** — Turn text into vectors for semantic search, clustering, and dedup: model choice, dimensions, normalization, cosine similarity, and batching — use when you need meaning-based comparison, not keywords.
- **ai-few-shot-prompting** — Steer format and behavior with in-context examples (k-shot) when zero-shot is inconsistent — covers example selection, ordering, and label balance to avoid majority-label bias.
- **ai-fine-tuning-decision** — Decide IF and HOW to fine-tune (LoRA/QLoRA vs full vs prompt/RAG) and avoid the classic 'fine-tune when you should've RAG'd' mistake — use before committing to a training run.
- **ai-function-tool-calling** — Wire LLMs to external actions via tool/function calling: schema design, the call→execute→result loop, parallel calls, and forced tool choice — use to let a model fetch data or take actions.
- **ai-guardrails-safety** — Add input/output guardrails to an LLM app: content moderation, PII redaction, topic/scope restriction, schema validation, and a fallback chain — use before exposing an LLM to users or untrusted input.
- **ai-hallucination-mitigation** — Reduce confident fabrication: grounding/RAG, citation enforcement, abstention thresholds, chain-of-verification, and self-consistency — use for any factual or high-stakes output.
- **ai-image-generation** — Generate and edit images with diffusion/text-to-image models: prompt structure, negative prompts, img2img/inpainting, control (ControlNet/reference), and seeds — use to create or modify visuals programmatically.
- **ai-llm-as-judge** — Use an LLM to grade outputs reliably: rubric design, pairwise vs pointwise, bias mitigation (position/verbosity/self-preference), and judge calibration — use to scale eval beyond humans.
- **ai-llm-evals** — Build an offline eval harness for LLM systems: golden datasets, deterministic vs model-graded metrics, regression gates in CI — use before shipping any prompt/model change.
- **ai-model-selection-routing** — Pick and route between LLMs by task: capability/cost/latency/context tradeoffs, prompt-based vs learned routers, cascades, and fallback chains — use to match each request to the cheapest model that can do it.
- **ai-multimodal-vision** — Use vision LLMs for image understanding, OCR, document/chart extraction, and grounding: detail/resolution control, multi-image prompts, and structured extraction — use to read images, screenshots, or PDFs.
- **ai-prompt-engineering** — Engineer reliable LLM prompts: role+task+constraints+format scaffolding, delimiter discipline, instruction placement, and iterative refinement — use when output is vague, inconsistent, or ignores constraints.
- **ai-prompt-injection-defense** — Defend LLM apps against prompt injection and tool-misuse: untrusted-content isolation, instruction/data separation, least-privilege tools, and the dual-LLM/two-loop pattern — use whenever the model ingests external content.
- **ai-rag-patterns** — Production RAG beyond naive retrieve-then-stuff: hybrid search, reranking, corrective/self-RAG, and query rewriting — use when naive RAG misses relevant docs or hallucinates over them.
- **ai-semantic-caching** — Cache LLM responses by meaning, not exact string: embedding-similarity lookup, threshold tuning, TTL/invalidation, and the false-hit risk — use to cut cost/latency on repetitive or paraphrased queries.
- **ai-speech-stt-tts** — Add speech to LLM apps — transcription (Whisper/STT), text-to-speech, streaming, diarization, and latency budgeting for voice agents — use to build voice interfaces or process audio.
- **ai-streaming-responses** — Stream LLM output token-by-token for low perceived latency: SSE handling, partial-JSON/tool-call streaming, backpressure, and clean cancellation — use for any interactive or long-output UI.
- **ai-structured-output** — Force valid JSON/typed output via JSON Schema, constrained decoding, and Pydantic validation — use whenever an LLM output feeds code instead of a human.
- **ai-vector-search** — Build and query a vector index for similarity search: ANN algorithms (HNSW/IVF), distance metrics, metadata filtering, and recall tuning — use to retrieve nearest neighbors at scale.

## Building agentic software (agentic-*) — 18

- **agentic-agent-vs-workflow** — Choose a deterministic workflow vs an autonomous agent — predictability/cost/testability vs flexibility; start simplest, add agency only when the steps can't be predicted.
- **agentic-prompt-chaining** — Decompose into a fixed sequence of LLM calls with programmatic gates between steps; trade latency for per-step accuracy — the simplest reliable workflow.
- **agentic-routing** — Classify the input and dispatch to a specialized prompt/model/handler; separation of concerns + cost tiering, with an explicit 'other/unsure' default.
- **agentic-parallelization** — Run subtasks concurrently — sectioning (independent parts) or voting (same task N times, aggregate) — to cut wall-clock latency or raise confidence/coverage.
- **agentic-orchestrator-workers** — A lead agent decomposes a task at runtime, dispatches to worker sub-agents in isolated contexts, and synthesizes — for open-ended work whose subtasks you can't predict.
- **agentic-evaluator-optimizer** — Loop a generator and an evaluator — produce, critique against grounded criteria, refine until it passes — bounded by a max-iteration cap; use real checks over LLM-judge.
- **agentic-subagent-design** — Design focused sub-agents: single responsibility, explicit input/output contract, isolated context, least-privilege tools, distilled structured returns.
- **agentic-tool-design** — Design the agent-computer interface (ACI): clear names/types/descriptions, poka-yoke, structured actionable errors, right-sized outputs; test with agent-shaped inputs.
- **agentic-skill-authoring** — Write effective skills/instructions: description as the trigger signal, progressive disclosure, one capability per skill, concrete imperative how-to.
- **agentic-context-engineering** — Treat context as a finite, degrading budget: just-in-time retrieval over stuffing, compaction, external memory, sub-agent isolation; fight context rot.
- **agentic-state-durability** — Make long runs durable: checkpoint to external storage, idempotent resumable steps, idempotency keys for side effects; test the kill-and-resume path.
- **agentic-human-in-the-loop** — Gate consequential/irreversible actions behind approval, escalate on uncertainty, present a tight decision surface; pair with durable pause/resume.
- **agentic-mcp-tools-integration** — Connect agents to tools/data via MCP (servers exposing tools/resources/prompts over stdio/HTTP); reuse existing servers, build custom for your own systems, treat as a security boundary.
- **agentic-failure-recovery** — Resilient loops: retry+backoff on idempotent transients, fallback chains, error-reflection, bounded iterations/cost, fail loud into the trace.
- **agentic-eval-and-tracing** — Evaluate agents on end-state + trajectory, trace runs as spans (calls/tools/tokens/latency), gate changes behind a CI regression eval.
- **agentic-cost-budgeting** — Control cost/latency: per-role model routing, sub-agent token budgets, prompt-cache the stable prefix, trim outputs, cost-per-task as a first-class metric.
- **agentic-permissions-least-privilege** — Scope agents to least-privilege tools, sandbox execution, isolate untrusted content (prompt-injection), confirm destructive actions, scoped short-lived creds.
- **agentic-app-architecture** — Architect an agentic app end-to-end: core loop (context→act→verify), decoupled model/tool/state/orchestration layers, observability + eval-gate + guardrails from day one.

## Software eng + system design (sde-*) — 29

- **sde-api-design-rest-grpc-graphql** — Pick and design the right API style - resource-oriented REST, contract-first gRPC, client-shaped GraphQL - with versioning and errors.
- **sde-async-event-loops** — Master non-blocking I/O - the single-threaded event loop, async/await, futures, and not blocking the loop with CPU work.
- **sde-back-of-envelope-estimation** — Compute QPS, storage, bandwidth, and memory budgets fast to size every component and justify design choices with numbers.
- **sde-caching-strategies** — Apply cache-aside, write-through, write-back, write-around with correct invalidation, TTLs, and stampede protection.
- **sde-cap-pacelc-theorem** — Reason about consistency vs availability under partitions (CAP) and the latency-vs-consistency tradeoff even without them (PACELC).
- **sde-cdn-edge-delivery** — Serve static and cacheable content from edge PoPs - cache headers, TTL, purge, origin shielding, and dynamic edge logic.
- **sde-ci-cd** — Automate build-test-deploy - fast pipeline stages, trunk-based flow, and safe rollout via blue-green/canary with rollback.
- **sde-concurrency-locking** — Write correct concurrent code - races, mutexes, deadlock, optimistic vs pessimistic locking, and lock-free atomics.
- **sde-database-indexing** — Speed reads with B-tree and hash indexes - composite key order, covering indexes, and the write-cost tradeoff.
- **sde-debugging-method** — Debug systematically - reproduce, isolate via bisection/binary search, form and test hypotheses, fix root cause not symptom.
- **sde-design-chat-system** — Design WhatsApp/Messenger - WebSocket connections, message store, online presence, fan-out, ordering, and delivery receipts.
- **sde-design-key-value-store** — Design a distributed KV store like Dynamo - consistent hashing, replication, quorum, vector clocks, gossip, and tunable consistency.
- **sde-design-news-feed** — Design a social feed - fan-out on write vs read, the celebrity hot-key problem, hybrid push/pull, ranking, and feed caching.
- **sde-design-patterns-gof** — Reach for the right Gang-of-Four pattern - factory, strategy, observer, decorator, adapter, singleton - and know when not to.
- **sde-design-rate-limiter-service** — Design a distributed rate-limiter service - algorithm choice, shared Redis counters, atomicity, and where to place it.
- **sde-design-url-shortener** — Design TinyURL/bit.ly - short-key generation (base62, counter, hash), 301 vs 302 redirect, KV store, and read-heavy caching.
- **sde-idempotency** — Make retries safe - idempotency keys, dedup stores, and designing operations that survive at-least-once delivery and client retries.
- **sde-load-balancing** — Distribute traffic across servers - L4 vs L7, algorithms, health checks, and avoiding the LB as a single point of failure.
- **sde-message-queues-event-driven** — Decouple services with queues and logs - Kafka vs RabbitMQ, delivery guarantees, consumer groups, ordering, and backpressure.
- **sde-microservices-vs-monolith** — Choose between modular monolith and microservices - decomposition boundaries, the distributed-systems tax, and the migration path.
- **sde-observability** — Make systems debuggable in prod - structured logs, RED/USE metrics, distributed traces, correlation IDs, and symptom-based alerts.
- **sde-rate-limiting** — Throttle traffic to protect services - token bucket, leaky bucket, sliding window, distributed counters, and 429 semantics.
- **sde-refactoring** — Improve code structure without changing behavior - small safe steps under test coverage, smell-driven, never mixed with features.
- **sde-replication-consistency** — Replicate data for availability and read scale - leader-follower, replication lag, sync vs async, and quorum reads/writes.
- **sde-scalability-horizontal-scaling** — Scale out with stateless services, vertical vs horizontal tradeoffs, and the path from single server to multi-tier fleet.
- **sde-sharding-partitioning** — Split data across nodes by hash, range, or directory - shard-key choice, hot spots, resharding, and cross-shard query pain.
- **sde-solid-principles** — Apply SOLID to keep OO code flexible - single responsibility, open-closed, Liskov, interface segregation, dependency inversion.
- **sde-system-design-method** — Drive any system-design problem through the canonical 5-step flow: requirements, estimation, API, data model, then scale.
- **sde-testing-strategy** — Build the test pyramid - fast unit, focused integration, few e2e - plus TDD red-green-refactor and what to mock at boundaries.

## Power BI (pbi-*) — 23

- **pbi-bookmarks** — Use bookmarks + selection pane + buttons to build navigation, toggles, show/hide states, and guided storytelling
- **pbi-calculate-filter-context** — Master CALCULATE to modify filter context — the single most important DAX function; filter args, removing/keeping filters, context transition
- **pbi-calculation-groups** — Eliminate measure sprawl with calculation groups — apply YTD/PY/YoY/currency logic to any base measure via SELECTEDMEASURE
- **pbi-composite-models** — Combine Import + DirectQuery + DirectQuery-over-PBI-datasets in one composite model; manage storage modes and limited relationships
- **pbi-conditional-formatting** — Apply data-driven colors, data bars, icons, and dynamic formatting via rules or DAX measures on tables, matrices, and visuals
- **pbi-dataflows** — Centralize reusable ETL with Power BI/Fabric dataflows (Gen2) so multiple datasets share cleaned, certified tables
- **pbi-deployment-pipelines** — Promote content across Dev/Test/Prod workspaces with deployment pipelines, parameter rules, and workspace governance
- **pbi-drillthrough-tooltips** — Build drillthrough pages and report-page tooltips to give detail-on-demand without cluttering the main report
- **pbi-gateways-refresh** — Configure on-prem data gateways, scheduled and incremental refresh, and diagnose refresh failures and timeouts
- **pbi-iterators-sumx-averagex** — Row-by-row aggregation with SUMX/AVERAGEX/MAXX when you need per-row math before aggregating, plus context-transition gotchas
- **pbi-kpis-cards-visual-calcs** — Build KPI cards, the KPI visual, and visual calculations (GA May 2026) for running totals/moving averages without new model measures
- **pbi-measures-vs-calc-columns** — Decide measure vs calculated column vs visual calculation; when each stores/computes and why measures win for aggregation
- **pbi-parameters-whatif** — Build what-if scenario analysis with numeric range parameters and field/calculation parameters for dynamic measure/axis switching
- **pbi-performance-vertipaq-aggregations** — Tune model speed: reduce VertiPaq cardinality, use aggregation tables, and profile DAX with Performance Analyzer/DAX Studio
- **pbi-power-query-m-transforms** — Shape and clean data in Power Query M before load — unpivot, merge, type, custom columns, and folding-aware transforms
- **pbi-relationships-cardinality** — Configure relationship cardinality, cross-filter direction, and active/inactive relationships; fix many-to-many and ambiguity
- **pbi-report-design-ux** — Lay out reports for clarity and speed — grid alignment, visual hierarchy, theme JSON, consistent formatting, and fewer-faster visuals
- **pbi-row-level-security** — Implement RLS with DAX filter roles, dynamic USERPRINCIPALNAME security, and propagation across the star schema
- **pbi-star-schema-modeling** — Design a star schema (facts + conformed dimensions) instead of a flat table or snowflake — the foundation of fast, correct Power BI models
- **pbi-storage-modes** — Choose Import vs DirectQuery vs Direct Lake (2026: on-SQL vs on-OneLake) by data size, freshness, and capacity
- **pbi-time-intelligence** — YTD/QTD/MTD, prior-period and YoY comparisons with TOTALYTD, SAMEPERIODLASTYEAR, DATEADD — requires a marked date table
- **pbi-variables-var-return** — Use VAR/RETURN to make DAX readable, avoid recomputation, and dodge the context-capture trap that bites filter-modifying measures
- **pbi-visual-selection** — Pick the right chart for the analytical question — comparison, trend, composition, distribution, relationship — and avoid misleading visuals

## Power Automate (pa-*) — 20

- **pa-ai-builder** — AI Builder in flows: prebuilt + custom document processing, GPT prompts, extract/classify text, sentiment, and credit consumption
- **pa-apply-to-each-loops** — Apply to each, Do until, concurrency control, nested loops, and why loops destroy flow performance (batch instead)
- **pa-approvals** — Approvals connector: Start and wait, approval types (first-to-respond/everyone/custom), parallel approvers, reminders, escalation
- **pa-child-flows** — Reusable child flows via Run a Child Flow, request/respond trigger, passing typed inputs/outputs, solution requirement, sync limits
- **pa-cloud-flow-basics** — Cloud flow anatomy: one trigger -> sequential actions, dynamic content, Peek code/JSON, test and run history, the maker portal
- **pa-conditions-switch** — Condition (if/else branches), nested conditions vs Switch action, multi-criteria AND/OR rows, expression-mode conditions
- **pa-connectors-custom** — Standard vs premium connectors, connection references, and building custom connectors from OpenAPI/Postman with auth + policies
- **pa-dataverse-triggers-actions** — Dataverse connector: When a row is added/modified/deleted (scope/filter), List/Get/Add/Update rows, FetchXML, $expand, @odata.bind
- **pa-desktop-flows-rpa** — Power Automate Desktop RPA: attended vs unattended, machine/gateway, UI/web automation selectors, run from a cloud flow, error handling
- **pa-error-handling-runafter** — Configure run after (failed/skipped/timed out), Scope try/catch/finally pattern, result() for error details, Terminate with status
- **pa-expressions-wdl** — Workflow Definition Language: concat/if/coalesce/formatDateTime, triggerBody()/items(), null-safe ?[] access, type coercion
- **pa-filter-array-odata** — Filter array action (in-memory) vs source-side OData $filter, Select for projection, and pushing filters to the data source
- **pa-http-rest-action** — HTTP premium action for REST: method/headers/body/auth, Parse JSON the response, pagination, and the HTTP-trigger webhook
- **pa-outlook-teams-flows** — Outlook (send/receive/shared mailbox) + Teams (post message, adaptive cards, wait for response) automation patterns
- **pa-pagination** — Pagination settings to fetch beyond default 100/256 limits, threshold caps, skip-token loops, and HTTP @odata.nextLink paging
- **pa-retry-policy-timeout** — Per-action retry policy (default/none/fixed/exponential), action timeout (ISO 8601 duration), and handling 429 throttling
- **pa-sharepoint-flows** — SharePoint flows: item/file triggers, Get items with OData Filter Query, Update item, Send an HTTP request to SharePoint REST, attachments
- **pa-solutions-alm** — Solutions + ALM: environments (dev/test/prod), managed vs unmanaged, connection references, environment variables, pac CLI, pipelines
- **pa-trigger-types** — Automated vs instant vs scheduled triggers, trigger conditions, Split On, concurrency, and the infinite-loop trap
- **pa-variables-vs-compose** — Initialize/Set/Increment/Append variables vs Compose for immutable values; when each wins, scope rules, array-build pitfalls

## Copilot Studio (copilot-*) — 15

- **copilot-actions-flows-connectors** — Add tools/actions to an agent: call a Power Automate flow, a connector action, a prompt, or an MCP server; wire inputs/outputs and handle auth.
- **copilot-agents-overview** — Decide agent type and orchestration mode when starting a new Copilot Studio agent: classic vs generative, declarative M365 vs standalone, autonomous vs conversational.
- **copilot-analytics-transcripts** — Measure agent performance and debug real conversations using the Analytics dashboards, session details, conversation transcripts, and Dataverse/Application Insights export.
- **copilot-authentication-variables** — Configure agent authentication (no auth / Entra ID / manual OAuth) and manage variable scope (topic, global, system) including passing Entra user identity to flows.
- **copilot-channels-teams-web-m365** — Publish an agent to channels: Microsoft Teams, custom website embed, M365 Copilot, SharePoint, Power Pages, Direct Line API, and the right channel for each audience.
- **copilot-content-moderation-guardrails** — Configure content moderation, response controls, and guardrails at agent/topic/prompt level to balance answer coverage against safety and off-topic responses.
- **copilot-conversational-nodes** — Build conversation flow with Message, Question, and Condition nodes including adaptive cards, multiple-choice options, and branching logic in the topic canvas.
- **copilot-entities-slot-filling** — Extract structured values from user input with prebuilt/custom entities and slot-fill required question variables; stop the bot re-asking for info already given.
- **copilot-generative-answers-knowledge** — Ground an agent on enterprise data with generative answers over SharePoint, Dataverse, files, public websites, and connectors; fix 'no answer found' grounding gaps.
- **copilot-generative-vs-classic-orchestration** — Choose and configure classic (topic-routing) vs generative (LLM-planned) orchestration, and migrate an existing classic agent to generative without breaking flows.
- **copilot-human-handoff** — Hand off a conversation to a live human agent with full context via Escalate topic + engagement hub (D365 Omnichannel / Genesys / contact center), or notify in Teams.
- **copilot-m365-declarative-agents** — Build M365 Copilot declarative agents and extensions: instructions, knowledge, capabilities, API/MCP plugins, and ship via Agents Toolkit or Copilot Studio.
- **copilot-publishing-alm** — Publish, version, and move agents across environments using solutions, connection references, and environment variables for proper dev/test/prod ALM.
- **copilot-testing-test-pane** — Test an agent in the Test pane: trace topic/tool routing, inspect variable values, watch generative orchestration steps, and debug why a turn went wrong.
- **copilot-topics-trigger-phrases** — Author classic topics and write trigger phrases / topic descriptions so the orchestrator routes the right conversation path; fix topics that never fire.

## Power Apps (papps-*) — 15

- **papps-canvas-vs-model-driven** — Choose canvas vs model-driven (vs custom pages): pixel UI on any connector vs Dataverse-metadata-driven apps; when each wins and the hybrid.
- **papps-collections-and-variables** — State: global vars (Set), context vars (UpdateContext), collections (ClearCollect/Collect/Patch), scope rules, and the OnStart-vs-named-formula choice.
- **papps-components-libraries** — Reusable components & component libraries: custom + behavior input/output properties, instance vs definition, and sharing across apps for consistency.
- **papps-data-sources-connectors** — Connecting data: standard vs premium connectors, SharePoint/SQL/Dataverse/Excel, implicit vs explicit connections, connection references for ALM.
- **papps-dataverse-tables-relationships** — Dataverse data modeling: tables, columns/types, primary name, choice/lookup columns, 1:N/N:N relationships, and querying related rows in Power Fx.
- **papps-delegation** — THE #1 gotcha: delegation — which functions/operators each data source pushes to the server vs evaluates locally on the 500/2000-row cap, per source.
- **papps-galleries-and-forms** — Galleries (Items, ThisItem, Selected, templates) and Edit/Display/View forms (DataSource, Item, Update, SubmitForm); when to use which.
- **papps-model-driven-forms-views** — Model-driven UI: main forms (tabs/sections/columns), views (columns, filter, sort), and business rules for no-code validation/show-hide logic.
- **papps-offline-caching** — Offline canvas apps: SaveData/LoadData local cache, Connection.Connected detection, queue-and-sync writes, and the new offline-first capabilities/limits.
- **papps-patch-and-submission** — Writing data with Patch: create vs update, Defaults(), patching relationships/lookups & choices, ForAll+Patch bulk writes, error handling on writes.
- **papps-performance-optimization** — Canvas perf: cut OnStart, Concurrent parallel loads, delegate at source, minimize control count & nested galleries, ClearCollect caching, monitor profiling.
- **papps-power-fx-basics** — Power Fx essentials: declarative formulas, behavior vs property formulas, operators, If/Switch, error-handling (IfError/IsError), named formulas.
- **papps-responsive-layout** — Responsive canvas apps: disable fixed-aspect Size/Width, containers (horizontal/vertical/auto-layout), Parent-relative sizing, and breakpoints with App.Width.
- **papps-screens-navigation** — Screens & navigation: Navigate transitions, Back, passing context, Param() deep links, OnVisible/OnHidden, and the single-screen anti-pattern.
- **papps-theming** — Theming canvas apps: central color/font tokens via named formulas/App.Theme, applying to controls, modern controls + theme JSON, and consistency at scale.

## M365 + Graph (m365-*) — 17

- **m365-app-registration-oauth2** — Register an Entra app and choose client-credentials (app-only) vs authorization-code (delegated) flow with correct scopes — when setting up any Graph auth
- **m365-change-notifications-webhooks** — Subscribe to Graph change notifications (webhooks) for mail, lists, drives, and Teams instead of polling — when reacting to M365 changes in near-real-time
- **m365-entra-id-basics** — Manage Entra ID users, groups, roles, and conditional access fundamentals via Graph/PowerShell — when handling identity, licensing, or RBAC
- **m365-excel-graph-api** — Read/write Excel workbook ranges, tables, and formulas via Graph workbook sessions — when automating xlsx in OneDrive/SharePoint without opening the file
- **m365-graph-api-basics** — Call Microsoft Graph REST endpoints (/me, /users, /sites, /drives, /groups) against v1.0 vs beta — when querying any M365 data via HTTP
- **m365-graph-batch-requests** — Combine up to 20 Graph calls into one $batch request to cut round-trips and latency — when issuing many small Graph calls
- **m365-graph-pagination** — Follow @odata.nextLink to page through large Graph collections without losing items or hardcoding skip tokens — when a list returns partial results
- **m365-graph-powershell-sdk** — Administer M365 from the Microsoft Graph PowerShell SDK (Connect-MgGraph, Get-Mg* / New-Mg* cmdlets) — when scripting tenant admin tasks
- **m365-graph-query-params** — Shape Graph responses with $select, $filter, $expand, $orderby, $top, $count and ConsistencyLevel for advanced queries — when a call returns too much or needs server-side filtering
- **m365-graph-throttling-retry** — Handle Graph 429 throttling with Retry-After and exponential backoff so automations survive rate limits — when bulk-calling Graph
- **m365-least-privilege-scopes** — Choose the minimal Graph permission and delegated-vs-application type, then enforce app access policies — when securing any Graph integration
- **m365-office-scripts-automate** — Write Office Scripts (TypeScript) for Excel on the web and trigger them from Power Automate — when automating in-workbook logic with a no-Graph option
- **m365-onedrive-drive-items** — Upload, download, share, and traverse OneDrive/SharePoint files via driveItem endpoints and upload sessions — when moving files programmatically
- **m365-outlook-mail-calendar** — Send mail, read messages, and manage calendar events via Graph — when automating Outlook/Exchange email or scheduling
- **m365-sharepoint-graph-pnp** — Read/write SharePoint Online lists and document libraries via Graph or PnP PowerShell — when automating list items, files, or site provisioning
- **m365-spfx-overview** — Scaffold SharePoint Framework (SPFx) web parts/extensions and call Graph from them via MSGraphClientV3 — when building custom UI inside SharePoint/Teams
- **m365-teams-automation** — Post messages, create channels, and read Teams chats via Graph — when automating Teams notifications or channel management

## PowerPoint (pptx-*) — 20

- **pptx-accessibility** — Make decks accessible: alt text on images/charts, correct reading order, color contrast, table headers, meaningful link text, and the built-in Accessibility Checker
- **pptx-animations-transitions** — Apply tasteful entrance/emphasis/exit animations and slide transitions with the Animation Pane, timing/triggers, and the discipline to not overdo it
- **pptx-data-driven-charts** — Generate charts programmatically from CSV/DataFrame and refresh embedded chart data at scale — batch decks, monthly reporting, parameterized exports
- **pptx-dataviz-on-slides** — Think-cell-style data storytelling: waterfall/bridge, Mekko/marimekko, CAGR arrows, stacked-with-totals, value callouts, and chart decluttering for exec decks
- **pptx-embed-excel-objects** — Embed vs link Excel ranges/objects, paste options (picture/keep-formatting/embed), live-updating linked charts, and managing/breaking links before sending
- **pptx-icons-images-compression** — Insert scalable icons (SVG), source/crop/mask images cleanly, and compress media so the .pptx isn't 80MB — picture format, crop-to-shape, set transparency
- **pptx-master-cleanup-footer** — Clean a bloated deck: remove unused masters/layouts, fix multiple-theme drift, add slide numbers/date/footer correctly (skip on title), and standardize fonts
- **pptx-morph-transition** — Use Morph for smooth object movement/zoom/transform between slides (the keynote-style effect) including name-matching tricks and text morphs
- **pptx-native-charts** — Insert and format native (editable) PowerPoint charts — column/bar/line/combo/waterfall — with clean axes, data labels, and theme colors, not pasted images
- **pptx-pitch-deck-structure** — Architect a persuasive pitch/board deck — narrative arc, one-idea-per-slide, the canonical investor sequence, assertion-evidence titles, and an appendix
- **pptx-reusable-component-library** — Build a reusable asset/component library — slide library, custom layouts, Quick Parts/copies, themed shape defaults, and a starter .potx for consistent decks at scale
- **pptx-sections-organization** — Structure long decks with Sections for navigation, reordering, collapsing, and applying transitions per group; plus Slide Sorter and Zoom navigation
- **pptx-slide-master-layouts** — Build and edit Slide Master + custom layouts (placeholders, inheritance) so every slide is on-grid; fix off-template slides and rogue text boxes
- **pptx-slide-size-export** — Set slide size/aspect ratio (16:9 vs 4:3 vs custom A4), and export to PDF, high-res images, handouts, and MP4 video with the right settings
- **pptx-smartart-diagrams** — Use SmartArt for process/cycle/hierarchy/relationship diagrams, convert bullet lists to SmartArt, and know when to hand-build shapes instead
- **pptx-speaker-notes-presenter** — Write effective speaker notes, set up Presenter View (next-slide, timer, notes), rehearse timings, and export notes pages — without notes ever showing on screen
- **pptx-tables-pro** — Build readable slide tables — banded rows, merged header cells, right-aligned numbers, autofit control — and generate them from data without the default ugly grid
- **pptx-theme-template-build** — Author a reusable .thmx/.potx theme: theme colors (12-slot), theme fonts, effects, and ship a branded template that propagates everywhere
- **pptx-typography-grid-layout** — Slide typography and layout systems — type scale, alignment grids, guides, Align/Distribute, optical spacing, and killing the centered-everything AI-slop look
- **pptx-vba-automation** — Automate PowerPoint with VBA — batch-format slides, find/replace across a deck, export each slide, recolor shapes by theme, loop the object model (Slides/Shapes/TextRange)

## Excel + xlsm (xls-*) — 26

- **xls-array-formulas-legacy** — Legacy CSE array formulas vs modern dynamic arrays, implicit intersection @, array constants, SUMPRODUCT as array engine, migration
- **xls-auditing-trace** — Formula auditing: trace precedents/dependents, evaluate formula, show formulas, error checking, range finder, find broken links and circular refs
- **xls-charts-combo** — Charts and combo charts: dual-axis, secondary axis, sparklines, dynamic chart ranges off spill/Tables, data labels, chart types selection
- **xls-conditional-aggregation** — SUMIFS/COUNTIFS/AVERAGEIFS, SUMPRODUCT for complex multi-criteria math, MAXIFS/MINIFS, wildcard and date-range conditions
- **xls-conditional-formatting** — Conditional formatting: formula-based rules, data bars/color scales/icon sets, highlight duplicates, rule precedence, performance
- **xls-dashboards** — Interactive dashboards: KPI cards, slicers/timelines wiring, dynamic titles, sparklines, camera tool, layout and single-source design
- **xls-data-validation-dropdowns** — Data validation dropdowns (lists), dependent/cascading dropdowns, input/error messages, custom-formula validation, dynamic-array lists
- **xls-date-time** — Date/time math: serial numbers, EDATE/EOMONTH/WORKDAY/NETWORKDAYS, DATEDIF, time fractions, timezone/locale date-parse fixes
- **xls-dynamic-arrays-spill** — Dynamic array spill, FILTER/UNIQUE/SORT/SORTBY/SEQUENCE, spill operator #, #SPILL! errors, single-formula reports
- **xls-error-handling-formulas** — IFERROR vs IFNA, trapping #DIV/0! #N/A #VALUE! #REF! #SPILL! #CALC!, ISERROR/ISNA, error-tolerant lookups and aggregation
- **xls-financial-modelling** — Financial functions and model structure: NPV/XNPV/IRR/XIRR, PMT/IPMT/PPMT, depreciation, amortization schedules, 3-statement linkage best practices
- **xls-groupby-pivotby** — GROUPBY and PIVOTBY dynamic-array aggregation functions — formula-based pivot tables that auto-refresh, with custom LAMBDA aggregators
- **xls-import-export-csv** — CSV/text import and export: encoding (UTF-8 BOM), delimiter and locale traps, leading zeros, date misparse, Power Query vs legacy import
- **xls-lambda-let-functions** — LET for naming intermediate calcs, LAMBDA custom functions, recursion, and BYROW/BYCOL/MAP/REDUCE/SCAN helper functions
- **xls-named-ranges** — Named ranges and named formulas: scope (workbook vs sheet), dynamic names, Name Manager hygiene, using names in formulas and validation
- **xls-performance-large-files** — Large-workbook performance: calculation modes, volatile functions, full-column references, .xlsb format, used-range bloat, calc tree
- **xls-pivot-tables** — PivotTables: build, group dates/numbers, value field settings, % of total / running total, calculated fields, slicers/timelines, GETPIVOTDATA
- **xls-power-pivot-dax** — Power Pivot data model, relationships, DAX measures (CALCULATE/FILTER), row vs filter context, time intelligence, SUMX iterators
- **xls-power-query-transform** — Power Query (Get & Transform): import/clean/reshape data, unpivot, merge/append queries, M language, query folding, refresh
- **xls-protection-security** — Workbook/sheet/cell protection, locked vs unlocked cells, hide formulas, workbook structure lock, password limits, sensitivity labels
- **xls-regex-functions** — Native REGEXTEST/REGEXEXTRACT/REGEXREPLACE in Excel 365, capture groups, validation, extraction, cleaning with regular expressions
- **xls-structured-tables** — Excel Tables (Ctrl+T), structured references, total rows, auto-expand ranges, table-driven formulas and slicers
- **xls-text-functions-split** — TEXTSPLIT/TEXTJOIN/TEXTBEFORE/TEXTAFTER, LEFT/MID/RIGHT, SUBSTITUTE/TRIM/CLEAN, parsing and concatenating text
- **xls-whatif-goalseek-solver** — What-if analysis: Goal Seek, Solver for optimization with constraints, one/two-variable Data Tables, Scenario Manager
- **xls-xlookup-lookups** — XLOOKUP, INDEX/MATCH, two-way lookups, approximate match, multi-criteria and reverse lookups — replace VLOOKUP, handle not-found and left-lookups
- **xls-xlsm-structure** — What makes a macro-enabled .xlsm: OOXML/ZIP package, vbaProject.bin, content types, Trust Center/macro security, .xlsm vs .xlsb vs .xlsx

## VBA (vba-*) — 20

- **vba-ado-sql** — Query databases from VBA with ADO — Connection/Recordset, SQL SELECT/INSERT, parameterized commands to stop SQL injection, CopyFromRecordset to dump to a sheet, connection strings
- **vba-array-fast-readwrite** — Read a whole range into a Variant array, process in memory, write back in one shot — the order-of-magnitude speedup that avoids slow cell-by-cell loops; LBound/UBound, Transpose
- **vba-automate-office-apps** — Drive Outlook/Word/PowerPoint from Excel via late vs early binding — CreateObject vs GetObject, send mail, mail-merge, build decks; release objects, avoid orphaned EXE processes
- **vba-class-modules-oop** — Object-oriented VBA with class modules — properties (Get/Let/Set), private fields, methods, Class_Initialize/Terminate, custom events with RaiseEvent/WithEvents, collections of objects
- **vba-collections-dictionaries** — Use Collection and Scripting.Dictionary for lookups, dedup, grouping; .Exists, key/item iteration, Dictionary vs Collection tradeoffs, late vs early binding the Scripting runtime
- **vba-custom-udfs** — Build custom worksheet functions (UDFs) in VBA — Application.Volatile, Application.Caller, array-returning UDFs, #VALUE handling, Function Wizard categories, recalc behavior
- **vba-debugging** — Debug in the VBE — breakpoints (F9), step F8/Shift-F8, Watch and Locals windows, Immediate window Debug.Print and ?expr, Stop, conditional watch break, call stack, Err inspection
- **vba-deploy-addin-xlam** — Package and deploy macros as an Excel add-in (.xlam) — SaveAs xlOpenXMLAddIn, IsAddin, install via Add-ins dialog, AddIns.Add, ribbon integration, update/versioning, vs .xla legacy
- **vba-error-handling** — Robust error handling: On Error GoTo label, Err.Number/Description/Source, Resume/Resume Next, centralized cleanup, re-raise with Err.Raise, avoiding On Error Resume Next abuse
- **vba-event-handling** — Handle Worksheet (Change/SelectionChange/BeforeDoubleClick), Workbook (Open/BeforeSave/SheetChange), and Application events; Target.Address, disable events to avoid recursion
- **vba-file-io** — File and folder I/O: FileSystemObject (CreateTextFile/OpenTextFile/ReadAll), native Open/Print/Input, Dir loop over files, read/write CSV and text, check file exists, append mode
- **vba-loops-conditionals** — Control flow: For/For Each, Do While/Until, Select Case, If/ElseIf, Exit For/Do, nested loops, GoTo for cleanup; choosing For Each vs indexed For over collections
- **vba-macro-security-signing** — Macro security and digital signing — Trust Center settings, signed vs unsigned macros, SelfCert vs CA certs, trusted locations, VBA project password, distribute macros that don't get blocked
- **vba-performance-tuning** — Speed up macros: ScreenUpdating Off, Calculation manual, EnableEvents off, DisplayAlerts, restore in cleanup, avoid Select/Activate, array I/O, timing with Timer — the standard speed wrapper
- **vba-range-cells-manipulation** — Reference and manipulate ranges: Cells(r,c), Range, Offset, Resize, End(xlUp/xlToLeft), CurrentRegion, UsedRange, find last row, SpecialCells, Union/Intersect
- **vba-regexp** — Pattern matching with VBScript RegExp — extract/validate/replace text, Global/IgnoreCase, capturing groups via SubMatches, Test vs Execute, build a regex UDF, common patterns
- **vba-ribbon-customui** — Customize the Ribbon with customUI XML — Custom UI Editor, onAction callbacks, dynamic controls (getEnabled/getVisible/getImage), invalidate to refresh, getCustomUI for COM add-ins
- **vba-subs-vs-functions** — Write Sub vs Function procedures, pass ByRef/ByVal, Optional/ParamArray args, return values, scope with Public/Private — when to use which in Excel VBA
- **vba-userforms-controls** — Build UserForms with TextBox/ComboBox/ListBox/OptionButton/CheckBox/Frame, Initialize/Activate, Show modal vs modeless, validate input, populate ListBox.List 2-D, MultiPage tabs
- **vba-win32-api-declares** — Call Windows API from VBA with Declare statements — PtrSafe and LongPtr for 64-bit, Sleep/GetTickCount/timers, file dialogs, window handles, conditional compilation #If Win64

## Retail business (retail-*) — 25

- **retail-assortment-planning** — Build store/channel assortments by good-better-best tiering, depth-vs-breadth, MOS curves and SKU rationalization for assortment planning, line architecture, range review
- **retail-category-management** — Run the 8-step category management process: role, scorecard, strategies (traffic/transaction/profit/cash) and tactics for category review, role definition, category captain
- **retail-clv** — Estimate customer lifetime value (CLV/LTV) via margin x frequency x lifespan and retention/discount models to cap CAC and prioritize segments for LTV, unit economics, CAC payback
- **retail-demand-forecasting** — Forecast retail demand with moving averages, exponential smoothing, Holt-Winters seasonality and MAPE accuracy tracking for sales forecasts, baseline demand, replenishment planning
- **retail-ecommerce-conversion** — Optimize e-commerce conversion via funnel analysis, micro-conversions, cart/checkout abandonment, PDP and A/B testing for CRO, online conversion rate, checkout optimization
- **retail-gmroi-margin** — Calculate GMROI, gross margin %, maintained margin and contribution to rank product/category profitability for margin analysis, profitability, buyer scorecards
- **retail-kpi-dashboard** — Design a retail KPI dashboard with conversion, AUR, UPT, ATV, traffic and the metric tree linking them for sales dashboards, KPI reporting, performance metrics
- **retail-labor-scheduling** — Build store labor schedules from traffic-driven demand, sales-per-labor-hour and coverage to match staffing to footfall for workforce management, scheduling, SPLH
- **retail-markdown-optimization** — Optimize markdown cadence and depth to clear aged inventory while protecting margin using sell-through triggers and markdown ROI for clearance, aged stock, exit strategy
- **retail-market-basket** — Run market-basket / affinity analysis with support, confidence, lift to find cross-sell pairs and bundle opportunities for basket analysis, association rules, attach rate
- **retail-omnichannel-bopis** — Design omnichannel fulfillment: BOPIS, ship-from-store, endless aisle, unified inventory and fulfillment routing for buy-online-pickup-in-store, click-and-collect, store fulfillment
- **retail-open-to-buy** — Calculate and manage Open-To-Buy (OTB) dollar plans: planned purchases, EOM/BOM stock, monthly receipt flow for buy budgets, in-season buying control
- **retail-planogram-space** — Build planograms and allocate shelf space by space-to-sales, days-of-supply facings, eye-level zoning and adjacencies for shelf layout, facings, space planning
- **retail-pricing-strategy** — Set retail prices via cost-plus markup, keystone, price elasticity, psychological price points and competitive positioning for pricing, AUR, markup, price architecture
- **retail-private-label** — Develop and manage private label / own-brand: margin uplift, price gaps to national brands, tiering (value/standard/premium) and sourcing for own brand, store brand, exclusive label
- **retail-promotion-lift** — Measure promotional lift, baseline uplift, halo/cannibalization and promo ROI/profitability vs pre-promo baseline for promo analysis, campaign effectiveness, incrementality
- **retail-replenishment-autoreorder** — Design min/max and reorder-point auto-replenishment, EOQ order quantities and review cycles to automate restocking for replenishment, auto-reorder, par levels, basic stock
- **retail-returns-reverse-logistics** — Manage returns and reverse logistics: return rate, restocking/disposition, refurb-vs-liquidate and return fraud for reverse logistics, RMA, returns reduction
- **retail-rfm-segmentation** — Segment customers with RFM (recency, frequency, monetary) scoring and quintile tiers to target champions, at-risk, lapsed for customer segmentation, loyalty targeting, CRM
- **retail-safety-stock** — Compute safety stock and reorder points with service-level Z-scores, demand and lead-time variability for inventory buffers, stockout prevention, fill rate targets
- **retail-seasonality-454-calendar** — Apply the 4-5-4 retail calendar, fiscal weeks, comparable-week alignment and seasonal indices for retail calendar, fiscal year, comp sales, week-over-week planning
- **retail-sell-through-wos** — Compute sell-through %, weeks-of-supply (WOS), sell-through rate and forward cover to flag slow/fast movers for inventory health, in-season tracking, reorder timing
- **retail-shrink-loss-prevention** — Measure and reduce shrinkage from theft, fraud, admin error and damage using shrink % and shrink-source analysis for loss prevention, inventory accuracy, shrink reduction
- **retail-supply-chain-leadtime** — Manage lead time, order cycle and pipeline/in-transit inventory; compute lead-time demand and pipeline stock for supply chain, inbound logistics, on-time delivery
- **retail-vendor-management** — Manage suppliers with scorecards, terms negotiation, MOQ, allowances/co-op, and OTIF compliance for vendor management, supplier negotiation, trade terms

## Research methods (research-*) — 22

- **research-ab-testing-power** — Plan and read online A/B tests + power/sample-size analysis: MDE, power, alpha, sample size, peeking, novelty effects, SRM — use for product experiments and any two-arm comparison
- **research-citation-referencing** — Manage citations and apply referencing styles correctly: APA 7 / MLA 9 / Chicago / IEEE / Vancouver, in-text vs reference list, DOIs, reference managers — use when citing or formatting a bibliography
- **research-confidence-intervals-effect-sizes** — Report and interpret CIs and effect sizes (Cohen's d, r, odds ratio, eta-squared) — the magnitude/uncertainty layer p-values omit — use whenever reporting any quantitative result
- **research-data-cleaning** — Clean and prepare data for analysis: missing-data mechanisms (MCAR/MAR/MNAR) + imputation, outliers, type coercion, dedup, tidy/long format, validation — use before any modeling
- **research-data-visualization** — Build honest, clear research figures: chart choice by data type, error bars, axis integrity, color/accessibility, small multiples, publication-ready figures — use when presenting findings visually
- **research-descriptive-statistics** — Summarize data correctly: central tendency, dispersion, distribution shape, when mean vs median, outlier handling, the right chart — use before any inferential test
- **research-experimental-design-rct** — Design a randomized controlled trial / true experiment: randomization, control, blinding, between vs within, confound control, CONSORT — use when establishing causation
- **research-grounded-theory** — Build theory from data with grounded theory: open/axial/selective coding, constant comparison, theoretical sampling, memoing, core category, theoretical saturation — use to generate (not test) theory
- **research-hypothesis-testing-pvalues** — Run and interpret NHST correctly: null/alt, choosing the test, one vs two-tailed, what p actually means, Type I/II errors, multiple comparisons — use when testing a hypothesis
- **research-interview-methods** — Plan and run research interviews: structured/semi/unstructured, interview-guide funnel, probing, rapport, transcription, saturation — use when collecting qualitative interview data
- **research-linear-regression** — Fit and diagnose OLS linear regression: model spec, coefficient interpretation, R-squared, assumptions (LINE), multicollinearity, dummy coding — use for predicting/explaining a continuous outcome
- **research-literature-review** — Run a structured (narrative or scoping) literature review: search strings, screening, synthesis matrix, gap-spotting — use when reviewing prior work, building a related-work section, or mapping a field
- **research-logistic-regression** — Fit and interpret logistic regression for binary outcomes: log-odds, odds ratios, marginal effects, model fit (AUC, pseudo-R2), separation — use when the outcome is yes/no
- **research-meta-analysis** — Pool effects across studies: extract effect sizes, fixed vs random effects, heterogeneity (I-squared), forest/funnel plots, publication-bias tests, moderators — use to synthesize quantitative evidence
- **research-mixed-methods** — Design mixed-methods studies: convergent, explanatory-sequential, exploratory-sequential, integration/joint displays, priority & timing — use when combining qual + quant
- **research-qualitative-thematic-analysis** — Code qualitative data and run Braun & Clarke thematic analysis: open coding, codebook, themes vs codes, inter-coder reliability — use for interviews, open-ends, field notes
- **research-reproducibility-preregistration** — Make a study reproducible and preregister it: protocol/analysis plan, OSF/AsPredicted, registered reports, computational repro (seeds, envs, data/code sharing), confirmatory vs exploratory — use before data collection
- **research-sampling-methods** — Choose and execute a sampling strategy: probability (SRS, stratified, cluster, systematic) vs non-probability (quota, purposive, snowball) + sample-size logic — use when deciding who to study
- **research-source-verification-triangulation** — Verify primary sources and triangulate claims: primary vs secondary, provenance, lateral reading, CRAAP, source/method/investigator triangulation, retraction checks — use to fact-check and corroborate
- **research-survey-questionnaire-design** — Design a valid questionnaire: item wording, response scales, ordering, Likert vs semantic differential, pilot testing — use when building a survey instrument or fixing a leaky one
- **research-systematic-review-prisma** — Conduct a systematic review with PRISMA 2020 flow + checklist: protocol, databases, dual screening, risk-of-bias, reporting — use for rigorous evidence synthesis or a registered review
- **research-validity-reliability** — Establish measurement validity and reliability: internal/external/construct/statistical-conclusion validity, threats, reliability types (test-retest, internal consistency, inter-rater) + qualitative trustworthiness — use to defend rigor

## Business analytics (ba-*) — 16

- **ba-chart-selection** — Pick the right chart for the data relationship — comparison/composition/distribution/correlation/trend — bar vs line vs scatter vs box; kill pie>5-slices, dual-axis, and truncated-baseline deception.
- **ba-cohort-analysis** — Build retention/revenue cohort tables and triangle heatmaps by signup period, read retention curves (flattening = PMF), compute N-day and rolling retention; avoid survivorship and mixed-window bias.
- **ba-dashboard-design** — Design BI dashboards (Tableau/Power BI/Looker) that drive decisions: inverted-pyramid layout, the 5-second test, audience-tiered KPI/diagnostic/operational views; avoid chart-junk gauges and 30-tile vanity walls.
- **ba-data-quality-checks** — Validate dataset quality before analysis across the 6 dimensions (completeness/accuracy/consistency/validity/uniqueness/timeliness): null/dup/range/referential profiling, outlier detection; avoid analyzing dirty data silently.
- **ba-financial-statement-analysis** — Analyze P&L, balance sheet and cash-flow statements; build margin/liquidity/leverage/efficiency ratios, common-size + trend analysis; reconcile net income to operating cash and spot accrual red flags.
- **ba-funnel-analysis** — Build conversion funnels, compute step + overall conversion and drop-off, choose strict-order vs any-order and the conversion window; avoid the off-funnel-path and denominator-shift traps.
- **ba-kpi-metric-trees** — Design KPIs and decompose them into metric trees / driver trees (North Star → inputs), separate leading vs lagging, set SMART targets, and avoid vanity metrics and Goodhart gaming.
- **ba-process-mapping** — Map business processes with swimlane/BPMN and value-stream maps; capture actors, handoffs, decisions, SLAs; compute cycle vs lead time and %C&A; find bottlenecks, rework loops, and hidden waste.
- **ba-requirements-gathering** — Elicit analytics/BI requirements: stakeholder interviews, the 5 Whys to the real question, define metrics + grain + filters, write acceptance criteria and a data dictionary; avoid solutioning before the question.
- **ba-scenario-sensitivity-analysis** — Run scenario (base/bull/bear), sensitivity (one-way + tornado), and Monte Carlo analysis on models; use Excel Data Tables / Goal Seek / Scenario Manager; avoid changing many inputs at once.
- **ba-spreadsheet-modelling-discipline** — Build auditable financial/analytical spreadsheet models: inputs/calcs/outputs separation, one-formula-per-row consistency, named ranges, no hardcodes in formulas, error/trace checks; avoid fragile mega-formulas.
- **ba-sql-for-analysts** — Analyst SQL: window functions, CTEs, conditional aggregation, date_trunc cohorts, anti-joins for gaps; avoid the SELECT-DISTINCT fan-out trap and GROUP BY filtered-with-WHERE-not-HAVING bug.
- **ba-stakeholder-reporting** — Write executive summaries and stakeholder reports BLUF/Pyramid-Principle style: lead with the answer + ask, tier detail to audience, SCQA framing; avoid burying the recommendation in a data dump.
- **ba-storytelling-with-data** — Turn analysis into a persuasive data narrative (Knaflic/Duarte): context → conflict → resolution, preattentive focus, declarative chart titles, annotate the insight; strip chartjunk and cognitive load.
- **ba-time-series-forecasting** — Forecast business series: decompose trend/seasonality, pick naive/MA/Holt-Winters/ARIMA/Prophet by data shape, hold out + backtest with MAPE/RMSE; avoid leakage and random-split on time data.
- **ba-unit-economics** — Model unit economics: contribution margin, CAC, LTV (and LTV:CAC), payback period, cohort-based LTV; avoid revenue-not-margin LTV and blended-CAC vanity errors.

## Productivity / time-mgmt (prod-*) — 20

- **prod-deep-work** — Engineer distraction-free deep-work sessions (depth rituals, shutdown ritual, the 4 philosophies) for cognitively demanding output that creates disproportionate value
- **prod-delegation** — Delegate effectively using levels-of-delegation, RACI ownership, and clear outcome/context handoffs to scale your output and develop others instead of bottlenecking
- **prod-eisenhower-matrix** — Sort tasks by urgency x importance into the 4-quadrant Eisenhower matrix to escape reactive firefighting and protect quadrant-2 strategic work
- **prod-energy-management** — Schedule work to your ultradian rhythm and chronotype (90-min cycles, peak/trough/recovery, strategic renewal) so you match task type to available energy not just time
- **prod-focus-distraction-control** — Control distraction with environment design, notification hygiene, the distraction-capture pad, and Newport/Eyal indistractable tactics to protect sustained attention
- **prod-gtd-workflow** — Run David Allen's GTD five-step flow (capture, clarify, organize, reflect, engage) to get a trusted, stress-free system when your head is full of open loops
- **prod-habit-building** — Build durable habits with the cue-routine-reward loop and Atomic Habits laws (make it obvious/attractive/easy/satisfying), habit stacking, and the 2-day rule
- **prod-inbox-zero** — Reach and hold inbox zero with the OHIO triage (delete/delegate/respond/defer), filters, the 2-minute rule, and scheduled batch processing
- **prod-kanban-wip-limits** — Run a personal/team Kanban board with explicit WIP limits to visualize flow, expose bottlenecks, and finish work faster by limiting work-in-progress
- **prod-meeting-hygiene** — Run lean meetings and default-to-async (clear purpose/agenda/DRI, decision logs, no-meeting blocks, RFC docs) to reclaim maker time and reduce synchronous overhead
- **prod-note-taking-systems** — Build a second-brain note system with PARA organization and Zettelkasten atomic linked notes (CODE workflow, evergreen notes) for durable knowledge you can actually retrieve
- **prod-okr-goal-setting** — Set and run quarterly OKRs (qualitative Objective + 3-5 measurable Key Results) with scoring and check-ins to align ambitious goals with measurable outcomes
- **prod-pomodoro-technique** — Run the Pomodoro Technique (25/5 work-break cycles, interruption logging, estimation) to beat procrastination and make work-volume measurable
- **prod-prioritization-frameworks** — Choose and apply the right prioritization scoring model (RICE, ICE, MoSCoW, Weighted Scoring, Value-vs-Effort) to rank competing work objectively
- **prod-saying-no-boundaries** — Protect priorities by saying no well-positive-no technique, opportunity-cost framing, the Hell-Yeah-or-No filter, and pre-committed boundaries against overcommitment
- **prod-single-tasking** — Replace multitasking with deliberate single-tasking-task-switching cost, monotasking blocks, and one-tab discipline-to cut error rates and finish work faster
- **prod-smart-goals** — Convert vague intentions into SMART goals (Specific, Measurable, Achievable, Relevant, Time-bound) with leading indicators so goals become trackable and actionable
- **prod-time-blocking** — Design a time-blocked calendar (task batching, theme days, day-template) so every hour has an assigned job instead of an open-ended to-do list
- **prod-two-minute-rule** — Apply the 2-minute rule two ways-do-it-now for sub-2-min tasks (GTD) and the start-small habit version (Atomic Habits)-to crush small-task buildup and procrastination
- **prod-weekly-review** — Run a structured weekly review (clear, current, creative) to keep your task system trusted, reconcile calendar vs reality, and plan the week ahead
