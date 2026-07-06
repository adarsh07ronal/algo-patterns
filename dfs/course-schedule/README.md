# Course Schedule (Medium)

## Problem

There are `numCourses` courses labeled `0` to `numCourses - 1`. You are given `prerequisites`, an array of pairs `[a, b]` meaning you must take course `b` before course `a`. Return `true` if it's possible to finish all courses, `false` otherwise.

**Input representation**: `numCourses` is an int; `prerequisites` is a `list[list[int]]` of `[a, b]` pairs. This is represented internally as a directed graph via an adjacency list, where an edge `b -> a` means "b must come before a."

**Examples**

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true   (take course 0, then course 1)
```

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false  (0 depends on 1 and 1 depends on 0 -> cycle, impossible)
```

**Constraints**: `1 <= numCourses <= 2000`; `0 <= prerequisites.length <= 5000`; no duplicate edges.

## Approach

"Can all courses be finished" is equivalent to "does the prerequisite graph contain a cycle?" — if there's a cycle, every course in it depends (transitively) on itself, so none of them can ever be taken first. This is a classic DFS cycle-detection problem on a **directed** graph, which needs three states per node (not just visited/unvisited) because a directed graph can revisit an already-fully-explored node without that being a cycle:

- `WHITE` (unvisited): haven't started exploring from this node.
- `GRAY` (in progress): currently on the DFS stack for the *current* root-to-node path. If DFS reaches a `GRAY` node again, that's a **back edge** — a cycle.
- `BLACK` (done): fully explored, all its dependencies are resolved with no cycle found through it. Revisiting a `BLACK` node from elsewhere is fine (it's just a diamond-shaped dependency, not a cycle) and lets us skip re-exploring it.

We DFS from each course; along the DFS path we mark the current node `GRAY` before recursing into its prerequisites and flip it to `BLACK` on the way back out (post-order). If a recursive call ever encounters a `GRAY` node, we've found a cycle and return `False` immediately. This state machine is exactly what distinguishes DFS cycle detection in directed graphs from the simpler "visited set" used for undirected connectivity.

## Edge Cases

- **No prerequisites at all**: adjacency lists are all empty, no DFS finds any edge, trivially `True`.
- **Self-loop** (`[0,0]`): course 0 depends on itself; DFS marks `0` gray, immediately recurses into `0` again, finds it `GRAY` -> cycle -> `False`.
- **Disconnected components**: the outer loop tries DFS from every course `0..numCourses-1` that's still `WHITE`, so isolated or separate clusters are all checked independently.
- **Diamond dependency** (`0` and `1` both depend on `2`, no cycle): `2` becomes `BLACK` after its first exploration; the second path to `2` sees `BLACK` and simply stops without falsely reporting a cycle — this is exactly why we need 3 colors instead of 2.
- **numCourses = 1, no prerequisites**: trivially `True`.

## Complexity

- **Time**: O(V + E) where `V = numCourses` and `E = len(prerequisites)` — each node is fully explored once (transitions to `BLACK` exactly once), and each edge is examined once.
- **Space**: O(V + E) for the adjacency list plus O(V) for the color array and O(V) recursion stack depth in the worst case (a long chain).

[<- Previous](../number-of-islands/README.md) | [Category Index](../README.md) | [Next ->](../clone-graph/README.md)
