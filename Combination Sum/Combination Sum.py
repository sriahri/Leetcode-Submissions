class Solution:
    def helper(self, i, result, current, arr, target):
        if i == len(arr):
            if target == 0:
                result.append(current[:])
            return
        if arr[i] <= target:
            current.append(arr[i])
            self.helper(i, result, current, arr, target-arr[i])
            current.pop()
        self.helper(i+1, result, current, arr, target)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        self.helper(0, result, current, candidates, target)
        return result