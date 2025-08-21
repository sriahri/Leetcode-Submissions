class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while i < len(nums) and k > 0:
            if nums[i] < 0:
                nums[i] *= -1
                k -= 1
            elif nums[i] == 0:
                return sum(nums)
            else:
                if k % 2 == 0:
                    return sum(nums)
                else:
                    return sum(nums) - 2*min(nums)
            i += 1
        if k % 2 == 0:
            return sum(nums)
        else:
            return sum(nums) - 2*min(nums)