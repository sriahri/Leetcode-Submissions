class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            s = str(num)
            if len(s) % 2 == 0:
                result += 1
        return result