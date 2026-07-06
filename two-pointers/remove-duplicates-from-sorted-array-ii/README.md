# Remove Duplicates from Sorted Array II (Medium)

## Problem

Given an integer array `nums` sorted in non-decreasing order, remove some
duplicates in-place such that each unique element appears at most **twice**.
The relative order of elements should be kept. Return `k`, the number of
elements after removal, where the first `k` elements of `nums` hold the
final result (elements after index `k` don't matter).

**Example 1:**

```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
```

**Example 2:**

```
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
```

**Constraints:**
- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.

## Approach

Use fast/slow same-direction pointers. `slow` (call it `k`) marks the next
position to write a "kept" element; `fast` scans through every element of
the original array. For each `nums[fast]`, decide whether it belongs in the
output by comparing it to the element **two positions before** the current
write position: `nums[k - 2]`. If `nums[fast] != nums[k - 2]` (or `k < 2`,
meaning fewer than two elements have been written yet), it's safe to keep —
write it to `nums[k]` and advance `k`.

Why this is correct: because the input is sorted, all duplicates of a value
are contiguous. Comparing against `nums[k-2]` (the last-but-one element
already accepted) tells us exactly how many copies of the current value
have already been kept, without needing a separate counter — if the value
two-back in the *output* matches the current value, then the output already
contains two copies of it, so a third must be dropped. Since the output is
built incrementally and only ever contains valid runs of at most two, this
lookback is always comparing against a real, correctly-placed value. This
achieves the in-place O(n) compaction directly, in one forward pass, versus
a brute-force approach that would repeatedly search-and-shift-left
every time a disallowed duplicate is found (O(n^2) in the worst case of
many duplicates).

## Edge Cases

- **Length <= 2** — every element is trivially allowed at most twice, so
  `k < 2` short-circuits and everything is kept, returning the original
  length.
- **All identical elements** (e.g. `[2,2,2,2]`) — only the first two are
  kept; `k` stops advancing after 2 and the function returns `2`.
- **No duplicates at all** — every comparison against `nums[k-2]` fails
  (values are strictly increasing), so every element is kept and `k`
  equals the original length.
- **Duplicates exactly at the "allowed twice" boundary** — a run of exactly
  two identical values is fully kept since the third occurrence never
  arises to compare against.
- **Negative numbers** — comparison logic is value-agnostic; works
  identically for negative, zero, or positive values.

## Complexity

- **Time:** O(n) — `fast` visits every element exactly once; `slow`/`k`
  only ever moves forward, and the lookback comparison is O(1).
- **Space:** O(1) — modifies `nums` in place using two index variables.

[<- Previous](../sort-colors/README.md) | [Category Index](../README.md) | [Next ->](../boats-to-save-people/README.md)
