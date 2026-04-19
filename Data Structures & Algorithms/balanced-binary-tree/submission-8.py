# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node) -> tuple[int, bool]:
        # return height and isbalanced
        if node is None:
            return 0, True

        left_h, left_balanced = self.dfs(node.left)
        right_h, right_balanced = self.dfs(node.right)

        height = 1 + max(left_h, right_h)

        current_balanced = abs(left_h - right_h) <= 1
        balanced = left_balanced and right_balanced and current_balanced
        
        return height, balanced


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        height, balanced = self.dfs(root)# Definition for a binary tree node.
        return balanced
