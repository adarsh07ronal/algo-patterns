from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_sum = 0
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_sum / level_size)

    return result


if __name__ == "__main__":
    # Example 1: [3,9,20,null,null,15,7]
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert average_of_levels(root1) == [3.0, 14.5, 11.0]

    # Example 2: [3,9,20]
    root2 = TreeNode(3, TreeNode(9), TreeNode(20))
    assert average_of_levels(root2) == [3.0, 14.5]

    # Single node
    assert average_of_levels(TreeNode(5)) == [5.0]

    print("ok")
