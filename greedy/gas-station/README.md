# Gas Station (Medium)

## Problem

There are `n` gas stations arranged in a circle. `gas[i]` is the amount of gas at station `i`, and `cost[i]` is the gas needed to travel from station `i` to station `i + 1`. Starting with an empty tank at some station, return the index of the starting station that lets you complete the entire circuit (going in one direction), or `-1` if no such station exists. It is guaranteed that if a solution exists, it is unique. The total gas is guaranteed to be either sufficient or insufficient for the whole trip (used to decide feasibility).

**Examples:**

- Input: `gas = [1, 2, 3, 4, 5]`, `cost = [3, 4, 5, 1, 2]` -> Output: `3` (starting at station 3: tank goes 4 -> 3(+5-2=6, wraps) ... ultimately completes the loop; station 3 is the unique valid start)
- Input: `gas = [2, 3, 4]`, `cost = [3, 4, 3]` -> Output: `-1` (total gas 9 < total cost 10, impossible)

**Constraints:**

- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`

## Approach

First, if `sum(gas) < sum(cost)`, it's impossible overall, return `-1`. Otherwise a valid start is guaranteed to exist, and there's a single pass to find it: track a running tank total as you simulate starting from a candidate index `start = 0`. Whenever the running tank goes negative at station `i`, none of the stations from `start` through `i` could have been a valid starting point either (starting anywhere in that range only gives you a less negative or equal tank by the time you reach `i`, since each of those partial sums is >= 0 by construction of not having failed earlier — so they can only make things worse or equal, never recover the deficit). So reset the candidate start to `i + 1` and reset the tank to `0`, and continue accumulating.

This is a stays-ahead / exchange argument: once the cumulative tank from `start` dips below zero at `i`, every station between `start` and `i` is provably disqualified (their remaining balance to `i` is non-negative by definition, so they'd hit the same or worse deficit at `i`), so skipping straight to `i + 1` loses no viable candidates. Since we already know a solution exists (because total gas >= total cost), the single surviving candidate after the scan must be it.

## Edge Cases

- `n = 1` -> valid only if `gas[0] >= cost[0]`; the algorithm handles this naturally (tank never goes negative, or total check fails).
- Total gas exactly equals total cost -> feasible; the tank may dip to exactly `0` at points but never below, and a start is found.
- All stations identical (`gas[i] == cost[i]` for all `i`) -> tank never goes negative, station `0` is returned.
- Total gas less than total cost -> immediately return `-1` without running the scan.

## Complexity

- **Time:** O(n) — one pass to sum totals (or fold into the same loop) and one pass to find the start index.
- **Space:** O(1) — only running totals and the candidate index are kept.

[<- Previous](../jump-game/README.md) | [Category Index](../README.md) | [Next ->](../task-scheduler/README.md)
