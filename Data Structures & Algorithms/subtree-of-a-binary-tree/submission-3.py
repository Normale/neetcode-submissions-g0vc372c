# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def dfs(self, node_a, node_b):
        same_val = node_a.val == node_b.val
        if node_a.val == self.subroot.val:
            if self.dfs(node_a.left, self.subroot.left) and self.dfs(node_a.right, self.subroot.right):
                return True
        if node_b.val == self.subroot.val:
            if self.dfs(node_b.left, self.subroot.left) and self.dfs(node_b.right, self.subroot.right):
                return True
        if same_val and self.dfs(node_a.left, node_b.left) and self.dfs(node_a.right, node_b.right):
            return True
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        self.subroot = subRoot

        if root.val == self.subroot.val:
            return self.dfs(root, self.subroot)
        return False