class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n%2 == 0:
            i = -1 * (n//2)
            while i <= n // 2:
                if i != 0:
                    result.append(i)
                i += 1
        else:
            x = n//2
            for i in range(-x, x + 1):
                result.append(i)
        return result