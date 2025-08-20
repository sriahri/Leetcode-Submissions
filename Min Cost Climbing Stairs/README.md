## Problem: https://leetcode.com/problems/min-cost-climbing-stairs
### 
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

### Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

### Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

### Constraints:
2 <= cost.length <= 1000 \
0 <= cost[i] <= 999

# Solution
## Approach
This is a DP problem. For step 1, the answer is just that. For step 2, we can start from step 2 itself or step 1 and go from there. So, the answer is the minimum of both the cost. From step 3, it shoud be the minimum till step 2 and step 1 and add the cost of the current step with it. So, the recurrence relation will be $$f(i) = cost[i] + min(f(i-1), f(i-2))  $$

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n
        if n < 2:
            return min(cost)
        dp[0] = cost[0]
        dp[1] = min(cost[0] + cost[1], cost[1])

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[n-1], dp[n-2])
```
