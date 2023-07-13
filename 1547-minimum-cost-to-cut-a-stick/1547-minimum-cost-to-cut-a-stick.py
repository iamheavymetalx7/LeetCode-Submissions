class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        c=len(cuts)
        
        
        cuts=[0]+cuts+[n]
        cuts.sort()
        
        
        dp=[[0]*(c+2) for _ in range(c+2)]
        
        # for i in range(1,c+1):
        #     for j in range(i):
        #         dp[i][j]=0
            
        for i in range(c,0,-1):
            for j in range(1,c+1):
                mini = 10**9
                if i>j:                                 ## important to write this!!
                    continue
                    
                for k in range(i,j+1):
                    ans = cuts[j+1]-cuts[i-1]+dp[i][k-1]+dp[k+1][j]
                    mini = min(ans, mini)

                dp[i][j] =mini
                
        return dp[1][c]
        
#         def f(i,j):
#             if i>j:
#                 return 0
            
            
#             if dp[i][j]!=-1:
#                 return dp[i][j]
            
            
#             mini = 10**9
#             for k in range(i,j+1):
#                 ans = cuts[j+1]-cuts[i-1]+f(i,k-1)+f(k+1,j)
#                 mini = min(ans, mini)
            
#             dp[i][j] =mini
#             return dp[i][j]
#         return f(1,c)