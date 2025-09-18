from math import factorial
class Solution:
    def getRow(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            if i==0:
                l.append(1)
            else:
                l.append(factorial(n)//(factorial(i)*factorial(n-i)))
        return l