## Problem: https://leetcode.com/problems/two-sum/description/
### Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

### Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

### Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

### Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

# Solution
## Intuition
Run 2 loops to check if 2 numbers sum up to a given target or not. The first loop iterates through the array and for each integer in the array, the inner loop is a linear search algorithm to find if the remainder is present or not. This is an $$O(n^2)$$ solution.


## Approach
The better optimal approach is to use a dictionary(hashmap) to check if the remainder is present or not. This approach will yield a time complexity of $$O(n)$$ but the trade off here is the space complexity which will be increased to $$O(n)$$.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target-nums[i]) in nums[i+1:]:
                return list([i,(i+1)+nums[i+1:].index(target-nums[i])])
```