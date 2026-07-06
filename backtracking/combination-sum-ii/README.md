# Combination Sum II (Medium)

## Problem

Given a collection of candidate numbers `candidates` (which may contain duplicates) and a target integer `target`, return all unique combinations where the candidate numbers sum to `target`. Each number in `candidates` may only be used **once** per combination. The solution set must not contain duplicate combinations.

**Example 1:**
```
Input:  candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

**Example 2:**
```
Input:  candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
```

**Constraints:**
- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Approach

This is Combination Sum with two twists: each element can be used at most once, and the input may contain duplicate values that must not produce duplicate combinations in the output.

First, sort `candidates`. Sorting does two jobs at once: it groups equal values next to each other (making duplicate combinations easy to skip) and it lets the running sum be pruned early (once `candidates[i] > remaining`, every later candidate is at least as large, so `break`).

At each recursive step starting from index `start`, loop `i` from `start` to the end. The choice is "include `candidates[i]` next." Since each element can only be used once, the recursive call moves to `start = i + 1` (not `i`, unlike Combination Sum I). To avoid duplicate combinations caused by duplicate values (e.g. two `1`s in the input), skip index `i` whenever `i > start and candidates[i] == candidates[i-1]` — this means "don't pick the same value again as the *first* choice at this recursion level," while still allowing two equal values to appear together in a combination when the second one is picked as a *follow-up* choice (deeper in the recursion, not skipped there because it's not the first index tried at that level).

The base case: `remaining == 0` records the current combination as a copy. Un-choosing (pop the last element and restore the remaining sum) happens after each recursive call returns, before the loop tries the next index.

## Edge Cases

- **Duplicate candidates** (e.g. two `1`s or three `2`s): the sort + "skip equal sibling at the same recursion depth" rule prevents duplicate combinations like getting `[1,2,5]` twice.
- **No valid combination**: recursion explores fully and returns `[]`.
- **All elements needed to reach target using distinct positions of the same value**: e.g. `[1,2,2]` in Example 2 — two of the three `2`s combine with the `1`, showing duplicates are usable across different recursion depths, just not at the same depth.
- **Candidate larger than target**: pruned immediately by the sorted-array `break`.

## Complexity

- **Time:** O(2^n) worst case (each of the n candidates is either included or not), though sorting adds O(n log n) and duplicate-skipping/pruning substantially reduces the real search space.
- **Space:** O(n) for recursion depth and the current combination buffer, excluding output storage.

[<- Previous](../combination-sum/README.md) | [Category Index](../README.md) | [Next ->](../palindrome-partitioning/README.md)
