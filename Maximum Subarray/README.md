## Problem: https://leetcode.com/problems/maximum-subarray/description/
### 
Given an integer array nums, find the subarray with the largest sum, and return its sum.

### Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

### Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

### Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

### Constraints:
1 <= nums.length <= $$10^5$$ \\
$$-10^4$$ <= nums[i] <= $$10^4$$ \\

# Solution

## Approach
The approach is to use the Kadane's algorithm. The algorithm is to check whether the current element when added to the result gives us the maximum sum or not. At every iteration, we get the subarray with maximum sum.
## Complexity
- Time complexity:
$$O(n)$$ \\

- Space complexity:
$$O(1)$$

## Code
```python3 []
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -sys.maxsize
        maxi = result
        for num in nums:
            maxi = max(maxi + num, num)
            result = max(maxi, result)
        return result
```
