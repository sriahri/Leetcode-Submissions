class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        if n==0:
            return ''
        elif n==1:
            return strs[0]
        strs.sort()
        end=min(len(strs[0]),len(strs[-1]))
        i=0
        while i<end and strs[0][i]==strs[-1][i]:
            i+=1
        return strs[0][:i]