# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node):
        if node.left:
            left_smaller = node.left.val < node.val 
            left_valid = self.dfs(node.left)
        else:
            left_smaller = True
            left_valid = True
        if node.right:
            right_greater = node.right.val > node.val 
            right_valid = self.dfs(node.right)
        else:
            right_greater = True
            right_valid = True

        return left_smaller and right_greater and left_valid and right_valid


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)