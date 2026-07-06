# Contains Duplicate II (Easy)

## Problem

Given an integer array `nums` and an integer `k`, return `true` if there exist two distinct indices `i` and `j` such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

**Example 1:**
```
Input:  nums = [1,2,3,1], k = 3
Output: true
Explanation: nums[0] == nums[3] and abs(0-3) = 3 <= 3
```

**Example 2:**
```
Input:  nums = [1,2,3,1,2,3], k = 2
Output: false
Explanation: matching values are always more than 2 apart
```

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`

## Approach

Reframe "two equal values within distance `k`" as: does a **fixed-size window** of width `k + 1` (positions `i - k ... i`) ever contain a duplicate? That window slides one step at a time as `i` increases, so a hash set makes a good tracker of "what's currently in the window":

1. Walk the array once. For the current index `i`, check whether `nums[i]` is already in the window's set — if so, its matching earlier occurrence is at most `k` positions back, so return `true` immediately.
2. Otherwise add `nums[i]` to the set.
3. Once the window would exceed size `k` (i.e., after processing index `i`, if `i >= k`), remove `nums[i - k]` from the set — that element is about to fall outside the allowed distance for all future indices.

The right edge expands every step (add current element); the left edge shrinks every step once the window reaches its cap of `k+1` elements (remove the element leaving the window). Because the set only ever holds the current window's elements, a hit in step 1 is guaranteed to be within distance `k`.

## Edge Cases

- **`k == 0`**: window size collapses to 1 element, so no two elements can ever be "duplicates within distance 0" (since `i` and `j` must be distinct indices) — correctly returns `false`.
- **`k >= nums.length`**: window never needs to shrink; effectively checks the whole array for any duplicate at all.
- **All identical elements**: returns `true` as soon as `k >= 1` and the array has at least 2 elements.
- **Single-element array**: no pair of distinct indices exists, returns `false`.

## Complexity

- **Time:** O(n) — each element is added to and removed from the set at most once.
- **Space:** O(min(n, k)) — the set never holds more than `k + 1` elements at a time.

[<- Previous](../maximum-average-subarray-i/README.md) | [Category Index](../README.md) | [Next ->](../longest-substring-without-repeating-characters/README.md)
