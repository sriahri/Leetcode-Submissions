## Problem: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description
### 
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

### Example 1:
Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

### Example 2:
Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

### Example 3:
Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

### Constraints:
3 <= arr.length <= 5 * $$10^4$$ \
-$$10^4$$ <= arr[i] <= $$10^4$$

# Solution
## Approach
The approach is to first check if the partition is possible or not. Once we determine it is possible, we find the sum from the front till we reach the required and store the index. Next, we find the sum from the back and store the index from the index. If the index from the back is less than the index from the front, the result is false. We need atleat one element in the middle.
## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        i = 0
        possible = True
        frontSum = 0
        while i < len(arr):
            frontSum += arr[i]
            if frontSum == total // 3:
                break
            i += 1
        if i == len(arr) - 1:
            possible = False
        j = len(arr) - 1
        backSum = 0
        while j >= 0:
            backSum += arr[j]
            if backSum == total // 3:
                break
            j -= 1
        if j == 0 or j <= i+1:
            possible = False
        return possible
```
