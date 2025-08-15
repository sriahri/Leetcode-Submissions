class Solution:
    def helper(self, ind, arr, current, result):
        if ind >= len(arr):
            result.append(arr[:])
        for i in range(ind, len(arr)):
            arr[ind], arr[i] = arr[i], arr[ind]
            self.helper(ind+1, arr, current, result)
            arr[ind], arr[i] = arr[i], arr[ind]
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(0, nums, [], result, )
        return result