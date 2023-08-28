class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # s -> string
        # p -> pattern
        #tip : read the question carefully, it is given that
        # "*" matches zero or more of the preceeding element
        n=len(s)
        m=len(p)
        
        @cache
        def recur(i,j):
            if j==m:
                if i==n:
                    return True
                return False
            
            ans = False
            if j+1<m and p[j+1]=="*":
                ans |= recur(i,j+2)  # do not take any char
                if i<len(s) and (p[j]==s[i] or p[j]=="."):
                    ans |= recur(i+1,j)
                    
            if i<len(s) and (p[j]==s[i] or p[j]=="."):
                ans |= recur(i+1,j+1)
            
            return ans
        
        return recur(0,0)
        
                
                