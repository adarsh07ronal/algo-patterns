# Dynamic Programming: How to Remember and Code It in an Interview

Unlike backtracking, DP doesn't have one universal 6-line skeleton — but every DP problem *does* answer the same 4 questions. Memorize the questions, not the code, and the code follows.

## The 4 questions that define any DP

1. **What does `dp[i]` (or `dp[i][j]`) mean, in one plain-English sentence?** ("the max money robbable from the first `i` houses", "the min coins to make amount `i`"). If you can't state this sentence, you don't have a DP yet — go back and find the subproblem.
2. **What's the recurrence?** How is `dp[i]` built from smaller/earlier entries — usually 1-3 choices, each pointing at a smaller index.
3. **What's the base case?** The smallest index(es) where the answer is trivial/known without recursing.
4. **Where's the final answer?** Often `dp[n]` or `dp[n-1]`, but sometimes `max(dp)` or `dp[n][m]`.

## Two implementation templates (same recurrence, opposite direction)

**Top-down (memoization)** — write the recursive definition first, this is usually the easiest way to *discover* the recurrence:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(i):
    if <base case>:
        return <base value>
    return <combine dp(smaller_index_1), dp(smaller_index_2), ...>
```

**Bottom-up (tabulation)** — same recurrence, filled iteratively, usually what interviewers want to see as the "final" answer since it makes space complexity easy to reason about (and optimize):
```python
dp = [<base values>] + [0] * n
for i in range(<start>, n + 1):
    dp[i] = <combine dp[i - 1], dp[i - 2], ...>
return dp[n]
```

Write top-down first if you're stuck on the recurrence — recursion mirrors the English sentence from Q1 directly. Convert to bottom-up once it works, if the interviewer wants the iterative version or an O(1)-space version.

## The 7 problems in this category, decoded

| Problem | `dp[i]` means | Recurrence | Base case |
|---|---|---|---|
| [Climbing Stairs](./climbing-stairs/README.md) | ways to reach step `i` | `dp[i] = dp[i-1] + dp[i-2]` | `dp[0]=1, dp[1]=1` |
| [House Robber](./house-robber/README.md) | max money from first `i` houses | `dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])` | `dp[0]=0` |
| [Coin Change](./coin-change/README.md) | min coins to make amount `i` | `dp[i] = min(dp[i-c] + 1 for c in coins if c<=i)` | `dp[0]=0`, unreachable = `inf` |
| [Longest Increasing Subsequence](./longest-increasing-subsequence/README.md) | length of LIS *ending at* index `i` | `dp[i] = max(dp[j] + 1 for j<i if nums[j]<nums[i])`, else `1` | `dp[i]=1` for all `i` |
| [Unique Paths](./unique-paths/README.md) | ways to reach cell `(i,j)` | `dp[i][j] = dp[i-1][j] + dp[i][j-1]` | first row/col all `1` |
| [Word Break](./word-break/README.md) | can `s[:i]` be segmented? | `dp[i] = any(dp[j] and s[j:i] in wordDict for j<i)` | `dp[0]=True` |
| [Longest Common Subsequence](./longest-common-subsequence/README.md) | LCS length of `s1[:i]`, `s2[:j]` | if chars match: `dp[i][j]=dp[i-1][j-1]+1`, else `max(dp[i-1][j], dp[i][j-1])` | `dp[0][*]=dp[*][0]=0` |

Notice the shape: Climbing Stairs / House Robber only look back 1-2 fixed steps → **O(1) space is possible** (just keep 2 rolling variables instead of a full array). Coin Change / LIS look back over *all* smaller indices → need the full `dp` array. Unique Paths / LCS are 2D because the state genuinely needs two indices to describe (a grid cell, or a pair of string prefixes).

## Decision checklist

1. **Does this smell like DP?** — the problem asks for optimal value (min/max), a count, or feasibility (yes/no) over a sequence of *choices*, and smaller instances of the same problem recur inside bigger ones (overlapping subproblems). If instead every subproblem is independent, it's just recursion/divide-and-conquer, not DP.
2. **Is it greedy instead?** — if you can convince yourself a single locally-best choice at each step is always safe (no need to compare against alternatives later), it might be greedy, not DP. If picking now can invalidate a *better* combination that shows up later, it's DP. (See [greedy cheatsheet](../greedy/interview-cheatsheet.md) for the contrast.)
3. **1D or 2D state?** — one sequence, one moving index → 1D. Two sequences, or a grid, or "index + some extra dimension" (remaining capacity, remaining moves) → 2D.
4. **Does the recurrence only look back a fixed, small window (i-1, i-2)?** → you can compress to O(1) space with rolling variables once it works. Don't do this prematurely — get the array version correct first.

## How to drill this so it's automatic

- For every new DP problem, **write the plain-English sentence for `dp[i]` before writing any code.** If you can't write the sentence, you don't understand the problem yet.
- Write the top-down recursive version first (mirrors the English sentence almost 1:1), verify with `assert` on the given examples, *then* convert to bottom-up if needed.
- Hand-trace the `dp` array for a tiny input (`n=3` or `n=4`) filling in the actual numbers — this is what catches off-by-one base-case bugs before you claim you're done.
- Say out loud: "the state is `dp[i] = <sentence>`, the recurrence is `<formula>`, base case is `<value>`, answer is `dp[n]`." That's the entire plan in one sentence, and it's what interviewers are listening for.

[<- Back to Dynamic Programming index](./README.md)
