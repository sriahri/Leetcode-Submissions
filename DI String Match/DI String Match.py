class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        result = []
        mini = 0
        maxi = len(s)
        for i in range(len(s)):
            if s[i] == 'I':
                result.append(mini)
                mini += 1
            else:
                result.append(maxi)
                maxi -= 1
        result.append(mini)
        return result
            