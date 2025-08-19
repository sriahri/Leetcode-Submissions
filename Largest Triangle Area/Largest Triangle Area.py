# import math
# class Solution:
#     def distanceCalc(self, x1, y1, x2, y2):
#         distanceX = (x2-x1)*(x2-x1)
#         distanceY = (y2-y1)*(y2-y1)
#         return math.sqrt(distanceX + distanceY)
#     def largestTriangleArea(self, points: List[List[int]]) -> float:
#         distances = []
#         n = len(points)
#         for i in range(n):
#             for j in range(i+1, n):
#                 x1, y1 = points[i]
#                 x2, y2 = points[j]
#                 distance = self.distanceCalc(x1, y1, x2, y2)
#                 distances.append(distance)
#         print(distances)
#         distances.sort(reverse = True)
#         print(distances)
#         side1 = distances[0]
#         side2 = distances[1]
#         side3 = distances[2]
#         semiPeri = (side1 + side2 + side3) / 2
#         result = math.sqrt(semiPeri * (semiPeri - side1) * (semiPeri - side2) * (semiPeri - side3))
#         return result

import math
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        result = 0
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    area = 1/2 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
                    result = max(area, result)
        return result
