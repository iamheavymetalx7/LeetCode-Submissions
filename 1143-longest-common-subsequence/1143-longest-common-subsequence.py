class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        
        
        dp=[[-1]*(m+1) for j in range(n+1)]
        
        for j in range(m+1):
            dp[0][j]=0
        
        for i in range(n+1):
            dp[i][0]=0
            
        for i in range(1,n+1):
            for j in range(1,m+1):
            
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        i=n
        j=m
        string=""
        
        while (i>0 and j>0):
            if text1[i-1]==text2[j-1]:
                string+=text1[i-1]
                i-=1
                j-=1
            else:
                if dp[i-1][j]>dp[i][j-1]:
                    i-=1
                else:
                    j-=1
        print(string[::-1])
        
        return dp[n][m]