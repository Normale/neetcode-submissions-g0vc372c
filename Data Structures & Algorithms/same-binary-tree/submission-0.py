# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node_a, node_b):
        if not node_a and not node_b:
            return True
        if not node_a or not node_b:
            return False
        same_val = node_a.val == node_b.val
        return same_val and self.dfs(node_a.left, node_b.left) and self.dfs(node_b.right, node_a.right)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p,q)