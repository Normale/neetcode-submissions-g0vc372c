class Solution:
    def dfs(self, node) -> tuple[int, int]:
        if not node.left and not node.right:
            return node.val, node.val

        if node.left:
            left_val, left_best = self.dfs(node.left)
        else:
            left_val, left_best = 0, float("-inf")

        if node.right:
            right_val, right_best = self.dfs(node.right)
        else:
            right_val, right_best = 0, float("-inf")

        max_value_one_branch = node.val + max(0, left_val, right_val)

        max_value_through_current = (
            node.val
            + max(0, left_val)
            + max(0, right_val)
        )

        max_value_both_branches = max(
            max_value_through_current,
            left_best,
            right_best
        )

        return max_value_one_branch, max_value_both_branches

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]