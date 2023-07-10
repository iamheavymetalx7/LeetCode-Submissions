class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        final =0
        def dfs(i,j,grid):
            if i<0 or j<0 or i>=n or j>=m or grid[i][j]==0:
                return 0
            
            current = grid[i][j]
            grid[i][j] = 0
            ans = current
            
            ans+=max(0,dfs(i+1,j,grid),dfs(i,j+1,grid),dfs(i-1,j,grid),dfs(i,j-1,grid))
            
            grid[i][j] = current
            return ans
            
            
        
        
        for i in range(n):
            for j in range(m):
                final=max(final, dfs(i,j,grid))
        return final
        