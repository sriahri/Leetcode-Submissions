## Problem: https://leetcode.com/problems/climbing-stairs/description/
### 
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 
### Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

### Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

### Constraints:
1 <= n <= 45

# Solution
## Approach
The approach is to use dynamic programming. For step 0, we will have 0 ways, for step 1, we will have 1 way. For all the other steps, we can have either have 1 step or 2 steps at a single time. So, the recurrence relation will be f(n) = f(n-1) + f(n-2)

- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+2)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+2):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
```
