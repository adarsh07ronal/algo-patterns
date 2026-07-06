# Minimum Size Subarray Sum (Medium)

## Problem

Given an array of positive integers `nums` and a positive integer `target`, find the minimal length of a contiguous subarray whose sum is greater than or equal to `target`. If no such subarray exists, return 0.

**Example 1:**
```
Input:  target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has sum 7 and is the shortest such subarray
```

**Example 2:**
```
Input:  target = 4, nums = [1,4,4]
Output: 1
```

**Constraints:**
- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

## Approach

**Variable-size window**, and specifically the "grow until valid, then shrink to find the minimum" flavor — the mirror image of problems that shrink until *invalid*.

Because all elements are positive, the running window sum only increases as `right` advances and only decreases as `left` advances — this monotonicity is what makes the two-pointer approach correct (it wouldn't work directly with negative numbers, since shrinking the window wouldn't reliably decrease the sum below target).

1. **Expand** `right` one step at a time, adding `nums[right]` to a running `window_sum`.
2. **Check** whether `window_sum >= target`. If not yet, keep expanding.
3. Once the window is valid (sum meets target), **shrink** from the left as much as possible while it remains valid, recording the window length at each step — this finds the shortest valid window ending at the current `right`.
4. Track the minimum length found across all `right` positions.

Expanding is triggered by "not enough sum yet"; shrinking is triggered by "sum already meets target, can we do better by removing from the left?"

## Edge Cases

- **No valid subarray exists** (e.g., `target` larger than the total sum of the array): the window never reaches `target`; return 0 (the "no answer found" sentinel, tracked by initializing best length to infinity and checking if it was ever updated).
- **A single element already meets target**: window shrinks immediately back to length 1 at that position.
- **Entire array required**: the window only becomes valid once it spans the whole array.
- **`target` very small (e.g., 1) with smallest element = 1**: shortest window is length 1, found immediately.

## Complexity

- **Time:** O(n) — `right` advances n times; `left` advances at most n times total across the entire scan since it never resets backward.
- **Space:** O(1) — only the running sum, window bounds, and best-length counter are stored.

[<- Previous](../longest-repeating-character-replacement/README.md) | [Category Index](../README.md) | [Next ->](../permutation-in-string/README.md)
