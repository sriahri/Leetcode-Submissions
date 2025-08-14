## Problem: https://leetcode.com/problems/search-insert-position/description/
### Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

### Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

### Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

### Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

### Constraints:
1 <= nums.length <= $$10^4$$ \\
$$-10^4$$ <= nums[i] <= $$10^4$$ \\
nums contains distinct values sorted in ascending order. \\
$$-10^4$$ <= target <= $$10^4$$

# Solution

## Approach
The approach is to use the binary search algorithm to find the target and return its index if it is found. If the element is not found, we will return the variable low.

## Complexity
- Time complexity:
$$O(logn)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low
```
