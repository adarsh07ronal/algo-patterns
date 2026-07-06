# Average of Levels in Binary Tree (Easy)

## Problem

Given the root of a binary tree, return the average value of the nodes on each level, as a list ordered from the root's level (level 0) downward.

**Example 1**

```
Input: root = [3,9,20,null,null,15,7]

        3
       / \
      9   20
         /  \
        15   7

Output: [3.0, 14.5, 11.0]
Explanation: level 0 -> [3] -> avg 3.0
             level 1 -> [9, 20] -> avg 14.5
             level 2 -> [15, 7] -> avg 11.0
```

**Example 2**

```
Input: root = [3,9,20]
Output: [3.0, 14.5]
```

**Constraints**

- The number of nodes is in `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`.
- The tree is not guaranteed balanced or complete.

**Input representation**: a binary tree built from `TreeNode` objects (`val`, `left`, `right`).

## Approach

Seed the queue with just the `root` (single source, since a tree has one starting point). Then repeatedly process one full level at a time: before draining the queue, record its current length `n` — that length is exactly the number of nodes at the current depth, because every node pushed so far in this round belongs to the same level (BFS never mixes levels while a level is being drained).

For each of those `n` nodes, pop it, add its value to a running sum, and push its non-null children onto the back of the queue (they'll be processed in the *next* round, since they were enqueued after all current-level siblings). Once all `n` nodes for the level are popped, divide the sum by `n` to get the level's average, and continue to the next round with whatever's now in the queue.

BFS fits perfectly here because "average of a level" is inherently a level-by-level aggregate — the queue-size snapshot trick is the standard way to carve a flat BFS queue into discrete levels without needing a separate structure to track depth per node.

## Edge Cases

- **Single-node tree**: queue starts with `[root]`, one level, one average equal to the root's value.
- **Skewed tree (all left or all right children)**: each level has exactly one node; still handled correctly since the queue-size snapshot works regardless of shape.
- **Large negative/positive values**: use plain Python ints/floats, which don't overflow.
- Root is guaranteed non-null per constraints, so no empty-tree check is required, but the code still returns `[]` gracefully if `root` were `None`.

## Complexity

- **Time**: O(n), where n is the number of nodes — every node is enqueued and dequeued exactly once.
- **Space**: O(w), where w is the maximum width of the tree (the largest number of nodes at any single level), since that's the peak queue size. In the worst case (a complete tree) w = O(n).

[Category Index](../README.md) | [Next ->](../minimum-depth-of-binary-tree/README.md)
