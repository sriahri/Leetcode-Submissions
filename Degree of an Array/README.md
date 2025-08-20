## Problem: https://leetcode.com/problems/degree-of-an-array/
### 
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

### Example 1:
Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

### Example 2:
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

### Constraints:
nums.length will be between 1 and 50,000. \
nums[i] will be an integer between 0 and 49,999.

# Solution
## Approach
The approach is to store the leftmost occurence and the rightmost occurence of a number in a hashmap along with the count. If the count of the number is equal to the degree of the array, then we compute the minimum length subarray required. At every possible element, we compute the minimum length required.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        d = {}
        leftOccurence = {}
        rightOccurence = {}
        for i in range(len(nums)):
            rightOccurence[nums[i]] = i
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                leftOccurence[nums[i]] = i
                d[nums[i]] = 1

        degree = 0
        for i in d.keys():
            if d[i] > degree:
                degree = d[i]
        result = len(nums)
        for num in d.keys():
            print(result)
            if d[num] == degree:
                result = min(result, rightOccurence[num] - leftOccurence[num] + 1)
        return result
```
