# Dynamic Programming

## Pattern

Dynamic programming (DP) solves problems that have two properties:

- **Optimal substructure** — the optimal solution to a problem can be built from optimal solutions to its subproblems.
- **Overlapping subproblems** — the same subproblems are solved repeatedly if you approach the problem naively (e.g. with plain recursion), so caching their results avoids redundant work.

There are two common ways to implement a DP solution:

- **Top-down (memoization)** — write the natural recursive solution, then cache (`memoize`) the result of each unique subproblem call (e.g. with a dict or `functools.lru_cache`) so it's only computed once. This is usually the easiest way to *discover* a DP solution, because it mirrors the recursive definition of the problem directly.
- **Bottom-up (tabulation)** — identify the smallest subproblems, solve them first, and iteratively build up to the final answer using a table (array or grid). This avoids recursion overhead/stack limits and often allows further space optimization (e.g. collapsing a 2D table into a rolling 1D array).

**How to recognize a DP problem:**

- The problem asks for an optimal value (min/max), a count of ways, or a yes/no feasibility, over a sequence, grid, or set of choices.
- A greedy (locally-optimal) choice doesn't obviously lead to a globally optimal answer.
- You can describe the answer to a problem of size `n` in terms of answers to smaller/related instances (a recurrence relation).
- Brute-force recursion would revisit the same subproblem multiple times with different call paths.

Once a recurrence relation and base case(s) are identified, the rest is mechanical: define the state, write the transition, decide on memoization vs tabulation, and work out the space/time complexity.

## Problems

| Difficulty | Problem | Notes |
|---|---|---|
| Easy | [Climbing Stairs](./climbing-stairs/README.md) | Fibonacci-style counting DP |
| Easy | [House Robber](./house-robber/README.md) | Linear DP with an adjacency constraint |
| Medium | [Coin Change](./coin-change/README.md) | Unbounded knapsack, minimize count |
| Medium | [Longest Increasing Subsequence](./longest-increasing-subsequence/README.md) | O(n^2) DP, optimizable to O(n log n) |
| Medium | [Unique Paths](./unique-paths/README.md) | 2D grid counting DP |
| Medium | [Word Break](./word-break/README.md) | String segmentation feasibility DP |
| Medium | [Longest Common Subsequence](./longest-common-subsequence/README.md) | Classic 2D string DP |

[<- Back to repo root](../README.md)
