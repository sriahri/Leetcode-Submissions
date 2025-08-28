## Problem: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/
###
Given an integer n, return any array containing n unique integers such that they add up to 0.

### Example 1:
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

### Example 2:
Input: n = 3
Output: [-1,0,1]

### Example 3:
Input: n = 1
Output: [0]

### Constraints:
1 <= n <= 1000

# Solution
## Approach
The approach is that for odd number of elements, we need have numbers starting from $$-n/2$$ to $$n/2$$ and for even number of elements, we will skip 0.

- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n%2 == 0:
            i = -1 * (n//2)
            while i <= n // 2:
                if i != 0:
                    result.append(i)
                i += 1
        else:
            x = n//2
            for i in range(-x, x + 1):
                result.append(i)
        return result
```
