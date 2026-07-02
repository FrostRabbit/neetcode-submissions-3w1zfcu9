class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.count = n
    
    def find(self, node: int) -> int:
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, a: int, b: int):
        p1 = self.find(a)
        p2 = self.find(b)
        if p1 != p2:
            self.parent[p1] = p2
            self.count-=1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for a,b in edges:
            dsu.union(a,b)
        
        return dsu.count

