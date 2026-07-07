# Binary Search

## Pattern

Binary search repeatedly cuts a search space in half using a comparison at the
midpoint, giving O(log n) time instead of O(n). There are two flavors used in
this folder:

1. **Classic binary search on a sorted array.** You're looking for a specific
   value (or boundary) in an array that is already sorted. At each step you
   compare `nums[mid]` to the target and discard the half that cannot contain
   the answer.

2. **Binary search on the answer** (a.k.a. "binary search over a monotonic
   predicate"). The array itself may not be sorted, or there may be no array
   at all — instead you search over a *range of candidate answers*
   (e.g. possible eating speeds, possible versions, possible capacities).
   The key requirement is a **monotonic predicate**: a boolean condition
   `feasible(x)` such that once it becomes true (or false) for some `x`, it
   stays that way for all larger `x`. That monotonicity is what lets you
   discard half the candidates at each step, exactly like classic binary
   search.

### Picking the loop invariant correctly

Most bugs in binary search come from an inconsistent invariant between
`lo`, `hi`, and how `mid` is computed and updated. Two common, safe templates:

- **Closed interval `[lo, hi]`, looking for an exact match or "does it
  exist":**
  ```python
  lo, hi = 0, n - 1
  while lo <= hi:
      mid = lo + (hi - lo) // 2
      if nums[mid] == target:
          return mid
      elif nums[mid] < target:
          lo = mid + 1
      else:
          hi = mid - 1
  ```
  Both `lo` and `hi` always point at indices that are still "in play." The
  loop ends when the interval is empty (`lo > hi`).

- **Half-open interval `[lo, hi)`, looking for the boundary where a
  predicate flips from false to true (the classic "first true" pattern):**
  ```python
  lo, hi = 0, n
  while lo < hi:
      mid = lo + (hi - lo) // 2
      if feasible(mid):
          hi = mid       # mid could be the answer, keep it in range
      else:
          lo = mid + 1   # mid is definitely not the answer
  return lo
  ```
  Here `hi` is exclusive, so it's fine to set `hi = mid` without risking an
  infinite loop, because `mid < hi` always holds and the range shrinks.

Rules of thumb to avoid off-by-one and infinite-loop bugs:
- Always use `mid = lo + (hi - lo) // 2` to avoid overflow (not an issue in
  Python, but it's the portable habit) and to bias `mid` toward `lo`, which
  matters when `hi = mid` is used (biasing the other way with `hi - lo + 1)
  // 2` matters when `lo = mid` is used).
- Never write `lo = mid` in a closed-interval loop without rounding `mid` up
  (`mid = lo + (hi - lo + 1) // 2`), or you can get stuck when `hi == lo + 1`.
- Make sure every branch strictly shrinks the interval — if `mid` can equal
  both the new `lo` and stay unexcluded, you'll loop forever.
- Decide up front whether the answer is guaranteed to exist in range; if not,
  validate the final `lo`/`mid` after the loop.

**[Interview cheatsheet: how to remember and code this pattern from scratch](./interview-cheatsheet.md)**

## Problems

| Difficulty | Problem | Notes |
|---|---|---|
| Easy | [Binary Search](./binary-search/README.md) | The textbook closed-interval search. |
| Easy | [First Bad Version](./first-bad-version/README.md) | Binary search on the answer with an API-call budget. |
| Medium | [Search in Rotated Sorted Array](./search-in-rotated-sorted-array/README.md) | Determine which half is sorted at each step. |
| Medium | [Find First and Last Position of Element in Sorted Array](./find-first-and-last-position-of-element-in-sorted-array/README.md) | Two boundary searches (leftmost/rightmost). |
| Medium | [Search a 2D Matrix](./search-a-2d-matrix/README.md) | Treat the matrix as a flattened sorted array. |
| Medium | [Koko Eating Bananas](./koko-eating-bananas/README.md) | Binary search on the answer over eating speed. |
| Medium | [Find Peak Element](./find-peak-element/README.md) | Binary search using local slope as the predicate. |

[<- Back to repo root](../README.md)
