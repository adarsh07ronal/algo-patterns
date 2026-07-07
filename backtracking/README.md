# Backtracking

## Pattern

Backtracking is a systematic way to search a combinatorial state space by building a solution incrementally, and abandoning ("backtracking out of") a partial solution as soon as it's clear it cannot lead to a valid answer. It's essentially depth-first search over a decision tree where each node represents a partial candidate solution.

The general template:

```
def backtrack(state, choices):
    if state is a complete solution:
        record(state)
        return

    for choice in choices:
        if choice is not valid given state:
            continue                # prune

        make(choice)                # choose
        backtrack(state, remaining_choices)   # explore
        undo(choice)                # un-choose (backtrack)
```

The three steps — **choose**, **explore**, **un-choose** — are the heart of the pattern. Mutating shared state (a running list, a visited set, a grid cell) in place and then undoing the mutation after the recursive call returns is what makes backtracking memory-efficient compared to copying state at every level.

Reach for backtracking when:
- You need to enumerate **all** solutions (all subsets, all permutations, all paths) rather than just one.
- Or you need to determine **existence** of a solution (does a path exist?) and can stop early once found.
- The problem has a natural recursive/tree-shaped decision structure (pick this or don't, place this here or not).
- **Pruning** (cutting off branches early based on a constraint, like "sum already exceeds target") can make an otherwise exponential search tractable in practice.

**[Interview cheatsheet: how to remember and code this pattern from scratch](./interview-cheatsheet.md)**

## Problems

| Difficulty | Problem | Notes |
|---|---|---|
| easy | [Subsets](./subsets/README.md) | Include/exclude decision at each index |
| easy | [Permutations](./permutations/README.md) | Track used elements, swap or visited-set approach |
| medium | [Combination Sum](./combination-sum/README.md) | Unlimited reuse of candidates, prune on running sum |
| medium | [Combination Sum II](./combination-sum-ii/README.md) | Single use per candidate, dedupe via sorting + skip |
| medium | [Palindrome Partitioning](./palindrome-partitioning/README.md) | Choice = where to cut next, validity check = palindrome |
| medium | [Word Search](./word-search/README.md) | Grid DFS with in-place visited marking |
| medium | [Letter Combinations of a Phone Number](./letter-combinations-of-a-phone-number/README.md) | Choice = which letter for current digit |

[<- Back to repo root](../README.md)
