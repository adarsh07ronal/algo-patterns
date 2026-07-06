# Search in Rotated Sorted Array (Medium)

## Problem

An array of distinct integers, originally sorted in ascending order, has
been rotated at some unknown pivot (e.g. `[0,1,2,4,5,6,7]` might become
`[4,5,6,7,0,1,2]`). Given the rotated array `nums` and a target value,
return the index of `target`, or `-1` if it's not present. Must run in
O(log n) time.

**Examples**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Constraints**
- All values in `nums` are unique.
- `nums` is guaranteed to be a rotation of an ascending-sorted array.
- `1 <= nums.length <= 5000`.

## Approach

The array as a whole isn't sorted, but a key structural fact still holds:
**at least one of the two halves split by any `mid` is always sorted.**
That's the property we exploit instead of a simple less-than/greater-than
comparison.

At each step, compare `nums[lo]` and `nums[mid]`:
- If `nums[lo] <= nums[mid]`, the left half `[lo, mid]` is sorted. Check
  whether `target` falls within `nums[lo] <= target < nums[mid]`; if so
  recurse into the left half (`hi = mid - 1`), otherwise the target must be
  in the right half (`lo = mid + 1`).
- Otherwise the right half `[mid, hi]` must be sorted. Check whether
  `target` falls within `nums[mid] < target <= nums[hi]`; if so recurse
  right (`lo = mid + 1`), otherwise go left (`hi = mid - 1`).

Because one side is always provably sorted, we can always decide in O(1)
whether the target could be hiding in that sorted side using ordinary range
checks, and discard the other side otherwise. This preserves the halving
behavior of standard binary search, so it still converges in O(log n) and
never discards the target's actual location.

## Edge Cases

- No rotation at all (`nums` fully sorted): the "left half sorted" branch is
  always taken, degenerating into classic binary search.
- Rotation point at index 0 or at the last index: still handled uniformly
  since the sortedness check (`nums[lo] <= nums[mid]`) works regardless of
  where the pivot is.
- Single-element array: loop body runs once with `lo == hi == mid`, checked
  directly.
- Target equal to `nums[lo]`, `nums[mid]`, or `nums[hi]`: range checks use
  `<=`/`>=` at the boundaries so these are matched correctly rather than
  skipped.
- Target not present: loop ends with `lo > hi`, return `-1`.

## Complexity

- **Time:** O(log n) — each iteration still discards at least half the
  remaining elements.
- **Space:** O(1) — iterative, only index variables.

[<- Previous](../first-bad-version/README.md) | [Category Index](../README.md) | [Next ->](../find-first-and-last-position-of-element-in-sorted-array/README.md)
