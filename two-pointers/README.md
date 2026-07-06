# Two Pointers

## Pattern

The two-pointers pattern solves array/string problems by walking two indices
through the data instead of nesting loops. There are two common shapes:

- **Opposite-direction pointers** — one pointer starts at the left end, the
  other at the right end, and they move toward each other. This is the go-to
  shape when you need to consider pairs (or a shrinking window) from both
  ends at once, e.g. checking a palindrome, finding a pair that sums to a
  target, or maximizing the area between two lines.
- **Same-direction pointers (fast/slow)** — both pointers start at (or near)
  the beginning and move forward, but at different rates or under different
  conditions. This shape is used for in-place compaction/partitioning: one
  pointer ("slow") marks where the next valid element should be written,
  while the other ("fast") scans ahead looking for it.

Sorted input is what usually makes this pattern possible: once the array is
sorted, moving a pointer left or right has a *predictable* effect on the
value it points to (larger or smaller), so you can reason about which
pointer to move to get closer to the answer. Without that monotonic
structure, you can't tell which pointer to advance without checking every
combination.

The payoff is complexity: a brute-force approach that checks every pair or
every possible split is O(n^2) or worse. Because each pointer only moves
forward (and the two pointers can cross at most once), the total number of
pointer moves across the whole run is bounded by O(n), collapsing nested
loops into a single linear pass (or O(n log n) when a sort is required
first).

## Problems

| Difficulty | Problem | Notes |
|---|---|---|
| Easy | [Valid Palindrome](./valid-palindrome/README.md) | Opposite-direction pointers skipping non-alphanumeric chars |
| Easy | [Merge Sorted Array](./merge-sorted-array/README.md) | Same-direction pointers merging from the back |
| Medium | [3Sum](./3sum/README.md) | Sort + fix one element, two-pointer scan for the rest |
| Medium | [Container With Most Water](./container-with-most-water/README.md) | Opposite-direction pointers, always move the shorter line |
| Medium | [Sort Colors](./sort-colors/README.md) | Dutch National Flag, three same-direction pointers |
| Medium | [Remove Duplicates from Sorted Array II](./remove-duplicates-from-sorted-array-ii/README.md) | Fast/slow pointers with a "look-back 2" write rule |
| Medium | [Boats to Save People](./boats-to-save-people/README.md) | Sort + greedy pairing of lightest and heaviest |

[<- Back to repo root](../README.md)
