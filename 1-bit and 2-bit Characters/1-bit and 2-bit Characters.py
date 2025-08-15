class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        count = 0
        for i in range(len(bits) - 2, -1, -1):
            if bits[i] == 1:
                count += 1
            else:
                break
        return True if count%2 == 0 else False