## Problem: https://leetcode.com/problems/majority-element/description/
### 
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

### Example 1:
Input: nums = [3,2,3]
Output: 3

### Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

### Constraints:
n == nums.length
1 <= n <= 5 * $$10^4$$
-$$10^9$$ <= nums[i] <= $$10^9$$

# Solution
## Approach
The approach is to consider the first element as the majority element and count the occurences of it. If it is not, then reduce the count. If at all the count is still 0, then the majority element is changed. Return the majority element.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counter = Counter(nums)
        # for key, value in counter.items():
        #     if value > len(nums)//2:
        #         return key

        count = 0
        majority = nums[0]
        for i in range(len(nums)):
            if majority == nums[i]:
                count += 1
            if count == 0:
                majority = nums[i]
            elif majority != nums[i]:
                count -= 1
            
        return majority
```
