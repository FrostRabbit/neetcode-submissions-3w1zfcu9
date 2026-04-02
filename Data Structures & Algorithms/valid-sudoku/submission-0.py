class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            know = set()
            for j in range(9):
                if board[i][j] == '.': continue
                if board[i][j] in know: return False
                know.add(board[i][j])
        for i in range(9):
            know = set()
            for j in range(9):
                if board[j][i] == '.': continue
                if board[j][i] in know: return False
                know.add(board[j][i])
        for i in range(9):
            know = set()
            for j in range(3):
                for k in range(3):
                    row = (i // 3)*3 +j
                    col = (i % 3)*3+k
                    if board[row][col] == '.': continue
                    if board[row][col] in know: return False
                    know.add(board[row][col])
        return True
            