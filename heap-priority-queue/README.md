# Heap / Priority Queue

## Pattern

A binary heap is a tree-shaped array structure that keeps one element —
the smallest (min-heap) or largest (max-heap) — always available at the
root. It gives you O(log n) push and O(log n) pop of that extreme element,
and O(1) peek, in exchange for *not* keeping the rest of the data sorted.
That trade-off is the whole point: most problems only ever need "give me
the current min/max, repeatedly, while the set changes," and a heap does
that far cheaper than re-sorting after every change.

Python's `heapq` module only implements a **min-heap** (the smallest item
is always at index 0). To simulate a max-heap, negate the values on the
way in and negate them back on the way out — push `-x` instead of `x`, and
the "smallest" negated value pops out first, which corresponds to the
largest original value.

Common use cases you'll see across this category:

- **Top-k / kth-largest problems** — keep a heap of size k instead of
  sorting the whole input; the heap bounds memory and work to O(n log k).
- **Streaming kth largest** — maintain a running heap so each new value
  can be incorporated in O(log k) instead of re-sorting from scratch.
- **Merging sorted sequences / smallest-sum pairs** — a heap seeded with
  one candidate per sequence lets you pull the next smallest overall
  element without comparing every remaining candidate.
- **Scheduling by priority** — greedily pick the "most urgent" (most
  frequent, heaviest, etc.) item on each step, which a max-heap gives you
  in O(log n) per step instead of O(n) per step with a linear scan.

## Problems

| Difficulty | Problem | Notes |
|---|---|---|
| Easy | [Last Stone Weight](./last-stone-weight/README.md) | Max-heap simulated via negation, repeatedly smash the two heaviest |
| Easy | [Kth Largest Element in a Stream](./kth-largest-element-in-a-stream/README.md) | Maintain a size-k min-heap across repeated `add` calls |
| Medium | [Top K Frequent Elements](./top-k-frequent-elements/README.md) | Count frequencies, then a size-k heap instead of a full sort |
| Medium | [Kth Largest Element in an Array](./kth-largest-element-in-an-array/README.md) | Size-k min-heap keeps only the k largest seen so far |
| Medium | [K Closest Points to Origin](./k-closest-points-to-origin/README.md) | Size-k max-heap keyed on squared distance |
| Medium | [Reorganize String](./reorganize-string/README.md) | Max-heap by frequency, greedily place the most frequent character that isn't the previous one |
| Medium | [Find K Pairs with Smallest Sums](./find-k-pairs-with-smallest-sums/README.md) | Min-heap seeded with one candidate per row, expand lazily |

[<- Back to repo root](../README.md)
