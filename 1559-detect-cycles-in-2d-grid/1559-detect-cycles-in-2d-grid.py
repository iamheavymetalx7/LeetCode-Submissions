class Solution:
    
    def dfs(self,i,j,parx,pary,grid,vis):
        
        n=len(grid)
        m=len(grid[0])
        if vis[i][j]:
            return True
        
        vis[i][j]=1
        
        dire=[(1,0),(0,1),(-1,0),(0,-1)]
        
        for x,y in dire:
            if 0<=i+x<n and 0<=j+y<m and (i+x,j+y)!=(parx,pary) and grid[i+x][j+y]==grid[i][j]:
                if self.dfs(i+x,j+y,i,j,grid,vis):
                    return True
        return False
                    
    
    
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        vis=[[False]*m for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                if not vis[i][j]:
                    if self.dfs(i,j,-1,-1,grid,vis):
                        return True
        return False
        
                
                