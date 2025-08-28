from collections import Counter
class Solution:
    def binarySearch(self, arr, k):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low+high) // 2
            if arr[mid] == k:
                return True
            elif arr[mid] > k:
                high = mid - 1
            else:
                low = mid + 1
        return False
    def checkIfExist(self, arr: List[int]) -> bool:
        # arr.sort()
        # found = self.binarySearch(arr, 0)
        # if found:
        #     if arr.count(0) > 1:
        #         return True
        #     else:
        #         arr.remove(0)
        # for i in arr:
        #     if self.binarySearch(arr, 2*i):
        #         return True
        # return False
        d = Counter(arr)
        for i in d.keys():
            if i == 0:
                if d[i] > 1:
                    return True
            elif 2*i in d:
                return True
        return False