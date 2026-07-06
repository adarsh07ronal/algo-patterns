# House Robber (Easy)

## Problem

You are a professional robber planning to rob houses along a street. Each house has a non-negative amount of money stashed. Adjacent houses have connected security systems, so robbing two adjacent houses on the same night triggers an alarm. Given an array of non-negative integers representing the money in each house, find the maximum amount you can rob without robbing two adjacent houses.

**Examples:**

- Input: `nums = [1,2,3,1]` -> Output: `4` (rob house 0 and house 2: `1 + 3 = 4`)
- Input: `nums = [2,7,9,3,1]` -> Output: `12` (rob houses 0, 2, 4: `2 + 9 + 1 = 12`)

**Constraints:**

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Approach

Define `dp[i]` as the maximum money obtainable considering only houses `0..i`. At house `i` you have two choices:

1. Skip house `i`: the best you can do is whatever was best up to house `i-1`, i.e. `dp[i-1]`.
2. Rob house `i`: you add `nums[i]` to the best result that does *not* include house `i-1`, i.e. `dp[i-2] + nums[i]`.

Taking the max of both choices gives the recurrence:

```
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

This has optimal substructure (the best overall plan is composed of the best plan for a smaller prefix) and overlapping subproblems (both choices at step `i+1` reuse `dp[i]` and `dp[i-1]`), which is exactly what DP exploits. Since each `dp[i]` only depends on the previous two values, we can roll the state into two variables instead of a full array.

## Edge Cases

- Empty list (`nums = []`) -> returns `0`, since there's nothing to rob.
- Single house (`nums = [x]`) -> returns `x`, since robbing the only house is optimal and there's no adjacency conflict.
- Two houses -> returns the max of the two, since robbing both is disallowed.
- All zeros -> returns `0` correctly since every choice sums to zero.

## Complexity

- **Time:** O(n) — a single pass over the houses, O(1) work per house.
- **Space:** O(1) — only two rolling variables (`prev`, `curr`) are tracked.

[<- Previous](../climbing-stairs/README.md) | [Category Index](../README.md) | [Next ->](../coin-change/README.md)
