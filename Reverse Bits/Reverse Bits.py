class Solution:
    def reverseBits(self, n: int) -> int:
        s=bin(n)[2:]
        #s=str(n)
        l=len(s)
        s=(32-l)*'0'+s
        s=s[::-1]
        x=int(s,2)
        return x