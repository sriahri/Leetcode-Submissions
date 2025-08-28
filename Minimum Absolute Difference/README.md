## Problem: https://leetcode.com/problems/minimum-absolute-difference/description/
### 
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 
### Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

### Example 2:
Input: arr = [1,3,6,10,15]
Output: [[1,3]]

### Example 3:
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]

### Constraints:
2 <= arr.length <= $$10^5$$
-106 <= arr[i] <= $$10^6$$

# Solution
## Approach
The approach is to first sort the array and first check the minimum absolute difference between 2 elements. Once, we get the minimum difference, we iterate through the array and check if the difference between consecutive elements is equal to the minimum absolute difference or not. If it is, add the pair to the result.
## Complexity
- Time complexity:
$$O(nlogn)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        result = []
        minDiff = arr[-1] - arr[0]
        for i in range(1, n):
            if arr[i] - arr[i-1] < minDiff:
                minDiff = arr[i] - arr[i-1]
        for i in range(1, n):
            if arr[i] - arr[i-1] == minDiff:
                result.append([arr[i-1], arr[i]])
        return result
```
