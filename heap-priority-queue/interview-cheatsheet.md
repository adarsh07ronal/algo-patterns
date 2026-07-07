# Heap / Priority Queue: How to Remember and Code It in an Interview

Python's `heapq` is *only* a min-heap. Every "I need the max" problem is solved by negating values on the way in and out. Beyond that one trick, there are just 2 idioms to recognize.

## The one trick: max-heap via negation

```python
import heapq
heap = []
heapq.heappush(heap, -value)     # push the negation
biggest = -heapq.heappop(heap)   # negate again on the way out
```

Say this out loud whenever a problem wants "largest"/"most frequent"/"closest is smallest but I need to evict the current largest" — it's the same 4 lines every time.

## The 2 idioms

**Idiom A — bounded heap of size k** (streaming top-k / kth largest):
```python
heap = []
for x in stream:
    heapq.heappush(heap, x)
    if len(heap) > k:
        heapq.heappop(heap)          # evict the smallest — heap[0] is always the kth largest so far
# heap[0] is now the answer (kth largest), or heap itself holds "the k largest/closest" unordered
```
Keeping the heap at size exactly `k` and always popping the smallest is what guarantees `heap[0]` is the k-th largest — you're letting the heap self-maintain "the k biggest survivors so far."

**Idiom B — seed with initial candidates, then pop-and-generate** (k-way merge / lazily expand only what you need):
```python
heap = [initial candidates...]
heapq.heapify(heap)
result = []
while heap and len(result) < k:
    item = heapq.heappop(heap)
    result.append(item)
    for next_candidate in derive_from(item):
        heapq.heappush(heap, next_candidate)
return result
```
This avoids generating all `n*m` candidates up front — you only ever generate the *next* candidate from whatever you just popped, which is why it beats brute-force sorting everything.

## The 7 problems in this category, decoded

| Problem | Idiom | Heap holds | Max or min heap |
|---|---|---|---|
| [Last Stone Weight](./last-stone-weight/README.md) | repeatedly pop 2 largest, push the difference back | all stone weights | max (negate) |
| [Kth Largest Element in a Stream](./kth-largest-element-in-a-stream/README.md) | A — bounded size `k`, persists across calls | the `k` largest values seen so far | min (so `heap[0]` = kth largest) |
| [Top K Frequent Elements](./top-k-frequent-elements/README.md) | A — bounded size `k`, keyed by frequency | `(count, value)` pairs | min (evict least frequent) |
| [Kth Largest Element in an Array](./kth-largest-element-in-an-array/README.md) | A — bounded size `k`, one-shot | array values | min (so `heap[0]` = kth largest after processing all) |
| [K Closest Points to Origin](./k-closest-points-to-origin/README.md) | A — bounded size `k`, keyed by distance | `(distance, point)` pairs | max (negate distance — evict the *farthest*, keep closest) |
| [Reorganize String](./reorganize-string/README.md) | always pop the most frequent remaining character, place it, push back after cooldown | `(count, char)` pairs | max (negate count) |
| [Find K Pairs with Smallest Sums](./find-k-pairs-with-smallest-sums/README.md) | B — seed with `(nums1[i]+nums2[0], i, 0)` for early `i`s, generate next pair lazily on pop | `(sum, i, j)` tuples | min |

## Decision checklist

1. **Do I want the max or the min at each step?** — `heapq` only gives min directly; negate on push/pop for max. Say which one you need *before* writing the push line, so you don't accidentally push the wrong sign.
2. **Is `k` fixed and small relative to the input?** → Idiom A: bound the heap to size `k`, evicting the "wrong-side extreme" (smallest, if you want the k largest) every time it grows past `k`. This is O(n log k), better than sorting everything (O(n log n)) when `k` is much smaller than `n`.
3. **Am I merging/generating from multiple sorted sources, or repeatedly deriving new candidates from whatever I just popped?** → Idiom B: seed the heap with a small number of initial candidates (not all `n*m` combinations), and only push the *next* one lazily each time you pop.
4. **Do I need to store more than just a number in the heap** (e.g. which array/index it came from, or a value paired with its count)? → push tuples; Python compares tuples element-by-element, so put the sort key first (`(count, char)`, `(distance, point)`) and a tie-breaker or payload after.
5. **Does the problem involve "place things with a cooldown/gap constraint"** (Reorganize String, similar in spirit to Task Scheduler in [greedy](../greedy/interview-cheatsheet.md))? → always greedily place the currently-most-frequent item, and hold recently-placed items out of the heap until their cooldown expires.

## How to drill this so it's automatic

- Before pushing anything, say "min-heap or max-heap" out loud — if max, remember the negation on *both* the push and the pop, not just one.
- For bounded-size-k problems, state the invariant explicitly: "the heap always contains exactly the k best-so-far; `heap[0]` is the worst of those k, which is why popping it when a better candidate arrives is safe."
- Trace a 4-5 element example by hand, writing out the heap's contents (as a sorted list, for clarity) after every push/pop — this is what catches sign errors in the negation trick.
- Remember tuple comparison in Python compares left-to-right — if two items tie on the first field, it'll compare the second field next, which can crash if that second field isn't comparable (e.g. raw objects). Add an index/tie-breaker field when in doubt.

[<- Back to Heap / Priority Queue index](./README.md)
