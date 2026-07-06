# Permutation in String (Medium)

## Problem

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1` as a contiguous substring (i.e., some contiguous substring of `s2` is an anagram of `s1`).

**Example 1:**
```
Input:  s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: "ba" is a substring of s2 and is a permutation of "ab"
```

**Example 2:**
```
Input:  s1 = "ab", s2 = "eidboaoo"
Output: false
```

**Constraints:**
- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.

## Approach

A permutation of `s1` occupying a contiguous span of `s2` means: some window of `s2` with length `len(s1)` has *exactly the same character frequency counts* as `s1`. That length constraint makes this a **fixed-size window** (width `len(s1)`), slid across `s2`.

1. Build a target frequency count for `s1` and an initial frequency count for the first `len(s1)` characters of `s2`.
2. Slide the window across `s2` one character at a time: adding the incoming right character's count and removing the outgoing left character's count — exactly like the fixed-window sum problems, but with a frequency vector instead of a single number.
3. After each slide, compare the window's frequency count to `s1`'s target count. If they match, a permutation was found.

To avoid an O(26) comparison at every single window position, track a single integer `matches` = "how many of the 26 letters currently have equal counts between window and target." Incrementing/decrementing `matches` only when a letter's count transitions into or out of equality (as it's updated) keeps each slide step O(1) amortized, so the whole scan is O(n).

## Edge Cases

- **`len(s1) > len(s2)`**: no window of that size can fit; return `false` immediately without entering the main loop.
- **`s1 == s2`**: the initial window itself is already a match.
- **Repeated characters in `s1`** (e.g., `"aab"`): frequency-count comparison naturally handles this correctly, unlike a plain character-set comparison.
- **No permutation exists anywhere**: the loop completes without any window matching; return `false`.

## Complexity

- **Time:** O(n + m) where `n = len(s2)`, `m = len(s1)` — O(m) to build the initial counts, O(n) to slide across the rest with O(1) work per step.
- **Space:** O(1) — frequency counts are fixed-size arrays of 26 lowercase letters.

[<- Previous](../minimum-size-subarray-sum/README.md) | [Category Index](../README.md) | [Next ->](../fruit-into-baskets/README.md)
