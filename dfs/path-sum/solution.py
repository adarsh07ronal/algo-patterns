class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: "TreeNode | None", targetSum: int) -> bool:
        if root is None:
            return False
        remaining = targetSum - root.val
        if root.left is None and root.right is None:
            return remaining == 0
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)


if __name__ == "__main__":
    #          5
    #         / \
    #        4   8
    #       /   / \
    #      11  13  4
    #     / \       \
    #    7   2       1
    tree1 = TreeNode(
        5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
    )
    assert Solution().hasPathSum(tree1, 22) is True

    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert Solution().hasPathSum(tree2, 5) is False

    assert Solution().hasPathSum(None, 0) is False

    single = TreeNode(7)
    assert Solution().hasPathSum(single, 7) is True
    assert Solution().hasPathSum(single, 0) is False

    # single-child chain: node with only a left child is not a leaf
    one_child = TreeNode(1, TreeNode(2))
    assert Solution().hasPathSum(one_child, 1) is False
    assert Solution().hasPathSum(one_child, 3) is True

    print("ok")
