## Problem: https://leetcode.com/problems/binary-prefix-divisible-by-5/description/
### 
You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

 

### Example 1:
Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.

### Example 2:
Input: nums = [1,1,1]
Output: [false,false,false]

### Constraints:
1 <= nums.length <= $$10^5$$ \
nums[i] is either 0 or 1.

# Solution
## Approach
The approach is to convert the binary representation at every iteration into an integer and check if if it is divisible by 5 or not.
One way to convert the binary representation into integer using the int method. Other way to do it by multiplying the current number with 2 and adding it to the current binary number.
## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # nums = list(map(str, nums))
        # result = []
        # for i in range(len(nums)):
        #     x = ''.join(nums[:i+1])
        #     if int(x, 2) % 5 == 0:
        #         result.append(True)
        #     else:
        #         result.append(False)
        # return result

        result = []
        number = 0
        for i in range(len(nums)):
            number = number * 2 + nums[i]
            result.append(number % 5 == 0)
        return result
```
