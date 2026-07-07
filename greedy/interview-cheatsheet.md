# Greedy: How to Remember and Code It in an Interview

There's no shared code skeleton for greedy the way there is for backtracking or BFS — the "template" is a *reasoning move* you make before writing any code: pick the obvious locally-best choice, then justify to yourself why a smarter choice could never beat it. If you can't complete that justification in a sentence or two, it's probably not greedy — see the DP cheatsheet's checklist for the contrast.

## The reasoning template (say this before coding)

1. **Propose the obvious rule.** ("always pick the cheapest option next", "always end the interval you're comparing as early as possible", "process transactions the moment they help profit").
2. **Justify it with an exchange argument**: "if an optimal solution did something else at this step, I can swap it for the greedy choice without making the overall answer worse — so greedy is at least as good." You don't need a formal proof in an interview, just this sentence said out loud.
3. **Implement.** Greedy code is almost always short: sort (if needed), then a single linear pass with 1-2 running variables. If your "greedy" solution needs nested loops comparing many combinations, you've probably drifted into brute force or actually need DP.

## The 7 problems in this category, decoded

| Problem | The greedy rule | Why it's safe (one-line exchange argument) |
|---|---|---|
| [Assign Cookies](./assign-cookies/README.md) | sort both arrays; give the smallest sufficient cookie to the least-greedy unsatisfied child | using a bigger-than-necessary cookie on an easy-to-please child only wastes capacity that a greedier child could've used later |
| [Best Time to Buy and Sell Stock II](./best-time-to-buy-and-sell-stock-ii/README.md) | add up every positive day-to-day price increase | any profitable multi-day hold decomposes exactly into its daily up-moves — buying/selling every up-tick captures the same total profit |
| [Jump Game](./jump-game/README.md) | track the farthest index reachable so far; fail only if you reach a spot beyond it | you never need to remember *which* jump got you somewhere, only the single best (farthest) reach so far |
| [Gas Station](./gas-station/README.md) | if total gas < total cost, impossible; else the station right after the deepest running-total dip is the unique start | if the tank goes negative starting at `i`, no station between the old start and `i` can be a valid start either — so you can jump straight past all of them |
| [Task Scheduler](./task-scheduler/README.md) | schedule around the *most frequent* task first; answer is `max(len(tasks), (max_count-1)*(n+1) + count_of_tasks_tied_for_max)` | the most frequent task is the one whose cooldown gaps are hardest to fill — everything else can always slot into those gaps if there's room |
| [Partition Labels](./partition-labels/README.md) | extend the current partition's end to the last occurrence of every letter seen so far; cut when you reach that end | a letter appearing later forces the partition to stay open that long anyway, so closing early would just create an invalid split |
| [Non-overlapping Intervals](./non-overlapping-intervals/README.md) | sort by **end** time; greedily keep an interval if it starts after the last kept interval's end | keeping the interval that ends *soonest* leaves the most room for future intervals to also fit — this is the classic interval-scheduling exchange argument |

## Decision checklist

1. **Can I sort by some key and then make one pass?** — most greedy problems reveal themselves once you find the right sort key (by size, by end time, by frequency).
2. **Does an early choice ever need to be un-done based on something discovered later?** If yes, it's not greedy — that's the DP tell (see [DP cheatsheet](../dynamic-programming/interview-cheatsheet.md)).
3. **Interval problems**: the sort key is almost always **end time**, not start time — sorting by end time is what makes "keep this interval if it doesn't overlap the last kept one" correct.
4. **"Maximize count of something satisfied" problems** (Assign Cookies-style): sort both sides, use two pointers, and always try to satisfy with the *smallest sufficient* resource.
5. **Running-total / prefix-sum problems** (Gas Station-style): track a running total and the point where it dips lowest — the station right after the dip is often the answer, because everything before the dip is now provably unreachable as a start.

## How to drill this so it's automatic

- Never start coding until you've said the exchange argument out loud — if you can't, you don't have a greedy solution yet, you have a guess.
- Try a small counter-example against your own proposed rule before committing (e.g., for Non-overlapping Intervals, check that sorting by *start* time instead of *end* time actually breaks on some 3-interval example) — this is exactly what interviewers probe for.
- Watch for the phrase "at most" / "unlimited transactions" / "maximize count" in the prompt — these are strong greedy signals, since they usually mean no complex interaction between choices.
- If you catch yourself wanting to compare "what if I had chosen differently 3 steps ago," that's DP creeping in, not greedy — stop and re-evaluate which pattern actually fits.

[<- Back to Greedy index](./README.md)
