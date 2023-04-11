class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        n=len(s)
        
        for i in range(n):
            if s[i]!="*":
                st.append(s[i])
            else:
                st.pop()
        
        ans="".join(st)
        return ans        