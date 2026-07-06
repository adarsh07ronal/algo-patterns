# Binary Search (Easy)

## Problem

Given a sorted array of distinct integers `nums` and a target integer
`target`, return the index of `target` in `nums`, or `-1` if it is not
present. The algorithm must run in O(log n) time.

**Examples**

```
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4          # nums[4] == 9

Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1         # 2 is not in nums
```

**Constraints**
- `nums` is sorted in ascending order.
- All elements of `nums` are distinct.
- `1 <= nums.length <= 10^4`.

## Approach

We're searching over the indices `[0, n-1]` of an already-sorted array. The
predicate we exploit is simple ordering: if `nums[mid] < target`, every index
`<= mid` is too small and can be discarded; if `nums[mid] > target`, every
index `>= mid` is too large and can be discarded. If `nums[mid] == target` we
are done.

Use a closed interval `lo = 0`, `hi = n - 1`, and loop while `lo <= hi`,
computing `mid = lo + (hi - lo) // 2`. Each iteration strictly shrinks the
interval by excluding `mid` from further consideration (`lo = mid + 1` or
`hi = mid - 1`), so the loop always terminates, and because the array is
sorted, discarding a half never discards the target — this is why the
algorithm converges to the correct answer (or correctly proves it's absent
when `lo > hi`).

## Edge Cases

- Empty considerations are avoided by the constraint `nums.length >= 1`; a
  single-element array still works (`lo == hi == 0` on the first check).
- Target smaller than every element: `hi` walks down below `lo` immediately,
  loop ends, return `-1`.
- Target larger than every element: `lo` walks up past `hi`, loop ends,
  return `-1`.
- Target at the first or last index: found directly once `mid` lands there;
  the closed-interval bounds correctly include both ends.
- Since all elements are distinct, there's never ambiguity about which
  occurrence to return.

## Complexity

- **Time:** O(log n) — each iteration halves the remaining search interval.
- **Space:** O(1) — only a few index variables are used, no extra data
  structures.

[Category Index](../README.md) | [Next ->](../first-bad-version/README.md)
