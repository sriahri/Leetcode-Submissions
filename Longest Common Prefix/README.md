## Problem: https://leetcode.com/problems/longest-common-prefix/description/
### Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
### Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

### Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

### Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

# Solution
## Intuition
For all the given strings, check each string character by character and determine the longest prefix.


## Approach
First, sort the list of strings. This is because the lexographically smallest strings come first. If there is a common prefix, then it will be the same for all the strings. So, we only compare the first string and the last string for getting the longest common prefix. This is because the first and last string are the most distinct ones of the lot.

## Complexity
- Time complexity:
$$O(nlogn)$$ Where n is the length list of strings

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        if n==0:
            return ''
        elif n==1:
            return strs[0]
        strs.sort()
        end=min(len(strs[0]),len(strs[-1]))
        i=0
        while i<end and strs[0][i]==strs[-1][i]:
            i+=1
        return strs[0][:i]
```
