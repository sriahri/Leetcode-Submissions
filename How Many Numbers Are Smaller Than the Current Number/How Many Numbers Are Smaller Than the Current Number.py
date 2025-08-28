class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        ranks = {}
        for i in range(len(arr)):
            if arr[i] not in ranks:
                ranks[arr[i]] = i
        result = [-1] * len(nums)
        for i in range(len(nums)):
            result[i] = ranks[nums[i]]
        return result