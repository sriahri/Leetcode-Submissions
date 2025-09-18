## Problem: https://leetcode.com/problems/pascals-triangle/description/
### 
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it

### Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

### Example 2:
Input: numRows = 1
Output: [[1]]

### Constraints:
1 <= numRows <= 30

# Solution
## Approach
The approach is to calculate all the elements and store them in a list and return it. We can also use the mathematical approach to compute the values using factorial logic based on the row number and the count value. This is more beneficial if it is required to just print the given nth row.

## Complexity
- Time complexity:
$$O(n^2)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        l=[]
        for i in range(1,n+1):
            x=[]
            c=1
            for j in range(1,i+1):
                x.append(c)
                c=((c*(i-j))//j)
            l.append(x)
        return l
```
