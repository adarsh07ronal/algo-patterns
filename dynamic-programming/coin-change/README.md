# Coin Change (Medium)

## Problem

Given an array of integer coin denominations `coins` and an integer `amount`, return the fewest number of coins needed to make up that amount using an unlimited supply of each coin. If the amount cannot be made up by any combination of the coins, return `-1`.

**Examples:**

- Input: `coins = [1,2,5], amount = 11` -> Output: `3` (`11 = 5 + 5 + 1`)
- Input: `coins = [2], amount = 3` -> Output: `-1` (odd amount can't be made from only 2s)

**Constraints:**

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

## Approach

Let `dp[a]` be the minimum number of coins needed to make amount `a`. To build amount `a`, the last coin used must be some `c` from `coins` (with `c <= a`), and the rest of the amount, `a - c`, must be made optimally as well — that's the optimal substructure: the best way to make `a` is one coin plus the best way to make `a - c`, minimized over all valid coins:

```
dp[a] = min(dp[a - c] + 1) for every coin c <= a
dp[0] = 0
```

This is an unbounded knapsack-style DP (each coin can be reused any number of times), solved bottom-up: fill `dp[0..amount]` in increasing order of `a`, since `dp[a]` depends only on smaller amounts. Amounts that remain unreachable are tracked with a sentinel value (infinity); if `dp[amount]` is still infinity at the end, no combination works, so return `-1`.

## Edge Cases

- `amount = 0` -> `dp[0] = 0` by definition, so the answer is `0` coins needed.
- No combination reaches `amount` (e.g. `coins = [2], amount = 3`) -> `dp[amount]` stays at the sentinel/infinity value, so the code returns `-1`.
- A coin larger than `amount` -> naturally skipped since the inner loop only considers coins `c <= a`.
- Single coin denomination that evenly divides `amount` -> works via repeated addition, e.g. `coins=[1]` always succeeds.

## Complexity

- **Time:** O(amount * len(coins)) — for each amount from 1 to `amount`, we try every coin.
- **Space:** O(amount) — one DP array indexed by amount.

[<- Previous](../house-robber/README.md) | [Category Index](../README.md) | [Next ->](../longest-increasing-subsequence/README.md)
