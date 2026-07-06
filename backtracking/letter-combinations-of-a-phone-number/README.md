# Letter Combinations of a Phone Number (Medium)

## Problem

Given a string `digits` containing digits from `2` to `9` inclusive, return all possible letter combinations that the number could represent, using the standard telephone keypad mapping (as on old phone keypads). Return the answer in any order.

The mapping is: `2`->"abc", `3`->"def", `4`->"ghi", `5`->"jkl", `6`->"mno", `7`->"pqrs", `8`->"tuv", `9`->"wxyz".

**Example 1:**
```
Input:  digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Example 2:**
```
Input:  digits = ""
Output: []
```

**Example 3:**
```
Input:  digits = "2"
Output: ["a","b","c"]
```

**Constraints:**
- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.

## Approach

At each recursive step, the current digit at position `index` determines the set of letter choices available — for example digit `'2'` offers `{a, b, c}`. The choice is "which letter do I append for this digit?" Try each letter mapped to `digits[index]`: append it to the current combination, recurse to `index + 1` to handle the next digit, then remove it (undo) before trying the next letter for the current digit.

The base case is `index == len(digits)`: every digit has been assigned a letter, so the current combination is complete and gets recorded (as a string join or already-built string). Because every digit maps to a small fixed set of letters (3 or 4), there's no invalid state to prune — every combination of choices is valid, so this is really an enumeration over the Cartesian product of the per-digit letter sets, implemented via backtracking for clarity and to build the combinations incrementally.

## Edge Cases

- **Empty input** (`digits = ""`): should return `[]` (not `[""]`) — handled with an explicit early return before starting the recursion, since the problem defines no combinations for an empty digit string.
- **Single digit** (`digits = "2"`): returns exactly the 3 (or 4, for `7`/`9`) letters mapped to that digit as single-character strings.
- **Digits with 4 letters** (`7` -> "pqrs", `9` -> "wxyz"): the letter set size varies per digit, so the mapping lookup must handle both 3- and 4-letter groups correctly.
- **Maximum length input** (4 digits): at most `4^4 = 256` combinations, trivial for backtracking.

## Complexity

- **Time:** O(4^n · n) where n = `len(digits)` — worst case every digit maps to 4 letters, giving up to `4^n` combinations, each of length n to build.
- **Space:** O(n) for the recursion depth and current combination buffer, excluding output storage.

[<- Previous](../word-search/README.md) | [Category Index](../README.md)
