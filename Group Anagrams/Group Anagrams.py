from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[None]*len(strs)
        a=[]
        for i in range(len(strs)):
            x=str(sorted(strs[i]))
            s=''.join(x)
            l[i]=s
        d=Counter(l)
        for i in d.keys():
            y=[]
            for j in range(len(l)):
                if i==l[j]:
                    y.append(strs[j])
            a.append(y)
        return a