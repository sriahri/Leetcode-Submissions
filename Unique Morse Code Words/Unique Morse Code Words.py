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
