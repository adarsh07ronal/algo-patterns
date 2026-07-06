# Longest Increasing Subsequence (Medium)

## Problem

Given an integer array `nums`, return the length of the longest strictly increasing subsequence (elements don't need to be contiguous, but must preserve relative order).

**Examples:**

- Input: `nums = [10,9,2,5,3,7,101,18]` -> Output: `4` (one such subsequence: `[2,3,7,101]` or `[2,3,7,18]`)
- Input: `nums = [7,7,7,7]` -> Output: `1` (no strictly increasing pair exists, so the best is a single element)

**Constraints:**

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

## Approach

**Classic O(n^2) DP:** define `dp[i]` as the length of the longest increasing subsequence that *ends* at index `i`. For each `i`, look at every earlier index `j < i`: if `nums[j] < nums[i]`, then `nums[i]` could extend the subsequence ending at `j`, giving a candidate length `dp[j] + 1`. Taking the max over all valid `j` (or `1` if none extend, meaning `nums[i]` starts its own subsequence):

```
dp[i] = max(dp[j] + 1 for all j < i where nums[j] < nums[i]), else 1
```

The answer is `max(dp)` over all `i`, since the LIS could end anywhere. This has overlapping subproblems because `dp[i]` for different `i` all draw on the same set of smaller `dp[j]` values.

**Faster O(n log n) approach (used in the solution):** maintain a list `tails` where `tails[k]` is the smallest possible tail value of an increasing subsequence of length `k+1` seen so far. For each new number `x`, binary-search for the first position in `tails` that is `>= x` and overwrite it (or append `x` if it's larger than everything currently in `tails`). `tails` doesn't represent an actual subsequence, but its length always equals the LIS length, because keeping tail values as small as possible maximizes the chance of future extensions. This works because replacing a larger tail with a smaller one can only help extend subsequences later, never hurt.

## Edge Cases

- Single element -> `tails` gets one entry, so the answer is `1`.
- All equal elements (e.g. `[7,7,7,7]`) -> since the comparison is strict (`<`), each new `7` overwrites `tails[0]` instead of extending, so the final length stays `1`.
- Strictly decreasing array -> every new element replaces `tails[0]`, so the answer is `1`.
- Strictly increasing array -> every element appends to `tails`, so the answer equals the array length.

## Complexity

- **Time:** O(n log n) — n elements, each doing a binary search (`bisect_left`) over `tails`, which has size at most n.
- **Space:** O(n) — the `tails` array can grow up to size n in the worst case.

[<- Previous](../coin-change/README.md) | [Category Index](../README.md) | [Next ->](../unique-paths/README.md)
