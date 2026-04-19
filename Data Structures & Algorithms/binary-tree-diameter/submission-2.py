# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node) -> Tuple[int, int]:
        """Returns height and diameter."""
        if not node:
            return 0, 0
        left_h, left_d = self.dfs(node.left)
        right_h, right_d = self.dfs(node.right)

        height = 1 + max(left_h, right_h)
        diameter = max(left_h + right_h, left_d, right_d)
        return height, diameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # return max of left + max of right?
        if not root.left and not root.right:
            return 0
        h, d = self.dfs(root)
        return d