class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def DFS(r,c,i):
            if i == len(word): return True

            if r<0  or c< 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            
            board[r][c] = "*"

            res = DFS(r-1,c,i+1) or DFS(r+1,c,i+1) or DFS(r,c-1,i+1) or DFS(r,c+1,i+1)
            board[r][c] = word[i]

            return res

        
        for i in range(rows):
            for j in range(cols):
                if DFS(i,j,0): return True
        
        return False