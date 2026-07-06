class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: "TreeNode | None") -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    # [3,9,20,null,null,15,7]
    tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert Solution().maxDepth(tree1) == 3

    # [1]
    tree2 = TreeNode(1)
    assert Solution().maxDepth(tree2) == 1

    # []
    assert Solution().maxDepth(None) == 0

    # skewed left chain of 4 nodes
    skewed = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert Solution().maxDepth(skewed) == 4

    print("ok")
