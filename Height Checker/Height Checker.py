class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        result = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                result += 1
        return result