## Problem: https://leetcode.com/problems/reverse-bits/description/
### 
Reverse bits of a given 32 bits signed integer.

### Example 1:
Input: n = 43261596

Output: 964176192

Explanation:

Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000


### Example 2:
Input: n = 2147483644

Output: 1073741822

Explanation:

Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110

### Constraints:
0 <= n <= $$2^31$$ - 2
n is even.

# Solution
## Approach
The approach is to first convert the integer into binary numbers. Now, reverse the binary representation and append the 0s at the start till the total length reaches 32.

## Complexity
- Time complexity:
$$O(logn)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def reverseBits(self, n: int) -> int:
        s=bin(n)[2:]
        #s=str(n)
        l=len(s)
        s=(32-l)*'0'+s
        s=s[::-1]
        x=int(s,2)
        return x
```
