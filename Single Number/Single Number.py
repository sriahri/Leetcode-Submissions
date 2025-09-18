from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=Counter(nums)
        for i in d.keys():
            if d[i]==1:
                return i
            