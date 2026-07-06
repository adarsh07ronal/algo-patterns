# Climbing Stairs (Easy)

## Problem

You are climbing a staircase with `n` steps. Each time you can climb either 1 or 2 steps. Count the number of distinct ways you can climb to the top.

**Examples:**

- Input: `n = 2` -> Output: `2` (ways: `[1,1]`, `[2]`)
- Input: `n = 3` -> Output: `3` (ways: `[1,1,1]`, `[1,2]`, `[2,1]`)

**Constraints:**

- `1 <= n <= 45`

## Approach

Let `dp[i]` be the number of distinct ways to reach step `i`. To reach step `i`, your last move was either a single step from `i-1`, or a double step from `i-2`. Since these are the only two ways to arrive at `i`, and they lead to disjoint sets of paths, the counts add:

```
dp[i] = dp[i-1] + dp[i-2]
```

Base cases: `dp[1] = 1` (only one way: a single step) and `dp[2] = 2` (either two single steps or one double step). This is exactly the Fibonacci recurrence, which is the textbook example of overlapping subproblems — computing `dp[i]` naively via recursion recomputes `dp[i-2]` many times, which DP (here, simple bottom-up iteration with two rolling variables) avoids.

## Edge Cases

- `n = 1` -> returns `1` directly (only one way, no climbing needed beyond the base step).
- `n = 2` -> returns `2` directly from the base case.
- Larger `n` (up to 45) -> handled by iterating forward with O(1) extra state; values stay within standard integer range.

## Complexity

- **Time:** O(n) — one pass from 3 to n, each step doing O(1) work.
- **Space:** O(1) — only two rolling variables are kept instead of a full array.

[Category Index](../README.md) | [Next ->](../house-robber/README.md)
