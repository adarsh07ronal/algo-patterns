# Find Peak Element (Medium)

## Problem

A peak element is an element strictly greater than its neighbors. Given an
integer array `nums` where `nums[i] != nums[i+1]` for all valid `i`, find
any peak element and return its index. Assume `nums[-1] = nums[n] = -infinity`
(so the array's boundaries always count as valid neighbors). Must run in
O(log n) time.

**Examples**

```
Input: nums = [1,2,3,1]
Output: 2          # nums[2] = 3 is a peak

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5      # both are valid peaks
```

**Constraints**
- `1 <= nums.length <= 1000`.
- `nums[i] != nums[i+1]` for all adjacent pairs.

## Approach

We binary search over indices using the **local slope** as the monotonic-ish
signal (it's not global monotonicity, but the key guarantee is: whichever
direction the slope at `mid` points, a peak is guaranteed to exist in that
direction). Compare `nums[mid]` to `nums[mid + 1]`:

- If `nums[mid] < nums[mid + 1]`, the sequence is rising at `mid`, so
  walking right must eventually hit a peak (worst case, the last element,
  which has `-infinity` as its right neighbor). Discard the left half:
  `lo = mid + 1`.
- If `nums[mid] > nums[mid + 1]` (guaranteed distinct, so no equality case),
  the sequence is falling at `mid`, so a peak must exist at `mid` or
  somewhere to the left. Discard the right half: `hi = mid`.

Using the half-open `[lo, hi)` template with `hi = n - 1` initially (so `mid`
never reads `nums[mid + 1]` out of bounds), the interval shrinks every
iteration and always contains at least one peak, because a boundary is
implicitly `-infinity` on both ends. When `lo == hi`, that index is
necessarily a peak.

## Edge Cases

- Single-element array: no comparisons needed, `lo == hi == 0` is trivially
  a peak (both neighbors are the implicit `-infinity`).
- Strictly increasing array: every comparison pushes right, converging on
  the last index, which is a valid peak since its right neighbor is
  `-infinity`.
- Strictly decreasing array: every comparison pushes left, converging on
  index 0.
- Multiple peaks present: the algorithm returns whichever one the binary
  search path happens to land on — any is acceptable per the problem.
- Peak at index 0 or `n - 1`: handled naturally by the `-infinity` boundary
  convention baked into the comparisons.

## Complexity

- **Time:** O(log n) — each step halves the search interval.
- **Space:** O(1) — only index variables.

[<- Previous](../koko-eating-bananas/README.md) | [Category Index](../README.md)
