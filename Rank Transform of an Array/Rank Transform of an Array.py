class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(list(set(arr)))
        ranks = {}
        result = [-1] * len(arr)
        for i in range(len(sorted_arr)):
            ranks[sorted_arr[i]] = i+1
        for i in range(len(arr)):
            result[i] = ranks[arr[i]]
        return result