class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        result = max(nums) - min(nums) - k - k
        return result if result >= 0 else 0