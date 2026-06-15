class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        take = {i:[] for i in range(numCourses)}
        for t,p in prerequisites:
            take[t].append(p)
        visited = set()
        def dfs(course):
            if course in visited: return False
            if take[course] == []: return True

            visited.add(course)
            for p in take[course]:
                if not dfs(p): return False
            visited.remove(course)
            take[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True