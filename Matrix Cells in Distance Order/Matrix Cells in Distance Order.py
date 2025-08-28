class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        d = {}
        for i in range(rows):
            for j in range(cols):
                d[(i, j)] = abs(i-rCenter) + abs(j-cCenter)
        result = []
        d = list(sorted(d.items(), key=lambda x: x[1]))
        for a, b in d:
            result.append(list(a))
        return result