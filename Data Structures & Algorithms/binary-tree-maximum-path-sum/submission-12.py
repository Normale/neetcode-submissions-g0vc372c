class Solution:
    def dfs(self, node) -> tuple[int, int]:
        """
        Returns:
        max_value_one_branch:
            best path starting at this node and going down one side

        max_value_both_branches:
            best path anywhere inside this subtree
        """

        if not node.left and not node.right:
            return node.val, node.val

        if node.left:
            left_val, left_exclusive_val = self.dfs(node.left)
        else:
            left_val, left_exclusive_val = 0, float("-inf")

        if node.right:
            right_val, right_exclusive_val = self.dfs(node.right)
        else:
            right_val, right_exclusive_val = 0, float("-inf")

        max_value_one_branch = node.val + max(
            0,
            left_val,
            right_val
        )

        max_value_through_current_node = (
            node.val
            + max(0, left_val)
            + max(0, right_val)
        )

        max_value_both_branches = max(
            max_value_through_current_node,
            left_exclusive_val,
            right_exclusive_val
        )

        return max_value_one_branch, max_value_both_branches

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))