# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            level = []
            qlen = len(q)
            found = False
            for i in range(qlen):
                node = q.popleft()
                if not node:
                    continue
                if found == False:
                    res.append(node.val)
                    found = True
                
                q.append(node.right)
                q.append(node.left)
        return res