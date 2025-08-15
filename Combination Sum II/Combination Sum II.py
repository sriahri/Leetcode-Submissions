class Solution:
    def helper(self, ind, target, arr, current, result):
        if target == 0:
            result.append(current[:])
            return
        for i in range(ind, len(arr)):
            if i > ind and arr[i] == arr[i-1]:
                continue
            if arr[i] > target:
                break
            current.append(arr[i])
            self.helper(i+1, target-arr[i], arr[:], current, result)
            current.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.helper(0, target, candidates, [], result)
        return result