class Solution:
    def dfs(self,i,j,grid):
        n=len(grid)
        m=len(grid[0])
        if i<0 or i>=n or j<0 or j>=m:
            return False
        
        if grid[i][j]==1:
            return True

        ## like marking it as visited
        grid[i][j]=1
        
        up=self.dfs(i-1,j,grid)
        down=self.dfs(i+1,j,grid)
        left=self.dfs(i,j-1,grid)
        right=self.dfs(i,j+1,grid)
        
        return up and left and right and down

        
        
        
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        count=0
        
        n=len(grid)
        m=len(grid[0])
        
#         0s denote the land while 1s denote the water
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0 and self.dfs(i,j,grid):
                    count+=1
        return count