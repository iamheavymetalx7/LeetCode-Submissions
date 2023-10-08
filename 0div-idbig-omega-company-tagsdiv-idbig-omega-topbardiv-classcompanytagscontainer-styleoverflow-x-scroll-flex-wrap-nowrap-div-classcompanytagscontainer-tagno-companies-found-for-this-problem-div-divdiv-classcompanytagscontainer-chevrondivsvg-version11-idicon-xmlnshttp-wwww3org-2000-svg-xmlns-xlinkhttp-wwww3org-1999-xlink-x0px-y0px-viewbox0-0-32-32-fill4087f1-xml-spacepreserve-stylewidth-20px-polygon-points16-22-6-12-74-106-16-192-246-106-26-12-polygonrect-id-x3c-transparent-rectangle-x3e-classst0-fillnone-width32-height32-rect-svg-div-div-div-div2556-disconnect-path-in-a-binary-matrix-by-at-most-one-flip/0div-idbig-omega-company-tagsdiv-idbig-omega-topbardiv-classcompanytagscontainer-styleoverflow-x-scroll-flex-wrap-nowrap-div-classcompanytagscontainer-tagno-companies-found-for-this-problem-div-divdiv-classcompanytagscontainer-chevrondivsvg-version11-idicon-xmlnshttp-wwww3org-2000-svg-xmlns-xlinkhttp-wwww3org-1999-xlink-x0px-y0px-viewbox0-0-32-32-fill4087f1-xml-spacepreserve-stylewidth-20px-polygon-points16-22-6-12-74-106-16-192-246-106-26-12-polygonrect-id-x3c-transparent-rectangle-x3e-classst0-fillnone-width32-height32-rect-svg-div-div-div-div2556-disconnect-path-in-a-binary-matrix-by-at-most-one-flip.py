class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        n,m = len(grid),len(grid[0])

        def dfs(i,j):
            if i==n-1 and j==m-1:
                return True
            
            if not (0<=i<n) or not (0<=j<m) or  (grid[i][j]==0):
                return False
            
            grid[i][j]=0
            return (dfs(i+1,j) or dfs(i,j+1))
        
        dfs(0,0)
        grid[0][0]=1
        
        
        return not dfs(0,0)