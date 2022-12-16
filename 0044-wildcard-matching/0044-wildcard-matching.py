class Solution:
    def isMatch(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        
        dp =[[-1]*(m+1) for j in range(n+1)]
        
        def recur(i,j):
            if i==0 and j==0:
                return True
            if i>0 and j==0:
                return False
            if i==0 and j>0:
                for jj in range(j):
                    if t[jj]!="*":
                        return False
                return True
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i-1]==t[j-1] or t[j-1]=="?":
                dp[i][j] =  recur(i-1,j-1)
                return dp[i][j]
            if t[j-1]=="*":
                dp[i][j] = recur(i-1,j) or recur(i,j-1)
                return dp[i][j]
            else:
                dp[i][j] = False
                return dp[i][j]
        return recur(n,m)
        
        