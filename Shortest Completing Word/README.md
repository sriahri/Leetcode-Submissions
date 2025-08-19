## Problem: https://leetcode.com/problems/shortest-completing-word/description
### 
Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

### Example 1:
Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.

### Example 2:
Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.

### Constraints:
1 <= licensePlate.length <= 7 \
licensePlate contains digits, letters (uppercase or lowercase), or space ' '. \
1 <= words.length <= 1000 \
1 <= words[i].length <= 15 \
words[i] consists of lower case English letters.

# Solution

## Approach
The approach is to first use a hashmap and count all the letters in the license plate. Then for every word in the list count all the characters in the word and compare them with the license plate letters and the corresponding count. At every possible result word, keep track of the shortest word.

## Complexity
- Time complexity:
$$O(n * max(len(words[i])))$$ \

- Space complexity:
$$O(n)$$

## Code
```python3 []
from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        copy = ''
        for letter in licensePlate:
            if letter.isalpha():
                copy += letter
        licensePlate = copy
        licensePlateDict = Counter(licensePlate)
        result = None
        for word in words:
            flag = True
            original = word
            word = word.lower()
            wordDict = Counter(word)
            for letter in licensePlateDict.keys():
                if letter not in wordDict:
                    flag = False
                    break
                else:
                    if wordDict[letter] < licensePlateDict[letter]:
                        flag = False
                        break
            if flag:
                if result:
                    if len(result) > len(original):
                        result = original
                else:
                    result = original
        return result
```
