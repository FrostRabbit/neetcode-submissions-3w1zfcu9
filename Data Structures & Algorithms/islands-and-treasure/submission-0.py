class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: q.append((i,j,0))
        while q:
            rd,cd,cnt=q.popleft()
            for i,j in dirs:
                x,y = rd+i, cd+j
                if 0<=x<len(grid) and 0<=y < len(grid[0]) and grid[x][y] == 2147483647:
                    q.append((x,y,cnt+1))
                    grid[x][y] = cnt+1
            