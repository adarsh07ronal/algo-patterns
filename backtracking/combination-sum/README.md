# Combination Sum (Medium)

## Problem

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one chosen number differs.

**Example 1:**
```
Input:  candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```

**Example 2:**
```
Input:  candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

**Constraints:**
- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are distinct.
- `1 <= target <= 40`

## Approach

At each recursive step the choice is: "which candidate (starting from the current index onward) do I add next to the running combination?" Because a number can be reused unlimited times, after choosing `candidates[i]` the recursive call stays at index `i` (not `i+1`) so it remains eligible to be picked again. To avoid generating the same combination in different orders (e.g. `[2,3]` and `[3,2]`), candidates are only ever chosen at index `>= start`, meaning once you move past index `i` you can never go back to a smaller index.

The running sum is tracked alongside the combination. Pruning: if adding `candidates[i]` would make the running sum exceed `target`, skip it (and if the array is sorted, break out of the loop entirely since all further candidates are even larger). The base case: if the running sum equals `target`, record a copy of the current combination and return; if it exceeds `target`, back out without recording.

After recursing with a candidate included, the code un-chooses it (pops it and subtracts it from the running sum) before trying the next candidate index — the standard backtracking undo step.

## Edge Cases

- **No valid combination** (e.g. `candidates = [5]`, `target = 3`): the recursion explores and finds nothing, returning `[]`.
- **Target exactly equals one candidate**: that single-element combination is captured (e.g. `[7]` in Example 1).
- **Repeated use of the smallest candidate**: e.g. `[2,2,2,2]` for target 8 with candidate 2 — validates the "stay at index i" reuse logic.
- **Sorting candidates first** enables early-exit pruning (`break` once `candidates[i] > remaining`) which meaningfully cuts down the search space for larger inputs.

## Complexity

- **Time:** O(2^target) in the worst case (loose bound driven by branching over reuse choices up to the target sum); in practice pruning keeps it well below this. Building/copying each valid combination costs O(target / min(candidates)) additional work.
- **Space:** O(target / min(candidates)) for the maximum recursion depth and the current combination buffer, excluding output storage.

[<- Previous](../permutations/README.md) | [Category Index](../README.md) | [Next ->](../combination-sum-ii/README.md)
