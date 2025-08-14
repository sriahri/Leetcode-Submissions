class Solution:
    def twoSum(self, nums, target):
        res = []
        i = 0
        j = len(nums)-1
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
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                passing = nums[j+1:]
                twoSumRes = self.twoSum(passing, target - nums[i] - nums[j])
                if twoSumRes:
                    for x, y in twoSumRes:
                        sub = [nums[i], nums[j], x, y]
                        res.append(sub)
        return res

        # nums.sort()
        # res = []
        # quad = []

        # def kSum(k, start, target):
        #     if k == 2:
        #         end = len(nums)
        #         while start < end:
        #             if nums[start] + nums[end] == target:
        #                 quad.append(nums[start])
        #                 quad.append(nums[end])
        #                 start += 1
        #                 while start < end and nums[start] == nums[start - 1]:
        #                     start += 1
        #             elif nums[start] + nums[end] > target:
        #                 end -= 1
        #             else:
        #                 start += 1
        #     for i in range(start, len(nums) - k + 1):
        #         if i > start and nums[i] == nums[i-1]:
        #             continue
        #         quad.append(nums[i])
        #         kSum(i+1, target-nums[i])
        #         quad.pop()
        #     if len(quad) == 4:
        #         res.append(quad)
        #         quad = []
        # kSum(4, 0, target)
        # return res