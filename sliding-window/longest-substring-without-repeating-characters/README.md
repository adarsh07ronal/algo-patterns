# Longest Substring Without Repeating Characters (Medium)

## Problem

Given a string `s`, find the length of the longest substring without repeating characters.

**Example 1:**
```
Input:  s = "abcabcbb"
Output: 3
Explanation: the answer is "abc", with length 3
```

**Example 2:**
```
Input:  s = "bbbbb"
Output: 1
Explanation: the answer is "b", with length 1
```

**Constraints:**
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces.

## Approach

This is a **variable-size window**. There's no target width — the window should grow as long as all characters inside it are unique, and only shrink when a repeat is forced.

Track a hash map of `character -> most recent index seen`, plus `left`, the current window's start:

1. **Expand** by advancing `right` through the string one character at a time, adding `s[right]` to the map.
2. **Check** whether `s[right]` was already seen *inside the current window* (i.e., its last-seen index is `>= left`). If so, the window now contains a duplicate.
3. **Shrink** by jumping `left` directly to `last_seen[s[right]] + 1` — no need to shrink one step at a time, since we know exactly where the offending duplicate is.
4. After each step, the window `[left, right]` is guaranteed duplicate-free, so update the best length as `right - left + 1`.

The key insight that makes this O(n) instead of O(n^2): `left` only ever moves forward, and jumping it straight to `last_seen + 1` avoids re-scanning the window to find the duplicate.

## Edge Cases

- **Empty string**: loop body never executes, returns 0.
- **All identical characters** (`"bbbbb"`): every new character forces `left` to jump right up to (and past) the previous occurrence, keeping the window at length 1.
- **All unique characters**: window never shrinks; answer is the full string length.
- **Repeated character whose last occurrence is *before* the current window** (e.g., `"abba"` at the final `a`): the naive check `char in map` would wrongly shrink past valid characters, so the condition must also verify `last_seen[char] >= left`, not just that the character was ever seen.

## Complexity

- **Time:** O(n) — `right` advances n times; `left` also only advances forward, never backward, across the whole scan.
- **Space:** O(min(n, alphabet size)) for the last-seen-index map.

[<- Previous](../contains-duplicate-ii/README.md) | [Category Index](../README.md) | [Next ->](../longest-repeating-character-replacement/README.md)
