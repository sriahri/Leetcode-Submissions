## Problem: https://leetcode.com/problems/duplicate-zeros/
### 
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

### Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

### Example 2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

### Constraints:
1 <= arr.length <= $$10^4$$ \
0 <= arr[i] <= 9

# Solution
## Approach
The approach is to first find the indices of the element 0 in the given list. Add zeros in the list at that index. Remove all the extra elements.

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        indices = []
        for i in range(n):
            if arr[i] == 0:
                indices.append(i)
        for i in range(len(indices)):
            arr.insert(indices[i] + i, 0)
        for i in range(len(arr) - n):
            arr.pop()
```
