from math import *
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        dp=[[-1 for x in range(m)] for y in range(n)]
        def recur(i,j):
            if j<0 or j>=m:
                return math.inf
            
            if i==n-1:
                return matrix[n-1][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            dir1=matrix[i][j]+recur(i+1,j-1)
            dir2=matrix[i][j]+recur(i+1,j)
            dir3=matrix[i][j]+recur(i+1,j+1)
            
            dp[i][j]  = min(dir1,dir2,dir3)
            return dp[i][j]
        
        minPath = math.inf
        for j in range(m):
            minPath=min(minPath,recur(0,j))
            
        return minPath