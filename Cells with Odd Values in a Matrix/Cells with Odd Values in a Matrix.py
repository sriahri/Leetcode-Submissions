class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n

        for i, j in indices:
            rows[i] += 1
            cols[j] += 1
        result = 0
        for r in rows:
            for c in cols:
                if (r+c) % 2 != 0:
                    result += 1
        return result