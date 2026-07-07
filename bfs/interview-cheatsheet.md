# BFS: How to Remember and Code It in an Interview

One skeleton, one knob: **how many things start in the queue.** Single-source BFS gives shortest path from one point; multi-source BFS (seed the queue with *everything* at distance 0 simultaneously) gives shortest distance from the nearest of many sources, in the same number of lines.

## The universal skeleton

```python
from collections import deque

def bfs(sources):
    queue = deque(sources)          # one item for single-source, many for multi-source
    visited = set(sources)
    level = 0

    while queue:
        for _ in range(len(queue)):        # process one full level at a time
            node = queue.popleft()
            if <node is the target / base case>:
                return level
            for neighbor in neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        level += 1

    return <not found, e.g. -1>
```

The `for _ in range(len(queue))` inner loop is what gives you clean level-by-level processing (needed whenever the answer is "number of levels" or "number of minutes/turns") — without it you still visit nodes in the right *order*, but you lose the notion of "which level am I currently on."

## Decision checklist

1. **Am I asked for a shortest path / minimum steps / minimum time in an *unweighted* graph or grid?** → BFS guarantees the first time you reach a node is via the shortest path, because it explores strictly in order of distance. (DFS does not have this guarantee — see the [DFS cheatsheet](../dfs/interview-cheatsheet.md) for when to reach for that instead.)
2. **Is there one starting point, or several simultaneously?** → single-source: `queue = deque([start])`. Multi-source (e.g. every rotten orange starts rotting in the same minute, every 0-cell is already at distance 0): `queue = deque(all_sources)` — this is the single biggest "aha" that separates BFS problems from each other, since it looks almost identical to single-source but changes what "distance" means.
3. **Do I need to know *which level* I'm on** (minutes elapsed, levels of a tree)? → use the `for _ in range(len(queue))` batch-processing form. If I only care about *reachability* (does a path exist at all, no distance needed), a plain `while queue` without the inner batch loop is simpler.
4. **What counts as a "neighbor"?** — tree: `left`/`right`; grid: usually the 4 orthogonal cells (sometimes 8, check the problem); general graph/state-space (like a combination lock): whatever a single legal "move" produces.

## The 7 problems in this category, decoded

| Problem | Sources | What "distance"/level means | Neighbor definition |
|---|---|---|---|
| [Average of Levels in Binary Tree](./average-of-levels-in-binary-tree/README.md) | `[root]` | tree depth | `node.left`, `node.right` |
| [Minimum Depth of Binary Tree](./minimum-depth-of-binary-tree/README.md) | `[root]` | depth to *first* leaf found | `node.left`, `node.right`; base case = leaf node |
| [Binary Tree Level Order Traversal](./binary-tree-level-order-traversal/README.md) | `[root]` | which output list a node's value goes into | `node.left`, `node.right` |
| [Rotting Oranges](./rotting-oranges/README.md) | **all** initially-rotten cells at once | minutes elapsed | 4 orthogonal grid neighbors that are fresh |
| [01 Matrix](./01-matrix/README.md) | **all** cells that are already `0` | distance to nearest `0` | 4 orthogonal grid neighbors |
| [Open the Lock](./open-the-lock/README.md) | `["0000"]` (minus deadends) | number of turns | the 8 lock states reachable by turning one wheel by one notch |
| [Shortest Path in Binary Matrix](./shortest-path-in-binary-matrix/README.md) | `[(0,0)]` | path length | all 8 surrounding cells (not just 4!) that are `0` |

## How to drill this so it's automatic

- Before coding, answer out loud: "single-source or multi-source?" and "do I need level numbers?" — those two answers fully determine the skeleton's shape.
- Multi-source is just "seed the queue with a list instead of one item" — don't overthink it as a different algorithm; it's the identical loop.
- Always mark a node `visited` **at the moment you enqueue it**, not when you dequeue it — marking on dequeue lets the same node get added to the queue multiple times before it's ever processed, which silently blows up runtime on grid problems.
- Hand-trace the queue's contents level by level for a 3x3 grid or 4-node tree before declaring done — this is what catches "forgot to check grid boundaries" or "used 4-directional when the problem wanted 8-directional" (as in Shortest Path in Binary Matrix).

[<- Back to BFS index](./README.md)
