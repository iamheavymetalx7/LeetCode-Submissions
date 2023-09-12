class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n=len(matrix);m=len(matrix[0])
        dire =[(1,0),(0,1),(-1,0),(0,-1)]
        
        dp =[[0]*(m) for _ in range(n)]
        
        def dfs(i,j):
            if dp[i][j]!=0:
                return dp[i][j]
            
            ans =1
            
            for dx,dy in dire:
                dx+=i
                dy+=j
                if 0<=dx<n and 0<=dy<m and matrix[dx][dy]>matrix[i][j]:
                    ans=max(ans,1+dfs(dx,dy))
                    
            dp[i][j]=ans
            return dp[i][j]
        
        ans = 0
        for i in range(n):
            for j in range(m):
                ans =max(ans,dfs(i,j))
        return ans
 