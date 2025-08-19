class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi = max(nums)
        result = nums.index(maxi)
        for num in nums:
            if maxi < 2*num and num != maxi:
                return -1
        return result
