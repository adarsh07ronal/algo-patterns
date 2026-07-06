from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    queue = deque([root])
    depth = 1

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1

    return depth


if __name__ == "__main__":
    # Example 1: [3,9,20,null,null,15,7]
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert min_depth(root1) == 2

    # Example 2: [2,null,3,null,4,null,5,null,6] - right-leaning chain
    root2 = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
    assert min_depth(root2) == 5

    # Empty tree
    assert min_depth(None) == 0

    # Single node
    assert min_depth(TreeNode(1)) == 1

    print("ok")
