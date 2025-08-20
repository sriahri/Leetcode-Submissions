class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        d = {}
        leftOccurence = {}
        rightOccurence = {}
        for i in range(len(nums)):
            rightOccurence[nums[i]] = i
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                leftOccurence[nums[i]] = i
                d[nums[i]] = 1

        degree = 0
        for i in d.keys():
            if d[i] > degree:
                degree = d[i]
        result = len(nums)
        for num in d.keys():
            print(result)
            if d[num] == degree:
                result = min(result, rightOccurence[num] - leftOccurence[num] + 1)
        return result
