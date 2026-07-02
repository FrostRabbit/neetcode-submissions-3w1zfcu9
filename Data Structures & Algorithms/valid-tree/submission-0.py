class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 < len(edges) and len(edges) < n-1 : return False
        nei = [[] for _ in range(n)]

        for a, b in edges:
            nei[a].append(b)
            nei[b].append(a)
        
        visited = set()
        def DFS(node, parent):
            if node in visited: return False
            visited.add(node)
            for i in nei[node]:
                if i == parent: continue

                if not DFS(i, node):
                    return False
            
            return True
        
        return DFS(0, -1) and len(visited) == n