class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n=len(s)
        
        st=[0] ## the score of current frame
        score=0
        
        
        for i in range(n):
            if s[i]=="(":
                st.append(0)
            else:
                v=st.pop()
                st[-1]+=max(2*v,1)
        return st.pop()
            