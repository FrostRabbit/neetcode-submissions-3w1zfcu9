class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        def dfs(r,c):
            if r >=m or r<0 or c<0 or c>=n or board[r][c] != 'O':
                return
            board[r][c] = 'A'
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        for i in range(m):
            for j in range(n):
                if (i==0 or j == 0 or i==m-1 or j==n-1):
                    dfs(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'