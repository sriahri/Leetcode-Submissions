## Problem: https://leetcode.com/problems/sort-array-by-parity-ii/
### 
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

### Example 1:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

### Example 2:
Input: nums = [2,3]
Output: [2,3]

### Constraints:
2 <= nums.length <= 2 * $$10^4$$
nums.length is even.
Half of the integers in nums are even.
0 <= nums[i] <= 1000

# Solution
## Approach
The approach is to store the even numbers and odd numbers separately. Sort them individually and store them finally in a result list.
## Complexity
- Time complexity:
$$O(nlogn)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        result = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        even.sort()
        odd.sort()
        i = 0
        n = len(nums)
        while i < n//2:
            result.append(even[i])
            result.append(odd[i])
            i += 1
        return result
```
