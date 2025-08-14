## Problem: https://leetcode.com/problems/reverse-integer/description/
### Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

### Example 1:
Input: x = 123
Output: 321

### Example 2:
Input: x = -123
Output: -321

### Example 3:
Input: x = 120
Output: 21
 

### Constraints:

-231 <= x <= 231 - 1

# Solution
## Intuition
Convert the given integer into a string and consider the sign of the integer into consideration, then reverse the string and convert it back to an integer.


## Approach
First, consider the sign of the given integer and convert it to its absolute value.
We will use the algorithm that takes in digit and digit from the end and adds it to the result. If there is any overflow in the process, we wil return 0 otherwise we will return the valid value multiplied with the sign.

## Complexity
- Time complexity:
$$O(logn)$$ Where n is the number.

- Space complexity:
$$O(1)$$ It is constant

## Code
```python3 
    import sys
    class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = -1 if x < 0 else 1
        x = x*sign
        while x != 0:
            remainder = x%10
            result = result * 10 + remainder
            if result > (2**31 - 1) :
                return 0
            x = x//10
        return result * sign
```