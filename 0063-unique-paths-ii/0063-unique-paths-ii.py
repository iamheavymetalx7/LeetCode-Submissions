class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp = [[-1 for x in range(m)] for y in range(n)]
        def recur(i,j):
            if i<=n-1 and j<=m-1 and obstacleGrid[i][j]==1:
                return 0
            if i==n-1 and j==m-1:
                return 1
            if i>=n or j>=m:
                return 0

            if dp[i][j]!=-1:
                return dp[i][j]
            
            dir1=recur(i+1,j)
            dir2=recur(i,j+1)
            
            dp[i][j]=dir1+dir2
            return dp[i][j]
        return recur(0,0)