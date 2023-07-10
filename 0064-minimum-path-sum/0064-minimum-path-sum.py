class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        dp=[[-1]*(m+1) for _ in range(n+1)]
        
        maxi=10**9
        def dfs(i,j):
            if i==0 and j==0:
                return grid[i][j]
            if i<0 or j<0:
                return maxi
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            up = grid[i][j]+dfs(i,j-1)
            left=grid[i][j]+dfs(i-1,j)
            
            dp[i][j] =min(up,left)
            
            return dp[i][j]
        
        return dfs(n-1,m-1)