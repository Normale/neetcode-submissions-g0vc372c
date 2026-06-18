"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = dict()
        
        def dfs(node):
            if node in visited:
                return visited[node.val]
            cloned_node = Node(val=node.val)
            visited[node.val] = cloned_node
            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    n_clone = dfs(neighbor)
                else:
                    n_clone = visited[neighbor.val]
                cloned_node.neighbors.append(n_clone)

            return cloned_node
        c = dfs(node)
        return c