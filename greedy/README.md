# Greedy Algorithms

## Pattern

A greedy algorithm builds a solution step by step, at each step making the choice that looks best *right now* — without reconsidering earlier choices — and hoping (or, better, proving) that this sequence of locally optimal choices adds up to a globally optimal solution.

**Justifying a greedy choice is safe.** "It seemed to work on the examples" is not a proof. Two common techniques:

- **Exchange argument:** assume an optimal solution exists that does *not* make the greedy choice. Show you can swap/modify it to make the greedy choice instead without making the solution worse. If every optimal solution can be transformed this way, the greedy choice is safe.
- **No-worse-off / stays-ahead argument:** show that after each greedy step, the greedy solution is at least as good as any other solution could be at the same point (e.g. greedy always has at least as much "slack" or "profit" available going forward).

Both boil down to the same idea: the greedy choice never closes off a path to optimality that matters.

**Recognizing greedy vs. DP.** Greedy tends to work when:

- The problem has *optimal substructure* (an optimal solution to the whole problem contains optimal solutions to subproblems) **and**
- It also has the *greedy-choice property* — a single locally best choice, once made, never needs to be revisited.

If instead the best choice at a step *depends on* choices made later, or you find yourself needing to compare many different partial solutions to know which is really best (i.e., the locally best choice can be wrong in light of future information), that's a signal you need dynamic programming instead. A practical tell: if a greedy strategy fails on some counter-example you can construct (sort order matters, ties matter, a "small" choice now blocks a "big" choice later that you can't undo), the problem usually needs DP or a more careful search rather than greedy.

**[Interview cheatsheet: how to remember and code this pattern from scratch](./interview-cheatsheet.md)**

## Problems

| Difficulty | Problem | Notes |
|---|---|---|
| Easy | [Assign Cookies](./assign-cookies/README.md) | Sort both arrays, match smallest sufficient cookie to smallest greed factor |
| Easy | [Best Time to Buy and Sell Stock II](./best-time-to-buy-and-sell-stock-ii/README.md) | Capture every positive day-to-day price increase |
| Medium | [Jump Game](./jump-game/README.md) | Track the farthest reachable index while scanning left to right |
| Medium | [Gas Station](./gas-station/README.md) | Reset the candidate start whenever the running tank goes negative |
| Medium | [Task Scheduler](./task-scheduler/README.md) | Schedule around the most frequent task using idle-slot arithmetic |
| Medium | [Partition Labels](./partition-labels/README.md) | Extend the current partition to the last occurrence of every letter seen so far |
| Medium | [Non-overlapping Intervals](./non-overlapping-intervals/README.md) | Sort by end time, keep the interval that frees up the earliest |

[<- Back to repo root](../README.md)
