class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        cols = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            x = []
            for j in range(m):
                x.append(matrix[j][i])
            cols.append(x)
        result = []
        print(cols)
        for i in range(m):
            for j in range(n):
                if min(matrix[i]) == max(cols[j]):
                    result.append(min(matrix[i]))
        return result