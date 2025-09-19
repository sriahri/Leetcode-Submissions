## Problem: https://leetcode.com/problems/contains-duplicate/description/
### 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

### Example 1:
Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

### Example 2:
Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

### Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

### Constraints:
1 <= nums.length <= $$10^5$$
-$$10^9$$ <= nums[i] <= $$10^9$$

# Solution
## Approach
The approach is to use Counter to form a hashmap and check if the count of any value is greater than 1 or not.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=Counter(nums)
        for i in d.keys():
            if d[i]>1:
                return True
        return False
```