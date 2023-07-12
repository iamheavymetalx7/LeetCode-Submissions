class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n=len(s)
        m=len(p)
        
        dp=[[False]*(m+1) for _ in range(n+1)]
        
        dp[0][0]  = True
        
        for i in range(1,n+1):
            dp[i][0] = False
            
        for j in range(1,m+1):
            for x in range(1,j+1):
                flag=True
                if p[x-1]!='*':
                    flag=False 
                    break
            dp[0][j]=flag
            
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==p[j-1] or p[j-1]=="?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j]=False
        
        return dp[n][m]
                    
            
        
        
        
        
#         def f(i,j):
#             if i<0 and j<0: i==0,j==0
#                 return True
#             if i>=0 and j<0: i>0 j==0
#                 return False
#             if j>=0 and i<0: j>0 and i==0
#                 for x in range(j+1):
#                     if p[x]!="*":
#                         return False
#                 return True

#             if dp[i][j]!=-1:
#                 return dp[i][j]
            
#             if s[i]==p[j] or p[j]=="?":
#                 dp[i][j] = f(i-1,j-1)
#                 return dp[i][j]
#             if p[j]=="*":
#                 dp[i][j] = f(i-1,j) or f(i,j-1)
#                 return dp[i][j]
            
#             dp[i][j] = False
#             return dp[i][j]
        
        
#         return f(n-1,m-1)