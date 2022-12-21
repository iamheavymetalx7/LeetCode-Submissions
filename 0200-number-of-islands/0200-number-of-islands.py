class Solution:
    def solve(self,i,j,grid):
        n=len(grid)
        m=len(grid[0])
        
        grid[i][j]="0"
        
        dire =[(1,0),(-1,0),(0,1),(0,-1)]
        
        for x,y in dire:
            if 0<=i+x<n and 0<=j+y<m and grid[i+x][j+y]=="1":
                self.solve(i+x,j+y,grid)
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m=len(grid),len(grid[0])
        cnt=0
        if m==0:
            return cnt
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    self.solve(i,j,grid)
                    cnt+=1
        return cnt        
        
        