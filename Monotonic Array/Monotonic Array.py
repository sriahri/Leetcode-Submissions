class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # n = len(nums)
        # sortedNums = sorted(nums)
        # if nums == sortedNums or nums[::-1] == sortedNums:
        #     return True
        # return False

        n = len(nums)
        if n <= 1:
            return True
        flag = True
        if nums[0] > nums[1]:
            flag = False
        i = 1
        while i < n and nums[i] == nums[i-1]: 
            i += 1
        if i < n and nums[i] < nums[i-1]:
            flag = False
        while i < n:
            if flag:
                if nums[i] < nums[i-1]:
                    return False
            else:
                if nums[i] > nums[i-1]:
                    return False
            i += 1
        return True