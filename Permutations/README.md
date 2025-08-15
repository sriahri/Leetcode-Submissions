## Problem: https://leetcode.com/problems/permutations/description/
### 
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
 
### Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

### Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

### Example 3:
Input: nums = [1]
Output: [[1]]

### Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

# Solution

## Approach
The approach is to use the backtracking approach. Add the current element to the list and if the index is greater than the length of the input, then add the current list to the result. Then, backtrack by removing the latest added element in the list and add the next element. Repeat this process until the base conditions are met.

## Complexity
- Time complexity:
$$O(n!)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def helper(self, ind, arr, current, result):
        if ind >= len(arr):
            result.append(arr[:])
        for i in range(ind, len(arr)):
            arr[ind], arr[i] = arr[i], arr[ind]
            self.helper(ind+1, arr, current, result)
            arr[ind], arr[i] = arr[i], arr[ind]
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(0, nums, [], result, )
        return result
```
