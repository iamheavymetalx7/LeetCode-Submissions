class Solution:
    def solve(self, grid,i,j):
        global area
        n=len(grid)
        m=len(grid[0])
        
        
        grid[i][j]=0
        area = area+1
        
        
        dire =[(1,0),(0,1),(-1,0),(0,-1)]
        
        for x,y in dire:
            if 0<=i+x<n and 0<=j+y<m and grid[i+x][j+y]==1:
                self.solve(grid,i+x,j+y)
        
            
    
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        global area
        n=len(grid)
        m=len(grid[0])
        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    area=0
                    self.solve(grid,i,j)
                    ans=max(ans,area)
        return ans
                    
