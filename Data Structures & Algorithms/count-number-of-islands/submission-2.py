class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        res = 0
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        def BFS(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row,col = q.popleft()

                for i,j in direction:
                    di= row+i
                    dj= col+j
                    if di<0 or dj<0 or di >= len(grid) or dj >= len(grid[0]) or grid[di][dj]=="0":
                        continue
                    
                    q.append((di,dj))
                    grid[di][dj]="0"
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] =="1":
                    BFS(i,j)
                    res +=1
        return res