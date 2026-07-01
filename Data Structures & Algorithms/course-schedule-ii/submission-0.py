class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0]*numCourses
        nei = [[] for _ in range(numCourses)]
        q = deque()
        take = 0
        results = []
        for a,b in prerequisites:
            degree[a] += 1
            nei[b].append(a)
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            take += 1
            degree[node]-=1
            results.append(node)
            for n in nei[node]:
                degree[n] -= 1
                if degree[n] == 0:
                    q.append(n)
        
        if take == numCourses:
            return results

        return []
        