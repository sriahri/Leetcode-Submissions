## Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
### You are given a string s, find the length of the longest substring without duplicate characters.

 

### Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

### Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

### Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

### Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

# Solution
## Intuition
Generate all the substrings of the given string and then check whether each string contains unique characters or not. This algorithm will take the time complexity of $$O(n^2)$$ where n is the length of the input string.


## Approach
We will use the sliding window technique paired with Hashmap to check for the longest substring with unique characters. First, we start the window with length 1 and a hashmap that stores the indices of the characters that are present in the window. If we encounter a character that is already present in the window, then we move the window such that there are only unique characters in it. The maximum length is calculated after adding each character into the window and deleting the window.

## Complexity
- Time complexity:
$$O(n)$$ Where n is the length of the input string.

- Space complexity:
$$O(n)$$ Where n is the length of the input string.

## Code
```python3 
    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            res = 0
            hashMap = {}
            pointer_left, pointer_right = 0, 0
            while pointer_left < len(s) and pointer_right < len(s):
                if s[pointer_right] not in hashMap:
                    hashMap[s[pointer_right]] = 1
                else:
                    res = max(res, len(hashMap.keys()))
                    while s[pointer_left] != s[pointer_right]:
                        del hashMap[s[pointer_left]]
                        pointer_left += 1
                    hashMap[s[pointer_right]] = 1
                    pointer_left += 1
                pointer_right += 1
            return max(res, len(hashMap.keys()))
```