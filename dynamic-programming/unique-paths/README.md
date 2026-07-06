# Unique Paths (Medium)

## Problem

A robot is located at the top-left corner of an `m x n` grid. It can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. Count how many unique paths exist.

**Examples:**

- Input: `m = 3, n = 7` -> Output: `28`
- Input: `m = 3, n = 2` -> Output: `3` (paths: right-down-down, down-right-down, down-down-right)

**Constraints:**

- `1 <= m, n <= 100`
- The answer is guaranteed to fit in a 32-bit integer.

## Approach

Let `dp[i][j]` be the number of unique paths from the top-left corner to cell `(i, j)`. The robot can only arrive at `(i, j)` from directly above `(i-1, j)` or directly to the left `(i, j-1)`, so the number of ways to reach `(i, j)` is the sum of the ways to reach those two predecessor cells:

```
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

Base case: the entire first row and first column are all `1`, since there's exactly one way to reach any cell along the top edge (all rights) or left edge (all downs) — no choices are available. This is optimal substructure (any path to `(i,j)` decomposes into a path to a predecessor cell plus one move) with overlapping subproblems (many paths share the same prefix cells).

Because each row only depends on the row above it and cells to its left, the 2D table can be collapsed into a single 1D array of size `n`, updated in place left-to-right, row-by-row.

## Edge Cases

- `m = 1` or `n = 1` -> only one path exists (a straight line), since the 1D `dp` array stays all `1`s.
- `m = 1 and n = 1` -> robot starts at the destination, so there's exactly `1` trivial path.
- Square grid (`m == n`) -> the recurrence still applies symmetrically; result is the binomial coefficient `C(m+n-2, m-1)`.

## Complexity

- **Time:** O(m * n) — every cell in the grid is visited once.
- **Space:** O(n) — using the rolling 1D array optimization instead of a full 2D table.

[<- Previous](../longest-increasing-subsequence/README.md) | [Category Index](../README.md) | [Next ->](../word-break/README.md)
