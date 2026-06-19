---
name: ai-streaming-responses
description: >-
  Stream LLM output token-by-token for low perceived latency: SSE handling, partial-JSON/tool-call streaming, backpressure, and clean cancellation — use for any interactive or long-output UI.
---

# ai-streaming-responses

Streaming sends tokens as they're generated (SSE / chunked deltas), so the user sees output immediately — it cuts PERCEIVED latency (time-to-first-token) without reducing total cost. Accumulate deltas into the full message; for structured output, you receive PARTIAL JSON — either wait for completion to parse, or use an incremental/partial JSON parser to render fields as they stream. Tool calls also stream incrementally (name first, then args byte-by-byte) — buffer until the call is complete before executing, since args arrive in fragments. Handle the terminal event (finish_reason: stop/length/tool_calls) to know why it ended (hitting max_tokens mid-JSON is a common bug — detect 'length' and continue or raise limit). Support CANCELLATION: when the user stops or navigates away, abort the request to stop billing for unwanted tokens (use AbortController / close the stream). Add timeouts and reconnection for dropped streams. Pitfalls: assuming each chunk is a whole word (it's sub-token fragments — don't split on chunk boundaries for parsing), and trying to JSON.parse partial output and crashing. Common mistake: not handling 'length' truncation, shipping cut-off JSON to the parser.

**Tools:** SSE/streaming API, delta accumulation, partial JSON parsing, streamed tool_calls, abort/cancel, TTFT
