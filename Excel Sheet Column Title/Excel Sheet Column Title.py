class Solution:
    def convertToTitle(self, n: int) -> str:
        res=''
        while n>0:
            r=n%26
            n=n//26
            if r==0:
                res+='Z'
            else:
                res+=chr(r+64)
            if r==0:
                n-=1
        return res[::-1]