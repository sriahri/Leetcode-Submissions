## Problem: https://leetcode.com/problems/sqrtx/description/
### 
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
### Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

### Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

### Constraints:
0 <= x <= $$2^31$$ - 1

# Solution
## Approach
The approach is to start with 1 and check if it is the square root of the given number or not. Else, continue this until the result is found.

- Time complexity:
$$O(sqrt(n))$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def mySqrt(self, x: int) -> int:
        res = 1
        while res * res <= x:
            res += 1
        return res - 1
```
