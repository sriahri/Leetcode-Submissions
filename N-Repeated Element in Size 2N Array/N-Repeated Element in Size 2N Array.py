from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = Counter(nums)
        n = len(nums)//2
        for k, v in d.items():
            if v == n:
                return k