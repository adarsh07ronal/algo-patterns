# Permutations (Easy)

## Problem

Given an array `nums` of distinct integers, return all possible permutations, in any order.

**Example 1:**
```
Input:  nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2:**
```
Input:  nums = [0,1]
Output: [[0,1],[1,0]]
```

**Constraints:**
- `1 <= nums.length <= 6`
- All integers in `nums` are distinct.
- `-10 <= nums[i] <= 10`

## Approach

Build each permutation position by position. At each recursive step, the choice is: "which unused number goes in the next slot of the current permutation?" Try every number not yet used, place it, recurse to fill the next slot, then remove it (un-choose) before trying the next candidate — this is the classic choose/explore/un-choose loop.

A `used` boolean array (or a set) tracks which numbers are already placed so the same value isn't picked twice in one permutation. The base case is reached when the current permutation's length equals `len(nums)`; at that point it's a complete permutation and gets recorded as a copy.

Because every element is distinct and every permutation is built by trying all not-yet-used values at each slot, every ordering is generated exactly once, with no duplicate-skipping logic required.

## Edge Cases

- **Single element** (`nums = [5]`): only one permutation, `[[5]]`.
- **Two elements**: exactly `2! = 2` permutations, matches Example 2.
- **Largest input** (`n = 6`): `6! = 720` permutations, small enough for straightforward backtracking.
- All values are guaranteed distinct, so there is no risk of generating duplicate permutations from equal values.

## Complexity

- **Time:** O(n · n!) — there are `n!` permutations, each taking O(n) to copy into the result and O(n) work per recursive level to scan for an unused element.
- **Space:** O(n) for the recursion depth, the `used` tracking structure, and the current permutation buffer (excluding output storage, which is O(n · n!)).

[<- Previous](../subsets/README.md) | [Category Index](../README.md) | [Next ->](../combination-sum/README.md)
