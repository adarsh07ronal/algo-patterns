# Longest Common Subsequence (Medium)

## Problem

Given two strings `text1` and `text2`, return the length of their longest common subsequence (LCS) — a sequence that appears in both strings in the same relative order, but not necessarily contiguously. If there is no common subsequence, return `0`.

**Examples:**

- Input: `text1 = "abcde", text2 = "ace"` -> Output: `3` (the LCS is `"ace"`)
- Input: `text1 = "abc", text2 = "def"` -> Output: `0` (no characters in common)

**Constraints:**

- `1 <= text1.length, text2.length <= 1000`
- Both strings consist only of lowercase English characters.

## Approach

Let `dp[i][j]` be the length of the LCS of the prefixes `text1[0:i]` and `text2[0:j]`. Consider the last characters of these prefixes, `text1[i-1]` and `text2[j-1]`:

- If they match, that character must be part of some LCS of the prefixes (extending the best LCS of the strings without that final character), so `dp[i][j] = dp[i-1][j-1] + 1`.
- If they don't match, the LCS can't use both final characters simultaneously, so the best is whichever of dropping the last character of `text1` or dropping the last character of `text2` gives a longer result: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

Base case: `dp[0][j] = dp[i][0] = 0`, since an empty string has no common subsequence with anything. The final answer is `dp[m][n]`. This is a textbook 2D DP: the LCS of two prefixes is built from LCS values of shorter prefixes (optimal substructure), and those smaller LCS values are reused across many `(i, j)` pairs (overlapping subproblems).

## Edge Cases

- One string is empty -> the corresponding row/column of `dp` stays `0`, so the result is `0`.
- No characters in common at all (e.g. `"abc"` vs `"def"`) -> every cell stays `0` since no match ever triggers the diagonal `+1`.
- Identical strings -> the LCS equals the whole string, and `dp[m][n]` correctly reaches `m` (or `n`).
- One string is a subsequence of the other -> `dp[m][n]` equals the length of the shorter string.

## Complexity

- **Time:** O(m * n) — filling every cell of the `(m+1) x (n+1)` table once.
- **Space:** O(m * n) for the full 2D table (can be optimized to O(min(m, n)) with a rolling 1D array, since each row only depends on the row above).

[<- Previous](../word-break/README.md) | [Category Index](../README.md)
