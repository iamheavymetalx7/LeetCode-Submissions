class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        n,m = len(grid),len(grid[0])
        dire=[(1,0),(0,1)]
        def dfs(i,j):
            if i==n-1 and j==m-1:
                return True
            
            if not (0<=i<n) or not (0<=j<m) or  (grid[i][j]==0):
                return False
            
            grid[i][j]=0
            for dx,dy in dire:
                dx+=i
                dy+=j
                if dfs(dx,dy):
                    return True
        
        dfs(0,0)
        grid[0][0]=1
        
        print(grid)
        
        return not dfs(0,0)