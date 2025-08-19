## Problem: https://leetcode.com/problems/largest-triangle-area/description/
### 
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

### Example 1:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.

### Example 2:
Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000

### Constraints:
3 <= points.length <= 50 \
-50 <= xi, yi <= 50 \
All the given points are unique.

# Solution

## Approach
The approach is to consider 3 points at once and use the shoelace formuls(Gauss Formula) to compute the area of the triangle. At each step, store the maximum area of the triangle.
The other approach is to use the Heron's formula to compute the area of the triangle given its sides. Also, compute the side length using the distance formula. Check whether the given sides can form a triangle or not. Since it is mentioned that there is always a valid triangle formation, we need to figure out the triangle. Since, it is complex, we use the other method with the larger time complexity.
## Complexity
- Time complexity:
$$O(n^3)$$ \

- Space complexity:
$$O(1)$$

## Code
```python3 []
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
```
