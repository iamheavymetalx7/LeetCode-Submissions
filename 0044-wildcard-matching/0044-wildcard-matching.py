# the comments are to understand the taulation from the previous submitted solution!!
class Solution:
    def isMatch(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        
        dp =[[False]*(m+1) for j in range(n+1)]
        # if i==0 and j==0:
        #     return True
        
        dp[0][0]=True

        # if i>0 and j==0:
        #     return False
        
        for i in range(1,n+1):
            dp[i][0]=False

#         if i==0 and j>0:
#             for jj in range(1,j+1):
#                 if t[jj-1]!="*":
#                     return False
#             return True

        for j in range(1,m+1):
            for jj in range(1,j+1):
                flag=True
                if t[jj-1]!="*":
                    flag=False
                    break
            dp[0][j]=flag           
                           
                    
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1] or t[j-1]=="?":
                    dp[i][j]= dp[i-1][j-1]
                elif t[j-1]=="*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j]=False
                    
        return dp[n][m]


  