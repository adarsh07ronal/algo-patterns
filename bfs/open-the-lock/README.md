# Open the Lock (Medium)

## Problem

A lock has 4 circular wheels, each with digits `0-9`. Each wheel can be turned one slot in either direction: `'9'` -> `'0'` wraps forward, and `'0'` -> `'9'` wraps backward. The lock starts at `"0000"`. Given a list `deadends` (states that, if reached, lock the wheels permanently and cannot be turned from) and a `target` string, return the minimum number of turns required to reach `target`, or `-1` if it's impossible.

**Example 1**

```
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: a sequence of turns 0000 -> 1000 -> 1100 -> 1200 -> 1201 -> 1202 -> 0202
takes 6 turns without ever landing on a deadend.
```

**Example 2**

```
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: turning the last wheel back from '0' to '9' reaches "0009" in 1 move.
```

**Example 3**

```
Input: deadends = ["0000"], target = "8888"
Output: -1
Explanation: the starting state is itself a deadend, so no move can ever be made.
```

**Constraints**

- `1 <= deadends.length <= 500`.
- `deadends[i].length == 4`.
- `target.length == 4`.
- `target` is not in `deadends`.
- `target` and every string in `deadends` consist only of digits.

**Input representation**: `deadends: List[str]`, `target: str`; lock states represented as 4-character digit strings.

## Approach

This problem is not about a physical grid or tree — it's about an **implicit graph** where each node is one of the 10,000 possible 4-digit states, and an edge connects two states that differ by turning exactly one wheel one step. "Minimum number of turns" is precisely "shortest path length in this unweighted graph," which is the textbook signal to use BFS.

Seed the queue with the single source `"0000"` at distance 0 — unless `"0000"` is itself a deadend, in which case there's no valid starting move at all, so return `-1` immediately. Maintain a `visited` set (pre-seeded with all `deadends`, so they're treated as already-visited and BFS will simply never step onto them or expand from them) to avoid revisiting states and looping forever.

Process the queue level by level (level = number of turns so far). For each state popped, if it equals `target`, return the current turn count. Otherwise, generate all 8 neighbor states (each of the 4 wheels turned +1 or -1, with wraparound via modulo arithmetic), skip any neighbor already visited or in the deadend set, mark it visited, and enqueue it for the next round.

BFS is the right tool because it explores the state graph outward in strict order of turn-count, so the first time `target` is dequeued (or detected) is guaranteed to be via the fewest possible turns — exactly analogous to a word-ladder or shortest-hop problem.

## Edge Cases

- **Start equals target** (`target == "0000"`): the BFS pops the start state on round 0 and immediately returns 0, since the check for reaching target happens before expanding.
- **Start is a deadend**: pre-checking `"0000" in deadends` before starting BFS (or relying on it being pre-marked visited and thus never processed) means the function correctly returns `-1` since no moves are ever possible.
- **Target unreachable due to deadends fully surrounding it**: BFS exhausts the queue without finding `target`, correctly returning `-1`.
- **Wraparound at digit boundaries** (`'0'` <-> `'9'`): handled via modulo-10 arithmetic on each digit rather than plain increment/decrement.
- **Deadends containing duplicate or irrelevant entries**: using a set naturally dedupes and has no effect beyond marking those exact states unreachable.

## Complexity

- **Time**: O(10^4) in the worst case — there are only 10,000 possible 4-digit states, each generating 8 neighbor transitions, so work is bounded by a constant independent of input size (O(N * 8) where N = 10^4 possible states).
- **Space**: O(10^4) for the `visited` set and the queue in the worst case.

[<- Previous](../01-matrix/README.md) | [Category Index](../README.md) | [Next ->](../shortest-path-in-binary-matrix/README.md)
