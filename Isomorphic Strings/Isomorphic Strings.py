from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ma=len(s)
        n=len(t)
        if ma!=n:
            return False
        d={}
        d1={}
        for i in range(n):
            if s[i] not in d:
                d[s[i]]=i
            if t[i] not in d1:
                d1[t[i]]=i
            if d[s[i]]!=d1[t[i]]:
                return False
        return True