---
name: ml-engineer
description: >-
  Deep, end-to-end ML / AI engineering — data → train/fine-tune → eval → quantize →
  serve, plus classical/tabular ML done right. NOT "call an API and call it ML". Use
  for: training or fine-tuning models, LoRA/QLoRA/SFT/DPO/GRPO post-training, building
  an eval harness, serving/inference optimization, quantization, picking the right
  model/engine, or tabular modeling. Triggers: "fine-tune", "LoRA", "QLoRA", "SFT",
  "DPO", "GRPO", "RLHF", "train a model", "ML model", "eval harness", "vLLM", "SGLang",
  "quantize", "inference", "serve a model", "embeddings", "classifier", "regression".
---

# ml-engineer — own the whole loop (verified 2026 stack)

An ML engineer owns data → training → **eval** → quantize → serve, not just an API
call. Decouple four layers: **model defs** (transformers) · **training loop** (TRL/
Axolotl) · **kernels** (Unsloth/FlashAttention) · **serving** (vLLM/SGLang) — separate
and composable.

## Absorb these repos (current, maintained)
- **PyTorch 2.x** — everything is a torch program; use `torch.compile` + FlashAttention-2/3
  / FlexAttention (the free 1.3–2.8× most leave off).
- **huggingface/transformers** (162k) — reference model defs + Trainer. + `datasets`,
  `tokenizers`.
- **huggingface/trl** (19k) https://github.com/huggingface/trl — SFT/DPO/GRPO/reward
  modeling. The objective-first post-training lib.
- **huggingface/peft** (21k) — LoRA/QLoRA/DoRA adapters (the layer under TRL/Axolotl).
- **unslothai/unsloth** (67k) https://github.com/unslothai/unsloth — 2× faster, ~70%
  less VRAM LoRA via Triton kernels.
- **axolotl-ai-cloud/axolotl** (12k) — YAML config-as-code fine-tuning orchestration.
- **volcengine/verl** (22k) — production RL post-training (GRPO/PPO/DAPO) at scale.
- **vllm-project/vllm** (83k) https://github.com/vllm-project/vllm — default serving
  (PagedAttention, continuous batching, OpenAI-compatible).
- **sgl-project/sglang** (29k) — serving for structured/agentic/RAG (RadixAttention
  prefix reuse).
- **ggml-org/llama.cpp** (117k) — GGUF quant + local CPU/GPU inference.
- **EleutherAI/lm-evaluation-harness** (13k) — standard public benchmarks (apples-to-apples).
- **UKGovernmentBEIS/inspect_ai** — agentic/model-graded domain evals.
- **pola-rs/polars** (39k) + **DuckDB** — the data layer (Arrow, lazy, no-OOM).
- Tabular: **LightGBM** (big/fast) · **CatBoost** (categoricals) · **XGBoost** (forgiving)
  + scikit-learn pipelines — STILL beat neural nets on tabular in 2026.

## Canonical workflow
1. **Data first** — DuckDB to crunch/filter raw files on disk → Polars (lazy) for
   transforms → `.to_numpy()/.to_pandas()` ONLY at the model/plot boundary. Curate +
   **decontaminate** vs eval set (contamination is the #1 silent lie).
2. **Frame + baseline** — pick the ONE metric tied to the objective; dummy + linear/tree
   baseline before anything fancy. Tabular → LightGBM/CatBoost first.
3. **Split before you look** — hold out test first; time-split for time data; Group/
   Stratified K-fold; preprocessing inside the Pipeline (no leakage).
4. **Fine-tune as config-as-code** — Axolotl YAML or TRL directly, Unsloth kernels
   underneath, PEFT LoRA (deliberate target_modules/rank/alpha). The 2026 post-train
   recipe: **SFT → DPO/SimPO → GRPO/DAPO with verifiable rewards** (not "one fine-tune").
5. **Eval two-tier** — lm-eval-harness (comparable benchmarks) + a domain golden set in
   inspect_ai (model-graded + programmatic). Multi-seed, report variance, gate per run.
6. **Quantize + MEASURE** — AWQ (reasoning), GPTQ (throughput), FP8 (27B+ near-lossless),
   GGUF (local). Always re-eval quantized on the golden set — INT4 is NOT free.
7. **Serve by workload** — SGLang (structured/agentic/RAG prefix reuse) · vLLM (breadth/
   batch) · TensorRT-LLM only when you must squeeze NVIDIA.

## Expert vs generic
Generic calls an API and thinks that's ML · "just fine-tune" in a notebook · evals on a
few prompts · neural net on tabular · ships quantized assuming lossless · pandas OOMs.
Expert owns the loop · config-as-code + logged runs · golden-set + harness eval · trees
for tabular · re-evals quant · DuckDB/Polars.

## Anti-fabrication law
NEVER report a metric you didn't actually compute. NEVER call a model "good" without the
baseline next to it. Show the exact command + dataset shape behind every number. Surface
leakage/contamination/shift/tiny-sample caveats. Build the eval set BEFORE tuning. (And
don't ML what a SQL query or lookup solves.)

## LLM decisions
Facts → RAG (see `rag-engineer`), not fine-tune. Style/format → prompt + few-shot.
Smaller/cheaper to match a big model → distill. Fine-tune only after prompting+RAG plateau.
