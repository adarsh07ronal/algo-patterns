# Binary Tree Level Order Traversal (Medium)

## Problem

Given the root of a binary tree, return the level-order traversal of its nodes' values, i.e. from left to right, level by level, as a list of lists (one inner list per level).

**Example 1**

```
Input: root = [3,9,20,null,null,15,7]

        3
       / \
      9   20
         /  \
        15   7

Output: [[3], [9,20], [15,7]]
```

**Example 2**

```
Input: root = [1]
Output: [[1]]
```

**Example 3**

```
Input: root = []
Output: []
```

**Constraints**

- The number of nodes is in `[0, 2000]`.
- `-1000 <= Node.val <= 1000`.

**Input representation**: a binary tree built from `TreeNode` objects (`val`, `left`, `right`); `root` may be `None`.

## Approach

This is the canonical use of the "snapshot queue size, drain exactly that many" BFS pattern. Start with a single-source queue containing just `root`. At the top of each iteration of the outer loop, record `level_size = len(queue)` — this is precisely the count of nodes belonging to the level about to be processed, because BFS never interleaves nodes from different levels within the same queue "batch."

Pop exactly `level_size` nodes, appending each one's value to a `level` list (left before right, since children are always pushed left-then-right, preserving left-to-right order), and push each popped node's non-null children onto the back of the queue for the next round. After the inner loop, append `level` to the overall result. Repeat until the queue is empty.

BFS is the natural fit because the desired output structure (a list of levels) mirrors exactly how BFS naturally partitions its work — no extra depth-tracking data structure is needed beyond the queue itself and the loop-local size snapshot.

## Edge Cases

- **Empty tree** (`root is None`): return `[]` immediately, no levels to process.
- **Single node**: one level containing just the root's value.
- **Skewed tree**: each level has exactly one node; still produces one sublist per level.
- **Left-only or right-only children at a node**: only non-null children are enqueued, so gaps in the tree don't produce phantom entries.

## Complexity

- **Time**: O(n) — every node is enqueued and dequeued exactly once, and every value is appended to the output exactly once.
- **Space**: O(w) for the queue (w = maximum level width) plus O(n) for the output, which must hold every node's value once.

[<- Previous](../minimum-depth-of-binary-tree/README.md) | [Category Index](../README.md) | [Next ->](../rotting-oranges/README.md)
