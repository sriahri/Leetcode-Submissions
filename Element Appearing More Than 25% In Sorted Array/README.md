## Problem: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/
### 
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
 
### Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

### Example 2:
Input: arr = [1,1]
Output: 1

### Constraints:
1 <= arr.length <= $$10^4$$ \
0 <= arr[i] <= $$10^5$$

# Solution
## Approach
The approach is to first find the length of the array and find the quarter length of it. Check if the element at the current position is equal to the element after quarter length positions.

- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr) // 4
        for i in range(len(arr) - quarter):
            if arr[i] == arr[i+quarter]:
                return arr[i]
```
