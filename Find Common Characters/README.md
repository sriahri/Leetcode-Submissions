## Problem: https://leetcode.com/problems/find-common-characters/description/
### 
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

### Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

### Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

### Constraints:
1 <= words.length <= 100 \
1 <= words[i].length <= 100 \
words[i] consists of lowercase English letters.

# Solution
## Approach
The approach is to first assume that all the characters that are present in the first word are present in all the words. Use a hashmap to count all the letters in a word and check if the letters in the resultant hashmap are present in the word or not. If not, update the result set accordingly.
## Complexity
- Time complexity:
$$O(nxlen(words[i]))$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = {}
        first = Counter(words[0])
        result = Counter(words[0])
        for i in range(1, len(words)):
            word = words[i]
            d = Counter(word)
            for k, v in result.items():
                if k not in d:
                    result[k] = 0
                if k in d:
                    result[k] = min(v, d[k])
        answer = ''
        for k, v in result.items():
            answer += k * v
        return list(answer)
```
