class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0]*numCourses
        nei = [[] for _ in range(numCourses)]
        q = deque()
        results = []
        for a,b in prerequisites:
            degree[a] += 1
            nei[b].append(a)

        
        def DFS(node):
            degree[node] -= 1
            results.append(node)
            for n in nei[node]:
                degree[n] -= 1
                if degree[n] == 0:
                    DFS(n)
        
        for i in range(numCourses):
            if degree[i] == 0:
                DFS(i)
        if len(results) == numCourses:
            return results

        return []
        