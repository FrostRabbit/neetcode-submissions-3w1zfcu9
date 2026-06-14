"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodemap ={}
        def dfs(n):
            if n in nodemap:
                return nodemap[n]

            copy = Node(n.val)
            nodemap[n]=copy
            for x in n.neighbors:
                copy.neighbors.append(dfs(x))
            return copy
        return dfs(node) if node else None
            