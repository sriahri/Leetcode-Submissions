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