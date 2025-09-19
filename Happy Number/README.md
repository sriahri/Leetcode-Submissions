## Problem: https://leetcode.com/problems/happy-number/description/
### 
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

### Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

### Example 2:
Input: n = 2
Output: false

### Constraints:
1 <= n <= $$2^31 - 1$$

# Solution
## Approach
The approach is to use the slow pointer and fast pointer technique(Tortoise and hare algorithm) to check if there is a cycle that is formed or not. If a cycle is detected, we break the loop and check the slow pointer is 1 or not.

## Complexity
- Time complexity:
$$O()$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
def numSquareSum(n): 
    squareSum = 0; 
    while(n): 
        squareSum += (n % 10) * (n % 10); 
        n = int(n / 10); 
    return squareSum;
class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n; 
        fast = n; 
        while(True): 

            # move slow number 
            # by one iteration 
            slow = numSquareSum(slow); 

            # move fast number 
            # by two iteration 
            fast = numSquareSum(numSquareSum(fast)); 
            if(slow != fast): 
                continue; 
            else: 
                break; 

        # if both number meet at 1,  
        # then return true 
        return (slow == 1);
