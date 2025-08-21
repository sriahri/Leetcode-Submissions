class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        result = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        even.sort()
        odd.sort()
        i = 0
        n = len(nums)
        while i < n//2:
            result.append(even[i])
            result.append(odd[i])
            i += 1
        return result