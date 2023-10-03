class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        sx,sy = 0,0,
        n,m = len(grid),len(grid[0])
        empty = 1
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    sx,sy =i,j
                elif grid[i][j]==0:
                    empty+=1
                    
        val = [0]
        
        def dfs(x,y,cnt):
            if (x<0 or x>=n or y<0 or y>=m or grid[x][y]==-1):
                return 
            
            if grid[x][y]==2:
                if cnt==empty:
                    val[0]+=1
                return
            
           
            grid[x][y] = -1
            dfs(x+1,y,cnt+1)
            dfs(x-1,y,cnt+1)
            dfs(x,y+1,cnt+1)
            dfs(x,y-1,cnt+1)
            grid[x][y] = 0
        
        dfs(sx,sy,0)
        return val[0]
            