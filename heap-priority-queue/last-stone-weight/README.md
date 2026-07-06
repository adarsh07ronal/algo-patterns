# Last Stone Weight (Easy)

## Problem

You are given an array of integers `stones` where `stones[i]` is the
weight of the `i`th stone. On each turn, pick up the two heaviest stones
and smash them together. Suppose the two heaviest stones have weights `x`
and `y` with `x <= y`:

- If `x == y`, both stones are destroyed.
- If `x != y`, the stone of weight `x` is destroyed, and the stone of
  weight `y` has new weight `y - x`.

Repeat until at most one stone remains. Return the weight of the last
remaining stone, or `0` if none remain.

**Example 1:**

```
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
- Smash 7 and 8 -> 1, stones = [2,4,1,1,1]
- Smash 2 and 4 -> 2, stones = [2,1,1,1]
- Smash 2 and 1 -> 1, stones = [1,1,1]
- Smash 1 and 1 -> 0, stones = [1]
- 1 is the last remaining weight.
```

**Example 2:**

```
Input: stones = [1]
Output: 1
```

**Constraints:**
- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`

## Approach

At every step you need the two *currently heaviest* stones, and the set of
stones keeps changing (one or two are removed, at most one is added back).
That "repeatedly grab the max" requirement is exactly what a max-heap is
for: build it once in O(n), then each turn is pop-max, pop-max, and
optionally push the difference — each O(log n) — instead of re-scanning
the whole array for the top two every turn (which would be O(n) per turn).

`heapq` only gives a min-heap, so every stone weight is pushed negated
(`-w`). The most negative value sits at the root and corresponds to the
largest original weight, so popping twice and negating back gives the two
heaviest stones. If their difference is nonzero, it's pushed back negated
so it re-enters the max-heap ordering correctly.

The loop continues while more than one stone remains. At the end, either
one negated weight is left (negate it back and return it) or the heap is
empty (return 0).

## Edge Cases

- **Single stone** — loop body never runs; return that stone's weight
  directly.
- **All stones destroyed evenly** (heap becomes empty) — return `0`.
- **Two equal stones** — both destroyed, nothing pushed back, matches the
  "x == y" rule.
- **Many equal weights** — ties are broken arbitrarily by the heap, but
  since equal stones destroy each other identically regardless of which
  "copy" is chosen, the result is unaffected.

## Complexity

- **Time:** O(n log n) — building the heap is O(n), and each of up to n
  smashing turns does O(1) pops/pushes at O(log n) each.
- **Space:** O(n) — the heap holds all stones (negated) at once.

[Category Index](../README.md) | [Next ->](../kth-largest-element-in-a-stream/README.md)
