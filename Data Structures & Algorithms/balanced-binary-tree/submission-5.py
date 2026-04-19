# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node) -> int:
        # return height and isbalanced
        if node is None:
            return 0

        left_h, left_balanced = self.dfs(node.left)
        right_h, right_balanced = self.dfs(node.right)

        if not left_balanced or not right_balanced:
            return 0, False
        current_balanced = left_h == right_h
        if not current_balanced:
            return 0, False
        
        return left_h + 1, True


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        height, balanced = self.dfs(root)# Definition for a binary tree node.
        return balanced
