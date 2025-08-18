class Solution:
    def isSafe(self, main_row, main_col, board):
        row = main_row
        col = main_col
        while row < len(board):
            if board[row][col] == 'Q':
                return False
            row += 1
        row = main_row
        col = main_col
        while row >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
        row = main_row
        col = main_col
        while col < len(board):
            if board[row][col] == 'Q':
                return False
            col += 1
        row = main_row
        col = main_col
        while col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1
        row = main_row
        col = main_col
        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1
        row = main_row
        col = main_col
        while row >= 0 and col < len(board):
            if board[row][col] == 'Q':
                return False
            row -= 1
            col += 1
        row = main_row
        col = main_col
        while row < len(board) and col < len(board):
            if board[row][col] == 'Q':
                return False
            row += 1
            col += 1
        row = main_row
        col = main_col
        while row < len(board) and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1
        row = main_row
        col = main_col
        return True
    def solve(self,col, n, board, res):
        if col == n:
            cur = []
            for x in board:
                cur.append(''.join(x))
            res.append(cur[:])
            return
        for i in range(n):
            if self.isSafe(i, col, board):
                board[i][col] = 'Q'
                self.solve(col+1, n, board, res)
                board[i][col] = '.'
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for i in range(n)]
        rows = n
        cols = n
        result = []
        self.solve(0, n, board, result)
        return result