## Problem: https://leetcode.com/problems/palindrome-number/description/
### Given an integer x, return true if x is a palindrome, and false otherwise.

 
### Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

### Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

### Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

### Constraints:
$$(-2^31 <= x <= 2^31 - 1)$$

# Solution
## Intuition
Convert the given integer into a string, then reverse the string and check if the string and its reverse is equal or not. If they are equal, we will return true, else false.


## Approach
The better optimal approach is if the number is less than 0, then the answer is false, Now, we need to only check for the positive numbers. Reverse the number and check if the number is same or not.

## Complexity
- Time complexity:
$$O(logn)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        if s[0]=='-':
            return False
        a=s[::-1]
        if s==a:
            return True
        return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        copy = x
        if x < 0:
            return False
        while x != 0:
            res = res * 10 + x%10
            x = x//10
        if res == copy:
            return True
        return False
```
