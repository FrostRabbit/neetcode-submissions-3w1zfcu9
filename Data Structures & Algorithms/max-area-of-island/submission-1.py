class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        def BFS(r,s):
            count = 0
            q = deque()
            grid[r][s]=0
            q.append((r,s))

            while q:
                cr,cs= q.popleft()
                count+=1
                for i,j in dirs:
                    x = cr+i
                    y = cs+j
                    if x<0 or y<0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y]!=1:
                        continue
                    q.append((x,y))
                    grid[x][y]=0
            return count
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res,BFS(i,j))
        
        return res