class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        res = 0
        def DFS(r,c):
            if r <0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0":
                return

            grid[r][c]="0"
            DFS(r-1,c)
            DFS(r+1,c)
            DFS(r,c-1)
            DFS(r,c+1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    DFS(i,j)
                    res += 1
        
        return res

