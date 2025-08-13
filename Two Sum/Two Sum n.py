class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in d and d[target -nums[i]] != i:
                return [i, d[target-nums[i]]]