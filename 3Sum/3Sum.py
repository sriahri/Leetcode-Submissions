class Solution:

    def twoSum(self, nums, target):
        res = []
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                res.append([nums[i], nums[j]])
                i += 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return res
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        if len(nums) < 3:
            return res
        x = nums.count(0)
        if x == len(nums):
            return [[0, 0, 0]]
        for i in range(len(nums)):
            if nums[i] != nums[i-1]:
                if i == len(nums) -1:
                    return res
                passing = nums[i+1:]
                # print(passing)
                twoSumRes = self.twoSum(passing, -nums[i])
                if twoSumRes:
                    for x, y in twoSumRes:
                        sub = [nums[i]]
                        sub.append(x)
                        sub.append(y)
                        res.append(sub)
        return res