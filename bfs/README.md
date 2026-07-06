# Breadth-First Search (BFS)

## Pattern

Breadth-First Search explores a graph or tree outward from a starting point (or points) one "layer" at a time: visit all neighbors of the start before visiting any neighbor of a neighbor. This is implemented with a FIFO queue — push the starting node(s), then repeatedly pop from the front, process the node, and push its unvisited neighbors onto the back.

Because BFS always finishes exploring every node at distance `k` before touching any node at distance `k + 1`, the first time it reaches a target it has necessarily done so via a shortest possible path (in terms of number of edges/steps), as long as every edge has equal weight. This is the core reason to reach for BFS: it gives shortest-path / minimum-steps guarantees "for free," with no extra bookkeeping beyond tracking distance or level as you go.

**What's typically tracked**

- A `queue` (`collections.deque` in Python — `popleft()` is O(1), unlike `list.pop(0)`).
- A `visited` set (or an in-place marker, e.g. mutating a grid cell) so the same node isn't enqueued twice — this bounds the work to O(nodes + edges).
- Either an explicit "distance" or "steps" counter, or a level-by-level approach where the current queue size at the top of the loop tells you exactly how many nodes belong to the current level.

**Typical use cases**

- Shortest path / fewest steps in an unweighted graph or implicit state graph (e.g. lock combinations, word ladders).
- Level-order traversal of a tree, or anything that needs "process everything at depth `d` before depth `d + 1`" (e.g. level averages, minimum depth).
- Multi-source spread / simultaneous propagation, where multiple starting points all begin at distance 0 and spread outward together (e.g. rotting oranges, 01 matrix) — seed the queue with *all* sources up front instead of just one.

**BFS vs DFS**

Reach for BFS when:
- You need the *shortest* path, minimum number of steps, or minimum depth in an unweighted setting.
- You need strict level-by-level processing or a per-level aggregate (sum, average, max).
- You have multiple simultaneous sources spreading at the same rate.

Prefer DFS instead when you need to explore full paths, enumerate all possibilities, detect cycles, or when memory for a wide-but-shallow graph would make BFS's queue much larger than DFS's stack.

## Problems

| Difficulty | Problem | Notes |
|---|---|---|
| easy | [Average of Levels in Binary Tree](./average-of-levels-in-binary-tree/README.md) | Level-order traversal, average each level's values |
| easy | [Minimum Depth of Binary Tree](./minimum-depth-of-binary-tree/README.md) | BFS terminates the instant it finds the first leaf |
| medium | [Binary Tree Level Order Traversal](./binary-tree-level-order-traversal/README.md) | Canonical level-by-level queue traversal |
| medium | [Rotting Oranges](./rotting-oranges/README.md) | Multi-source BFS spreading simultaneously from all rotten cells |
| medium | [01 Matrix](./01-matrix/README.md) | Multi-source BFS from all zero cells to compute nearest-zero distance |
| medium | [Open the Lock](./open-the-lock/README.md) | BFS over an implicit state graph of lock combinations |
| medium | [Shortest Path in Binary Matrix](./shortest-path-in-binary-matrix/README.md) | BFS with 8-directional moves on a grid |

[<- Back to repo root](../README.md)
