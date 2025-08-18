class Solution:
    def isSafe(self, row, col, n, board):
        i = row
        j = col
        while i >= 0:
            if board[i][j] == 'Q':
                return False
            i -=1
        i = row
        j = col
        while i < n:
            if board[i][j] == 'Q':
                return False
            i += 1
        i = row
        j = col
        while j >= 0:
            if board[i][j] == 'Q':
                return False
            j -=1
        i = row
        j = col
        while j < n:
            if board[i][j] == 'Q':
                return False
            j += 1
        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -=1
            j -=1
        i = row
        j = col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -=1
            j += 1
        i = row
        j = col
        while i < n and j >= 0:
            if board[i][j] == 'Q':
                return False
            i += 1
            j -=1
        i = row
        j = col
        while i < n and j < n:
            if board[i][j] == 'Q':
                return False
            i += 1
            j += 1
        i = row
        j = col
        return True
    
    def solve(self, col, n, board, result):
        if col == n:
            result.append(board)
            return
        for row in range(n):
            if self.isSafe(row, col, n, board):
                board[row][col] = 'Q'
                self.solve(col+1, n, board, result)
                board[row][col] = '.'
    def totalNQueens(self, n: int) -> int:
        result = []
        board = [['.']*n for _ in range(n)]
        self.solve(0, n, board, result)
        return len(result)

