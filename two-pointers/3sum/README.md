# 3Sum (Medium)

## Problem

Given an integer array `nums`, return all unique triplets
`[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, `j != k`, and
`nums[i] + nums[j] + nums[k] == 0`. The result must not contain duplicate
triplets.

**Example 1:**

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Example 2:**

```
Input: nums = [0,1,1]
Output: []
```

**Constraints:**
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Approach

Sort `nums` first. Then fix the smallest element of each candidate triplet
by iterating `i` from left to right, and for the remaining subarray
`nums[i+1:]`, use two opposite-direction pointers `left = i + 1` and
`right = len(nums) - 1` to find pairs that sum to `-nums[i]`.

This reduces the classic O(n^3) brute force (try every triplet) to
O(n^2): sorting turns "find a pair summing to a target" into a solvable
two-pointer subproblem, because in a sorted array, moving `left` right only
increases the pair sum and moving `right` left only decreases it. That
monotonic relationship means at each step we know exactly which pointer to
move — if the current sum is too small, `left` must advance; if too large,
`right` must retreat — until they meet. That's an O(n) scan per fixed `i`
instead of an O(n) inner loop with an O(n) search each (which would still
be quadratic per `i`, cubic overall).

Sorting also makes duplicate elimination easy: skip over repeated values for
`i` (comparing to the previous `i`), and after finding a valid pair, skip
over repeated values for both `left` and `right` before continuing — since
duplicates are now adjacent, this is a cheap linear skip instead of needing
a hash-set of seen triplets.

## Edge Cases

- **Fewer than 3 elements** — return `[]` immediately (loop bounds prevent
  any iteration, or an explicit early check).
- **All zeros** (e.g. `[0,0,0,0]`) — must produce exactly one triplet
  `[0,0,0]`, not four; duplicate-skipping after a match handles this.
- **No triplet sums to zero** (e.g. `[1,2,3]`) — pointers scan through
  without a match, result stays empty.
- **Array already sorted / reverse sorted** — sorting is idempotent /
  handles reverse order, no special-casing needed.
- **Once `nums[i] > 0`**, since the array is sorted, no triplet starting
  from `i` onward can sum to zero (all remaining values are `>= nums[i] > 0`
  after sorting) — this lets us break out of the outer loop early as an
  optimization, though it isn't required for correctness.
- **Negative numbers dominate** — symmetric to the all-positive case, sums
  correctly move `right` inward when the running sum is too small (i.e.
  too negative) — actually handled by the same left/right movement rule
  since we compare against the target directly.

## Complexity

- **Time:** O(n^2) — O(n log n) to sort, then an O(n) outer loop each doing
  an O(n) two-pointer scan.
- **Space:** O(1) extra (excluding the output list and the space used by
  the sort, which is typically O(log n) to O(n) depending on the sort
  implementation).

[<- Previous](../merge-sorted-array/README.md) | [Category Index](../README.md) | [Next ->](../container-with-most-water/README.md)
