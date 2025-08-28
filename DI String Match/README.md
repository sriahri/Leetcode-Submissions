## Problem: https://leetcode.com/problems/di-string-match/description/
### 
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

### Example 1:
Input: s = "IDID"
Output: [0,4,1,3,2]

### Example 2:
Input: s = "III"
Output: [0,1,2,3]

### Example 3:
Input: s = "DDI"
Output: [3,2,0,1]

### Constraints:
1 <= s.length <= $$10^5$$ \
s[i] is either 'I' or 'D'.

# Solution
## Approach
The approach is to add the minimum element if the string is I and add the maximum character if the string is D. Finally, add either the minimum element or the maximum element since the result contains n + 1 elements.

- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        result = []
        mini = 0
        maxi = len(s)
        for i in range(len(s)):
            if s[i] == 'I':
                result.append(mini)
                mini += 1
            else:
                result.append(maxi)
                maxi -= 1
        result.append(mini)
        return result
            
```
