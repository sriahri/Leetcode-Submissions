class Solution:
    def generate(self, n: int) -> List[List[int]]:
        l=[]
        for i in range(1,n+1):
            x=[]
            c=1
            for j in range(1,i+1):
                x.append(c)
                c=((c*(i-j))//j)
            l.append(x)
        return l