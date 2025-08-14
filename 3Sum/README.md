## Problem: https://leetcode.com/problems/3sum/description/
### Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
 

### Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

### Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

### Example 3:
Input: nums = [0, 0, 0]
Output: [0,0, 0]
Explanation: The only possible triplet sums up to 0.
 

### Constraints:

3 <= nums.length <= 3000
$$-10^5$$ <= nums[i] <= $$10^5$$

# Solution
## Intuition
Run 3 loops to check if 3 numbers sum up to a 0 or not. The first loop iterates through the array and for each integer in the array, the second inner loop iterates through the array and for each integer in the array the third inner loop is a linear search algorithm to find if the remainder is present or not. This is an $$O(n^3)$$ solution.


## Approach
The better optimal approach is to first sort the array and then search for the triplets using the 2sum property for every element in the array. Since the array is sorted, we can use the property of binary seaech in the 2sum property to check if the remainder of the sum is present or not.

## Complexity
- Time complexity:
$$O(nlogn)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:

    def twoSum(self, nums, target):
        res = []
        i = 0
        j = len(nums) - 1
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
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        if len(nums) < 3:
            return res
        x = nums.count(0)
        if x == len(nums):
            return [[0, 0, 0]]
        for i in range(len(nums)):
            if nums[i] != nums[i-1]:
                if i == len(nums) -1:
                    return res
                passing = nums[i+1:]
                # print(passing)
                twoSumRes = self.twoSum(passing, -nums[i])
                if twoSumRes:
                    for x, y in twoSumRes:
                        sub = [nums[i]]
                        sub.append(x)
                        sub.append(y)
                        res.append(sub)
        return res
```
