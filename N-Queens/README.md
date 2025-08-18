## Problem: https://leetcode.com/problems/n-queens/description/
### 
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

### Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

### Example 2:
Input: n = 1
Output: [["Q"]]

### Constraints:
1 <= n <= 9

# Solution

## Approach
The approach is to use the backtracking approach and try all the possibilities of where a queen can be placed in a square starting from row 0 col 0, If the current position does not work out, then we try all the different positions. For every column, we check all the different positions of a row. For example, row 0, col 0 does not work out, we try position 1 and so on. First, we place a queen at row 0, the for col 1, we can place it at row 2, for col 2, there is  no place to place in the given 4x4 board. Now, we back track to the previous of the col 1 and try the other positions, etc.
## Complexity
- Time complexity:
$$O(n!)$$ \\

- Space complexity:
$$O(n)$$

## Code
```python3 []
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
```
