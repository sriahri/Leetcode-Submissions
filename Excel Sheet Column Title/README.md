## Problem: https://leetcode.com/problems/excel-sheet-column-title/description/
### 
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

### Example 1:
Input: columnNumber = 1
Output: "A"

### Example 2:
Input: columnNumber = 28
Output: "AB"

### Example 3:
Input: columnNumber = 701
Output: "ZY"

### Constraints:
1 <= columnNumber <= $$2^31 - 1$$

# Solution
## Approach
The approach is to find the remainder from the given column number and also the quotient with 26. If the remainder is 0, then the column number will have Z. For the quotient, till we get a single digit, we continue the same process.

## Complexity
- Time complexity:
$$O(logn)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def convertToTitle(self, n: int) -> str:
        res=''
        while n>0:
            r=n%26
            n=n//26
            if r==0:
                res+='Z'
            else:
                res+=chr(r+64)
            if r==0:
                n-=1
        return res[::-1]
```
