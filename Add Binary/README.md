## Problem: https://leetcode.com/problems/add-binary/description/
### 
Given two binary strings a and b, return their sum as a binary string.
 
### Example 1:
Input: a = "11", b = "1"
Output: "100"

### Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

### Constraints:
1 <= a.length, b.length <= $$10^4$$
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

# Solution
## Approach
The approach is to first convert the given binary numbers into integers and add them. Finally, convert the result to binary number.

- Time complexity:
$$O(1)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1=int(a,2)
        b1=int(b,2)
        res=a1+b1
        return bin(res)[2:]
```
