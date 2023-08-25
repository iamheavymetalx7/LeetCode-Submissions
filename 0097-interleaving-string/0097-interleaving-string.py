class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n=len(s1)
        m=len(s2)
        o=len(s3)
        if o!=(n+m):
            return False
        
        @cache
        def recur(i,j):
            if i+j==len(s3):
                return True
            
            ans = False
            
            if i<n and s3[i+j]==s1[i]:
                ans  |= recur(i+1,j)
            if j<m and s3[i+j]==s2[j]:
                ans |= recur(i,j+1)
            
            
            return ans
        val = recur(0,0)
        return val