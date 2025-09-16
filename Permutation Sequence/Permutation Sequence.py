class Solution:
    def facto(self, n):
        if n == 1:
            return 1
        return n*self.facto(n-1)
    def solve(self, l, n, k, result):
        if n == 1:
            result.append(l[0])
            return
        d = self.facto(n-1)
        x = k//d
        k = k%d
        result.append(l[x])
        l.remove(l[x])
        self.solve(l, n-1, k, result)
    def getPermutation(self, n: int, k: int) -> str:
        l = [str(i) for i in range(1, n+1)]
        result = []
        self.solve(l, n, k-1, result)
        return ''.join(result)