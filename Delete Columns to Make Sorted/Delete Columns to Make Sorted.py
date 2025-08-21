class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        n = len(strs)
        columns = [['.'] * n for _ in range(len(strs[0]))]
        print(columns)
        for i in range(n):
            for j in range(len(strs[i])):
                columns[j][i] = strs[i][j]
        print(columns)
        for s in columns:
            x = sorted(s)
            if x != s:
                result += 1
        return result            