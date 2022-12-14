class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for x in range(n)]for y in range(m)]
        
        def solve(i,j):
            if i == m-1 and j == n-1:
                return 1
            if i>=m or j>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            
            lft=solve(i+1,j)
            rgt=solve(i,j+1)
            dp[i][j]=lft+rgt
            return dp[i][j]
        return solve(0,0)