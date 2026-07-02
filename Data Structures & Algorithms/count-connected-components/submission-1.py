class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nei = [[] for _ in range(n)]

        for a,b in edges:
            nei[a].append(b)
            nei[b].append(a)
        result = 0
        visited = set()
        for i in range(n):
            if i in visited: continue
            q = deque()
            q.append(i)
            visited.add(i)
            while q:
                node = q.popleft()
                for x in nei[node]:
                    if x not in visited:
                        q.append(x)
                        visited.add(x)
            result += 1
        return result

