## Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
### There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

### Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

### Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

### Example 3:
Input: nums = [1], target = 0
Output: -1

### Constraints:
1 <= nums.length <= 5000 \\
$$-10^4$$ <= nums[i] <= $$10^4$$ \\
All values of nums are unique. \\
nums is an ascending array that is possibly rotated.\\
$$-10^4$$ <= target <= $$10^4$$

# Solution

## Approach
The approach is to use the binary search algorithm to find the target and return its index. But the traditional binary search algorithm does not work. We will find the pivot point and use the binary search algorithm on both the parts of the array to update the low and high variables accordingly.

## Complexity
- Time complexity:
$$O(logn)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[high] >= target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
```
