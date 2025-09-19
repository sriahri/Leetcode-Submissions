class Solution:
    def titleToNumber(self, s: str) -> int:
        #d={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11}
        n=len(s)
        c=0
        for i in range(len(s)):
            c+=(ord(s[n-i-1])-64)*(26**i)
        return c