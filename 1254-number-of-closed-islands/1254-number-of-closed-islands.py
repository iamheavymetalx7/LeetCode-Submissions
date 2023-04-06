class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        
        count=0
        
        def dfs(i,j):
            
            if i<0 or i>=n or j<0 or j>=m:
                return False
                        
            if grid[i][j]==1:
                return True
                
            grid[i][j]=1
            
            up=dfs(i-1,j)
            down=dfs(i+1,j)
            right=dfs(i,j+1)
            left=dfs(i,j-1)
            
            return up and left and down and right
            
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0 and dfs(i,j):
                    count+=1
                    
            
        
        
        return count