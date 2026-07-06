# Assign Cookies (Easy)

## Problem

Each child `i` has a greed factor `g[i]`, the minimum cookie size that will satisfy them. Each cookie `j` has a size `s[j]`. A cookie `j` can satisfy child `i` only if `s[j] >= g[i]`. Each child can receive at most one cookie, and each cookie can be given to at most one child. Maximize the number of content children.

**Examples:**

- Input: `g = [1, 2, 3]`, `s = [1, 1]` -> Output: `1` (only one cookie of size 1 can satisfy the child with greed factor 1)
- Input: `g = [1, 2]`, `s = [1, 2, 3]` -> Output: `2` (cookie of size 1 satisfies greed 1, cookie of size 2 satisfies greed 2)

**Constraints:**

- `1 <= g.length, s.length <= 3.4 * 10^4`
- `1 <= g[i], s[j] <= 2^31 - 1`

## Approach

Sort both `g` and `s`. Walk through the sorted cookies with a pointer, and for each cookie try to satisfy the least-greedy unsatisfied child (also tracked by a pointer). If the current cookie is big enough for the current child, assign it and advance both pointers; otherwise the cookie is too small for *any* remaining child (since children are sorted ascending), so discard it and move to the next, bigger cookie.

This is safe by an exchange argument: consider any optimal assignment. If the least-greedy child is satisfied by some cookie larger than the smallest cookie that could satisfy them, swap those two cookies — the least-greedy child is still satisfied (any sufficient cookie still suffices), and the other child who received the smallest cookie either still works or can be re-paired, without reducing the total count. Repeating this argument shows always giving the smallest sufficient cookie to the least-greedy remaining child never does worse than any other strategy.

## Edge Cases

- No cookies (`s` empty) or no children (`g` empty) -> loop doesn't execute, returns `0`.
- All cookies too small for every child -> pointer over cookies exhausts without any matches, returns `0`.
- More cookies than children (or vice versa) -> the smaller pointer naturally caps the number of matches.
- All children have identical greed / all cookies identical size -> still works since sorting is stable under ties and comparisons are `>=`.

## Complexity

- **Time:** O(n log n + m log m) for sorting `g` and `s` (n, m are their lengths), plus O(n + m) for the single pass with two pointers.
- **Space:** O(1) extra (ignoring sort space), or O(log n) for typical in-place sort recursion.

[Category Index](../README.md) | [Next ->](../best-time-to-buy-and-sell-stock-ii/README.md)
