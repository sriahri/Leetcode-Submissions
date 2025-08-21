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