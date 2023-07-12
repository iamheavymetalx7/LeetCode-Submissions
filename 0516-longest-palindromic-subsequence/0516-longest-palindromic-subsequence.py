class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        
        n,m=len(s),len(t)
        
        dp=[[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=0
        
        for j in range(m+1):
            dp[0][j]=0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                if s[i-1]==t[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[n][m]