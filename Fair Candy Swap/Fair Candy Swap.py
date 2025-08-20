class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        alice = Counter(aliceSizes)
        for bob in bobSizes:
            if diff + bob in alice:
                return [diff + bob, bob]