## Problem: https://leetcode.com/problems/4sum/description/
### Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

### Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

### Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

### Constraints:

1 <= nums.length <= 200
$$-10^9$$ <= nums[i] <= $$10^9$$
$$-10^9$$ <= target <= $$10^9$$

# Solution
## Intuition
Run 4 loops to check if 4 numbers sum up to a given target or not. The first loop iterates through the array and for each integer in the array, there will be 3 inner loops and the last inner loop is a linear search algorithm to find if the remainder is present or not. This is an $$O(n^4)$$ solution.


## Approach
The better optimal approach is to first sort the array and then search for the triplets using the 3sum property for every element in the array. Since the array is sorted, we can use the property of binary seaech in the 2sum property to check if the remainder of the sum is present or not.

## Complexity
- Time complexity:
$$O(n^2logn)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def twoSum(self, nums, target):
        res = []
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] + nums[j] == target:
                res.append([nums[i], nums[j]])
                i += 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return res
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                passing = nums[j+1:]
                twoSumRes = self.twoSum(passing, target - nums[i] - nums[j])
                if twoSumRes:
                    for x, y in twoSumRes:
                        sub = [nums[i], nums[j], x, y]
                        res.append(sub)
        return res

        # nums.sort()
        # res = []
        # quad = []

        # def kSum(k, start, target):
        #     if k == 2:
        #         end = len(nums)
        #         while start < end:
        #             if nums[start] + nums[end] == target:
        #                 quad.append(nums[start])
        #                 quad.append(nums[end])
        #                 start += 1
        #                 while start < end and nums[start] == nums[start - 1]:
        #                     start += 1
        #             elif nums[start] + nums[end] > target:
        #                 end -= 1
        #             else:
        #                 start += 1
        #     for i in range(start, len(nums) - k + 1):
        #         if i > start and nums[i] == nums[i-1]:
        #             continue
        #         quad.append(nums[i])
        #         kSum(i+1, target-nums[i])
        #         quad.pop()
        #     if len(quad) == 4:
        #         res.append(quad)
        #         quad = []
        # kSum(4, 0, target)
        # return res
```
