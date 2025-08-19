## Problem: https://leetcode.com/problems/unique-morse-code-words/description
### 
nternational Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.

### Example 1:
Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".

### Example 2:
Input: words = ["a"]
Output: 1

### Constraints:
1 <= words.length <= 100 \
1 <= words[i].length <= 12 \
words[i] consists of lowercase English letters.

# Solution

## Approach
The approach is to convert the letters in each word into morse code and stich the string. Use a hashmap to count the number of unique strings and return it.

## Complexity
- Time complexity:
$$O(n x max(len(words[i])))$$ \

- Space complexity:
$$O(n)$$

## Code
```python3 []
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morseCodeList = []
        result = {}
        for word in words:
            wordMorseCode = ''
            for letter in word:
                wordMorseCode += morseCode[ord(letter) - 97]
            if wordMorseCode in result:
                result[wordMorseCode] += 1
            else:
                result[wordMorseCode] = 1
        return len(result)
```
