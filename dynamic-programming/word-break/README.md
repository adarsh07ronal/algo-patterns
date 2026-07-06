# Word Break (Medium)

## Problem

Given a string `s` and a dictionary of strings `wordDict`, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words. The same dictionary word may be reused multiple times in the segmentation.

**Examples:**

- Input: `s = "leetcode", wordDict = ["leet","code"]` -> Output: `true` (`"leet" + "code"`)
- Input: `s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]` -> Output: `false` (no valid segmentation covers the whole string)

**Constraints:**

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- Each word in `wordDict` is non-empty.

## Approach

Let `dp[i]` be `True` if the prefix `s[0:i]` can be fully segmented into dictionary words. To determine `dp[i]`, consider every split point `j < i`: if `s[0:j]` is already known to be segmentable (`dp[j]` is `True`) and the remaining chunk `s[j:i]` is itself a dictionary word, then `s[0:i]` is segmentable too:

```
dp[i] = True if there exists j < i such that dp[j] is True and s[j:i] in wordDict
dp[0] = True   (empty prefix trivially "segments" into zero words)
```

The answer is `dp[len(s)]`. This is DP because the feasibility of segmenting a prefix depends only on the feasibility of segmenting shorter prefixes (optimal/feasible substructure), and those shorter prefixes are reused across many different candidate split points (overlapping subproblems) — a naive recursive solution without caching would re-examine the same prefixes exponentially many times.

Using a `set` for `wordDict` makes the `s[j:i] in words` membership check O(1) on average (amortized over word length for hashing).

## Edge Cases

- Empty dictionary (`wordDict = []`) -> no `s[j:i]` can ever match, so `dp` stays all `False` (except `dp[0]`) and the result is `False` unless `s` is empty.
- `s` exactly equals one dictionary word -> `dp[len(s)]` becomes `True` via the single split `j=0`.
- Word dictionary requires reusing a word multiple times (e.g. `"applepenapple"` with `["apple","pen"]`) -> handled naturally since `dp` doesn't track which words were used, only whether a prefix is reachable.
- No valid segmentation exists -> `dp[len(s)]` remains `False`.

## Complexity

- **Time:** O(n^2 * k) where n is `len(s)` and k is the average word length (from slicing/hashing substrings); often approximated as O(n^2) for reasoning purposes since substring slicing costs are typically small relative to n.
- **Space:** O(n) for the `dp` array, plus O(sum of word lengths) for the word set.

[<- Previous](../unique-paths/README.md) | [Category Index](../README.md) | [Next ->](../longest-common-subsequence/README.md)
