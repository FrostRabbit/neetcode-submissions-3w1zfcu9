class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        res = 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                elif grid[i][j] == 1:
                    count+=1

        while q:
            r,s,cnt = q.popleft()
            res = cnt
            for i,j in dirs:
                x,y = r+i,s+j
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 1:
                    grid[x][y] = 2
                    q.append((x,y,cnt+1))
                    count-=1
        return -1 if count>0 else res