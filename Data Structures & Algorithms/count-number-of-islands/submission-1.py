class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        def DFS(r,c):
            if r <0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]=="0":
                return

            grid[r][c]="0"
            DFS(r-1,c)
            DFS(r+1,c)
            DFS(r,c-1)
            DFS(r,c+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    DFS(i,j)
                    res += 1
        
        return res

