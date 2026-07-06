# Task Scheduler (Medium)

## Problem

Given a list of CPU `tasks` (each represented by a character, where the same character means the same type of task) and a non-negative cooldown integer `n`, find the minimum number of intervals (time units) the CPU needs to finish all tasks, given that identical tasks must be separated by at least `n` intervals (idle or other tasks may fill the gap).

**Examples:**

- Input: `tasks = ["A","A","A","B","B","B"]`, `n = 2` -> Output: `8` (one arrangement: `A B idle A B idle A B`)
- Input: `tasks = ["A","A","A","B","B","B"]`, `n = 0` -> Output: `6` (no cooldown needed, just run them back-to-back)

**Constraints:**

- `1 <= tasks.length <= 10^4`
- `tasks[i]` is an uppercase English letter
- `0 <= n <= 100`

## Approach

Count the frequency of each task. Let `maxFreq` be the highest frequency and `maxCount` be how many distinct tasks share that highest frequency. The most frequent task dictates the skeleton of the schedule: it needs `maxFreq` occurrences with `n`-sized gaps between them, forming `maxFreq - 1` gaps of size `n`, plus its own `maxFreq` slots. That gives a frame of size `(maxFreq - 1) * (n + 1) + maxCount` (the `maxCount` accounts for placing all tied most-frequent tasks in the very last gap-group alongside the leader, since ties can share the final slot row without adding new idle time).

Every other, less-frequent task can always be slotted into one of these gaps without ever forcing the schedule longer than this frame — there's no way to arrange things using fewer than `maxFreq` "rows" if a task must repeat `maxFreq` times with the mandatory cooldown, so this frame size is a hard lower bound. The only other lower bound is simply `len(tasks)` itself (if there are enough distinct tasks to fill every idle slot with real work, no idle time is needed at all). The answer is the max of these two: `max(len(tasks), (maxFreq - 1) * (n + 1) + maxCount)`.

This is safe because the frame-size formula is both a valid lower bound (forced by the most frequent task's cooldown requirement) and achievable (greedily filling idle slots round-robin with the next most-available task never fails to fit, since no other task has a higher count that would overflow a gap of size `n`).

## Edge Cases

- `n = 0` -> no cooldown constraint at all, answer is simply `len(tasks)`.
- Only one distinct task -> frame formula dominates: `(count - 1) * (n + 1) + 1`.
- Enough task variety to fill every gap -> `len(tasks)` dominates over the frame formula, meaning zero idle time is needed.
- Single task overall -> returns `1`.

## Complexity

- **Time:** O(t + 26) ~ O(t) where `t = len(tasks)` — one pass to count frequencies, then a constant-size (26 uppercase letters) scan to find `maxFreq` and `maxCount`.
- **Space:** O(1) — frequency table is bounded by the 26-letter alphabet.

[<- Previous](../gas-station/README.md) | [Category Index](../README.md) | [Next ->](../partition-labels/README.md)
