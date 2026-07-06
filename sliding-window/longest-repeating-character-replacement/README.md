# Longest Repeating Character Replacement (Medium)

## Problem

Given a string `s` consisting of uppercase English letters and an integer `k`, you can replace at most `k` characters in the string with any other uppercase letter. Find the length of the longest substring containing the same letter after performing at most `k` replacements.

**Example 1:**
```
Input:  s = "ABAB", k = 2
Output: 4
Explanation: replace the two 'A's (or two 'B's) to get "AAAA" or "BBBB"
```

**Example 2:**
```
Input:  s = "AABABBA", k = 1
Output: 4
Explanation: replace the middle 'A' with 'B' to get "AABBBBA"; the substring "BBBB" has length 4
```

**Constraints:**
- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

## Approach

**Variable-size window.** A window of length `L` is achievable if and only if `L - (count of the window's most frequent character) <= k` — that's exactly the number of characters you'd need to replace to make the whole window one letter, and it must fit within the budget `k`.

Maintain a frequency count of characters in the current window plus `max_freq`, the highest count of any single character currently in the window:

1. **Expand** `right` one step at a time, incrementing the count for `s[right]` and updating `max_freq = max(max_freq, count[s[right]])`.
2. **Check** the validity condition: `(right - left + 1) - max_freq <= k`.
3. **Shrink** from the left (decrementing the outgoing character's count and advancing `left`) only when the window becomes invalid (too many replacements needed).
4. Track the best window length seen.

A subtle but important trick: `max_freq` is **never decremented** even as the window shrinks past its peak. This is safe because the answer only grows when a *larger* window becomes valid, which requires an even higher `max_freq` than any seen before — so a stale (too-high) `max_freq` can only ever cause the window to shrink one extra, harmless step; it can never cause an invalid window to be reported as the answer, since the window size only grows when a strictly better `max_freq` is found to justify it.

## Edge Cases

- **`k >= s.length`**: the whole string can always be made uniform, so the answer is `len(s)`.
- **`k == 0`**: no replacements allowed; the window can only grow while all characters match, equivalent to "longest run of the same character."
- **All same character**: window never needs to shrink; answer is `len(s)`.
- **Empty string**: loop doesn't execute, returns 0.
- **Single character string**: answer is 1 regardless of `k`.

## Complexity

- **Time:** O(n) — `right` advances n times; `left` advances at most n times total across the whole run (amortized O(1) per step) since it never resets backward.
- **Space:** O(1) — the frequency table has at most 26 uppercase-letter entries.

[<- Previous](../longest-substring-without-repeating-characters/README.md) | [Category Index](../README.md) | [Next ->](../minimum-size-subarray-sum/README.md)
