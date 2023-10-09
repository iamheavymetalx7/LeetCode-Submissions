

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        dire =[(0,1),(1,0),(-1,0),(0,-1)]
        
        def dfs(i,j,vis):
            
            vis[i][j]=1
            for dx,dy in dire:
                dx+=i
                dy+=j
            
                
                if 0<=dx<n and 0<=dy<m and not vis[dx][dy] and grid[dx][dy]:
                    dfs(dx,dy,vis)
                        
        
        
        def cntIslands(grid):
            islands=0
            vis = [[0]*(m) for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if not vis[i][j] and grid[i][j]:
                        dfs(i,j,vis)
                        islands+=1
            return islands
                    
        
        number_islands = cntIslands(grid)
        if number_islands>1 or number_islands==0:
            return 0
        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    grid[i][j]=0
                    number_islands= cntIslands(grid)
                    grid[i][j]=1
                    
                    if number_islands>1 or number_islands==0:
                        return 1
        return 2