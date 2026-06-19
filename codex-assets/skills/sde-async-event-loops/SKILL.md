---
name: sde-async-event-loops
description: >-
  Master non-blocking I/O - the single-threaded event loop, async/await, futures, and not blocking the loop with CPU work.
---

# sde-async-event-loops

Async concurrency lets one thread juggle thousands of I/O-bound tasks by never blocking on I/O. The **event loop** (Node's libuv, Python asyncio, Go runtime) runs ready callbacks; when code awaits I/O, control returns to the loop to run other work, resuming when the OS signals completion. **async/await** is syntactic sugar over promises/futures/coroutines - `await` yields the loop, it does NOT spawn a thread. Concurrency without parallelism: one thread, interleaved tasks. **The cardinal sin: blocking the event loop** with CPU-bound work (a tight loop, sync crypto, big JSON parse, sync file read) - it freezes ALL pending tasks since there's one thread. Offload CPU work to a worker thread/process pool; keep the loop for I/O orchestration. Run independent awaits concurrently with `Promise.all`/`asyncio.gather`, not sequential awaits. **Pitfalls**: forgetting to await (fire-and-forget swallows errors and races), mixing sync blocking calls into async code, and unbounded concurrency exhausting connections/memory - bound it with a semaphore. Async shines for I/O-bound, high-fanout services; for CPU-bound throughput you still need real threads/processes.

**Tools:** event loop, async/await, promises/futures, libuv, coroutines, thread pool
