# Clone Graph (Medium)

## Problem

Given a reference to a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains an integer value and a list of references to its neighbors.

**Input representation**: a minimal `Node` class with `val` (int) and `neighbors` (`list[Node]`). The graph is connected, and node values are unique, so `val` doubles as an identifier. We're given a single starting `Node` and must return the corresponding cloned `Node`.

**Examples**

```
Input: adjacency list [[2,4],[1,3],[2,4],[1,3]]
(node 1 connects to 2 and 4; node 2 connects to 1 and 3; etc. — a 4-cycle)

    1 -- 2
    |    |
    4 -- 3

Output: a completely separate set of Node objects with the same values
        and the same connectivity pattern.
```

```
Input: adjacency list [[]]  (single node, no neighbors)
Output: a single cloned node with an empty neighbors list.
```

**Constraints**: number of nodes in `[0, 100]`; node values are unique in `[1, 100]`; the graph has no repeated edges and no self-loops; the graph is connected.

## Approach

Cloning a graph means visiting every reachable node exactly once (to make a copy of it) and exactly once fixing up its neighbor list to point at *cloned* neighbors — not the originals. Because the graph can contain cycles (e.g. our 4-cycle example), a naive recursive clone-then-recurse-into-neighbors approach would infinite-loop without protection.

The fix is the same one used in general graph DFS: keep a `visited` map from *original node -> its clone*. This map serves double duty:
1. It's the "have I visited this node" check that prevents infinite recursion on cycles.
2. It directly gives us the clone to reuse when a neighbor points back to an already-cloned node, so we never create duplicate clones for the same original node.

DFS procedure: given an original node, if it's already in the map, return its clone immediately (this is what breaks cycles). Otherwise, create a new clone with the same `val` and an empty neighbor list, **store it in the map before recursing** (critical — this is what prevents infinite recursion when a neighbor's DFS call leads back to this node), then for each original neighbor, recursively clone it and append the result to the new node's neighbor list.

## Edge Cases

- **Empty graph** (`node is None`): return `None` immediately, no traversal needed.
- **Single node with no neighbors**: DFS clones it, its neighbor list recursion loop simply doesn't execute (empty list), returns immediately.
- **Cycles** (including the whole graph being one big cycle, as in the example): handled by checking the `visited` map first, before doing any recursive work — this is the crux of the whole solution.
- **Self-loop** (a node listing itself as a neighbor): although the problem states no self-loops, the algorithm handles it correctly anyway since the visited-map check would return the in-progress clone rather than recursing infinitely.
- **Node revisited via multiple paths** (e.g. a diamond shape): the map ensures only one clone is ever created per original node, so identity is preserved consistently across all references.

## Complexity

- **Time**: O(V + E) — every node is cloned once (O(V)) and every edge is traversed once to wire up neighbor lists (O(E)).
- **Space**: O(V) for the `visited` map (which holds all clones) plus O(V) worst-case DFS recursion depth.

[<- Previous](../course-schedule/README.md) | [Category Index](../README.md) | [Next ->](../validate-binary-search-tree/README.md)
