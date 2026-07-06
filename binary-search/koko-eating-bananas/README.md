# Koko Eating Bananas (Medium)

## Problem

Koko has `piles` of bananas, `piles[i]` bananas in the `i`-th pile. She has
`h` hours before the guards return. Each hour she chooses one pile and eats
up to `k` bananas from it; if the pile has fewer than `k` bananas, she eats
all of them and doesn't touch another pile that hour. Find the minimum
integer eating speed `k` such that she can eat all the bananas within `h`
hours.

**Examples**

```
Input: piles = [3,6,7,11], h = 8
Output: 4

Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

**Constraints**
- `1 <= piles.length <= h <= 10^9` is not required, but `piles.length <= h`
  is implied by feasibility at `k = max(piles)`.
- `1 <= piles[i] <= 10^9`.

## Approach

This is the canonical "binary search on the answer" problem. We are not
searching an array — we're searching the space of possible integer speeds
`k`, from `1` to `max(piles)`.

Define `hours_needed(k) = sum(ceil(pile / k) for pile in piles)` — the total
hours required to finish all piles at speed `k`. The predicate
`feasible(k) = hours_needed(k) <= h` is monotonic: as `k` increases,
`hours_needed(k)` never increases (a faster speed can only finish a pile in
the same or fewer hours), so once `feasible(k)` becomes true it stays true
for all larger `k`. That monotonicity is exactly what binary search needs.

We binary search for the smallest `k` with `feasible(k) == True` using the
half-open `[lo, hi)` "first true" template: `lo = 1`, `hi = max(piles) + 1`.
At each `mid`, compute `hours_needed(mid)`; if feasible, the answer could be
`mid` or smaller (`hi = mid`), otherwise it must be larger (`lo = mid + 1`).
`k = max(piles)` is always feasible (each pile finishes in exactly one
hour), which guarantees a valid upper bound exists, so the search always
converges to a real answer.

## Edge Cases

- Single pile: `hours_needed(k)` reduces to a single `ceil` division; still
  works uniformly.
- `h` exactly equal to `len(piles)`: forces `k = max(piles)` since that's
  the only speed where every pile takes exactly one hour.
- Very generous `h` (much greater than needed): the smallest feasible `k`
  is `1`, found immediately since `feasible(1)` is checked as part of the
  search range starting at `lo = 1`.
- All piles the same size: `hours_needed` is just `len(piles) * ceil(pile/k)`,
  still monotonic in `k`.
- Large pile values (`10^9`): use integer ceiling division
  `(pile + k - 1) // k` to avoid floating-point rounding errors.

## Complexity

- **Time:** O(n log M) where `n = len(piles)` and `M = max(piles)` — each of
  the O(log M) binary search steps scans all piles to compute
  `hours_needed`.
- **Space:** O(1) — only counters and index variables.

[<- Previous](../search-a-2d-matrix/README.md) | [Category Index](../README.md) | [Next ->](../find-peak-element/README.md)
