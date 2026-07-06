# Subsets (Easy)

## Problem

Given an array `nums` of unique integers, return all possible subsets (the power set). The solution set must not contain duplicate subsets; subsets may be returned in any order.

**Example 1:**
```
Input:  nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2:**
```
Input:  nums = [0]
Output: [[],[0]]
```

**Constraints:**
- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All elements of `nums` are unique.

## Approach

At each index `i` of `nums`, there are exactly two choices: include `nums[i]` in the current subset, or don't. Backtracking explores both branches:

1. Record the current partial subset as a valid answer immediately (every prefix of choices is itself a complete subset — there's no separate "end" condition beyond running out of indices).
2. Recurse to index `i+1` on the "don't include" path implicitly by iterating forward and choosing which elements to add from the remaining suffix.

A cleaner way to phrase it: at each recursive call starting from index `start`, first append the current subset (a copy) to the result, then loop `i` from `start` to `n-1`, choosing `nums[i]`, recursing with `start = i+1`, and then un-choosing (popping) `nums[i]` before trying the next `i`. Because `i` only moves forward, each subset is generated exactly once and no duplicate-detection is needed since all elements are unique.

The base case is implicit: when `start == n`, the loop simply doesn't execute and the call returns after having already recorded the subset at entry.

## Edge Cases

- **Single element** (`nums = [0]`): produces exactly `[[], [0]]`.
- **Empty subset**: always included as the very first recorded result (recorded before any choice is made).
- **Largest input** (`n = 10`): produces `2^10 = 1024` subsets — well within brute-force backtracking limits.
- Since all elements are guaranteed unique, no duplicate subsets can arise, so no dedup logic is needed.

## Complexity

- **Time:** O(n · 2^n) — there are `2^n` subsets, and copying each subset into the result takes O(n) in the worst case.
- **Space:** O(n) for the recursion stack and the current subset buffer (excluding the output storage itself, which is O(n · 2^n)).

[Category Index](../README.md) | [Next ->](../permutations/README.md)
