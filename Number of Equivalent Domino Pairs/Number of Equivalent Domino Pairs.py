from collections import Counter
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for i in range(len(dominoes)):
            dominoes[i] = tuple([min(dominoes[i]), max(dominoes[i])])
        result = 0
        d = Counter(dominoes)
        for k, v in d.items():
            result += (v * (v-1))//2
        return result