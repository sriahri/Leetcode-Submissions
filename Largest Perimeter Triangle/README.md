## Problem: https://leetcode.com/problems/largest-perimeter-triangle/description/
### 
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

### Example 1:
Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

### Example 2:
Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.

### Constraints:
3 <= nums.length <= $$10^4$$ \
1 <= nums[i] <= $$10^6$$

# Solution
## Approach
The approach is to sort the numbers and check if the three largest number can form a triangle or not.

- Time complexity:
$$O(nlogn)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            a = nums[i]
            b = nums[i-1]
            c = nums[i-2]
            if b+c > a:
                return a+b+c
        return 0
```
