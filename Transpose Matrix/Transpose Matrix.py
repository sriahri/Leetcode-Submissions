class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        transpose = [[0] * m for _ in range(n)]
        for j in range(m):
            for i in range(n):
                transpose[i][j] = matrix[j][i]
        return transpose
