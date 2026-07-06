class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: "TreeNode | None") -> bool:
        def dfs(node: "TreeNode | None", low: float, high: float) -> bool:
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    valid = TreeNode(2, TreeNode(1), TreeNode(3))
    assert Solution().isValidBST(valid) is True

    # classic deceptive case: 6 is < grandparent 10 while in its right subtree
    deceptive = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6), TreeNode(20)))
    assert Solution().isValidBST(deceptive) is False

    single = TreeNode(1)
    assert Solution().isValidBST(single) is True

    # duplicate value should be invalid (strict inequality required)
    duplicate = TreeNode(2, TreeNode(2), None)
    assert Solution().isValidBST(duplicate) is False

    # skewed increasing chain
    skewed = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    assert Solution().isValidBST(skewed) is True

    print("ok")
