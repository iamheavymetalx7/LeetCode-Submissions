from math import *
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        
        dp = [[-1 for i in range(m)] for j in range(n)]
    
        def recur(i,j):
            if i==n-1 and j==m-1:
                return grid[n-1][m-1]
            if i>=n or j>=m:
                return math.inf
            if dp[i][j]!=-1:
              return dp[i][j]
            
            dir1=grid[i][j]+recur(i+1,j)
            dir2=grid[i][j]+recur(i,j+1)
            dp[i][j]=min(dir1,dir2)
            
            return dp[i][j]
        return recur(0,0)
        