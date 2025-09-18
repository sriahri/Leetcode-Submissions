## Problem: https://leetcode.com/problems/single-number/description/
### 
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

### Example 1:
Input: nums = [2,2,1]

Output: 1

### Example 2:
Input: nums = [4,1,2,1,2]

Output: 4

### Example 3:
Input: nums = [1]

Output: 1

### Constraints:
1 <= nums.length <= 3 * $$10^4$$
-3 * $$10^4$$ <= nums[i] <= 3 * $$10^4$$
Each element in the array appears twice except for one element which appears only once.

# Solution
## Approach
The approach is to count all the elements using Counter and check whose count is 1.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=Counter(nums)
        for i in d.keys():
            if d[i]==1:
                return i
```
