## Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
### Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

### Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

### Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
### Constraints:

1 <= haystack.length, needle.length <= $$10^4$$
haystack and needle consist of only lowercase English characters.

# Solution

## Approach
Python has a built-in method named index that returns the first occurence of the given substring in a string only if it is present, otherwise it raises an exception. Also, there is a method find() that returns the first occurence of the substring in a string if it is present, otherwise it returns -1.
We will use the sliding window technique with a fixed window size as the length of the needle and checks if the needle is present in the haystack or not.
## Complexity
- Time complexity:
$$O(n)$$ Where n is the length of the input string(haystack).

- Space complexity:
$$O(1)$$

## Code
```python3 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        window = len(needle)
        i = 0
        while i <= n - window:
            if haystack[i:i+window] == needle:
                return i
            i += 1
        return -1
```