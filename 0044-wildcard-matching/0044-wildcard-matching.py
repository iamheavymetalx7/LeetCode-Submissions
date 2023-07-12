class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n=len(s)
        m=len(p)
        
        dp=[[-1]*(m) for _ in range(n)]
        
        def f(i,j):
            if i<0 and j<0:
                return True
            if i>=0 and j<0:
                return False
            if j>=0 and i<0:
                for x in range(j+1):
                    if p[x]!="*":
                        return False
                return True

            if dp[i][j]!=-1:
                return dp[i][j]
            
            if s[i]==p[j] or p[j]=="?":
                dp[i][j] = f(i-1,j-1)
                return dp[i][j]
            if p[j]=="*":
                dp[i][j] = f(i-1,j) or f(i,j-1)
                return dp[i][j]
            
            dp[i][j] = False
            return dp[i][j]
        
        
        return f(n-1,m-1)