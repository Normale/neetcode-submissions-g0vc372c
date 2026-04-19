# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node) -> bool:
        pair = (node.left is None, node.right is None)
        if all(pair):
            return True
        if pair[0] and not pair[1] or pair[1] and not pair[0]:
            return False
        else:
            return dfs(node.left) and dfs(node.right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)