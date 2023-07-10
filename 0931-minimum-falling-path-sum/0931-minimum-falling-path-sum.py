# from math import *
# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         n=len(matrix)
#         m=len(matrix[0])
#         dp=[[-1 for x in range(m)] for y in range(n)]
#         def recur(i,j):
#             if j<0 or j>=m:
#                 return math.inf
            
#             if i==0:
#                 return matrix[i][j]
#             if dp[i][j]!=-1:
#                 return dp[i][j]
#             dir1=matrix[i][j]+recur(i-1,j-1)
#             dir2=matrix[i][j]+recur(i-1,j)
#             dir3=matrix[i][j]+recur(i-1,j+1)
            
#             dp[i][j]  = min(dir1,dir2,dir3)
#             return dp[i][j]
        
#         minPath = math.inf
#         for j in range(m):
#             minPath=min(minPath,recur(n-1,j))
            
#         return minPath

from math import *
class Solution:
    def minFallingPathSum(self, a: List[List[int]]) -> int:
        n=len(a)
        m=len(a[0])
        dp=[[10**9 for x in range(m)] for y in range(n)]

        
        for j in range(m):
            dp[0][j]=a[0][j]
            
        for i in range(1,n):
            for j in range(m):
                
                v1=a[i][j]+dp[i-1][j]
                v2=a[i][j]
                if j-1>=0:
                    v2+=dp[i-1][j-1]
                else:
                    v2+=10**9
                v3=a[i][j]
                if j+1<m:
                    v3+=dp[i-1][j+1]
                else:
                    v3+=10**9
                
                dp[i][j]=min(v1,v2,v3)
        
        ans=10**9
        
        for j in range(m):
            ans=min(ans,dp[n-1][j])
        
        return ans