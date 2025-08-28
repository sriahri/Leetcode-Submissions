## Problem: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
### 
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

Return the sum of lengths of all good strings in words.

### Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

### Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

### Constraints:
1 <= words.length <= 1000 \
1 <= words[i].length, chars.length <= 100 \
words[i] and chars consist of lowercase English letters.

# Solution
## Approach
The approach is to first count the characters in the given chars using a hashmap. Next for every word, count all the characters in each word using a hashmap and check if the word can be formed or not using the chars. If the word can be formed, add the length of the word to the result.
## Complexity
- Time complexity:
$$O(n^2)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsCount = Counter(chars)
        result = 0
        for word in words:
            d = Counter(word)
            flag = True
            for k, v in d.items():
                if k in charsCount:
                    if v > charsCount[k]:
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:
                result += len(word)
        return result
```
