# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node):
        if node.left and node.right:
            node_valid = node.left.val < node.val < node.right.val
        left_valid = self.dfs(node.left) if node.left else True
        right_valid = self.dfs(node.right) if node.right else True

        return node_valid and left_valid and right_valid


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)