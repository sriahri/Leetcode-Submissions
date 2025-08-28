class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = {}
        for i in range(len(mat)):
            d[i] = mat[i].count(1)
        d = list(sorted(d.items(), key=lambda x:x[1]))
        result = []
        for i, j in d:
            result.append(i)
        return result[:k]