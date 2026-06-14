class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            while q:
                x,y=q.popleft()
                for rd,cd in dirs:
                    a,b=x+rd,y+cd
                    if a >=m or a<0 or b<0 or b>=n or board[a][b] == 'X'or board[a][b] == 'A':
                        continue
                    board[a][b] = 'A'
                    q.append((a,b))

        for i in range(m):
            for j in range(n):
                if (i==0 or j == 0 or i==m-1 or j==n-1) and board[i][j]=='O':
                    board[i][j]='A'
                    bfs(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'