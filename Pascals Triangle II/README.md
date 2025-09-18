## Problem: https://leetcode.com/problems/pascals-triangle-ii/description/
### 
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

### Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

### Example 2:
Input: rowIndex = 0
Output: [1]

### Example 3:
Input: rowIndex = 1
Output: [1,1]

### Constraints:
1 <= numRows <= 33

# Solution
## Approach
We can use the mathematical approach to compute the values using factorial logic based on the row number and the count value. This is more beneficial if it is required to just print the given nth row.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
from math import factorial
class Solution:
    def getRow(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            if i==0:
                l.append(1)
            else:
                l.append(factorial(n)//(factorial(i)*factorial(n-i)))
        return l
```
