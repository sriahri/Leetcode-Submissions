class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # positions = []
        # n = len(s)
        # for i in range(n):
        #     if s[i] == c:
        #         positions.append(i)
        # answer = []
        # for i in range(n):
        #     result = n + 1
        #     for j in positions:
        #         if abs(i - j) < result:
        #             result = abs(i - j)
        #     answer.append(result)
        # return answer

        n = len(s)
        found = s.find(c)
        answer = [-1] * (n)
        for i in range(n):
            if s[i] == c:
                found = i
                answer[i] = 0
            else:
                answer[i] = abs(found - i)
        for i in range(n-1, -1, -1):
            if s[i] == c:
                found = i
            if s[i] != c:
                answer[i] = min(answer[i], abs(found - i))
        return answer
