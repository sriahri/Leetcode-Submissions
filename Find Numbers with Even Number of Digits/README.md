## Problem: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
### 
Given an array nums of integers, return how many of them contain an even number of digits.
 
### Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

### Example 2:
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.

### Constraints:
1 <= nums.length <= 500 \
1 <= nums[i] <= $$10^5$$
# Solution
## Approach
The approach is to first convert the numbers to string and check if the length of the string is even or not.

- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            s = str(num)
            if len(s) % 2 == 0:
                result += 1
        return result
```
