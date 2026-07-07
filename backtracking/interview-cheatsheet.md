# Backtracking: How to Remember and Code It in an Interview

Subsets, Permutations, Combination Sum (and its variants) all come from the *same* 6-line skeleton. Don't memorize each problem's code separately — memorize the skeleton once, then know which 3 knobs to turn.

## The universal skeleton

```python
def solve(...):
    result = []
    path = []

    def backtrack(start, ...):
        if <base case>:
            result.append(path[:])
            return                # sometimes omitted — see below

        for i in range(<loop range>):
            if <skip condition>:
                continue

            path.append(choice)          # CHOOSE
            backtrack(<next state>)      # EXPLORE
            path.pop()                   # UN-CHOOSE

    backtrack(<initial state>)
    return result
```

Say "**choose, explore, un-choose**" out loud while writing the 3 lines inside the loop — that's the muscle memory to build, not the whole function.

## The only 3 things that change between problems

| | Subsets | Permutations | Combination Sum |
|---|---|---|---|
| **Base case** | none — append at *every* node | `len(path) == len(nums)` | `remaining == 0` |
| **Loop range** | `range(start, n)` | `range(0, n)` (always full range) | `range(start, n)` |
| **Next recursive call** | `backtrack(i+1)` | `backtrack()` + `used[i]` flag | `backtrack(i)` — **same** `i` |
| **Why** | never revisit an earlier index → no duplicate subsets | order matters, so every position is considered every time; `used[]` blocks reuse instead of `start` | same element reusable unlimited times, so don't advance past `i` |

That table *is* the thing to memorize — 3 rows, not 3 programs. See [`subsets`](./subsets/README.md), [`permutations`](./permutations/README.md), and [`combination-sum`](./combination-sum/README.md) for the fully worked, traced versions this table summarizes.

## Decision checklist (run this in your head the moment you spot "this is backtracking")

1. **Does order matter?** (`[1,2]` vs `[2,1]` — different answers?)
   - Yes → permutation-style: loop full `range(0, n)` every time, use a `used[]` array.
   - No → combination-style: loop `range(start, n)`, never go backwards.
2. **Can the same element be reused multiple times?**
   - Yes (Combination Sum) → recurse with `backtrack(i, ...)`.
   - No (Combination Sum II, Subsets) → recurse with `backtrack(i+1, ...)`.
3. **When do I record an answer?**
   - Every node, unconditionally → Subsets-style (no `if`, no `return`, just fall through the loop).
   - Only when some condition hits (`remaining == 0`, `len(path) == n`) → append inside an `if`, then `return`.
4. **Do I need to skip duplicates?** (input has repeated values, e.g. `[1, 1, 2]`)
   - Sort first, then in the loop: `if i > start and nums[i] == nums[i-1]: continue`.
5. **Can I prune early?**
   - Sort first, then: `if nums[i] > remaining: break` (not `continue` — everything after is bigger too, since the array is sorted).

## How to drill this so it's automatic

- Don't re-derive from scratch each time — **type the 6-line skeleton from memory, blank**, 5-10 times until your hands know it without thinking.
- Then for each of the classic problems (Subsets, Permutations, Combination Sum, Combination Sum II), just fill in the 3 blanks from the table above.
- Before declaring the code done in an interview: **hand-trace `n=2` or `n=3`** on paper/whiteboard. It catches the off-by-one in `i` vs `i+1` immediately, and interviewers explicitly want to see you verify your own code.
- Say the plan out loud *before* coding: "I'll backtrack — choose an element, recurse, undo. Since [order doesn't matter / duplicates are allowed / whatever], I'll advance the start index by [`i` / `i+1`] and use `range(start, n)`." That sentence alone answers 3 of the 4 checklist questions and shows the interviewer you're pattern-matching, not memorizing.

[<- Back to Backtracking index](./README.md)
