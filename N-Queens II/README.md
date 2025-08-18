## Problem: https://leetcode.com/problems/n-queens-ii/description/
### 
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

### Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

### Example 2:
Input: n = 1
Output: 1

### Constraints:
1 <= n <= 9

# Solution

## Approach
The approach is to use the backtracking approach and try all the possibilities of where a queen can be placed in a square starting from row 0 col 0, If the current position does not work out, then we try all the different positions. For every column, we check all the different positions of a row. For example, row 0, col 0 does not work out, we try position 1 and so on. First, we place a queen at row 0, the for col 1, we can place it at row 2, for col 2, there is  no place to place in the given 4x4 board. Now, we back track to the previous of the col 1 and try the other positions, etc.
Count all the possible ways directly by checking if the current position is safe or not for every position. This means that even if the board is fully placed we should go back and try the other possibilities as well.

## Complexity
- Time complexity:
$$O(n!)$$ \\

- Space complexity:
$$O(n)$$

## Code
```python3 []
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
```
