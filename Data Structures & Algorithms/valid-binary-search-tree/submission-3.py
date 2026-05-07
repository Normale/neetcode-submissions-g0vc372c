# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node):
        left_smaller = node.left.val < node.val if node.left else True
        right_greater = node.right.val > node.val if node.right else True

        left_valid = self.dfs(node.left) if node.left else True
        right_valid = self.dfs(node.right) if node.right else True

        return left_smaller and right_greater and left_valid and right_valid


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)