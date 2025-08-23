## Problem: https://leetcode.com/problems/valid-boomerang/
### 
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.


### Example 1:
Input: points = [[1,1],[2,3],[3,2]]
Output: true

### Example 2:
Input: points = [[1,1],[2,2],[3,3]]
Output: false

### Constraints:
points.length == 3 \
points[i].length == 2 \
0 <= xi, yi <= 100

# Solution
## Approach
The approach is to first check if all the given three points are unique or not. If they are unique, check the slopes of the points with one another. If all three slopes are equal, then they are in a straight line. Else, they are not.
## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

## Code
```python3 []
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
```
