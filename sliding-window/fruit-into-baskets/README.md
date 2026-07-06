# Fruit Into Baskets (Medium)

## Problem

You are visiting a row of fruit trees represented by an array `fruits`, where `fruits[i]` is the type of fruit the `i`-th tree produces. You have exactly two baskets, and each basket can hold only a single type of fruit (unlimited quantity). Starting from any tree, you must pick exactly one fruit from every tree while walking to the right, stopping as soon as you'd need a third basket. Return the maximum number of fruits you can pick.

This is equivalent to: find the length of the longest contiguous subarray that contains at most 2 distinct values.

**Example 1:**
```
Input:  fruits = [1,2,1]
Output: 3
Explanation: pick all three trees (types 1, 2, 1 — only 2 distinct types)
```

**Example 2:**
```
Input:  fruits = [0,1,2,2]
Output: 3
Explanation: [1,2,2] has 3 fruits with 2 distinct types
```

**Constraints:**
- `1 <= fruits.length <= 10^5`
- `0 <= fruits[i] <= fruits.length - 1`

## Approach

**Variable-size window** with the constraint "at most 2 distinct values currently in the window." Maintain a frequency map of fruit type -> count within the window:

1. **Expand** `right` one step at a time, incrementing the count for `fruits[right]` in the map (this may introduce a 3rd distinct type).
2. **Check** whether the map now has more than 2 distinct keys.
3. **Shrink** from the left while there are more than 2 distinct types: decrement the count for `fruits[left]`, and remove its entry entirely once the count hits 0 (so the distinct-key count is accurate), advancing `left`.
4. After each step the window has at most 2 distinct types, so update the best length as `right - left + 1`.

This is structurally identical to "longest substring with at most k distinct characters" with k fixed at 2 — the two baskets are just a story wrapper around the general at-most-k-distinct-values sliding window.

## Edge Cases

- **Only 1 distinct type in the whole array**: the map never exceeds 2 keys, so the window never shrinks; answer is the full array length.
- **Every element distinct**: the window shrinks aggressively, staying at length 2 (or 1 at the very start) throughout — dominant case for a strictly increasing/unique array.
- **Single tree**: trivially returns 1 (0 distinct-key violations possible).
- **Best window at the very end of the array**: since `best` is updated on every valid step (not just when shrinking occurs), no window position is missed.

## Complexity

- **Time:** O(n) — `right` advances n times; `left` advances at most n times total across the whole scan.
- **Space:** O(1) — the frequency map holds at most 3 keys at any instant (2 valid + 1 that triggers a shrink).

[<- Previous](../permutation-in-string/README.md) | [Category Index](../README.md)
