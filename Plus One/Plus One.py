class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(map(str, digits))
        x = int(s) + 1
        return list(map(int, str(x)))