---
name: career-ml-ai-interview-prep
description: >-
  Prep the ML/AI interview tracks — ML fundamentals, coding, ML system design, and LLM/applied-AI rounds — use when targeting MLE, AI engineer, or research-engineer roles.
---

# career-ml-ai-interview-prep

ML/AI loops have 4 distinct tracks; prep each. (1) **ML fundamentals (oral):** bias-variance, regularization (L1/L2, dropout), overfitting diagnosis, gradient descent variants, metric choice (precision/recall/F1/AUC, when accuracy lies on imbalanced data), cross-validation, feature engineering, leakage. (2) **Coding:** same DSA patterns as SWE *plus* implement-from-scratch (k-means, logistic regression, attention, a metric). (3) **ML system design:** use a template — problem framing → data & labels → features → model choice → **offline metrics → online metrics/AB test** → serving (batch vs realtime), latency, retraining cadence, monitoring (drift, train-serve skew). (4) **LLM/applied-AI (2026):** prompt vs RAG vs fine-tune vs agents tradeoffs, RAG architecture (chunking, embeddings, retrieval, reranking), eval (LLM-as-judge, golden sets), hallucination mitigation, context/cost/latency tradeoffs.

**What top candidates do differently:** in ML system design they obsess over *data and the offline/online metric loop* (where models actually fail) rather than model architecture, and they reason about train-serve skew and monitoring — production concerns juniors skip.

**Common mistake:** memorizing model trivia but unable to frame a business problem as an ML problem, picking accuracy on imbalanced data, ignoring the labeling/data pipeline, and for LLM roles reaching for fine-tuning when RAG or better prompting solves it cheaper.

**Tools:** bias-variance, eval metrics, ML system design template, RAG/fine-tuning tradeoffs, train-serve skew
