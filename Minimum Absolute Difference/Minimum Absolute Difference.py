class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        result = []
        minDiff = arr[-1] - arr[0]
        for i in range(1, n):
            if arr[i] - arr[i-1] < minDiff:
                minDiff = arr[i] - arr[i-1]
        for i in range(1, n):
            if arr[i] - arr[i-1] == minDiff:
                result.append([arr[i-1], arr[i]])
        return result