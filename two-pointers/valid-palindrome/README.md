# Valid Palindrome (Easy)

## Problem

Given a string `s`, determine if it is a palindrome, considering only
alphanumeric characters and ignoring case.

**Example 1:**

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

**Constraints:**
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Approach

Use two pointers, `left` starting at index 0 and `right` starting at the
last index, moving toward each other. At each step, skip over any character
that isn't alphanumeric by advancing the relevant pointer without comparing
anything. Once both pointers rest on alphanumeric characters, compare them
case-insensitively; if they differ, the string isn't a palindrome. If they
match, move both pointers inward and repeat until they meet or cross.

This is correct because a palindrome is defined by symmetry around the
center: the first "real" character must match the last "real" character,
the second must match the second-to-last, and so on. Two pointers closing
in from both ends check exactly this symmetry condition directly, in one
pass, without building a cleaned-up copy of the string (which would cost
extra space) or comparing every pair of positions (which would be
wasteful/incorrect anyway — palindrome-checking only ever needs the mirrored
pairs, not all pairs).

## Edge Cases

- **Empty-after-filtering string** (e.g. `",."`) — pointers cross without
  ever comparing anything, loop ends, correctly returns `true` (vacuously a
  palindrome).
- **Single character** — `left == right` immediately, loop body never runs
  a mismatched comparison, returns `true`.
- **All non-alphanumeric characters** — same as the empty-after-filtering
  case; both pointers skip past each other and meet, returns `true`.
- **Mixed case letters** — handled by lowercasing (or case-insensitive
  compare) before comparing.
- **Even vs. odd length effective strings** — the `left < right` loop
  condition naturally stops at the middle for both parities; no special
  casing needed.

## Complexity

- **Time:** O(n) — each pointer visits each index at most once; total work
  is linear in the length of `s`.
- **Space:** O(1) — only two index variables are used; no copy of the
  string is created.

[Category Index](../README.md) | [Next ->](../merge-sorted-array/README.md)
