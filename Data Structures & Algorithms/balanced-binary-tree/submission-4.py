# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node) -> bool:
        if node is None:
            return False
        pair = (node.left is None, node.right is None)
        if node.left is None and node.right is None:
            return True
        else:
            return self.dfs(node.left) and self.dfs(node.right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)