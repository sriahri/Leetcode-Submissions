class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        i = 0
        possible = True
        frontSum = 0
        while i < len(arr):
            frontSum += arr[i]
            if frontSum == total // 3:
                break
            i += 1
        if i == len(arr) - 1:
            possible = False
        j = len(arr) - 1
        backSum = 0
        while j >= 0:
            backSum += arr[j]
            if backSum == total // 3:
                break
            j -= 1
        if j == 0 or j <= i+1:
            possible = False
        return possible