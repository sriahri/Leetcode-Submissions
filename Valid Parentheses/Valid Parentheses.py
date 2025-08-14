class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        op=['(','[','{']
        cl=[')',']','}']
        st=[s[0]]
        for i in range(1,len(s)):
            temp=s[i]
            if st:
                if temp in op:
                    st.append(temp)
                else:
                    ind=cl.index(temp)
                    if st[-1]==op[ind]:
                        st.pop()
                    else:
                        st.append(temp)
            else:
                st.append(temp)
        if st:
            return False
        return True