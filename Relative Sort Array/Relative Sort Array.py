from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = Counter(arr1)
        result = []
        for i in arr2:
            result += [i] * d[i]
            del d[i]
        remaining = []
        for i in d.keys():
            remaining += [i] * d[i]
        remaining.sort()
        result += remaining
        return result