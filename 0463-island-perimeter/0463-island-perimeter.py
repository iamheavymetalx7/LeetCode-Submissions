class Solution:
    def dfs(self,i,j,grid):
        global perimeter
        n=len(grid)
        m=len(grid[0])
        dire =[(1,0),(-1,0),(0,1),(0,-1)]
        
        if i<0 or i>=n or j<0 or j>=m:
            perimeter+=1
            return
        
        if grid[i][j]==0:
            perimeter+=1
            return
        
        if grid[i][j]==-1:
            return
        
        grid[i][j]=-1
        
        for x,y in dire:
            self.dfs(i+x,j+y,grid)
            
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        
        global perimeter
        perimeter =0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    self.dfs(i,j,grid)
        return perimeter