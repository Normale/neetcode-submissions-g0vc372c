# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, max_so_far):
        if not node:
            return 0
        max_so_far = max(node.val, max_so_far)
        count = 0
        if node.val >= max_so_far:
            count += 1
        count += self.dfs(node.left, max_so_far)
        count += self.dfs(node.right, max_so_far)

        return count 
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float('-inf'))