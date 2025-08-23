class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # nums = list(map(str, nums))
        # result = []
        # for i in range(len(nums)):
        #     x = ''.join(nums[:i+1])
        #     if int(x, 2) % 5 == 0:
        #         result.append(True)
        #     else:
        #         result.append(False)
        # return result

        result = []
        number = 0
        for i in range(len(nums)):
            number = number * 2 + nums[i]
            result.append(number % 5 == 0)
        return result