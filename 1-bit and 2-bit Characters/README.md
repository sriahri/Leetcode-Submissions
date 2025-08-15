## Problem: https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
### 
We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

 
### Example 1:
Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.

### Example 2:
Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.

### Constraints:
1 <= bits.length <= 1000 \\
bits[i] is either 0 or 1. \\

# Solution

## Approach
The approach is to count the number of consecutive 1s that are present in the given bit array from the end. The last element can be ignored because it is always zero. If there are no consecutive 1s in the array, then we can pair them with 0s. If the number of consecutive 1s is odd, then it is False, else True.
## Complexity
- Time complexity:
$$O(n)$$ Where n is the length of the input array.

- Space complexity:
$$O(1)$$

## Code
```python3 
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        count = 0
        for i in range(len(bits) - 2, -1, -1):
            if bits[i] == 1:
                count += 1
            else:
                break
        return True if count%2 == 0 else False
```