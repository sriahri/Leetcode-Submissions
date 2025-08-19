## Problem: https://leetcode.com/problems/most-common-word/description/
### 
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Note that words can not contain punctuation symbols.

### Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

### Example 2:
Input: paragraph = "a.", banned = []
Output: "a"

### Constraints:
1 <= paragraph.length <= 1000 \
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.". \
0 <= banned.length <= 100 \
1 <= banned[i].length <= 10 \
banned[i] consists of only lowercase English letters.

# Solution

## Approach
The approach is to first remove all the punctuation symbols and replace them with whitespace chars from the given string. Then, use a hashmap to store and count the words that are not banned and store the word with the maximum count.

## Complexity
- Time complexity:
$$O(n)$$ \

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for char in "!?',;.":
            paragraph = paragraph.replace(char, ' ')
        d = {}
        result = None
        maxi = 0
        for word in paragraph.split():
            word = word.strip()
            if word not in banned:
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
        for word in d.keys():
            if d[word] > maxi:
                maxi = d[word]
                result = word
        return result
```
