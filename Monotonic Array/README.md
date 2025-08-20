## Problem: https://leetcode.com/problems/monotonic-array/description/
### 
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.


### Example 1:
Input: nums = [1,2,2,3]
Output: true

### Example 2:
Input: nums = [6,5,4,4]
Output: true

### Example 3:
Input: nums = [1,3,2]
Output: false

### Constraints:
1 <= nums.length <= $$10^5$$ \
-105 <= nums[i] <= $$10^5$$
# Solution
## Approach
The basic approach is to first sort the array and check if the array is the same as the sorted one or not.
The other approach is to first check if the array is increasing or decreasing. If it is increasing, then each element must be greater than the previous element. If it is decreasing, then each element must be smaller than the previous element.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # n = len(nums)
        # sortedNums = sorted(nums)
        # if nums == sortedNums or nums[::-1] == sortedNums:
        #     return True
        # return False

        n = len(nums)
        if n <= 1:
            return True
        flag = True
        if nums[0] > nums[1]:
            flag = False
        i = 1
        while i < n and nums[i] == nums[i-1]: 
            i += 1
        if i < n and nums[i] < nums[i-1]:
            flag = False
        while i < n:
            if flag:
                if nums[i] < nums[i-1]:
                    return False
            else:
                if nums[i] > nums[i-1]:
                    return False
            i += 1
        return True
```
