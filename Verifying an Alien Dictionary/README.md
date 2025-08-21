## Problem: https://leetcode.com/problems/verifying-an-alien-dictionary/
###
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

### Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

### Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

### Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character

### Constraints:
1 <= words.length <= 100 \
1 <= words[i].length <= 20 \
order.length == 26 \
All characters in words[i] and order are English lowercase letters.

# Solution
## Approach
The approach is to check if the current word is greater than the previous word or not. For this, first we try to make both the word lengths same by adding whitespace characters at the end. So that if the whitespace is compared to a normal character, it will always be less.
Also, we skip all the characters that are same in both words, we are only concerned about the characters that are different and check those corresponding position in the alien alphabet.

## Complexity
- Time complexity:
$$O(n x max(len(words[i])))$$

- Space complexity:
$$O(1)$$

## Code
```python3 []
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        for i in range(1, n):
            curr = words[i]
            prev = words[i-1]
            length = min(len(curr), len(prev))
            j = 0
            max_length = max(len(curr), len(prev))
            prev += ' ' * (max_length - length)
            curr += ' ' * (max_length - length)
            while j < max_length and curr[j] == prev[j]:
                j += 1
            if j < max_length and order.find(curr[j]) < order.find(prev[j]):
                return False
        return True            
```
