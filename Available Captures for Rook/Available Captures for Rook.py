class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        result = 0
        m = len(board)
        n = len(board[0])
        position = None
        for i in range(m):
            if position:
                break
            for j in range(n):
                if board[i][j] == 'R':
                    position = [i, j]
                    break
        i, j = position
        while i < m:
            if board[i][j] == 'B':
                break
            if board[i][j] == 'p':
                result += 1
                break
            i += 1
        i, j = position
        while j < n:
            if board[i][j] == 'B':
                break
            if board[i][j] == 'p':
                result += 1
                break
            j += 1
        i, j = position
        while i >= 0:
            if board[i][j] == 'B':
                break
            if board[i][j] == 'p':
                result += 1
                break
            i -= 1
        i, j = position
        while j >= 0:
            if board[i][j] == 'B':
                break
            if board[i][j] == 'p':
                result += 1
                break
            j -= 1
        return result