## Problem: https://leetcode.com/problems/group-anagrams/description/
### 
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

### Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

### Example 2:
Input: strs = [""]
Output: [[""]]

### Example 3:
Input: strs = ["a"]
Output: [["a"]]

### Constraints:
1 <= strs.length <= $$10^4$$ \\
0 <= strs[i].length <= 100 \\
strs[i] consists of lowercase English letters. \\

# Solution

## Approach
The approach is to sort all the strings in the array and count all the anagrams and store them in a dictionary. Then run 2 loops to check if 2 strings are same or not. If they are same store them in a list and append them to the result list.
## Complexity
- Time complexity:
$$O(n*max(len(s[i]))log(max(len(s[i]))) or n^2)$$ \\

- Space complexity:
$$O(n)$$

## Code
```python3 []
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[None]*len(strs)
        a=[]
        for i in range(len(strs)):
            x=str(sorted(strs[i]))
            s=''.join(x)
            l[i]=s
        d=Counter(l)
        for i in d.keys():
            y=[]
            for j in range(len(l)):
                if i==l[j]:
                    y.append(strs[j])
            a.append(y)
        return a
```
