import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -sys.maxsize
        maxi = result
        for num in nums:
            maxi = max(maxi + num, num)
            result = max(maxi, result)
        return result
