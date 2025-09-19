## Problem: https://leetcode.com/problems/excel-sheet-column-number/description/
### 
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

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
Input: columnTitle = "A"
Output: 1

### Example 2:
Input: columnTitle = "AB"
Output: 28

### Example 3:
Input: columnTitle = "ZY"
Output: 701

### Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].

# Solution
## Approach
The approach is to check the individual letter and convert it into number using the exponential operator.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def titleToNumber(self, s: str) -> int:
        #d={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11}
        n=len(s)
        c=0
        for i in range(len(s)):
            c+=(ord(s[n-i-1])-64)*(26**i)
        return c
```
