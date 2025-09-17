class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        n = len(nums1)
        while i < n and nums2:
            if nums1[i] > nums2[0]:
                nums1.insert(i, nums2.pop(0))
                nums1.pop()
            i += 1
        i = -1
        while nums2:
            nums1[i] = nums2.pop()
            i -= 1