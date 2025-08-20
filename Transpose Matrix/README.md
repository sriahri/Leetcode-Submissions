## Problem: https://leetcode.com/problems/transpose-matrix/
### 
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

### Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

### Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

### Constraints:
m == matrix.length \
n == matrix[i].length \
1 <= m, n <= 1000 \
1 <= m * n <= $$10^5$$ \
$$-10^9$$ <= matrix[i][j] <= $$10^9$$
# Solution
## Approach
Transpose the matrix by converting the row elements into columns and column elements into rows

## Complexity
- Time complexity:
$$O(mxn)$$

- Space complexity:
$$O(mxn)$$

## Code
```python3 []
class Solution:
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        transpose = [[0] * m for _ in range(n)]
        for j in range(m):
            for i in range(n):
                transpose[i][j] = matrix[j][i]
        return transpose
```
