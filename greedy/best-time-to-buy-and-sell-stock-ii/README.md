# Best Time to Buy and Sell Stock II (Easy)

## Problem

Given an array `prices` where `prices[i]` is the price of a stock on day `i`, find the maximum profit achievable. You may complete as many transactions as you like, but you must sell the stock before you can buy again (you can hold at most one share at a time).

**Examples:**

- Input: `prices = [7, 1, 5, 3, 6, 4]` -> Output: `7` (buy at 1, sell at 5 for profit 4; buy at 3, sell at 6 for profit 3; total 7)
- Input: `prices = [1, 2, 3, 4, 5]` -> Output: `4` (buy at 1, sell at 5, or equivalently sum every daily gain: 1+1+1+1)
- Input: `prices = [7, 6, 4, 3, 1]` -> Output: `0` (prices only fall, never trade)

**Constraints:**

- `1 <= prices.length <= 3 * 10^4`
- `0 <= prices[i] <= 10^4`

## Approach

Sum up every positive difference between consecutive days: `sum(max(0, prices[i] - prices[i-1]))`. This is equivalent to greedily buying the moment the price is about to go up and selling right before it goes down.

Why is this safe? Any multi-day upward run, say from day `a` to day `b`, can be decomposed into a chain of single-day gains `(a, a+1), (a+1, a+2), ..., (b-1, b)`, and the sum of those single-day gains telescopes to exactly `prices[b] - prices[a]` — the same profit as one big buy-low/sell-high trade over that run, since there's no cost or limit to the number of transactions. So capturing every daily uptick is never worse than, and always matches, the best possible sequence of buy/sell trades — there is no advantage to "waiting" through a dip since you're free to re-buy immediately after any sell.

## Edge Cases

- Single price point -> no adjacent pairs to compare, profit is `0`.
- Strictly decreasing prices -> every day-to-day difference is negative, contributes `0`, total profit `0`.
- Strictly increasing prices -> every difference is positive and summing them telescopes to `prices[-1] - prices[0]`, matching one continuous hold.
- All prices equal -> every difference is `0`, profit `0`.

## Complexity

- **Time:** O(n) — one linear scan comparing each day to the previous.
- **Space:** O(1) — only a running total is kept.

[<- Previous](../assign-cookies/README.md) | [Category Index](../README.md) | [Next ->](../jump-game/README.md)
