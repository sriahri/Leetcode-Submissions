class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = arr[-1]
        n = len(arr)
        result = [-1] * n
        for i in range(n-2, -1, -1):
            maxi = max(maxi, arr[i+1])
            result[i] = maxi
        return result