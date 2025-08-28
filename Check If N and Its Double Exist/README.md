## Problem: https://leetcode.com/problems/check-if-n-and-its-double-exist/description/
### 
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

### Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

### Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.

### Constraints:
2 <= arr.length <= 500 \
$$-10^3$$ <= arr[i] <= $$10^3$$

# Solution
## Approach
The approach is to sort the array and check for every element there is a double element or not using binary search. This will take $$O(nlogn)$$ time complexity.
The other approach is to use a hashmap and store all the elements in it and check if there is a double element or not. The time complexity in this case is $$O(n)$$.

- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
from collections import Counter
class Solution:
    def binarySearch(self, arr, k):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low+high) // 2
            if arr[mid] == k:
                return True
            elif arr[mid] > k:
                high = mid - 1
            else:
                low = mid + 1
        return False
    def checkIfExist(self, arr: List[int]) -> bool:
        # arr.sort()
        # found = self.binarySearch(arr, 0)
        # if found:
        #     if arr.count(0) > 1:
        #         return True
        #     else:
        #         arr.remove(0)
        # for i in arr:
        #     if self.binarySearch(arr, 2*i):
        #         return True
        # return False
        d = Counter(arr)
        for i in d.keys():
            if i == 0:
                if d[i] > 1:
                    return True
            elif 2*i in d:
                return True
        return False
```
