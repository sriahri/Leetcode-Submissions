## Problem: https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
### 
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
 
### Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

### Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

### Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

### Constraints:
m == mat.length \
n == mat[i].length \
1 <= n, m <= 50 \
1 <= matrix[i][j] <= $$10^5$$. \
All elements in the matrix are distinct.

# Solution
## Approach
The approach is to first store all elements in each column into a list. Next,for each row, check all columns whether they match the condition or not.

- Time complexity:
$$O(m*n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        cols = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            x = []
            for j in range(m):
                x.append(matrix[j][i])
            cols.append(x)
        result = []
        print(cols)
        for i in range(m):
            for j in range(n):
                if min(matrix[i]) == max(cols[j]):
                    result.append(min(matrix[i]))
        return result
```
