from collections import Counter
class Solution:
    def containsNearbyDuplicate(self, l: List[int], k: int) -> bool:
        # n=len(l)
        # d=Counter(l)
        # for i in d.keys():
        #     if d[i]>1:
        #         j=l.index(i)
        #         y=l[::-1].index(i)
        #         y=n-y
        #         for x in range(j,y):
        #             if l[x] in l[x+1:k+x+1]:
        #                 return True
        # return False
        q=[]
        s=set()
        for i in l:
            if i in s:
                return True
            q.append(i)
            s.add(i)
            if len(q)>k:
                j=q.pop(0)
                s.remove(j)
        return False