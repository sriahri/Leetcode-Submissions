class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        ans=0
        while i<len(s):
            s1=d[s[i]]
            if i+1<len(s):
                s2=d[s[i+1]]
                if s2>s1:
                    ans+=s2-s1
                    i+=2
                else:
                    ans+=s1
                    i+=1
            else:
                ans+=s1
                i+=1
        return ans