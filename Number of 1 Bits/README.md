## Problem: https://leetcode.com/problems/number-of-1-bits/description/
### 
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

### Example 1:
Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

### Example 2:
Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

### Example 3:
Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

### Constraints:
1 <= columnNumber <= $$2^31 - 1$$

# Solution
## Approach
The approach is to find first convert the given integer into its binary representation and count the number of 1s in it.

## Complexity
- Time complexity:
$$O(logn)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def hammingWeight(self, n: int) -> int:
        s=bin(n)[2:]
        return s.count('1')
```
