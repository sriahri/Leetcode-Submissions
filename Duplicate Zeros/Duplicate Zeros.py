class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        indices = []
        for i in range(n):
            if arr[i] == 0:
                indices.append(i)
        for i in range(len(indices)):
            arr.insert(indices[i] + i, 0)
        for i in range(len(arr) - n):
            arr.pop()