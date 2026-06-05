# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# ```text
#       A
#      / \
#     B   C
#    / \   \
#   D   E   F
# ```

# Preorder (N → L → R)
# A, B, D, E, C, F

# Inorder (L → N → R)
# D, B, E, A, C, F

# Postorder (L → R → N)
# D, E, B, F, C, A

# ```
# ```

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # from preorder we already have a root
        # root = preorder[0]
        # and from inorder we can divide left - right
        # everything left of root in inorder is left, everything right is right
        # then in the left part of inorder, we can take root = preorder[1] 
        
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        root.left = self.buildTree(
            preorder[1: 1 + mid],
            inorder[:mid]
        )

        root.right = self.buildTree(
            preorder[1 + mid :],
            inorder[mid + 1:]
        )
        return root
        # todo: optimize it to use O(n) - hashmap 






