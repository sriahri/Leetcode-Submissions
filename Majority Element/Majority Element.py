from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counter = Counter(nums)
        # for key, value in counter.items():
        #     if value > len(nums)//2:
        #         return key

        count = 0
        majority = nums[0]
        for i in range(len(nums)):
            if majority == nums[i]:
                count += 1
            if count == 0:
                majority = nums[i]
            elif majority != nums[i]:
                count -= 1
            
        return majority