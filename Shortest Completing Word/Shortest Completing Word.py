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
