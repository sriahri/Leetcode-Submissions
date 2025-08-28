class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        x, y, z = 0, 0, 0
        for i in range(len(grid)):
            maxX = 0
            maxY = 0
            for j in range(len(grid)):
                maxX = max(maxX, grid[j][i])
                maxY = max(maxY, grid[i][j])
                if grid[i][j] > 0:
                    z += 1
            x += maxX
            y += maxY
        return x + y +z