class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        
        cnt=0
        
        def dfs(i,j):
            nonlocal val
            if i<0 or i>=n or j<0 or j>=m:
                return True
            
            if grid[i][j]==0:
                return
            
            if grid[i][j]==1:
                val+=1
            grid[i][j]=0
            
            
            up=dfs(i-1,j)
            down=dfs(i+1,j)
            left=dfs(i,j-1)
            right=dfs(i,j+1)
            
            return up or down or left or right
    
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    val=0
                    if not dfs(i,j):
                        cnt+=val
        return cnt
                
        