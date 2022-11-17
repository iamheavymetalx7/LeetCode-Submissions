from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        st=deque()
        for i in range(len(s)):
            if len(st)==0:
                st.append(s[i])
            else:
                if st[-1]=="(" and s[i]==")":
                    st.pop()
                elif st[-1]=="{" and s[i]=="}":
                    st.pop()
                elif st[-1]=="[" and s[i]=="]":
                    st.pop()
                else:
                    st.append(s[i])
        if len(st)==0:
            return True
        return False
        