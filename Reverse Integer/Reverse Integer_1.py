class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        if x<0:
            a=s[-1:-len(s):-1]
            a=int(a)-2*(int(a))
        else:
            a=s[::-1]
        a=int(a)
        if a>2147483647 or a<-2147483647:
            return 0
        return a
        