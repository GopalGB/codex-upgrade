---
name: algo-linked-lists
description: >-
  Linked-list operations with pointer surgery — reverse, detect/remove cycle, merge, find middle, reorder — using dummy nodes and fast/slow pointers.
---

# algo-linked-lists

A singly linked list gives O(1) insert/delete at a known node but O(n) random access. Two idioms solve most problems. **Dummy head node**: prepend a sentinel so the real head needs no special-casing during insert/delete — return `dummy.next`. **Fast/slow pointers (Floyd)**: slow moves 1, fast moves 2 → slow lands on the middle; if fast catches slow, there's a cycle; to find the cycle entry, reset one pointer to head and advance both by 1 until they meet. 

**Reverse** with three pointers: `while cur: nxt=cur.next; cur.next=prev; prev=cur; cur=nxt`; reverse-in-groups-of-k extends this. 

Pitfalls: (1) losing the rest of the list by reassigning `next` before saving it — always cache `nxt` first. (2) null-pointer derefs at the tail — check `fast and fast.next` before `fast.next.next`. (3) off-by-one on 'remove Nth from end' — use two pointers n apart with a dummy. (4) creating cycles accidentally when rewiring. Draw the pointers before coding.

**Tools:** dummy head, fast/slow (Floyd), in-place reverse, prev/cur/next
