---
name: algo-stacks-queues-monotonic
description: >-
  Stacks, queues, and the monotonic-stack/deque pattern — valid-parens, next-greater-element, sliding-window-max, histogram, span — in amortized O(n).
---

# algo-stacks-queues-monotonic

A **stack** (LIFO) handles nesting/matching: valid-parentheses (push openers, pop on matching closer), expression eval, undo. A **queue/deque** (FIFO) handles order-preserving processing and BFS. The power move is the **monotonic stack**: keep elements in increasing (or decreasing) order; when a new element violates the order, pop and resolve each popped element against the newcomer. This answers next-greater/next-smaller, daily-temperatures, stock-span, and largest-rectangle-in-histogram in amortized O(n) (each element pushed/popped once). 

The **monotonic deque** solves sliding-window-maximum: maintain indices in decreasing value order, pop the front when it leaves the window, pop the back while smaller than the incoming — front is always the window max, O(n) total. 

Pitfalls: (1) deciding increasing vs decreasing — pick by what you query (next-greater → decreasing stack). (2) storing values when you need indices (for distances/windows, store indices). (3) forgetting to drain remaining stack elements at the end (they have no next-greater → default answer). (4) not evicting out-of-window indices in the deque.

**Tools:** stack LIFO, queue/deque FIFO, monotonic stack, monotonic deque
