# Find First and Last Position of Element in Sorted Array (Medium)

## Problem

Given an array of integers `nums` sorted in ascending order (possibly with
duplicates) and a target value, return `[first_index, last_index]` — the
indices of the first and last occurrence of `target` in `nums`. If `target`
is not found, return `[-1, -1]`. Must run in O(log n) time.

**Examples**

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3, 4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1, -1]
```

**Constraints**
- `0 <= nums.length <= 10^5`.
- `nums` is sorted in non-decreasing order.

## Approach

This is two separate "find the boundary" binary searches over the same
array, each using the half-open `[lo, hi)` template with a monotonic
predicate:

- **Leftmost occurrence:** predicate `nums[mid] >= target`. This is false
  for all indices left of the first occurrence and true from the first
  occurrence onward — monotonic, so binary search finds the smallest index
  where it's true. After the search, verify that index actually holds
  `target` (it might not, if `target` isn't present at all).
- **Rightmost occurrence:** search for the leftmost index where
  `nums[mid] > target`, then subtract 1. Equivalently, this finds the
  boundary just past the last occurrence of `target`.

Both searches only ever ask "is `nums[mid]` at least/more than `target`?" —
a monotonic yes/no question over the sorted array — so each independently
converges to the correct boundary in O(log n), and running both gives the
full `[first, last]` range.

## Edge Cases

- Empty array (`nums.length == 0`): the search range is empty from the
  start, immediately returns `[-1, -1]`.
- Target not present anywhere: the leftmost search lands on an index whose
  value (if any) doesn't match `target`, so we detect this with a bounds
  and equality check and return `[-1, -1]`.
- Target present exactly once: leftmost and rightmost searches return the
  same index.
- Target at the very first or very last index: half-open bounds
  (`hi = n` initially) correctly include the last index and `lo = 0`
  includes the first.
- All elements equal to target: leftmost search returns `0`, rightmost
  returns `n - 1`.

## Complexity

- **Time:** O(log n) — two independent binary searches, each O(log n).
- **Space:** O(1) — only index variables.

[<- Previous](../search-in-rotated-sorted-array/README.md) | [Category Index](../README.md) | [Next ->](../search-a-2d-matrix/README.md)
