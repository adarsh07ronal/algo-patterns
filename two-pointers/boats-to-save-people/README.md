# Boats to Save People (Medium)

## Problem

Given an array `people` where `people[i]` is the weight of the `i`-th
person, and an integer `limit` representing the maximum weight capacity of
each boat, return the minimum number of boats required to carry every
person. Each boat carries at most two people at a time, provided their
combined weight does not exceed `limit`.

**Example 1:**

```
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
```

**Example 2:**

```
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2), (3)
```

**Constraints:**
- `1 <= people.length <= 5 * 10^4`
- `1 <= people[i] <= limit <= 3 * 10^4`

## Approach

Sort `people` by weight, then use two opposite-direction pointers: `light`
at index 0 (lightest person) and `heavy` at the last index (heaviest
person). Repeatedly try to pair them: if `people[light] + people[heavy] <=
limit`, put them in the same boat and advance `light` inward; either way,
the heaviest remaining person always gets a boat, so advance `heavy`
inward too. Count one boat per iteration.

The greedy insight is: the heaviest remaining person must go on *some*
boat regardless — no one heavier is left, so nothing changes if we decide
their boat companion optimally *now*. The best possible companion for them
is the lightest remaining person: if the heaviest can't fit with the
lightest, they can't fit with anyone else remaining either (everyone else
is even heavier), so they must ride alone. If the heaviest *can* fit with
the lightest, pairing them is never worse than pairing the heaviest with
someone else — doing so only frees up a *heavier* leftover person to
potentially pair with someone later, which is strictly more flexible than
using up the lightest person on a boat that didn't need them. This greedy
exchange argument is what justifies two pointers over checking all
pairings (which would be combinatorial, not just O(n^2)).

## Edge Cases

- **Single person** — one boat, regardless of weight (as long as
  `weight <= limit`, guaranteed by constraints).
- **Every pair fits** (e.g. all weights are `limit / 2` or less) — pointers
  close in by 2 each iteration, producing `ceil(n / 2)` boats.
- **No pair fits** (e.g. every person's weight alone is close to `limit`)
  — `heavy` decrements alone each time, producing `n` boats, one per
  person.
- **Odd number of people** — the middle element ends up as either `light`
  or `heavy` when the pointers meet (`light == heavy`); the loop condition
  `light <= heavy` ensures that last solo person still gets counted.
- **A single person's weight equals `limit` exactly** — they can never
  share a boat (no room for anyone else, including weight-0 people, which
  don't exist per constraints), so they always ride alone; the sum check
  naturally forces `heavy` to decrement without `light` moving.

## Complexity

- **Time:** O(n log n) — dominated by the sort; the two-pointer scan
  afterward is O(n).
- **Space:** O(1) extra (excluding sort space, typically O(log n) to O(n)
  depending on the sort implementation), plus O(n) if sorting is not
  allowed to be in-place on the input.

[<- Previous](../remove-duplicates-from-sorted-array-ii/README.md) | [Category Index](../README.md)
