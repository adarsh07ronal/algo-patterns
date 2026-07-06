# Palindrome Partitioning (Medium)

## Problem

Given a string `s`, partition it such that every substring of the partition is a palindrome. Return all possible palindrome partitionings of `s`.

**Example 1:**
```
Input:  s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

**Example 2:**
```
Input:  s = "a"
Output: [["a"]]
```

**Constraints:**
- `1 <= s.length <= 16`
- `s` consists only of lowercase English letters.

## Approach

The choice at each recursive step is "where does the next cut go?" — equivalently, "how long is the next palindromic substring starting at the current position?" Starting from index `start`, try every possible end index `end` for the next piece (`s[start:end]`). If that piece is a palindrome, it's a valid choice: append it to the current partition, recurse on the remainder starting at `end`, then remove it (undo) before trying a longer piece.

The base case is `start == len(s)`: the whole string has been consumed by valid palindromic pieces, so the current partition is complete and gets recorded as a copy.

The pruning here is the palindrome check itself — a substring that isn't a palindrome is never explored further, since any partition that includes it can never be all-palindrome. Checking palindromes with a simple `s == s[::-1]` (or two-pointer check) at each candidate cut keeps the branching factor low in practice, since most substrings of random strings aren't palindromes. For repeated palindrome checks on the same string, this can optionally be sped up with precomputed DP table `is_pal[i][j]`, but a direct check is sufficient given the small constraint (`length <= 16`).

## Edge Cases

- **Single character** (`s = "a"`): every single character is trivially a palindrome, so the only partition is `[["a"]]`.
- **Entire string is a palindrome** (e.g. `"aba"`): includes the whole-string partition `[["aba"]]` alongside finer-grained ones.
- **No repeated characters** (e.g. `"abc"`): only the all-singletons partition `[["a","b","c"]]` is valid, since no multi-character substring is a palindrome.
- **All identical characters** (e.g. `"aaaa"`): produces many valid partitions since every substring is a palindrome — exercises the full exponential branching.

## Complexity

- **Time:** O(n · 2^n) worst case — there are up to `2^(n-1)` ways to partition a string of length n, and each palindrome check/copy costs O(n).
- **Space:** O(n) for the recursion depth and current partition buffer, excluding output storage which can be O(n · 2^n) in the worst case (e.g. all identical characters).

[<- Previous](../combination-sum-ii/README.md) | [Category Index](../README.md) | [Next ->](../word-search/README.md)
