class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        d = {}
        for point in points:
            if tuple(point) in d:
                return False
            else:
                d[tuple(point)] = 1
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        slope, slope1, slope2 = 0, 0, 0
        if x2 != x1:
            slope = abs((y2-y1)/(x2-x1))
        if x2 != x3:
            slope1 = abs((y2-y3)/(x2-x3))
        if x1 != x3:
            slope2 = abs((y1-y3)/(x1-x3))

        return slope != slope1 or slope != slope2