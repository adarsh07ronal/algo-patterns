# Maximum Average Subarray I (Easy)

## Problem

Given an integer array `nums` and an integer `k`, find a contiguous subarray of length exactly `k` that has the maximum average value, and return that average.

**Example 1:**
```
Input:  nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: subarray [12,-5,-6,50] has sum 51, average 51/4 = 12.75
```

**Example 2:**
```
Input:  nums = [5], k = 1
Output: 5.0
```

**Constraints:**
- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Approach

This is the canonical **fixed-size window**: the width `k` never changes, so instead of summing each of the `n - k + 1` windows from scratch (O(n*k)), maintain a running sum and slide it:

1. Compute the sum of the first `k` elements — this is the initial window.
2. Slide the window one position at a time: adding `nums[right]` (the element entering on the right) and subtracting `nums[right - k]` (the element leaving on the left) keeps the running sum correct in O(1) per step.
3. Track the maximum sum seen across all windows, then divide by `k` once at the end (dividing every step is unnecessary work — the window with the max sum also has the max average since `k` is constant).

The right edge always expands (advances) and the left edge always shrinks in lockstep, exactly `k` apart — there's no separate "shrink until valid" phase because the window is never invalid, just repositioned.

## Edge Cases

- **`k == nums.length`**: only one window exists (the whole array); the loop that slides beyond the initial window simply doesn't execute.
- **`k == 1`**: every single element is its own window; the answer is `max(nums)`.
- **All negative numbers**: works unmodified since we track the running sum's maximum, not just positive contributions.
- **Single-element array**: trivially returns that element as a float.

## Complexity

- **Time:** O(n) — one pass to build the initial sum, one pass to slide across the rest.
- **Space:** O(1) — only the running sum and the best-sum-so-far are stored.

[Category Index](../README.md) | [Next ->](../contains-duplicate-ii/README.md)
