# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node) -> tuple[int, int]:
        """Returns tuple[max_value_one_branch, max_value_both_branches]."""
        if not node.left and not node.right:
            return node.val, node.val
        if node.right:
            right_val, right_exclusive_val = self.dfs(node.right)
        else:
            right_val, right_exclusive_val = 0, 0
        if node.left:
            left_val, left_exclusive_val = self.dfs(node.left)
        else:
            left_val, left_exclusive_val = 0, 0
        total = node.val + max(left_val, right_val)
        
        max_value_one_branch = total
        max_value_both_branches = max(
            node.val + left_val + right_val,
            right_exclusive_val,
            left_exclusive_val
        )
        return max_value_one_branch, max_value_both_branches

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = max(self.dfs(root))        
        print(result)
        return result